from __future__ import annotations

import importlib.util
import io
import json
import os
import subprocess
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

SCRIPT = (
    Path(__file__).resolve().parents[3]
    / ".agents"
    / "skills"
    / "ralph-loop-manager"
    / "scripts"
    / "preflight.py"
)
SPEC = importlib.util.spec_from_file_location("ralph_manager_preflight", SCRIPT)
assert SPEC and SPEC.loader
preflight = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(preflight)


class ExactSignalTests(unittest.TestCase):
    def test_accepts_exact_boolean_signal(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "signal.json"
            path.write_text(json.dumps({"isEverythingDone": False}), encoding="utf-8")
            self.assertFalse(preflight.exact_signal(path))

    def test_rejects_extra_non_boolean_and_duplicate_properties(self) -> None:
        invalid = [
            '{"isEverythingDone": false, "extra": 1}',
            '{"isEverythingDone": 0}',
            '{"isEverythingDone": false, "isEverythingDone": true}',
        ]
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "signal.json"
            for value in invalid:
                with self.subTest(value=value):
                    path.write_text(value, encoding="utf-8")
                    with self.assertRaises(ValueError):
                        preflight.exact_signal(path)


class ScopeResolutionTests(unittest.TestCase):
    def test_accepts_existing_repository_contained_path(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp).resolve()
            target = repo / "feature"
            target.mkdir()
            hard_stops: list[dict[str, str]] = []
            result = preflight.resolve_target(repo, "feature", hard_stops)
            self.assertEqual({"kind": "directory", "value": "feature"}, result)
            self.assertEqual([], hard_stops)

    def test_rejects_existing_path_outside_repository(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp).resolve()
            repo = base / "repo"
            outside = base / "outside"
            repo.mkdir()
            outside.mkdir()
            hard_stops: list[dict[str, str]] = []
            result = preflight.resolve_target(repo, str(outside), hard_stops)
            self.assertEqual("outside", result["kind"])
            self.assertEqual("TARGET_OUTSIDE_REPOSITORY", hard_stops[0]["code"])

    def test_rejects_missing_path_but_allows_feature_label_for_semantic_gate(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp).resolve()
            hard_stops: list[dict[str, str]] = []
            missing = preflight.resolve_target(repo, "missing/path", hard_stops)
            self.assertEqual("missing", missing["kind"])
            self.assertEqual("TARGET_PATH_MISSING", hard_stops[0]["code"])

            hard_stops = []
            label = preflight.resolve_target(repo, "Contact form feature", hard_stops)
            self.assertEqual({"kind": "feature-label", "value": "Contact form feature"}, label)
            self.assertEqual([], hard_stops)


class ControllerContainmentTests(unittest.TestCase):
    def test_accepts_regular_file_inside_canonical_root(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp).resolve()
            controller = root / "controller.py"
            controller.write_text("pass\n", encoding="utf-8")
            self.assertTrue(preflight.is_contained_regular_file(controller, root))

    def test_rejects_file_outside_root(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp).resolve()
            root = base / "root"
            root.mkdir()
            controller = base / "controller.py"
            controller.write_text("pass\n", encoding="utf-8")
            self.assertFalse(preflight.is_contained_regular_file(controller, root))

    def test_rejects_ancestor_link_that_resolves_outside_root(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp).resolve()
            root = base / "root"
            outside = base / "outside"
            root.mkdir()
            outside.mkdir()
            (outside / "controller.py").write_text("pass\n", encoding="utf-8")
            linked_dir = root / "linked"
            if os.name == "nt":
                created = subprocess.run(
                    ["cmd.exe", "/d", "/c", "mklink", "/J", str(linked_dir), str(outside)],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    check=False,
                )
                if created.returncode != 0:
                    self.skipTest(f"directory junctions unavailable: {created.stdout.strip()}")
            else:
                os.symlink(outside, linked_dir, target_is_directory=True)
            self.assertFalse(preflight.is_contained_regular_file(linked_dir / "controller.py", root))


class FailClosedCliTests(unittest.TestCase):
    def test_missing_repository_returns_structured_hard_stop(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            missing = Path(temp) / "missing"
            output = io.StringIO()
            with redirect_stdout(output):
                result = preflight.main(["--repo", str(missing), "--target", "Feature"])
            payload = json.loads(output.getvalue())
            self.assertEqual(2, result)
            self.assertEqual("HARD_STOP", payload["status"])
            self.assertEqual("REPOSITORY_DIRECTORY_MISSING", payload["hard_stops"][0]["code"])
            self.assertFalse(payload["launch_performed"])

    def test_existing_other_repository_returns_project_scope_hard_stop(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            other_repo = Path(temp)
            output = io.StringIO()
            with redirect_stdout(output):
                result = preflight.main(["--repo", str(other_repo), "--target", "Feature"])
            payload = json.loads(output.getvalue())
            self.assertEqual(2, result)
            self.assertEqual("PROJECT_SCOPE_MISMATCH", payload["hard_stops"][0]["code"])
            self.assertFalse(payload["launch_performed"])

    def test_command_timeout_becomes_nonzero_result_instead_of_traceback(self) -> None:
        timeout = subprocess.TimeoutExpired(["slow"], 3)
        with patch.object(preflight.subprocess, "run", side_effect=timeout):
            result = preflight.run(["slow"], Path.cwd(), timeout=3)
        self.assertEqual(124, result.returncode)
        self.assertIn("Timed out after 3 seconds", result.stdout)

    def test_existing_hard_stop_suppresses_controller_execution(self) -> None:
        expected_profile_text = " ".join(value for values in preflight.EXPECTED_PROFILES.values() for value in values)

        def fake_run(command: list[str], cwd: Path, timeout: float = 20) -> subprocess.CompletedProcess[str]:
            if command[0] == preflight.sys.executable and any(str(part).endswith("ralph_loop.py") for part in command):
                self.fail("controller dry-run executed after a deterministic HARD STOP")
            if "rev-parse" in command:
                output = str(preflight.OWNED_REPOSITORY)
            elif "profile" in command or "config" in command:
                output = expected_profile_text
            else:
                output = ""
            return subprocess.CompletedProcess(command, 0, stdout=output)

        output = io.StringIO()
        with (
            patch.object(preflight, "run", side_effect=fake_run),
            patch.object(preflight.shutil, "which", side_effect=lambda command: command),
            patch.dict(preflight.os.environ, {"RESEND_API_KEY": "", "RESEND_FROM_EMAIL": ""}),
            redirect_stdout(output),
        ):
            result = preflight.main(["--repo", str(preflight.OWNED_REPOSITORY), "--target", "B06-02"])
        payload = json.loads(output.getvalue())
        self.assertEqual(2, result)
        self.assertIn("EMAIL_NOT_READY", [item["code"] for item in payload["hard_stops"]])
        self.assertNotIn("controller-dry-run", [item["name"] for item in payload["checks"]])


if __name__ == "__main__":
    unittest.main(verbosity=2)

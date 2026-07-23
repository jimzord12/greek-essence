from __future__ import annotations

import contextlib
import io
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

TOOLS = Path(__file__).resolve().parents[1] / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from ralph_loop import (  # noqa: E402
    ControllerState,
    LockConflict,
    RalphError,
    save_controller_state,
)

try:
    from ralph_loop import CampaignIdentity, TransitionResult, transition_campaign_state  # noqa: E402
    TRANSITION_IMPORT_ERROR: ImportError | None = None
except ImportError as exc:  # RED until the transition API is implemented.
    CampaignIdentity = None  # type: ignore[assignment,misc]
    TransitionResult = None  # type: ignore[assignment,misc]
    transition_campaign_state = None  # type: ignore[assignment]
    TRANSITION_IMPORT_ERROR = exc

try:
    import transition_campaign as transition_cli  # noqa: E402
    CLI_IMPORT_ERROR: ImportError | None = None
except ImportError as exc:  # RED until the explicit CLI is implemented.
    transition_cli = None  # type: ignore[assignment]
    CLI_IMPORT_ERROR = exc


TIMESTAMP = "20260723T152431123456Z"
COMPLETED = {"campaign_id": "bootstrap-b07-03", "task_id": "B07-03", "resolved_tier": "2"}
NEW = {"campaign_id": "campaign-next", "task_id": "B08-01", "resolved_tier": "2"}


class TransitionContractTests(unittest.TestCase):
    def require_transition_api(self, cli: bool = False) -> None:
        if TRANSITION_IMPORT_ERROR is not None:
            self.fail(f"transition API absent: {TRANSITION_IMPORT_ERROR}")
        if cli and CLI_IMPORT_ERROR is not None:
            self.fail(f"transition CLI absent: {CLI_IMPORT_ERROR}")

    def identity(self, values: dict[str, str]) -> CampaignIdentity:
        self.require_transition_api()
        assert CampaignIdentity is not None
        return CampaignIdentity(**values)

    def write_completed_state(
        self,
        state_dir: Path,
        *,
        campaign_id: str = COMPLETED["campaign_id"],
        task_id: str = COMPLETED["task_id"],
        resolved_tier: str = COMPLETED["resolved_tier"],
        current_root_pid: int | None = None,
    ) -> bytes:
        state = ControllerState(
            campaign_id,
            task_id,
            resolved_tier,
            successful_extensions=2,
            timeout_retries=1,
            current_iteration=7,
            current_root_pid=current_root_pid,
            assessment_log="sensitive-state-marker",
            diagnosis_log="private-diagnosis-marker",
        )
        save_controller_state(state_dir, state)
        return (state_dir / "controller-state.json").read_bytes()

    def transition(self, state_dir: Path, *, completed: dict[str, str] = COMPLETED, new: dict[str, str] = NEW, **kwargs: object) -> TransitionResult:
        self.require_transition_api()
        assert transition_campaign_state is not None
        return transition_campaign_state(
            state_dir,
            self.identity(completed),
            self.identity(new),
            timestamp_utc=TIMESTAMP,
            **kwargs,
        )

    def assert_rejected_without_mutation(self, state_dir: Path, original: bytes, call: object) -> None:
        state_path = state_dir / "controller-state.json"
        state_before = state_path.read_bytes() if state_path.exists() else None
        archive_dir = state_dir / "archive"
        archives_before = {
            path.name: path.read_bytes() for path in archive_dir.glob("*.json")
        } if archive_dir.exists() else {}
        with self.assertRaises((RalphError, ValueError, OSError)):
            call()  # type: ignore[operator]
        if state_before is None:
            self.assertFalse(state_path.exists())
        else:
            self.assertEqual(state_before, state_path.read_bytes())
        archives_after = {
            path.name: path.read_bytes() for path in archive_dir.glob("*.json")
        } if archive_dir.exists() else {}
        self.assertEqual(archives_before, archives_after)
        self.assertFalse((state_dir / "ralph.lock").exists())

    def test_success_archives_exact_completed_bytes_and_writes_zeroed_new_state(self) -> None:
        self.require_transition_api()
        with tempfile.TemporaryDirectory() as temp:
            state_dir = Path(temp)
            original = self.write_completed_state(state_dir)
            completion_signal = state_dir / "completion-signal.json"
            completion_signal.write_bytes(b'{"isEverythingDone": true}')
            with patch("ralph_loop.read_completion_signal", side_effect=AssertionError("completion signal must not be touched")):
                result = self.transition(state_dir)

            self.assertIsInstance(result, TransitionResult)
            self.assertEqual(state_dir / "controller-state.json", result.state_path)
            self.assertEqual(original, result.archive_path.read_bytes())
            self.assertEqual(
                "controller-state-bootstrap-b07-03-B07-03-20260723T152431123456Z.json",
                result.archive_path.name,
            )
            self.assertEqual(1, len(list((state_dir / "archive").glob("*.json"))))
            current = json.loads((state_dir / "controller-state.json").read_text(encoding="utf-8"))
            self.assertEqual(NEW, {key: current[key] for key in NEW})
            self.assertEqual(
                {
                    "successful_extensions": 0,
                    "timeout_retries": 0,
                    "current_iteration": None,
                    "current_root_pid": None,
                    "assessment_log": None,
                    "diagnosis_log": None,
                },
                {key: current[key] for key in (
                    "successful_extensions", "timeout_retries", "current_iteration",
                    "current_root_pid", "assessment_log", "diagnosis_log",
                )},
            )
            self.assertEqual(b'{"isEverythingDone": true}', completion_signal.read_bytes())
            self.assertFalse((state_dir / "ralph.lock").exists())
            self.assertFalse(any(state_dir.glob("controller-state.json.*")))

    def test_live_lock_owner_fails_without_state_or_archive_change(self) -> None:
        self.require_transition_api()
        with tempfile.TemporaryDirectory() as temp:
            state_dir = Path(temp)
            original = self.write_completed_state(state_dir)
            lock = state_dir / "ralph.lock"
            lock.write_text(str(os.getpid()), encoding="utf-8")
            with patch("ralph_loop._pid_is_running", return_value=True):
                with self.assertRaises(LockConflict):
                    self.transition(state_dir)
            self.assertEqual(original, (state_dir / "controller-state.json").read_bytes())
            self.assertEqual(str(os.getpid()), lock.read_text(encoding="utf-8"))
            self.assertFalse((state_dir / "archive").exists())

    def test_non_null_recorded_root_fails_whether_pid_is_live_or_dead(self) -> None:
        self.require_transition_api()
        for is_live in (True, False):
            with self.subTest(is_live=is_live), tempfile.TemporaryDirectory() as temp:
                state_dir = Path(temp)
                original = self.write_completed_state(state_dir, current_root_pid=48291)
                with patch("ralph_loop.terminate_process_tree") as terminate, patch(
                    "ralph_loop._pid_is_running", return_value=is_live
                ):
                    self.assert_rejected_without_mutation(
                        state_dir,
                        original,
                        lambda: self.transition(state_dir, pid_is_running_fn=lambda _: is_live),
                    )
                terminate.assert_not_called()

    def test_completed_identity_and_tier_mismatch_fail_closed(self) -> None:
        self.require_transition_api()
        cases = [
            ("campaign_id", {**COMPLETED, "campaign_id": "wrong-campaign"}),
            ("task_id", {**COMPLETED, "task_id": "wrong-task"}),
            ("resolved_tier", {**COMPLETED, "resolved_tier": "3"}),
        ]
        for field, completed in cases:
            with self.subTest(field=field), tempfile.TemporaryDirectory() as temp:
                state_dir = Path(temp)
                original = self.write_completed_state(state_dir)
                self.assert_rejected_without_mutation(
                    state_dir,
                    original,
                    lambda completed=completed: self.transition(state_dir, completed=completed),
                )

    def test_missing_or_malformed_controller_state_fails_closed(self) -> None:
        self.require_transition_api()
        malformed = [
            ("missing", None),
            ("duplicate", '{"campaign_id":"bootstrap-b07-03","campaign_id":"other"}'),
            ("wrong schema", json.dumps({"campaign_id": "bootstrap-b07-03"})),
            ("wrong field type", json.dumps({
                "campaign_id": "bootstrap-b07-03", "task_id": "B07-03", "resolved_tier": "2",
                "successful_extensions": True, "timeout_retries": 0, "current_iteration": None,
                "current_root_pid": None, "assessment_log": None, "diagnosis_log": None,
            })),
        ]
        for label, payload in malformed:
            with self.subTest(state=label), tempfile.TemporaryDirectory() as temp:
                state_dir = Path(temp)
                if payload is not None:
                    state_dir.mkdir(parents=True, exist_ok=True)
                    (state_dir / "controller-state.json").write_text(payload, encoding="utf-8")
                self.assert_rejected_without_mutation(state_dir, b"", lambda: self.transition(state_dir))
                if payload is None:
                    self.assertFalse((state_dir / "controller-state.json").exists() or (state_dir / "archive").exists())
                else:
                    self.assertEqual(payload.encode("utf-8"), (state_dir / "controller-state.json").read_bytes())
                    self.assertFalse((state_dir / "archive").exists())

    def test_incomplete_or_inappropriately_same_new_identity_is_rejected(self) -> None:
        self.require_transition_api()
        cases = [
            ("campaign whitespace", {**NEW, "campaign_id": "  "}),
            ("task whitespace", {**NEW, "task_id": "\t"}),
            ("tier whitespace", {**NEW, "resolved_tier": " "}),
            ("same campaign", {**NEW, "campaign_id": COMPLETED["campaign_id"]}),
            ("same task", {**NEW, "task_id": COMPLETED["task_id"]}),
        ]
        for label, new in cases:
            with self.subTest(identity=label), tempfile.TemporaryDirectory() as temp:
                state_dir = Path(temp)
                original = self.write_completed_state(state_dir)
                self.assert_rejected_without_mutation(
                    state_dir,
                    original,
                    lambda new=new: self.transition(state_dir, new=new),
                )

        with tempfile.TemporaryDirectory() as temp:
            state_dir = Path(temp)
            original = self.write_completed_state(state_dir)
            result = self.transition(state_dir, new={**NEW, "resolved_tier": COMPLETED["resolved_tier"]})
            self.assertEqual(original, result.archive_path.read_bytes())

    def test_archive_name_collision_preserves_current_state(self) -> None:
        self.require_transition_api()
        with tempfile.TemporaryDirectory() as temp:
            state_dir = Path(temp)
            original = self.write_completed_state(state_dir)
            archive = state_dir / "archive" / "controller-state-bootstrap-b07-03-B07-03-20260723T152431123456Z.json"
            archive.parent.mkdir(parents=True)
            archive.write_bytes(b"pre-existing archive")
            self.assert_rejected_without_mutation(state_dir, original, lambda: self.transition(state_dir))
            self.assertEqual(b"pre-existing archive", archive.read_bytes())

    def test_new_state_temp_write_or_fsync_failure_preserves_old_state_and_no_archive(self) -> None:
        self.require_transition_api()
        with tempfile.TemporaryDirectory() as temp:
            state_dir = Path(temp)
            original = self.write_completed_state(state_dir)
            with patch("ralph_loop.os.fsync", side_effect=OSError("new state fsync failed")):
                self.assert_rejected_without_mutation(state_dir, original, lambda: self.transition(state_dir))

    def test_archive_write_or_fsync_failure_preserves_old_current_state_and_no_partial_archive(self) -> None:
        self.require_transition_api()
        with tempfile.TemporaryDirectory() as temp:
            state_dir = Path(temp)
            original = self.write_completed_state(state_dir)
            with patch("ralph_loop.os.fsync", side_effect=[None, OSError("archive fsync failed")]):
                with self.assertRaises((RalphError, ValueError, OSError)):
                    self.transition(state_dir)
                self.assertEqual(original, (state_dir / "controller-state.json").read_bytes())
                archives = list((state_dir / "archive").glob("*.json")) if (state_dir / "archive").exists() else []
                self.assertTrue(not archives or all(path.read_bytes() == original for path in archives))
                self.assertFalse((state_dir / "ralph.lock").exists())

    def test_atomic_replace_failure_preserves_old_current_state_and_complete_archive(self) -> None:
        self.require_transition_api()
        with tempfile.TemporaryDirectory() as temp:
            state_dir = Path(temp)
            original = self.write_completed_state(state_dir)
            replace = Mock(side_effect=OSError("replace failed"))
            with self.assertRaises(OSError):
                self.transition(state_dir, replace_fn=replace)
            replace.assert_called_once()
            self.assertEqual(original, (state_dir / "controller-state.json").read_bytes())
            archives = list((state_dir / "archive").glob("*.json"))
            self.assertEqual(1, len(archives))
            self.assertEqual(original, archives[0].read_bytes())
            self.assertFalse(any(path.name.startswith("controller-state.json.") for path in state_dir.iterdir()))
            self.assertFalse((state_dir / "ralph.lock").exists())

    def test_cli_requires_all_six_identities_and_returns_structured_nonzero_failure(self) -> None:
        self.require_transition_api(cli=True)
        assert transition_cli is not None
        with tempfile.TemporaryDirectory() as temp:
            flags = [
                "--completed-campaign-id",
                "--completed-task-id",
                "--completed-resolved-tier",
                "--new-campaign-id",
                "--new-task-id",
                "--new-resolved-tier",
            ]
            values = [
                COMPLETED["campaign_id"],
                COMPLETED["task_id"],
                COMPLETED["resolved_tier"],
                NEW["campaign_id"],
                NEW["task_id"],
                NEW["resolved_tier"],
            ]
            for omitted in range(len(flags)):
                output = io.StringIO()
                arguments = [
                    "--state-dir", temp,
                ]
                for index, (flag, value) in enumerate(zip(flags, values)):
                    if index != omitted:
                        arguments.extend([flag, value])
                # Every omission must fail before state initialization.
                with self.subTest(omitted=flags[omitted]), contextlib.redirect_stdout(output), contextlib.redirect_stderr(io.StringIO()):
                    result = transition_cli.main(arguments)
                self.assertNotEqual(0, result)
                payload = json.loads(output.getvalue())
                self.assertIn("outcome", payload)
                self.assertNotEqual("COMPLETE", payload["outcome"])

    def test_transition_events_are_bounded_and_contain_no_prompt_command_or_raw_state(self) -> None:
        self.require_transition_api()
        with tempfile.TemporaryDirectory() as temp:
            state_dir = Path(temp)
            self.write_completed_state(state_dir)
            self.transition(state_dir)
            logs = list((state_dir / "logs").glob("*.jsonl"))
            self.assertEqual(1, len(logs))
            lines = logs[0].read_text(encoding="utf-8").splitlines()
            events = [json.loads(line) for line in lines]
            names = {event["event"] for event in events}
            for expected in (
                "campaign_transition_start",
                "campaign_transition_validation_complete",
                "campaign_transition_archive_complete",
                "campaign_transition_state_replace_complete",
                "campaign_transition_complete",
            ):
                self.assertIn(expected, names)
            forbidden_keys = {"prompt", "command", "raw_state", "state_content", "credentials"}
            forbidden_values = {"sensitive-state-marker", "private-diagnosis-marker"}
            for event in events:
                self.assertFalse(forbidden_keys.intersection(event))
                self.assertTrue(forbidden_values.isdisjoint(json.dumps(event)))


if __name__ == "__main__":
    unittest.main(verbosity=2)

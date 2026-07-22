from __future__ import annotations

import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1] / "tools"
import sys

if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from ralph_loop import (  # noqa: E402
    CompletionSignalError,
    HermesProcessError,
    IterationTimeout,
    LifecycleLogger,
    LockConflict,
    LoopOutcome,
    _acquire_lock,
    _pid_is_running,
    build_hermes_command,
    hermes_executor,
    read_completion_signal,
    run_loop,
)

import smoke_test  # noqa: E402


class FakeProcess:
    def __init__(self, return_code: int = 0, wait_error: BaseException | None = None, pid: int | None = None) -> None:
        self.return_code = return_code
        self.wait_error = wait_error
        self.pid = pid
        self.terminated = False
        self.killed = False

    def poll(self) -> int | None:
        return self.return_code if self.terminated or self.killed else None

    def wait(self, timeout: float | None = None) -> int:
        if self.wait_error is not None and not self.terminated and not self.killed:
            raise self.wait_error
        return self.return_code

    def terminate(self) -> None:
        self.terminated = True

    def kill(self) -> None:
        self.killed = True


class CompletionSignalTests(unittest.TestCase):
    def write_signal(self, root: Path, value: object) -> None:
        path = root / ".scratch" / "ralph-loop" / "completion-signal.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value), encoding="utf-8")

    def test_exact_boolean_values_are_read(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.write_signal(root, {"isEverythingDone": False})
            self.assertFalse(read_completion_signal(root))
            self.write_signal(root, {"isEverythingDone": True})
            self.assertTrue(read_completion_signal(root))

    def test_missing_signal_is_configuration_error(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaisesRegex(CompletionSignalError, "Cannot read completion signal"):
                read_completion_signal(Path(temp))

    def test_malformed_signal_is_configuration_error(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / ".scratch" / "ralph-loop" / "completion-signal.json"
            path.parent.mkdir(parents=True)
            path.write_text("{", encoding="utf-8")
            with self.assertRaisesRegex(CompletionSignalError, "Malformed completion signal"):
                read_completion_signal(Path(temp))

    def test_non_object_missing_and_extra_properties_are_rejected(self) -> None:
        invalid = [[], "true", None, {}, {"isEverythingDone": False, "extra": 1}]
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for value in invalid:
                self.write_signal(root, value)
                with self.subTest(value=value), self.assertRaises(CompletionSignalError):
                    read_completion_signal(root)

    def test_non_boolean_and_duplicate_properties_are_rejected(self) -> None:
        invalid_json = [
            '{"isEverythingDone": 1}',
            '{"isEverythingDone": "true"}',
            '{"isEverythingDone": false, "isEverythingDone": true}',
        ]
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            path = root / ".scratch" / "ralph-loop" / "completion-signal.json"
            path.parent.mkdir(parents=True)
            for text in invalid_json:
                path.write_text(text, encoding="utf-8")
                with self.subTest(text=text), self.assertRaises(CompletionSignalError):
                    read_completion_signal(root)


class LoopTests(unittest.TestCase):
    def signal_writer(self, root: Path, value: bool) -> None:
        path = root / ".scratch" / "ralph-loop" / "completion-signal.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({"isEverythingDone": value}), encoding="utf-8")

    def signal_reader(self, root: Path) -> bool:
        return read_completion_signal(root)

    def test_true_at_startup_does_not_launch_hermes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.signal_writer(root, True)
            launched: list[int] = []
            result = run_loop(
                root,
                execute_fn=lambda iteration, timeout: launched.append(iteration),
                state_dir=root / "runtime",
            )
            self.assertEqual(LoopOutcome.COMPLETE, result)
            self.assertEqual([], launched)

    def test_false_iteration_that_sets_true_stops_without_second_launch(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.signal_writer(root, False)
            launched: list[int] = []

            def execute(iteration: int, timeout: float | None) -> None:
                launched.append(iteration)
                self.signal_writer(root, True)

            result = run_loop(root, execute_fn=execute, state_dir=root / "runtime")
            self.assertEqual(LoopOutcome.COMPLETE, result)
            self.assertEqual([1], launched)

    def test_each_false_iteration_is_fresh_and_has_no_resume(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.signal_writer(root, False)
            commands: list[list[str]] = []

            def execute(iteration: int, timeout: float | None) -> None:
                commands.append(build_hermes_command(root, iteration))

            result = run_loop(
                root,
                max_iterations=2,
                execute_fn=execute,
                state_dir=root / "runtime",
            )
            self.assertEqual(LoopOutcome.LIMIT_REACHED, result)
            self.assertEqual(2, len(commands))
            for command in commands:
                self.assertNotIn("--resume", command)
                self.assertIn("gpt-5.6-sol", command)
                self.assertIn("openai-codex", command)

    def test_iteration_limit_is_distinct_non_success(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.signal_writer(root, False)
            result = run_loop(
                root,
                max_iterations=0,
                execute_fn=lambda iteration, timeout: self.fail("must not launch"),
                state_dir=root / "runtime",
            )
            self.assertEqual(LoopOutcome.LIMIT_REACHED, result)

    def test_invalid_signal_prevents_launch(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.signal_writer(root, False)
            signal_path = root / ".scratch" / "ralph-loop" / "completion-signal.json"
            signal_path.write_text("[]", encoding="utf-8")
            launched: list[int] = []
            with self.assertRaises(CompletionSignalError):
                run_loop(
                    root,
                    execute_fn=lambda iteration, timeout: launched.append(iteration),
                    state_dir=root / "runtime",
                )
            self.assertEqual([], launched)

    def test_exception_releases_lock(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.signal_writer(root, False)
            runtime = root / "runtime"
            with self.assertRaises(RuntimeError):
                run_loop(
                    root,
                    execute_fn=lambda iteration, timeout: (_ for _ in ()).throw(RuntimeError("stop")),
                    state_dir=runtime,
                )
            self.assertFalse((runtime / "ralph.lock").exists())

    def test_stale_lock_recovers_and_live_lock_conflicts(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            runtime = Path(temp)
            lock = runtime / "ralph.lock"
            lock.write_text("2147483647", encoding="utf-8")
            acquired = _acquire_lock(runtime)
            try:
                self.assertEqual(str(os.getpid()), lock.read_text(encoding="utf-8"))
                with self.assertRaises(LockConflict):
                    _acquire_lock(runtime)
            finally:
                acquired.unlink(missing_ok=True)

    def test_windows_invalid_pid_system_error_is_stale(self) -> None:
        with patch("ralph_loop.os.kill", side_effect=SystemError("invalid PID")):
            self.assertFalse(_pid_is_running(26708))


class LifecycleLoggingTests(unittest.TestCase):
    def read_events(self, path: Path) -> list[dict[str, object]]:
        return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]

    def test_logger_records_controller_and_parent_identity_as_jsonl(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "lifecycle.jsonl"
            logger = LifecycleLogger(path, campaign_id="campaign", task_id="task", resolved_tier="2")
            logger.emit("controller_start", controller_pid=123, parent_pid=456)
            event = self.read_events(path)[0]
            self.assertEqual("controller_start", event["event"])
            self.assertEqual(123, event["controller_pid"])
            self.assertEqual(456, event["parent_pid"])
            self.assertEqual("campaign", event["campaign_id"])
            self.assertEqual("task", event["task_id"])
            self.assertEqual("2", event["resolved_tier"])
            self.assertRegex(str(event["timestamp_utc"]), r"Z$")

    def test_logger_write_failure_does_not_change_controller_flow(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            logger = LifecycleLogger(Path(temp) / "lifecycle.jsonl", "campaign", "task", "2")
            with patch("pathlib.Path.open", side_effect=OSError("disk unavailable")):
                logger.emit("controller_start", controller_pid=123)
            self.assertIn("disk unavailable", logger.last_error or "")

    def test_executor_records_root_state_poll_and_finally_boundaries(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            runtime = root / "runtime"
            logger = LifecycleLogger(runtime / "lifecycle.jsonl", "campaign", "task", "2")
            fake = FakeProcess(return_code=0, pid=43210)
            state = __import__("ralph_loop").ControllerState("campaign", "task", "2")
            with patch("ralph_loop.subprocess.Popen", return_value=fake):
                hermes_executor(root, runtime, 1, 10, state=state, lifecycle=logger)
            events = self.read_events(logger.path)
            names = [event["event"] for event in events]
            for expected in (
                "root_launch_start",
                "root_launched",
                "controller_state_write_start",
                "controller_state_write_complete",
                "root_poll_result",
                "executor_finally_enter",
                "root_pid_clear_start",
                "root_pid_clear_complete",
                "executor_finally_exit",
            ):
                self.assertIn(expected, names)
            launched = next(event for event in events if event["event"] == "root_launched")
            self.assertEqual(43210, launched["root_pid"])
            self.assertEqual("hermes", launched["root_executable"])
            self.assertEqual("greekroot", launched["root_profile"])
            self.assertNotIn("command", launched)
            self.assertNotIn("prompt", launched)

    def test_initial_state_write_failure_terminates_launched_root(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            fake = FakeProcess(return_code=0)
            with patch("ralph_loop.subprocess.Popen", return_value=fake), patch(
                "ralph_loop.save_controller_state", side_effect=OSError("state disk unavailable")
            ):
                with self.assertRaisesRegex(OSError, "state disk unavailable"):
                    hermes_executor(Path(temp), Path(temp) / "runtime", 1, 10)
            self.assertTrue(fake.terminated)

    def test_executor_continues_when_lifecycle_path_is_unwritable(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            runtime = root / "runtime"
            blocked_path = runtime / "blocked"
            blocked_path.mkdir(parents=True)
            logger = LifecycleLogger(blocked_path, "campaign", "task", "2")
            fake = FakeProcess(return_code=0)
            with patch("ralph_loop.subprocess.Popen", return_value=fake):
                hermes_executor(root, runtime, 1, 10, lifecycle=logger)
            self.assertIn("Error", logger.last_error or "")

    def test_cleanup_state_failure_does_not_mask_primary_exception(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            fake = FakeProcess(return_code=0)
            with patch("ralph_loop.subprocess.Popen", return_value=fake), patch(
                "ralph_loop.supervise_process", side_effect=RuntimeError("primary failure")
            ), patch(
                "ralph_loop.save_controller_state", side_effect=[None, OSError("clear failure")]
            ):
                with self.assertRaisesRegex(RuntimeError, "primary failure"):
                    hermes_executor(Path(temp), Path(temp) / "runtime", 1, 10)
            self.assertTrue(fake.terminated)

    def test_termination_failure_does_not_mask_primary_exception(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            fake = FakeProcess(return_code=0)
            with patch("ralph_loop.subprocess.Popen", return_value=fake), patch(
                "ralph_loop.save_controller_state", side_effect=OSError("primary state failure")
            ), patch(
                "ralph_loop.terminate_process_tree", side_effect=RuntimeError("termination failure")
            ):
                with self.assertRaisesRegex(OSError, "primary state failure") as raised:
                    hermes_executor(Path(temp), Path(temp) / "runtime", 1, 10)
            self.assertTrue(any("termination failure" in note for note in raised.exception.__notes__))

    def test_run_loop_records_lock_and_return_lifecycle(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            runtime = root / "runtime"
            self.write_signal(root, True)
            result = run_loop(root, state_dir=runtime, campaign_id="campaign", task_id="task", resolved_tier="2")
            self.assertEqual(LoopOutcome.COMPLETE, result)
            logs = list((runtime / "logs").glob("controller-lifecycle-*.jsonl"))
            self.assertEqual(1, len(logs))
            names = [event["event"] for event in self.read_events(logs[0])]
            self.assertEqual("controller_start", names[0])
            for expected in (
                "lock_acquire_start", "lock_acquired", "loop_return",
                "lock_release_start", "lock_release_complete", "controller_exit",
            ):
                self.assertIn(expected, names)

    def write_signal(self, root: Path, value: bool) -> None:
        path = root / ".scratch" / "ralph-loop" / "completion-signal.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({"isEverythingDone": value}), encoding="utf-8")


class CommandAndProcessTests(unittest.TestCase):
    def test_smoke_runner_explicitly_caps_live_execution_at_two_iterations(self) -> None:
        with patch("smoke_test.ralph_main", return_value=2) as run:
            result = smoke_test.main(["--campaign-id", "campaign-smoke"])
        self.assertEqual(2, result)
        run.assert_called_once_with([
            "--max-iterations", "2", "--campaign-id", "campaign-smoke"
        ])

    def test_root_command_is_pinned_and_has_three_entrypoints(self) -> None:
        command = build_hermes_command(Path("C:/repo"), 1)
        self.assertEqual("hermes", command[0])
        self.assertIn("greekroot", command)
        self.assertIn("gpt-5.6-sol", command)
        self.assertIn("openai-codex", command)
        self.assertNotIn("--resume", command)
        prompt = command[command.index("-q") + 1]
        for entrypoint in (
            ".scratch/ralph-loop/RALPH_LOOP.md",
            ".scratch/ralph-loop/HANDOFF.md",
            ".scratch/ralph-loop/KNOWLEDGE.md",
        ):
            self.assertIn(entrypoint, prompt)

    def test_nonzero_hermes_exit_reports_log_path(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            fake = FakeProcess(return_code=7)
            with patch("ralph_loop.subprocess.Popen", return_value=fake):
                with self.assertRaisesRegex(HermesProcessError, r"log: .+iteration-0001"):
                    hermes_executor(Path(temp), Path(temp) / "runtime", 1, 10)

    def test_timeout_terminates_child_and_reports_log_path(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            fake = FakeProcess(wait_error=subprocess.TimeoutExpired("hermes", 1))
            with patch("ralph_loop.subprocess.Popen", return_value=fake):
                with self.assertRaisesRegex(IterationTimeout, r"timed out; log: .+iteration-0001"):
                    hermes_executor(Path(temp), Path(temp) / "runtime", 1, 1)
            self.assertTrue(fake.terminated)


if __name__ == "__main__":
    unittest.main(verbosity=2)

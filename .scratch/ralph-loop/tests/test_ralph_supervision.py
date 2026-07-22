from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1] / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from ralph_loop import (  # noqa: E402
    ControllerState,
    Diagnosis,
    HardStop,
    IterationTimeout,
    LockConflict,
    LoopOutcome,
    ProcessTreeError,
    build_retry_prompt,
    load_controller_state,
    parse_diagnosis,
    parse_health_response,
    run_loop,
    run_readonly_assessor,
    save_controller_state,
    supervise_process,
    terminate_process_tree,
)


class StrictResponseTests(unittest.TestCase):
    def test_health_exact_booleans_only(self) -> None:
        self.assertTrue(parse_health_response('{"should_extend": true}'))
        self.assertFalse(parse_health_response('{"should_extend": false}'))
        invalid = [
            '{}', '{"wrong": true}', '{"should_extend": "true"}',
            '{"should_extend": 1}', '{"should_extend": null}', '[]',
            '{"should_extend": true, "extra": 1}',
            '{"should_extend": false, "should_extend": true}',
            '{', 'prose {"should_extend": true}', '{"should_extend": true} prose',
        ]
        for text in invalid:
            with self.subTest(text=text), self.assertRaises(ValueError):
                parse_health_response(text)

    def test_diagnosis_exact_schema_only(self) -> None:
        self.assertEqual(Diagnosis(True, "Create the approved closure commit."), parse_diagnosis(
            '{"should_retry": true, "steering": "Create the approved closure commit."}'
        ))
        self.assertEqual(Diagnosis(False, None), parse_diagnosis(
            '{"should_retry": false, "steering": null}'
        ))
        invalid = [
            '{}', '{"should_retry": true}',
            '{"should_retry": true, "steering": null}',
            '{"should_retry": true, "steering": "  "}',
            '{"should_retry": false, "steering": "no"}',
            '{"should_retry": "true", "steering": "x"}',
            '{"should_retry": true, "steering": "x", "extra": 1}',
            '{"should_retry": true, "should_retry": false, "steering": null}',
            'not json', '{"should_retry": false, "steering": null} prose',
        ]
        for text in invalid:
            with self.subTest(text=text), self.assertRaises(ValueError):
                parse_diagnosis(text)


class StateAndPromptTests(unittest.TestCase):
    def test_state_is_atomic_persistent_and_identity_bound(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            state_dir = Path(temp)
            state = load_controller_state(state_dir, "campaign-B06-02", "B06-02", "Tier 2 — Prototype")
            state.successful_extensions = 3
            state.timeout_retries = 1
            save_controller_state(state_dir, state)
            restored = load_controller_state(state_dir, "campaign-B06-02", "B06-02", "Tier 2 — Prototype")
            self.assertEqual((3, 1), (restored.successful_extensions, restored.timeout_retries))
            self.assertFalse((state_dir / "controller-state.json.tmp").exists())
            with self.assertRaises(ValueError):
                load_controller_state(state_dir, "other", "B06-03", "Tier 2 — Prototype")

    def test_malformed_or_out_of_range_state_fails_closed(self) -> None:
        valid = {
            "campaign_id": "campaign", "task_id": "task",
            "resolved_tier": "Tier 2 — Prototype", "successful_extensions": 0,
            "timeout_retries": 0, "current_iteration": None, "current_root_pid": None,
            "assessment_log": None, "diagnosis_log": None,
        }
        mutations = [
            {"successful_extensions": -1}, {"successful_extensions": 4},
            {"successful_extensions": True}, {"timeout_retries": -1},
            {"timeout_retries": 2}, {"timeout_retries": "0"},
            {"current_root_pid": False}, {"current_iteration": 0},
            {"assessment_log": 1}, {"extra": "not allowed"},
        ]
        for mutation in mutations:
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as temp:
                state_dir = Path(temp); payload = dict(valid); payload.update(mutation)
                (state_dir / "controller-state.json").write_text(json.dumps(payload), encoding="utf-8")
                with self.assertRaises(HardStop):
                    load_controller_state(state_dir, "campaign", "task", "Tier 2 — Prototype")
        with tempfile.TemporaryDirectory() as temp:
            state_dir = Path(temp); payload = dict(valid); payload.pop("task_id")
            (state_dir / "controller-state.json").write_text(json.dumps(payload), encoding="utf-8")
            with self.assertRaises(HardStop):
                load_controller_state(state_dir, "campaign", "task", "Tier 2 — Prototype")

    def test_retry_prompt_preserves_identity_tier_and_scope(self) -> None:
        prompt = build_retry_prompt(
            ControllerState("campaign-B06-02", "B06-02", "Tier 2 — Prototype"),
            "Closure is incomplete; create only the approved task commit.",
            "Review 02 approved; required checks passed.",
        )
        for expected in (
            "campaign-B06-02", "B06-02", "Tier 2 — Prototype",
            "Review 02 approved", "Closure is incomplete", "Do not begin another task",
            "Do not repeat already-approved work",
        ):
            self.assertIn(expected, prompt)


class FakeClock:
    def __init__(self) -> None:
        self.now = 0.0

    def monotonic(self) -> float:
        return self.now


class TimedProcess:
    def __init__(self, clock: FakeClock, exit_at: float | None = None) -> None:
        self.clock = clock
        self.exit_at = exit_at
        self.pid = 43210
        self.terminated = False
        self.killed = False

    def poll(self) -> int | None:
        if self.terminated or self.killed:
            return -1
        if self.exit_at is not None and self.clock.now >= self.exit_at:
            return 0
        return None

    def wait(self, timeout: float | None = None) -> int:
        if self.poll() is not None:
            return self.poll() or 0
        assert timeout is not None
        if self.exit_at is not None and self.exit_at <= self.clock.now + timeout:
            self.clock.now = self.exit_at
            return 0
        self.clock.now += timeout
        raise subprocess.TimeoutExpired("root", timeout)

    def terminate(self) -> None:
        self.terminated = True

    def kill(self) -> None:
        self.killed = True


class SupervisionTests(unittest.TestCase):
    def run_supervision(self, answers: list[bool], state_extensions: int = 0, exit_at: float | None = None):
        clock = FakeClock()
        process = TimedProcess(clock, exit_at=exit_at)
        state = ControllerState("campaign", "task", "Tier 2 — Prototype", state_extensions, 0)
        assessments: list[float] = []

        def assess() -> bool:
            assessments.append(clock.now)
            return answers.pop(0) if answers else False

        result = supervise_process(
            process, lease_seconds=10, assessment_seconds=4, state=state,
            assess_fn=assess, persist_fn=lambda _: None, completion_or_stop_fn=lambda: False,
            monotonic_fn=clock.monotonic, terminate_fn=lambda proc: setattr(proc, "terminated", True),
        )
        return result, process, state, assessments, clock.now

    def test_true_resets_lease_and_false_does_not(self) -> None:
        with self.assertRaises(IterationTimeout):
            self.run_supervision([True, False])
        # First assessment at 4; renewal moves timeout from 10 to 14.
        try:
            self.run_supervision([True, False])
        except IterationTimeout as exc:
            self.assertIn("lease expired", str(exc))

    def test_three_extensions_max_and_fourth_is_denied(self) -> None:
        clock = FakeClock()
        process = TimedProcess(clock)
        state = ControllerState("campaign", "task", "Tier 2 — Prototype")
        assessments: list[float] = []
        def assess() -> bool:
            assessments.append(clock.now)
            return True
        with self.assertRaises(IterationTimeout):
            supervise_process(
                process, lease_seconds=10, assessment_seconds=4, state=state,
                assess_fn=assess, persist_fn=lambda _: None,
                completion_or_stop_fn=lambda: False, monotonic_fn=clock.monotonic,
                terminate_fn=lambda proc: setattr(proc, "terminated", True),
            )
        self.assertEqual(3, state.successful_extensions)
        self.assertEqual([4.0, 8.0, 12.0], assessments)

    def test_existing_extension_count_survives_retry_process(self) -> None:
        clock = FakeClock()
        process = TimedProcess(clock)
        state = ControllerState("campaign", "task", "Tier 2 — Prototype", 3, 1)
        assessments: list[float] = []
        with self.assertRaises(IterationTimeout):
            supervise_process(
                process, lease_seconds=10, assessment_seconds=4, state=state,
                assess_fn=lambda: assessments.append(clock.now) or True,
                persist_fn=lambda _: None, completion_or_stop_fn=lambda: False,
                monotonic_fn=clock.monotonic,
                terminate_fn=lambda proc: setattr(proc, "terminated", True),
            )
        self.assertEqual(3, state.successful_extensions)
        self.assertEqual([], assessments)

    def test_root_exit_during_assessment_does_not_extend(self) -> None:
        clock = FakeClock()
        process = TimedProcess(clock)
        state = ControllerState("campaign", "task", "Tier 2 — Prototype")
        def assess() -> bool:
            process.exit_at = clock.now
            return True
        result = supervise_process(
            process, lease_seconds=10, assessment_seconds=4, state=state,
            assess_fn=assess, persist_fn=lambda _: None, completion_or_stop_fn=lambda: False,
            monotonic_fn=clock.monotonic, terminate_fn=lambda _: None,
        )
        self.assertEqual(0, result)
        self.assertEqual(0, state.successful_extensions)


class ProcessTreeTests(unittest.TestCase):
    def test_windows_tree_kill_is_scoped_to_root_pid(self) -> None:
        process = TimedProcess(FakeClock())
        completed = subprocess.CompletedProcess([], 0, stdout="SUCCESS")
        def completed_kill(*args, **kwargs):
            process.killed = True
            return completed
        with patch("ralph_loop.os.name", "nt"), patch("ralph_loop.subprocess.run", side_effect=completed_kill) as run:
            terminate_process_tree(process)
        command = run.call_args.args[0]
        self.assertEqual(["taskkill", "/PID", str(process.pid), "/T", "/F"], command)

    def test_ambiguous_surviving_tree_fails_closed(self) -> None:
        process = TimedProcess(FakeClock())
        completed = subprocess.CompletedProcess([], 1, stdout="failure")
        with patch("ralph_loop.os.name", "nt"), patch("ralph_loop.subprocess.run", return_value=completed):
            with self.assertRaises(ProcessTreeError):
                terminate_process_tree(process)


class RetryBehaviorTests(unittest.TestCase):
    def test_lock_conflict_cannot_create_or_change_controller_state(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); runtime = root / "runtime"; runtime.mkdir()
            (runtime / "ralph.lock").write_text(str(__import__("os").getpid()), encoding="utf-8")
            state_path = runtime / "controller-state.json"
            with self.assertRaises(LockConflict):
                run_loop(
                    root, state_dir=runtime, read_signal_fn=lambda _: False,
                    campaign_id="intruder", task_id="other",
                )
            self.assertFalse(state_path.exists())

    def test_timeout_diagnosis_preflight_and_one_retry_persist(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            runtime = root / "runtime"
            calls: list[str] = []
            attempts = 0
            def execute(iteration: int, timeout: float | None) -> None:
                nonlocal attempts
                attempts += 1
                calls.append(f"root-{iteration}")
                if attempts == 1:
                    raise IterationTimeout("expired after termination")
            def diagnose(state: ControllerState, iteration: int) -> Diagnosis:
                calls.append("diagnosis")
                return Diagnosis(True, "Perform closure only.")
            result = run_loop(
                root, max_iterations=1, iteration_timeout=10,
                assessment_threshold=4, state_dir=runtime,
                read_signal_fn=lambda _: False, execute_fn=execute,
                campaign_id="campaign", task_id="B06-02",
                diagnosis_fn=diagnose,
                preflight_fn=lambda: calls.append("preflight") or True,
            )
            self.assertEqual(LoopOutcome.LIMIT_REACHED, result)
            self.assertEqual(["root-1", "diagnosis", "preflight", "root-2"], calls)
            state = load_controller_state(runtime, "campaign", "B06-02", "Tier 2 — Prototype")
            self.assertEqual(1, state.timeout_retries)

    def test_failed_preflight_and_second_timeout_hard_stop(self) -> None:
        for failed_preflight in (True, False):
            with self.subTest(failed_preflight=failed_preflight), tempfile.TemporaryDirectory() as temp:
                root = Path(temp); runtime = root / "runtime"
                if not failed_preflight:
                    save_controller_state(runtime, ControllerState(
                        "campaign", "task", "Tier 2 — Prototype", timeout_retries=1
                    ))
                with self.assertRaises(HardStop):
                    run_loop(
                        root, max_iterations=1, iteration_timeout=10,
                        assessment_threshold=4, state_dir=runtime,
                        read_signal_fn=lambda _: False,
                        execute_fn=lambda *_: (_ for _ in ()).throw(IterationTimeout("expired")),
                        campaign_id="campaign", task_id="task",
                        diagnosis_fn=lambda *_: Diagnosis(True, "closure only"),
                        preflight_fn=lambda: not failed_preflight,
                    )

    def test_completion_after_timeout_prevents_diagnosis(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); signals = iter([False, True])
            result = run_loop(
                root, max_iterations=1, iteration_timeout=10,
                assessment_threshold=4, state_dir=root / "runtime",
                read_signal_fn=lambda _: next(signals),
                execute_fn=lambda *_: (_ for _ in ()).throw(IterationTimeout("expired")),
                diagnosis_fn=lambda *_: self.fail("diagnosis must not run"),
            )
            self.assertEqual(LoopOutcome.COMPLETE, result)

    def test_assessor_timeout_and_nonzero_exit_return_no_response(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            cases = [
                subprocess.TimeoutExpired("hermes", 1),
                subprocess.CompletedProcess([], 9, stdout='{"should_extend": true}'),
            ]
            for outcome in cases:
                with self.subTest(outcome=type(outcome).__name__), patch(
                    "ralph_loop.subprocess.run", side_effect=outcome if isinstance(outcome, BaseException) else None,
                    return_value=None if isinstance(outcome, BaseException) else outcome,
                ):
                    response, log = run_readonly_assessor(root, root / "runtime", "prompt", 1, "assessment", 1)
                self.assertIsNone(response)
                self.assertTrue(log.is_file())


if __name__ == "__main__":
    unittest.main(verbosity=2)

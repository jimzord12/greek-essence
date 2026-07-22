#!/usr/bin/env python3
"""Run supervised fresh Greek Essence Ralph root iterations."""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Callable

sys.dont_write_bytecode = True

ROOT_PROFILE = "greekroot"
ROOT_MODEL = "gpt-5.6-sol"
ROOT_PROVIDER = "openai-codex"
ASSESSOR_PROFILE = "greekreview"
ASSESSOR_MODEL = "gpt-5.6-terra"
COMPLETION_SIGNAL = Path(".scratch") / "ralph-loop" / "completion-signal.json"
HANDOFF = Path(".scratch") / "ralph-loop" / "HANDOFF.md"
PREFLIGHT = Path(".agents") / "skills" / "ralph-loop-manager" / "scripts" / "preflight.py"
DEFAULT_ITERATION_TIMEOUT = 3600.0
DEFAULT_ASSESSMENT_THRESHOLD = 2700.0
DEFAULT_ASSESSOR_TIMEOUT = 180.0
MAX_EXTENSIONS = 3
MAX_TIMEOUT_RETRIES = 1


class RalphError(RuntimeError):
    """Base class for operational Ralph failures."""


class CompletionSignalError(RalphError):
    pass


class HermesProcessError(RalphError):
    pass


class IterationTimeout(RalphError):
    pass


class LockConflict(RalphError):
    pass


class ProcessTreeError(RalphError):
    pass


class HardStop(RalphError):
    pass


class LoopOutcome(str, Enum):
    COMPLETE = "COMPLETE"
    LIMIT_REACHED = "LIMIT_REACHED"


@dataclass(eq=True)
class Diagnosis:
    should_retry: bool
    steering: str | None


@dataclass
class ControllerState:
    campaign_id: str
    task_id: str
    resolved_tier: str
    successful_extensions: int = 0
    timeout_retries: int = 0
    current_iteration: int | None = None
    current_root_pid: int | None = None
    assessment_log: str | None = None
    diagnosis_log: str | None = None


class LifecycleLogger:
    """Append privacy-bounded controller lifecycle events as durable JSONL."""

    def __init__(self, path: Path, campaign_id: str, task_id: str, resolved_tier: str) -> None:
        self.path = path
        self.campaign_id = campaign_id
        self.task_id = task_id
        self.resolved_tier = resolved_tier
        self.last_error: str | None = None
        try:
            self.path.parent.mkdir(parents=True, exist_ok=True)
        except OSError as exc:
            self.last_error = f"{type(exc).__name__}: {exc}"

    def emit(self, event: str, **fields: object) -> None:
        payload = {
            "timestamp_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "event": event,
            "campaign_id": self.campaign_id,
            "task_id": self.task_id,
            "resolved_tier": self.resolved_tier,
            **fields,
        }
        try:
            with self.path.open("a", encoding="utf-8") as handle:
                handle.write(json.dumps(payload, ensure_ascii=False) + "\n")
                handle.flush()
            self.last_error = None
        except (OSError, TypeError, ValueError) as exc:
            self.last_error = f"{type(exc).__name__}: {exc}"


def _lifecycle_log(state_dir: Path) -> Path:
    return state_dir / "logs" / f"controller-lifecycle-{time.strftime('%Y%m%d-%H%M%S')}-pid-{os.getpid()}.jsonl"


def default_state_dir() -> Path:
    base = Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData" / "Local"))
    return base / "hermes" / "ralph" / "greek-essence"


def _pairs_without_duplicates(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate property: {key}")
        result[key] = value
    return result


def _strict_json(text: str) -> object:
    try:
        return json.loads(text, object_pairs_hook=_pairs_without_duplicates)
    except (json.JSONDecodeError, ValueError) as exc:
        raise ValueError(f"invalid JSON: {exc}") from exc


def parse_health_response(text: str) -> bool:
    payload = _strict_json(text)
    if not isinstance(payload, dict) or set(payload) != {"should_extend"}:
        raise ValueError("health response must contain exactly should_extend")
    value = payload["should_extend"]
    if type(value) is not bool:
        raise ValueError("should_extend must be a JSON Boolean")
    return value


def parse_diagnosis(text: str) -> Diagnosis:
    payload = _strict_json(text)
    if not isinstance(payload, dict) or set(payload) != {"should_retry", "steering"}:
        raise ValueError("diagnosis must contain exactly should_retry and steering")
    should_retry = payload["should_retry"]
    steering = payload["steering"]
    if type(should_retry) is not bool:
        raise ValueError("should_retry must be a JSON Boolean")
    if should_retry:
        if not isinstance(steering, str) or not steering.strip():
            raise ValueError("retry diagnosis requires non-empty steering")
        return Diagnosis(True, steering.strip())
    if steering is not None:
        raise ValueError("no-retry diagnosis requires null steering")
    return Diagnosis(False, None)


def read_completion_signal(repo: Path) -> bool:
    path = repo.resolve() / COMPLETION_SIGNAL
    try:
        payload = _strict_json(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise CompletionSignalError(f"Cannot read completion signal {path}: {exc}") from exc
    except ValueError as exc:
        raise CompletionSignalError(f"Malformed completion signal {path}: {exc}") from exc
    if not isinstance(payload, dict) or set(payload) != {"isEverythingDone"}:
        raise CompletionSignalError(f"Completion signal {path} must contain exactly isEverythingDone")
    value = payload["isEverythingDone"]
    if type(value) is not bool:
        raise CompletionSignalError(f"Completion signal {path}.isEverythingDone must be a Boolean")
    return value


def save_controller_state(
    state_dir: Path,
    state: ControllerState,
    lifecycle: LifecycleLogger | None = None,
    *,
    reason: str = "state_update",
) -> None:
    if lifecycle is not None:
        lifecycle.emit(
            "controller_state_write_start",
            reason=reason,
            current_iteration=state.current_iteration,
            current_root_pid=state.current_root_pid,
        )
    state_dir.mkdir(parents=True, exist_ok=True)
    target = state_dir / "controller-state.json"
    temporary = state_dir / "controller-state.json.tmp"
    temporary.write_text(json.dumps(asdict(state), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    os.replace(temporary, target)
    if lifecycle is not None:
        lifecycle.emit(
            "controller_state_write_complete",
            reason=reason,
            state_path=str(target),
            current_iteration=state.current_iteration,
            current_root_pid=state.current_root_pid,
        )


def _validated_controller_state(payload: object) -> ControllerState:
    expected = {
        "campaign_id", "task_id", "resolved_tier", "successful_extensions",
        "timeout_retries", "current_iteration", "current_root_pid",
        "assessment_log", "diagnosis_log",
    }
    if not isinstance(payload, dict) or set(payload) != expected:
        raise ValueError("controller state has an unexpected schema")
    for key in ("campaign_id", "task_id", "resolved_tier"):
        if not isinstance(payload[key], str) or not payload[key].strip():
            raise ValueError(f"{key} must be a non-empty string")
    for key, maximum in (("successful_extensions", MAX_EXTENSIONS), ("timeout_retries", MAX_TIMEOUT_RETRIES)):
        value = payload[key]
        if type(value) is not int or not 0 <= value <= maximum:
            raise ValueError(f"{key} must be an integer from 0 through {maximum}")
    for key in ("current_iteration", "current_root_pid"):
        value = payload[key]
        if value is not None and (type(value) is not int or value <= 0):
            raise ValueError(f"{key} must be null or a positive integer")
    for key in ("assessment_log", "diagnosis_log"):
        value = payload[key]
        if value is not None and (not isinstance(value, str) or not value.strip()):
            raise ValueError(f"{key} must be null or a non-empty string")
    return ControllerState(**payload)  # type: ignore[arg-type]


def load_controller_state(
    state_dir: Path,
    campaign_id: str,
    task_id: str,
    resolved_tier: str,
    lifecycle: LifecycleLogger | None = None,
) -> ControllerState:
    target = state_dir / "controller-state.json"
    if not target.exists():
        state = ControllerState(campaign_id, task_id, resolved_tier)
        save_controller_state(state_dir, state, lifecycle, reason="initial_state")
        return state
    try:
        payload = _strict_json(target.read_text(encoding="utf-8"))
        state = _validated_controller_state(payload)
    except (OSError, TypeError, ValueError) as exc:
        raise HardStop(f"Controller state is unreadable or malformed: {target}: {exc}") from exc
    if (state.campaign_id, state.task_id, state.resolved_tier) != (campaign_id, task_id, resolved_tier):
        raise ValueError("controller state belongs to a different campaign, task, or resolved tier")
    return state


def root_prompt(extra: str | None = None) -> str:
    base = """You are the Greek Essence Ralph root orchestrator.

Start by reading exactly these three Ralph entry points:
- .scratch/ralph-loop/RALPH_LOOP.md
- .scratch/ralph-loop/HANDOFF.md
- .scratch/ralph-loop/KNOWLEDGE.md

Inspect repository reality and structured work files yourself. Resume only the authorized campaign task, preserve unrelated work, and stay within repository safety authority. Delegate substantial implementation to greekimpl and independent review to greekreview. Verify filesystem output. Update HANDOFF.md before ending. Set completion-signal.json true only after all managed work and final quality gates succeed. Never reset the signal automatically."""
    return base if not extra else base + "\n\n" + extra


def build_hermes_command(repo: Path, iteration: int, prompt: str | None = None) -> list[str]:
    del repo, iteration
    return ["hermes", "-p", ROOT_PROFILE, "chat", "-Q", "--yolo", "--pass-session-id", "--source", "ralph", "-m", ROOT_MODEL, "--provider", ROOT_PROVIDER, "-q", root_prompt(prompt)]


def _readonly_command(prompt: str) -> list[str]:
    return ["hermes", "-p", ASSESSOR_PROFILE, "chat", "-Q", "--pass-session-id", "--source", "ralph-supervisor", "-m", ASSESSOR_MODEL, "--provider", ROOT_PROVIDER, "-q", prompt]


def health_prompt(state: ControllerState) -> str:
    return f"""You are a read-only health assessor for the active Greek Essence Ralph root.
Campaign: {state.campaign_id}
Task: {state.task_id}
Resolved engineering tier: {state.resolved_tier}

Inspect repository evidence only: the active task contract/status and task-owned diff; report/evidence; review and correction state; recent Ralph/root/child activity; unresolved acceptance criteria, required gates, Blocking/High findings, handoff, dedicated commit, and completion reconciliation. Healthy means recent durable task-attributable progress on necessary unresolved work, including a finite changed recovery strategy or required closure. Evidence against extension includes optional/repeated tests, untied research, repeated reads or failed calls, unnecessary refactoring, speculative abstractions, enterprise-depth expansion, implausible edges, unrelated docs, scope expansion, claimed effort without durable evidence, accepted work with stalled closure, or work beyond the resolved tier.

Do not modify files, implement, create review files, commit, email, or control processes. Return exactly one JSON object and no prose: {{"should_extend": true}} or {{"should_extend": false}}. Uncertainty means false."""


def diagnosis_prompt(state: ControllerState) -> str:
    return f"""You are a read-only timeout diagnosis agent for Greek Essence Ralph.
Campaign: {state.campaign_id}
Task: {state.task_id}
Resolved engineering tier: {state.resolved_tier}
Health renewal already existed, so timeout is evidence that the root exceeded its accepted autonomous budget.

Inspect what is already complete in task status, diff, evidence/reports, reviews, HANDOFF, completion signal, commits, and runtime logs before recommending repetition. Classify closure incomplete, overengineering, review correction incomplete, tool/process stall, scope conflict, human decision required, or unknown failure. Recommend at most one same-task retry only when a narrow safe remaining action exists. Prefer the smallest recovery; preserve task and tier; do not rerun approved implementation/review. Human decision, conflict, or uncertainty means no retry.

Do not mutate files, implement, create reviews, commit, email, or control processes. Return only exactly one of:
{{"should_retry": true, "steering": "Non-empty bounded instruction."}}
{{"should_retry": false, "steering": null}}"""


def build_retry_prompt(state: ControllerState, steering: str, evidence: str) -> str:
    return f"""TIMEOUT RECOVERY FOR THE SAME TASK ONLY.
Original campaign: {state.campaign_id}
Original task: {state.task_id}
Resolved engineering tier: {state.resolved_tier}
Existing completed evidence/review state: {evidence}
Only remaining authorized work: the narrow same-task recovery below.
Diagnosis steering: {steering}
Do not repeat already-approved work. Do not begin another task. Do not delegate new implementation, rerun browser inspection or broad tests, or research when this is closure-only. Verify existing approved state, create the dedicated task commit, reconcile HANDOFF and the existing completion signal, then exit. Stop as soon as required acceptance and closure pass. Existing repository safety boundaries still apply."""


def _event_log(state_dir: Path, prefix: str, iteration: int) -> Path:
    logs = state_dir / "logs"
    logs.mkdir(parents=True, exist_ok=True)
    return logs / f"{prefix}-{iteration:04d}-{time.strftime('%Y%m%d-%H%M%S')}.log"


def run_readonly_assessor(repo: Path, state_dir: Path, prompt: str, timeout: float, prefix: str, iteration: int) -> tuple[str | None, Path]:
    log_path = _event_log(state_dir, prefix, iteration)
    try:
        result = subprocess.run(_readonly_command(prompt), cwd=repo, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding="utf-8", errors="replace", timeout=timeout, check=False)
        output = result.stdout
        log_path.write_text(output, encoding="utf-8")
        return (output if result.returncode == 0 else None), log_path
    except (OSError, subprocess.TimeoutExpired) as exc:
        log_path.write_text(f"{type(exc).__name__}: {exc}\n", encoding="utf-8")
        return None, log_path


def terminate_process_tree(process: subprocess.Popen[str]) -> None:
    if process.poll() is not None:
        return
    if os.name == "nt":
        pid = getattr(process, "pid", None)
        if pid is None:  # Test doubles and nonstandard launchers only.
            process.terminate()
            process.wait(timeout=5)
            return
        result = subprocess.run(["taskkill", "/PID", str(pid), "/T", "/F"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=10, check=False)
        if result.returncode != 0 and process.poll() is None:
            raise ProcessTreeError(f"Owned process tree for PID {pid} may still be running: {result.stdout.strip()}")
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired as exc:
            raise ProcessTreeError(f"Owned process tree for PID {process.pid} survived taskkill") from exc
        return
    process.terminate()
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait(timeout=5)


def supervise_process(process: subprocess.Popen[str], *, lease_seconds: float, assessment_seconds: float, state: ControllerState, assess_fn: Callable[[], bool], persist_fn: Callable[[ControllerState], None], completion_or_stop_fn: Callable[[], bool], monotonic_fn: Callable[[], float] = time.monotonic, terminate_fn: Callable[[subprocess.Popen[str]], None] = terminate_process_tree, event_fn: Callable[[str, dict[str, object]], None] | None = None, heartbeat_seconds: float = 5.0) -> int:
    def emit(event: str, **fields: object) -> None:
        if event_fn is not None:
            event_fn(event, fields)

    lease_start = monotonic_fn()
    assessed_this_lease = False
    while True:
        poll_result = process.poll()
        emit(
            "supervision_poll",
            root_pid=getattr(process, "pid", None),
            poll_result=poll_result,
            elapsed_seconds=monotonic_fn() - lease_start,
        )
        if poll_result is not None:
            return poll_result or 0
        now = monotonic_fn()
        if state.successful_extensions < MAX_EXTENSIONS and not assessed_this_lease and now - lease_start >= assessment_seconds:
            assessed_this_lease = True
            emit("assessment_start", root_pid=getattr(process, "pid", None), elapsed_seconds=now - lease_start)
            extend = assess_fn()
            poll_result = process.poll()
            emit("assessment_complete", root_pid=getattr(process, "pid", None), poll_result=poll_result, should_extend=extend)
            if poll_result is not None:
                return poll_result or 0
            if extend and not completion_or_stop_fn() and state.successful_extensions < MAX_EXTENSIONS:
                state.successful_extensions += 1
                persist_fn(state)
                emit("lease_extended", root_pid=getattr(process, "pid", None), successful_extensions=state.successful_extensions)
                lease_start = monotonic_fn()
                assessed_this_lease = False
                continue
        remaining = lease_seconds - (monotonic_fn() - lease_start)
        if remaining <= 0:
            emit("lease_expired", root_pid=getattr(process, "pid", None), poll_result=process.poll())
            terminate_fn(process)
            raise IterationTimeout("Ralph iteration lease expired")
        until_assessment = remaining
        if state.successful_extensions < MAX_EXTENSIONS and not assessed_this_lease:
            until_assessment = max(0.001, assessment_seconds - (monotonic_fn() - lease_start))
        wait_seconds = min(remaining, until_assessment)
        if event_fn is not None:
            wait_seconds = min(wait_seconds, heartbeat_seconds)
        emit("supervision_wait_start", root_pid=getattr(process, "pid", None), timeout_seconds=wait_seconds)
        try:
            code = process.wait(timeout=wait_seconds)
            emit("supervision_wait_return", root_pid=getattr(process, "pid", None), return_code=code)
            return code
        except subprocess.TimeoutExpired:
            emit("supervision_wait_timeout", root_pid=getattr(process, "pid", None), timeout_seconds=wait_seconds, poll_result=process.poll())
            continue


def _pid_is_running(pid: int) -> bool:
    if pid <= 0:
        return False
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    except (OSError, SystemError):
        return False
    return True


def _acquire_lock(state_dir: Path, lifecycle: LifecycleLogger | None = None) -> Path:
    state_dir.mkdir(parents=True, exist_ok=True)
    lock = state_dir / "ralph.lock"
    if lifecycle is not None:
        lifecycle.emit("lock_acquire_start", lock_path=str(lock), controller_pid=os.getpid())
    for attempt in range(2):
        try:
            descriptor = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            break
        except FileExistsError as exc:
            try:
                owner_pid = int(lock.read_text(encoding="utf-8").strip())
            except (OSError, ValueError) as read_exc:
                if lifecycle is not None:
                    lifecycle.emit("lock_conflict", lock_path=str(lock), reason="unreadable")
                raise LockConflict(f"Ralph loop has an unreadable lock: {lock}") from read_exc
            if attempt or _pid_is_running(owner_pid):
                if lifecycle is not None:
                    lifecycle.emit("lock_conflict", lock_path=str(lock), owner_pid=owner_pid)
                raise LockConflict(f"Ralph loop is already locked by PID {owner_pid}: {lock}") from exc
            if lifecycle is not None:
                lifecycle.emit("stale_lock_remove_start", lock_path=str(lock), owner_pid=owner_pid)
            lock.unlink(missing_ok=True)
            if lifecycle is not None:
                lifecycle.emit("stale_lock_remove_complete", lock_path=str(lock), owner_pid=owner_pid)
    else:
        raise LockConflict(f"Ralph loop could not acquire lock: {lock}")
    with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
        handle.write(str(os.getpid()))
        handle.flush()
    if lifecycle is not None:
        lifecycle.emit("lock_acquired", lock_path=str(lock), controller_pid=os.getpid())
    return lock


def _hard_stop_present(repo: Path) -> bool:
    try:
        return "HARD STOP" in (repo / HANDOFF).read_text(encoding="utf-8")
    except OSError:
        return True


def hermes_executor(repo: Path, state_dir: Path, iteration: int, timeout: float | None, *, assessment_threshold: float = DEFAULT_ASSESSMENT_THRESHOLD, assessor_timeout: float = DEFAULT_ASSESSOR_TIMEOUT, state: ControllerState | None = None, prompt: str | None = None, lifecycle: LifecycleLogger | None = None) -> Path:
    if timeout is None:
        timeout = DEFAULT_ITERATION_TIMEOUT
    state = state or ControllerState("legacy", "active-task", "Tier 2 — Prototype")
    log_path = _event_log(state_dir, "iteration", iteration)
    process: subprocess.Popen[str] | None = None
    with log_path.open("w", encoding="utf-8") as log:
        command = build_hermes_command(repo, iteration, prompt)
        if lifecycle is not None:
            lifecycle.emit(
                "root_launch_start",
                iteration=iteration,
                controller_pid=os.getpid(),
                parent_pid=os.getppid(),
                root_executable=command[0],
                root_profile=ROOT_PROFILE,
                root_model=ROOT_MODEL,
                root_provider=ROOT_PROVIDER,
                iteration_log=str(log_path),
            )
        log.write(json.dumps({"iteration": iteration, "command": command}, ensure_ascii=False) + "\n")
        log.flush()
        process = subprocess.Popen(command, cwd=repo, stdout=log, stderr=subprocess.STDOUT, text=True, encoding="utf-8", errors="replace")
        primary_exception = False
        try:
            if lifecycle is not None:
                lifecycle.emit(
                    "root_launched",
                    iteration=iteration,
                    controller_pid=os.getpid(),
                    root_pid=getattr(process, "pid", None),
                    root_executable=command[0],
                    root_profile=ROOT_PROFILE,
                    root_model=ROOT_MODEL,
                    root_provider=ROOT_PROVIDER,
                )
            state.current_iteration = iteration
            state.current_root_pid = getattr(process, "pid", None)
            save_controller_state(state_dir, state, lifecycle, reason="root_pid_set")

            def assess() -> bool:
                output, path = run_readonly_assessor(repo, state_dir, health_prompt(state), assessor_timeout, "assessment", iteration)
                state.assessment_log = str(path)
                save_controller_state(state_dir, state, lifecycle, reason="assessment_log_set")
                if output is None:
                    return False
                try:
                    return parse_health_response(output)
                except ValueError:
                    return False

            code = supervise_process(
                process,
                lease_seconds=timeout,
                assessment_seconds=assessment_threshold,
                state=state,
                assess_fn=assess,
                persist_fn=lambda value: save_controller_state(state_dir, value, lifecycle, reason="lease_extension"),
                completion_or_stop_fn=lambda: read_completion_signal(repo) or _hard_stop_present(repo),
                event_fn=(lambda event, fields: lifecycle.emit(event, iteration=iteration, **fields)) if lifecycle is not None else None,
            )
            if lifecycle is not None:
                lifecycle.emit(
                    "root_poll_result",
                    iteration=iteration,
                    root_pid=getattr(process, "pid", None),
                    poll_result=process.poll(),
                    supervised_return_code=code,
                )
        except IterationTimeout as exc:
            primary_exception = True
            if lifecycle is not None:
                lifecycle.emit("executor_exception", iteration=iteration, exception_type=type(exc).__name__, root_pid=getattr(process, "pid", None), poll_result=process.poll())
            if process.poll() is None:
                try:
                    terminate_process_tree(process)
                except BaseException as cleanup_exc:
                    exc.add_note(f"root cleanup also failed: {type(cleanup_exc).__name__}: {cleanup_exc}")
                    if lifecycle is not None:
                        lifecycle.emit("root_cleanup_failed", iteration=iteration, exception_type=type(cleanup_exc).__name__, root_pid=getattr(process, "pid", None))
            raise IterationTimeout(
                f"Ralph iteration {iteration} timed out; log: {log_path}"
            ) from exc
        except BaseException as exc:
            primary_exception = True
            if lifecycle is not None:
                lifecycle.emit("executor_exception", iteration=iteration, exception_type=type(exc).__name__, root_pid=getattr(process, "pid", None), poll_result=process.poll())
            if process.poll() is None:
                try:
                    terminate_process_tree(process)
                except BaseException as cleanup_exc:
                    exc.add_note(f"root cleanup also failed: {type(cleanup_exc).__name__}: {cleanup_exc}")
                    if lifecycle is not None:
                        lifecycle.emit("root_cleanup_failed", iteration=iteration, exception_type=type(cleanup_exc).__name__, root_pid=getattr(process, "pid", None))
            raise
        finally:
            if lifecycle is not None:
                lifecycle.emit("executor_finally_enter", iteration=iteration, root_pid=getattr(process, "pid", None), poll_result=process.poll())
                lifecycle.emit("root_pid_clear_start", iteration=iteration, root_pid=state.current_root_pid)
            state.current_root_pid = None
            clear_error: BaseException | None = None
            try:
                save_controller_state(state_dir, state, lifecycle, reason="root_pid_clear")
            except BaseException as exc:
                clear_error = exc
                if lifecycle is not None:
                    lifecycle.emit("root_pid_clear_failed", iteration=iteration, exception_type=type(exc).__name__)
            if lifecycle is not None:
                if clear_error is None:
                    lifecycle.emit("root_pid_clear_complete", iteration=iteration, root_pid=None)
                lifecycle.emit("executor_finally_exit", iteration=iteration, root_pid=None, poll_result=process.poll())
            if clear_error is not None and not primary_exception:
                raise clear_error
    if code != 0:
        raise HermesProcessError(f"Hermes iteration {iteration} exited {code}; log: {log_path}")
    return log_path


def run_preflight(repo: Path, task_id: str) -> bool:
    try:
        result = subprocess.run([sys.executable, str(repo / PREFLIGHT), "--repo", str(repo), "--target", task_id], cwd=repo, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=60, check=False)
        payload = _strict_json(result.stdout)
        return (
            result.returncode == 0
            and isinstance(payload, dict)
            and payload.get("status") == "STRUCTURAL_PASS"
            and payload.get("warnings") == []
            and payload.get("launch_performed") is False
        )
    except (OSError, subprocess.TimeoutExpired, ValueError):
        return False


def run_loop(repo: Path, *, max_iterations: int | None = None, iteration_timeout: float | None = DEFAULT_ITERATION_TIMEOUT, read_signal_fn: Callable[[Path], bool] | None = None, execute_fn: Callable[[int, float | None], object] | None = None, state_dir: Path | None = None, campaign_id: str = "legacy", task_id: str = "active-task", resolved_tier: str = "Tier 2 — Prototype", assessment_threshold: float = DEFAULT_ASSESSMENT_THRESHOLD, assessor_timeout: float = DEFAULT_ASSESSOR_TIMEOUT, diagnosis_fn: Callable[[ControllerState, int], Diagnosis | None] | None = None, preflight_fn: Callable[[], bool] | None = None, evidence_summary: str = "Inspect existing repository evidence and approved review state.") -> LoopOutcome:
    if max_iterations is not None and max_iterations < 0:
        raise ValueError("max_iterations must be zero or greater")
    if iteration_timeout is not None and iteration_timeout <= 0:
        raise ValueError("iteration_timeout must be greater than zero")
    if assessment_threshold <= 0 or (iteration_timeout is not None and assessment_threshold >= iteration_timeout):
        raise ValueError("assessment threshold must be positive and less than timeout")
    repo = repo.resolve(); state_dir = (state_dir or default_state_dir()).resolve()
    read_signal_fn = read_signal_fn or read_completion_signal
    lifecycle = LifecycleLogger(_lifecycle_log(state_dir), campaign_id, task_id, resolved_tier)
    lifecycle.emit(
        "controller_start",
        controller_pid=os.getpid(),
        parent_pid=os.getppid(),
        repo=str(repo),
        state_dir=str(state_dir),
        max_iterations=max_iterations,
    )
    lock: Path | None = None
    try:
        lock = _acquire_lock(state_dir, lifecycle)
        state = load_controller_state(state_dir, campaign_id, task_id, resolved_tier, lifecycle)
        iteration = 0
        retry_prompt: str | None = None
        while True:
            if read_signal_fn(repo):
                lifecycle.emit("loop_return", outcome=LoopOutcome.COMPLETE.value, reason="completion_signal_true", iteration=iteration)
                return LoopOutcome.COMPLETE
            if max_iterations is not None and iteration >= max_iterations:
                lifecycle.emit("loop_return", outcome=LoopOutcome.LIMIT_REACHED.value, reason="iteration_limit", iteration=iteration)
                return LoopOutcome.LIMIT_REACHED
            iteration += 1
            lifecycle.emit("iteration_start", iteration=iteration, controller_pid=os.getpid())
            executor = execute_fn or (lambda number, lease: hermes_executor(repo, state_dir, number, lease, assessment_threshold=assessment_threshold, assessor_timeout=assessor_timeout, state=state, prompt=retry_prompt, lifecycle=lifecycle))
            try:
                executor(iteration, iteration_timeout)
                lifecycle.emit("iteration_executor_return", iteration=iteration)
                retry_prompt = None
            except IterationTimeout:
                lifecycle.emit("iteration_timeout", iteration=iteration, current_root_pid=state.current_root_pid)
                if read_signal_fn(repo):
                    lifecycle.emit("loop_return", outcome=LoopOutcome.COMPLETE.value, reason="completion_after_timeout", iteration=iteration)
                    return LoopOutcome.COMPLETE
                if state.timeout_retries >= MAX_TIMEOUT_RETRIES:
                    raise HardStop("Second timeout for the task; automatic retry denied")
                if diagnosis_fn is None:
                    output, path = run_readonly_assessor(repo, state_dir, diagnosis_prompt(state), assessor_timeout, "diagnosis", iteration)
                    state.diagnosis_log = str(path); save_controller_state(state_dir, state, lifecycle, reason="diagnosis_log_set")
                    try:
                        diagnosis = parse_diagnosis(output) if output is not None else None
                    except ValueError:
                        diagnosis = None
                else:
                    diagnosis = diagnosis_fn(state, iteration)
                if diagnosis is None or not diagnosis.should_retry:
                    raise HardStop("Timeout diagnosis did not authorize a safe retry")
                if not (preflight_fn or (lambda: run_preflight(repo, task_id)))():
                    raise HardStop("Mandatory preflight failed; retry denied")
                state.timeout_retries += 1; save_controller_state(state_dir, state, lifecycle, reason="timeout_retry_increment")
                retry_prompt = build_retry_prompt(state, diagnosis.steering or "", evidence_summary)
                if max_iterations is not None:
                    max_iterations += 1
    except BaseException as exc:
        lifecycle.emit("controller_exception", controller_pid=os.getpid(), exception_type=type(exc).__name__)
        raise
    finally:
        if lock is not None:
            lifecycle.emit("lock_release_start", lock_path=str(lock), controller_pid=os.getpid())
            lock.unlink(missing_ok=True)
            lifecycle.emit("lock_release_complete", lock_path=str(lock), controller_pid=os.getpid(), lock_exists=lock.exists())
        lifecycle.emit("controller_exit", controller_pid=os.getpid(), parent_pid=os.getppid(), lock_acquired=lock is not None)


def _print_error(outcome: str, error: BaseException) -> None:
    print(json.dumps({"outcome": outcome, "error": str(error)}, indent=2))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--max-iterations", type=int)
    parser.add_argument("--iteration-timeout", type=float, default=DEFAULT_ITERATION_TIMEOUT)
    parser.add_argument("--assessment-threshold", type=float, default=DEFAULT_ASSESSMENT_THRESHOLD)
    parser.add_argument("--assessor-timeout", type=float, default=DEFAULT_ASSESSOR_TIMEOUT)
    parser.add_argument("--campaign-id", default="bootstrap-active-campaign")
    parser.add_argument("--task-id", default="active-task")
    parser.add_argument("--resolved-tier", default="Tier 2 — Prototype")
    parser.add_argument("--state-dir", type=Path, default=default_state_dir())
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    try:
        if args.dry_run:
            done = read_completion_signal(args.repo)
            print(json.dumps({"completion_signal": {"isEverythingDone": done}, "command": build_hermes_command(args.repo, 1), "supervision": {"assessment_threshold": args.assessment_threshold, "iteration_timeout": args.iteration_timeout, "max_extensions": MAX_EXTENSIONS, "max_timeout_retries": MAX_TIMEOUT_RETRIES}}, indent=2, ensure_ascii=False))
            return 0
        outcome = run_loop(args.repo, max_iterations=args.max_iterations, iteration_timeout=args.iteration_timeout, state_dir=args.state_dir, campaign_id=args.campaign_id, task_id=args.task_id, resolved_tier=args.resolved_tier, assessment_threshold=args.assessment_threshold, assessor_timeout=args.assessor_timeout)
        print(json.dumps({"outcome": outcome.value}, indent=2))
        return 0 if outcome is LoopOutcome.COMPLETE else 2
    except CompletionSignalError as exc:
        _print_error("INVALID_SIGNAL", exc); return 3
    except HermesProcessError as exc:
        _print_error("HERMES_FAILED", exc); return 4
    except IterationTimeout as exc:
        _print_error("TIMEOUT", exc); return 5
    except (HardStop, ProcessTreeError) as exc:
        _print_error("HARD_STOP", exc); return 7
    except LockConflict as exc:
        _print_error("LOCK_CONFLICT", exc); return 6
    except KeyboardInterrupt as exc:
        _print_error("INTERRUPTED", exc); return 130
    except Exception as exc:
        _print_error("ERROR", exc); return 1


if __name__ == "__main__":
    sys.exit(main())

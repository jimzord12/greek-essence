#!/usr/bin/env python3
"""Run fresh Greek Essence Ralph root iterations until the completion signal is true."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from enum import Enum
from pathlib import Path
from typing import Callable

sys.dont_write_bytecode = True

ROOT_PROFILE = "greekroot"
ROOT_MODEL = "gpt-5.6-sol"
ROOT_PROVIDER = "openai-codex"
COMPLETION_SIGNAL = Path(".scratch") / "ralph-loop" / "completion-signal.json"
DEFAULT_ITERATION_TIMEOUT = 3600.0


class RalphError(RuntimeError):
    """Base class for operational Ralph failures."""


class CompletionSignalError(RalphError):
    """The completion signal is missing, unreadable, or invalid."""


class HermesProcessError(RalphError):
    """Hermes returned a nonzero exit status."""


class IterationTimeout(RalphError):
    """A root iteration exceeded its configured timeout."""


class LockConflict(RalphError):
    """Another Ralph process owns the operational lock."""


class LoopOutcome(str, Enum):
    COMPLETE = "COMPLETE"
    LIMIT_REACHED = "LIMIT_REACHED"


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


def read_completion_signal(repo: Path) -> bool:
    """Read the exact one-property Boolean completion signal."""
    path = repo.resolve() / COMPLETION_SIGNAL
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise CompletionSignalError(f"Cannot read completion signal {path}: {exc}") from exc
    try:
        payload = json.loads(text, object_pairs_hook=_pairs_without_duplicates)
    except (json.JSONDecodeError, ValueError) as exc:
        raise CompletionSignalError(f"Malformed completion signal {path}: {exc}") from exc
    if not isinstance(payload, dict) or set(payload) != {"isEverythingDone"}:
        raise CompletionSignalError(
            f"Completion signal {path} must contain exactly isEverythingDone"
        )
    value = payload["isEverythingDone"]
    if type(value) is not bool:
        raise CompletionSignalError(
            f"Completion signal {path}.isEverythingDone must be a Boolean"
        )
    return value


def root_prompt() -> str:
    return """You are the Greek Essence Ralph root orchestrator.

Start by reading exactly these three Ralph entry points:
- .scratch/ralph-loop/RALPH_LOOP.md
- .scratch/ralph-loop/HANDOFF.md
- .scratch/ralph-loop/KNOWLEDGE.md

Inspect repository reality and the structured work files yourself. Select or resume one coherent highest-priority work unit, preserve unrelated work, and stay within the repository's existing safety authority. Delegate substantial implementation to the greekimpl profile (gpt-5.6-luna, high) and independent review to the greekreview profile (gpt-5.6-terra, high). Wait for real child completion and verify filesystem output; request compact summaries with verdict, findings, changed files, commands/results, and next action. Update HANDOFF.md before ending this iteration and add only durable reviewed discoveries to KNOWLEDGE.md. Set .scratch/ralph-loop/completion-signal.json to {"isEverythingDone": true} only after all managed work and final quality gates succeed. Never reset the signal automatically."""


def build_hermes_command(repo: Path, iteration: int) -> list[str]:
    """Build a fresh, non-resumed Sol root command for one iteration."""
    del repo, iteration
    return [
        "hermes",
        "-p",
        ROOT_PROFILE,
        "chat",
        "-Q",
        "--yolo",
        "--pass-session-id",
        "--source",
        "ralph",
        "-m",
        ROOT_MODEL,
        "--provider",
        ROOT_PROVIDER,
        "-q",
        root_prompt(),
    ]


def _event_log(state_dir: Path, iteration: int) -> Path:
    logs = state_dir / "logs"
    logs.mkdir(parents=True, exist_ok=True)
    stamp = time.strftime("%Y%m%d-%H%M%S")
    return logs / f"iteration-{iteration:04d}-{stamp}.log"


def _terminate_child(process: subprocess.Popen[str]) -> None:
    if process.poll() is not None:
        return
    process.terminate()
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait(timeout=5)


def hermes_executor(
    repo: Path,
    state_dir: Path,
    iteration: int,
    timeout: float | None,
) -> Path:
    """Run one fresh root process and return its durable event-log path."""
    log_path = _event_log(state_dir, iteration)
    command = build_hermes_command(repo, iteration)
    process: subprocess.Popen[str] | None = None
    with log_path.open("w", encoding="utf-8") as log:
        log.write(json.dumps({"iteration": iteration, "command": command}, ensure_ascii=False) + "\n")
        log.flush()
        try:
            process = subprocess.Popen(
                command,
                cwd=repo,
                stdout=log,
                stderr=subprocess.STDOUT,
                text=True,
                encoding="utf-8",
                errors="replace",
            )
            try:
                return_code = process.wait(timeout=timeout)
            except subprocess.TimeoutExpired as exc:
                _terminate_child(process)
                raise IterationTimeout(
                    f"Ralph iteration {iteration} timed out; log: {log_path}"
                ) from exc
        except BaseException:
            if process is not None:
                _terminate_child(process)
            raise

    if return_code != 0:
        raise HermesProcessError(
            f"Hermes iteration {iteration} exited {return_code}; log: {log_path}"
        )
    return log_path


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


def _acquire_lock(state_dir: Path) -> Path:
    state_dir.mkdir(parents=True, exist_ok=True)
    lock = state_dir / "ralph.lock"
    for attempt in range(2):
        try:
            descriptor = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            break
        except FileExistsError as exc:
            try:
                owner_pid = int(lock.read_text(encoding="utf-8").strip())
            except (OSError, ValueError) as read_exc:
                raise LockConflict(f"Ralph loop has an unreadable lock: {lock}") from read_exc
            if attempt or _pid_is_running(owner_pid):
                raise LockConflict(f"Ralph loop is already locked by PID {owner_pid}: {lock}") from exc
            lock.unlink(missing_ok=True)
    else:
        raise LockConflict(f"Ralph loop could not acquire lock: {lock}")
    with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
        handle.write(str(os.getpid()))
    return lock


def run_loop(
    repo: Path,
    *,
    max_iterations: int | None = None,
    iteration_timeout: float | None = DEFAULT_ITERATION_TIMEOUT,
    read_signal_fn: Callable[[Path], bool] | None = None,
    execute_fn: Callable[[int, float | None], object] | None = None,
    state_dir: Path | None = None,
) -> LoopOutcome:
    """Run fresh root iterations until true or an operational limit/failure."""
    if max_iterations is not None and max_iterations < 0:
        raise ValueError("max_iterations must be zero or greater")
    if iteration_timeout is not None and iteration_timeout <= 0:
        raise ValueError("iteration_timeout must be greater than zero")

    repo = repo.resolve()
    state_dir = (state_dir or default_state_dir()).resolve()
    read_signal_fn = read_signal_fn or read_completion_signal
    execute_fn = execute_fn or (
        lambda iteration, timeout: hermes_executor(repo, state_dir, iteration, timeout)
    )
    lock = _acquire_lock(state_dir)
    try:
        iteration = 0
        while True:
            if read_signal_fn(repo):
                return LoopOutcome.COMPLETE
            if max_iterations is not None and iteration >= max_iterations:
                return LoopOutcome.LIMIT_REACHED
            iteration += 1
            execute_fn(iteration, iteration_timeout)
    finally:
        lock.unlink(missing_ok=True)


def _print_error(outcome: str, error: BaseException) -> None:
    print(json.dumps({"outcome": outcome, "error": str(error)}, indent=2))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--max-iterations", type=int)
    parser.add_argument(
        "--iteration-timeout",
        type=float,
        default=DEFAULT_ITERATION_TIMEOUT,
        help="Seconds allowed for each root iteration (default: 3600).",
    )
    parser.add_argument("--state-dir", type=Path, default=default_state_dir())
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    try:
        if args.dry_run:
            done = read_completion_signal(args.repo)
            print(
                json.dumps(
                    {
                        "completion_signal": {"isEverythingDone": done},
                        "command": build_hermes_command(args.repo, 1),
                    },
                    indent=2,
                    ensure_ascii=False,
                )
            )
            return 0
        outcome = run_loop(
            args.repo,
            max_iterations=args.max_iterations,
            iteration_timeout=args.iteration_timeout,
            state_dir=args.state_dir,
        )
        print(json.dumps({"outcome": outcome.value}, indent=2))
        return 0 if outcome is LoopOutcome.COMPLETE else 2
    except CompletionSignalError as exc:
        _print_error("INVALID_SIGNAL", exc)
        return 3
    except HermesProcessError as exc:
        _print_error("HERMES_FAILED", exc)
        return 4
    except IterationTimeout as exc:
        _print_error("TIMEOUT", exc)
        return 5
    except LockConflict as exc:
        _print_error("LOCK_CONFLICT", exc)
        return 6
    except KeyboardInterrupt as exc:
        _print_error("INTERRUPTED", exc)
        return 130
    except Exception as exc:  # pragma: no cover - final CLI safety net
        _print_error("ERROR", exc)
        return 1


if __name__ == "__main__":
    sys.exit(main())

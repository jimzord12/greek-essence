#!/usr/bin/env python3
"""Run the Greek Essence bootstrap one reviewed work unit at a time with Hermes."""

from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import subprocess
import sys
import time
from enum import Enum
from pathlib import Path
from typing import Callable

sys.dont_write_bytecode = True

from check_state import Result, State, inspect_repository


ROOT_PROFILE = "greekroot"
ROOT_MODEL = "gpt-5.6-sol"
ROOT_PROVIDER = "openai-codex"
OPERATOR_AUTHORIZATION = (
    "The operator pre-authorizes task-owned repository-local creations, edits, overwrites, and "
    "deletions that are explicitly required by the active bootstrap contract or reviewer findings. "
    "Stop for changes outside this repository, unrelated deletion, credentials, system changes, "
    "pushes, deployments, remote changes, or Git history rewriting."
)


def _fresh_prompt(work_id: str) -> str:
    if work_id.startswith("PHASE-"):
        phase = work_id.removeprefix("PHASE-")
        return (
            f"Execute only the Phase {phase} review gate according to .scratch/bootstrap/protocol.md. "
            "Use a fresh greekreview Hermes profile session for the independent phase review. "
            "Complete the phase report, numbered review and any required response/re-review cycle; "
            "update dashboard, phase status and Ralph handoff; create the dedicated phase-review commit. "
            "Do not start the next task. " + OPERATOR_AUTHORIZATION
        )
    return (
        f"Execute exactly bootstrap task {work_id} according to .scratch/bootstrap/BOOTSTRAP-AGENTS.md "
        "and .scratch/bootstrap/protocol.md. Use a fresh greekimpl Hermes profile session for implementation "
        "and a different fresh greekreview profile session for review. Return corrections to the original "
        "implementer and re-review to the same reviewer. Complete evidence, closure, tracking, handoff and the "
        "dedicated Task-ID commit. Do not start another task. " + OPERATOR_AUTHORIZATION
    )


def _resume_prompt(work_id: str, repair_reasons: list[str]) -> str:
    prompt = (
        f"Resume and finish only {work_id}. Preserve the existing implementer and reviewer session identities, "
        "complete all required correction/re-review or phase-review cycles, update closure records and commit. "
        "Do not start another work unit. " + OPERATOR_AUTHORIZATION
    )
    if repair_reasons:
        prompt += "\n\nDeterministic postcondition failures to repair:\n- " + "\n- ".join(repair_reasons)
    return prompt


class LoopOutcome(str, Enum):
    COMPLETE = "COMPLETE"
    LIMIT_REACHED = "LIMIT_REACHED"
    BLOCKED = "BLOCKED"
    INCONSISTENT = "INCONSISTENT"


InspectFn = Callable[[], Result]
ExecuteFn = Callable[[str, str | None, list[str]], str]


def default_state_dir() -> Path:
    base = Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData" / "Local"))
    return base / "hermes" / "ralph" / "greek-essence"


def _read_runtime_state(state_dir: Path) -> dict[str, object]:
    path = state_dir / "state.json"
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}


def _write_runtime_state(state_dir: Path, payload: dict[str, object]) -> None:
    state_dir.mkdir(parents=True, exist_ok=True)
    target = state_dir / "state.json"
    temporary = state_dir / "state.json.tmp"
    temporary.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    temporary.replace(target)


def _extract_hermes_session_id(line: str) -> str | None:
    match = re.match(r"^session_id:\s*(\S+)\s*$", line.strip())
    return match.group(1) if match else None


def _normalise_path(value: str | Path) -> str:
    return str(Path(value).resolve()).replace("\\", "/").rstrip("/").lower()


def _discover_hermes_session_id(
    database: Path,
    repo: Path,
    started_after: float,
    *,
    timeout: float = 30,
) -> str | None:
    """Discover a just-started root session before quiet CLI output is emitted."""
    deadline = time.monotonic() + timeout
    expected_repo = _normalise_path(repo)
    while True:
        if database.exists():
            try:
                connection = sqlite3.connect(database, timeout=1)
                rows = connection.execute(
                    "SELECT id, git_repo_root, cwd FROM sessions "
                    "WHERE source = ? AND started_at >= ? ORDER BY started_at DESC",
                    ("ralph", started_after),
                ).fetchall()
                connection.close()
                for session, git_root, cwd in rows:
                    candidates = [value for value in (git_root, cwd) if value]
                    if any(_normalise_path(value) == expected_repo for value in candidates):
                        return str(session)
            except sqlite3.Error:
                pass
        if time.monotonic() >= deadline:
            return None
        time.sleep(0.1)


def build_hermes_command(
    repo: Path,
    work_id: str,
    session_id: str | None,
    repair_reasons: list[str],
) -> list[str]:
    command = [
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
    ]
    if session_id:
        command.extend(["--resume", session_id])
    command.extend(["-q", _resume_prompt(work_id, repair_reasons) if session_id else _fresh_prompt(work_id)])
    return command


def hermes_executor(
    repo: Path,
    state_dir: Path,
    work_id: str,
    session_id: str | None,
    repair_reasons: list[str],
) -> str:
    state_dir.mkdir(parents=True, exist_ok=True)
    logs = state_dir / "logs"
    logs.mkdir(exist_ok=True)
    stamp = time.strftime("%Y%m%d-%H%M%S")
    event_log = logs / f"{work_id}-{stamp}.log"
    command = build_hermes_command(repo, work_id, session_id, repair_reasons)

    discovered_session = session_id
    started_after = time.time()
    with event_log.open("w", encoding="utf-8") as log:
        process = subprocess.Popen(
            command,
            cwd=repo,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        assert process.stdout is not None
        if not discovered_session:
            local_app_data = Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData" / "Local"))
            profile_database = local_app_data / "hermes" / "profiles" / ROOT_PROFILE / "state.db"
            discovered_session = _discover_hermes_session_id(
                profile_database,
                repo,
                started_after,
            )
            if discovered_session:
                _write_runtime_state(
                    state_dir,
                    {
                        "work_id": work_id,
                        "hermes_session_id": discovered_session,
                        "last_event_log": str(event_log),
                    },
                )
        for line in process.stdout:
            log.write(line)
            log.flush()
            found = _extract_hermes_session_id(line)
            if found and found != discovered_session:
                discovered_session = found
                _write_runtime_state(
                    state_dir,
                    {
                        "work_id": work_id,
                        "hermes_session_id": discovered_session,
                        "last_event_log": str(event_log),
                    },
                )
        return_code = process.wait()

    if return_code != 0:
        raise RuntimeError(f"Hermes exited {return_code}; log: {event_log}")
    if not discovered_session:
        raise RuntimeError(f"Hermes did not emit a session ID; log: {event_log}")
    return discovered_session


def run_loop(
    repo: Path,
    *,
    max_tasks: int | None = None,
    max_repair_attempts: int = 2,
    inspect_fn: InspectFn | None = None,
    execute_fn: ExecuteFn | None = None,
    state_dir: Path | None = None,
) -> LoopOutcome:
    repo = repo.resolve()
    state_dir = state_dir or default_state_dir()
    inspect_fn = inspect_fn or (lambda: inspect_repository(repo))
    execute_fn = execute_fn or (
        lambda work_id, session_id, reasons: hermes_executor(
            repo, state_dir, work_id, session_id, reasons
        )
    )

    completed_this_run = 0
    repair_attempts = 0
    result = inspect_fn()

    while True:
        if result.state == State.COMPLETE:
            return LoopOutcome.COMPLETE
        if result.state == State.BLOCKED:
            return LoopOutcome.BLOCKED
        if (
            max_tasks is not None
            and completed_this_run >= max_tasks
            and result.state == State.READY
        ):
            return LoopOutcome.LIMIT_REACHED

        runtime = _read_runtime_state(state_dir)
        saved_work = runtime.get("work_id")
        saved_session = runtime.get("hermes_session_id")

        if result.state == State.INCONSISTENT:
            if not saved_work or not saved_session or repair_attempts >= max_repair_attempts:
                return LoopOutcome.INCONSISTENT
            work_id = str(saved_work)
            session_id = str(saved_session)
            repair_attempts += 1
        elif result.state == State.RESUMABLE:
            if saved_work != result.task or not saved_session:
                return LoopOutcome.INCONSISTENT
            work_id = str(result.task)
            session_id = str(saved_session)
        elif result.state == State.PHASE_REVIEW:
            work_id = str(result.task)
            session_id = str(saved_session) if saved_work == work_id and saved_session else None
            repair_attempts = 0
        elif result.state == State.READY:
            work_id = str(result.task)
            session_id = None
            repair_attempts = 0
        else:
            return LoopOutcome.INCONSISTENT

        before = result
        session_id = execute_fn(work_id, session_id, result.reasons)
        _write_runtime_state(
            state_dir,
            {
                "work_id": work_id,
                "hermes_session_id": session_id,
                "last_state": result.state.value,
            },
        )
        result = inspect_fn()

        if result.completed_tasks > before.completed_tasks:
            completed_this_run += result.completed_tasks - before.completed_tasks
            repair_attempts = 0
            _write_runtime_state(
                state_dir,
                {
                    "last_completed_work": work_id,
                    "hermes_session_id": None,
                    "last_state": result.state.value,
                },
            )
        elif before.state == State.PHASE_REVIEW and result.state == State.READY:
            repair_attempts = 0
            _write_runtime_state(
                state_dir,
                {
                    "last_completed_work": work_id,
                    "hermes_session_id": None,
                    "last_state": result.state.value,
                },
            )
        elif result.state in {State.READY, State.PHASE_REVIEW}:
            return LoopOutcome.INCONSISTENT


def _acquire_lock(state_dir: Path) -> Path:
    state_dir.mkdir(parents=True, exist_ok=True)
    lock = state_dir / "ralph.lock"
    try:
        descriptor = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError as exc:
        raise RuntimeError(f"Ralph loop is already locked: {lock}") from exc
    with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
        handle.write(str(os.getpid()))
    return lock


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--max-tasks", type=int)
    parser.add_argument("--max-repair-attempts", type=int, default=2)
    parser.add_argument("--state-dir", type=Path, default=default_state_dir())
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    if args.dry_run:
        result = inspect_repository(args.repo, allow_dirty=True)
        print(result.to_json())
        return 0

    lock = _acquire_lock(args.state_dir)
    try:
        outcome = run_loop(
            args.repo,
            max_tasks=args.max_tasks,
            max_repair_attempts=args.max_repair_attempts,
            state_dir=args.state_dir,
        )
        print(json.dumps({"outcome": outcome.value}, indent=2))
        return 0 if outcome in {LoopOutcome.COMPLETE, LoopOutcome.LIMIT_REACHED} else 1
    finally:
        lock.unlink(missing_ok=True)


if __name__ == "__main__":
    sys.exit(main())

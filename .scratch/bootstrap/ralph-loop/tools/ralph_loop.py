#!/usr/bin/env python3
"""Run the Greek Essence bootstrap one fully reviewed Codex task at a time."""

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

from check_state import Result, State, inspect_repository


PROMPT = "Use $bootstrap-next to execute exactly one valid bootstrap task."
RESUME_PROMPT = (
    "Resume and finish the active bootstrap task according to the protocol. "
    "Preserve the original implementer and reviewer identities, complete all review "
    "cycles, update handoff and knowledge records, commit the task, and do not start another task."
)


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


def _extract_session_id(event: object) -> str | None:
    if not isinstance(event, dict):
        return None
    if event.get("type") == "thread.started":
        value = event.get("thread_id") or event.get("threadId")
        return str(value) if value else None
    thread = event.get("thread")
    if isinstance(thread, dict) and event.get("type") == "thread.started":
        value = thread.get("id")
        return str(value) if value else None
    return None


def build_codex_command(repo: Path, session_id: str | None, repair_reasons: list[str]) -> list[str]:
    if session_id:
        prompt = RESUME_PROMPT
        if repair_reasons:
            prompt += "\n\nDeterministic postcondition failures to repair:\n- " + "\n- ".join(repair_reasons)
        return [
            "codex",
            "exec",
            "resume",
            "-c",
            'windows.sandbox="elevated"',
            "--json",
            session_id,
            prompt,
        ]
    return [
        "codex",
        "exec",
        "-C",
        str(repo),
        "-c",
        'windows.sandbox="elevated"',
        "--sandbox",
        "workspace-write",
        "--json",
        PROMPT,
    ]


def codex_executor(repo: Path, state_dir: Path, task: str, session_id: str | None, repair_reasons: list[str]) -> str:
    state_dir.mkdir(parents=True, exist_ok=True)
    logs = state_dir / "logs"
    logs.mkdir(exist_ok=True)
    stamp = time.strftime("%Y%m%d-%H%M%S")
    event_log = logs / f"{task}-{stamp}.jsonl"
    last_message = logs / f"{task}-{stamp}-last-message.md"
    command = build_codex_command(repo, session_id, repair_reasons)

    discovered_session = session_id
    final_message: str | None = None
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
        for line in process.stdout:
            log.write(line)
            log.flush()
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue
            found = _extract_session_id(event)
            if found and found != discovered_session:
                discovered_session = found
                _write_runtime_state(
                    state_dir,
                    {
                        "task_id": task,
                        "codex_session_id": discovered_session,
                        "last_event_log": str(event_log),
                    },
                )
            if isinstance(event, dict) and event.get("type") == "item.completed":
                item = event.get("item")
                if isinstance(item, dict) and item.get("type") == "agent_message":
                    text = item.get("text")
                    if isinstance(text, str):
                        final_message = text
        return_code = process.wait()

    if return_code != 0:
        raise RuntimeError(f"Codex exited {return_code}; log: {event_log}")
    if not discovered_session:
        raise RuntimeError(f"Codex did not emit a session ID; log: {event_log}")
    if final_message:
        last_message.write_text(final_message, encoding="utf-8")
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
        lambda task, session_id, reasons: codex_executor(
            repo, state_dir, task, session_id, reasons
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
        if max_tasks is not None and completed_this_run >= max_tasks:
            return LoopOutcome.LIMIT_REACHED

        runtime = _read_runtime_state(state_dir)
        saved_task = runtime.get("task_id")
        saved_session = runtime.get("codex_session_id")

        if result.state == State.INCONSISTENT:
            if not saved_task or not saved_session or repair_attempts >= max_repair_attempts:
                return LoopOutcome.INCONSISTENT
            task = str(saved_task)
            session_id = str(saved_session)
            repair_attempts += 1
        elif result.state == State.RESUMABLE:
            if saved_task != result.task or not saved_session:
                return LoopOutcome.INCONSISTENT
            task = str(result.task)
            session_id = str(saved_session)
        else:
            task = str(result.task)
            session_id = None
            repair_attempts = 0

        before_done = result.completed_tasks
        session_id = execute_fn(task, session_id, result.reasons)
        _write_runtime_state(
            state_dir,
            {
                "task_id": task,
                "codex_session_id": session_id,
                "last_state": result.state.value,
            },
        )
        result = inspect_fn()

        if result.completed_tasks > before_done:
            completed_this_run += result.completed_tasks - before_done
            repair_attempts = 0
            if result.state in {State.READY, State.COMPLETE}:
                _write_runtime_state(
                    state_dir,
                    {
                        "last_completed_task": task,
                        "codex_session_id": None,
                        "last_state": result.state.value,
                    },
                )
        elif result.state == State.READY:
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

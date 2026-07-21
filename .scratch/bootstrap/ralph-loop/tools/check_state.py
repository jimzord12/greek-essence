#!/usr/bin/env python3
"""Deterministically classify the Greek Essence bootstrap repository state."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import asdict, dataclass
from enum import Enum
from pathlib import Path
from typing import Iterable


class State(str, Enum):
    COMPLETE = "COMPLETE"
    READY = "READY"
    RESUMABLE = "RESUMABLE"
    BLOCKED = "BLOCKED"
    INCONSISTENT = "INCONSISTENT"


EXIT_CODES = {
    State.COMPLETE: 0,
    State.READY: 10,
    State.RESUMABLE: 11,
    State.BLOCKED: 20,
    State.INCONSISTENT: 30,
}


@dataclass(frozen=True)
class Result:
    state: State
    task: str | None
    completed_tasks: int
    total_tasks: int
    git_clean: bool
    reasons: list[str]

    def to_json(self) -> str:
        payload = asdict(self)
        payload["state"] = self.state.value
        return json.dumps(payload, indent=2)


@dataclass(frozen=True)
class Task:
    task_id: str
    status: str
    phase_number: str
    path: Path
    implementer: str | None
    reviewer: str | None
    completed_at: str | None


def _field(text: str, key: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.+?)\s*$", text)
    if not match:
        return None
    value = match.group(1).strip()
    return None if value in {"", "null", "None", "—"} else value


def _task_files(bootstrap: Path) -> Iterable[Path]:
    return sorted((bootstrap / "phases").glob("*/tasks/*/task.md"))


def _load_tasks(bootstrap: Path) -> list[Task]:
    tasks: list[Task] = []
    for path in _task_files(bootstrap):
        text = path.read_text(encoding="utf-8")
        task_id = _field(text, "id")
        status = _field(text, "status")
        if not task_id or not status:
            continue
        phase_number = path.relative_to(bootstrap / "phases").parts[0].split("-", 1)[0]
        tasks.append(
            Task(
                task_id=task_id,
                status=status,
                phase_number=phase_number,
                path=path,
                implementer=_field(text, "implementer_agent"),
                reviewer=_field(text, "reviewer_agent"),
                completed_at=_field(text, "completed_at"),
            )
        )
    return tasks


def _phase_states(bootstrap: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    for path in sorted((bootstrap / "phases").glob("*/status.md")):
        phase_number = path.parent.name.split("-", 1)[0]
        text = path.read_text(encoding="utf-8")
        match = re.search(r"\*\*Phase state:\*\*\s*([^\r\n]+)", text)
        if match:
            result[phase_number] = match.group(1).strip()
    return result


def _phase_task_rows(bootstrap: Path) -> dict[str, dict[str, str]]:
    result: dict[str, dict[str, str]] = {}
    for path in sorted((bootstrap / "phases").glob("*/status.md")):
        phase_number = path.parent.name.split("-", 1)[0]
        rows: dict[str, str] = {}
        for line in path.read_text(encoding="utf-8").splitlines():
            match = re.match(r"^\|\s*(B\d{2}-\d{2})\s*\|\s*([^|]+?)\s*\|$", line)
            if match:
                rows[match.group(1)] = match.group(2).strip()
        result[phase_number] = rows
    return result


def _readme_state(bootstrap: Path) -> tuple[dict[str, tuple[str, int, int]], str | None, str | None]:
    path = bootstrap / "README.md"
    if not path.exists():
        return {}, None, None
    text = path.read_text(encoding="utf-8")
    phases: dict[str, tuple[str, int, int]] = {}
    for line in text.splitlines():
        match = re.match(r"^\|\s*(\d{2})\s+—[^|]*\|\s*([^|]+?)\s*\|\s*(\d+)\s*/\s*(\d+)\s*\|$", line)
        if match:
            phases[match.group(1)] = (match.group(2).strip(), int(match.group(3)), int(match.group(4)))

    def label(name: str) -> str | None:
        match = re.search(rf"(?m)^\*\*{re.escape(name)}:\*\*\s*(.+?)\s*$", text)
        if not match:
            return None
        value = match.group(1).strip().strip("`")
        return None if value.lower() in {"none", "—", "complete"} else value

    return phases, label("Current task"), label("Next unblocked task")


def _git(root: Path) -> tuple[bool, list[str], str | None]:
    status = subprocess.run(
        ["git", "status", "--porcelain=v1"], cwd=root, text=True, capture_output=True
    )
    if status.returncode != 0:
        return False, [], "Git status failed or the directory is not a repository."
    log = subprocess.run(
        ["git", "log", "--format=%s"], cwd=root, text=True, capture_output=True
    )
    if log.returncode != 0:
        return not bool(status.stdout.strip()), [], "Git log failed."
    return not bool(status.stdout.strip()), log.stdout.splitlines(), None


def _latest_review_approved(task: Task) -> bool:
    reviews = sorted((task.path.parent / "reviews").glob("[0-9][0-9]-review.md"))
    if not reviews:
        return False
    text = reviews[-1].read_text(encoding="utf-8")
    return bool(re.search(r"\*\*Verdict:\*\*\s*\**Approved\**", text, re.IGNORECASE))


def inspect_repository(
    root: Path,
    *,
    expected_task_count: int = 28,
    final_task_id: str = "B07-03",
    allow_dirty: bool = False,
) -> Result:
    root = root.resolve()
    bootstrap = root / ".scratch" / "bootstrap"
    reasons: list[str] = []
    tasks = _load_tasks(bootstrap)
    task_by_id = {task.task_id: task for task in tasks}
    phase_states = _phase_states(bootstrap)
    phase_rows = _phase_task_rows(bootstrap)
    readme_phases, readme_current, readme_next = _readme_state(bootstrap)
    git_clean, commit_subjects, git_error = _git(root)

    if git_error:
        reasons.append(git_error)
    if len(tasks) != expected_task_count:
        reasons.append(f"Expected {expected_task_count} tasks, found {len(tasks)}.")
    if len(task_by_id) != len(tasks):
        reasons.append("Task IDs are not unique.")

    for task in tasks:
        recorded = phase_rows.get(task.phase_number, {}).get(task.task_id)
        if recorded != task.status:
            reasons.append(
                f"{task.task_id} is {task.status} in task.md but {recorded or 'missing'} in phase status."
            )

    for phase_number, state in phase_states.items():
        phase_tasks = [task for task in tasks if task.phase_number == phase_number]
        done = sum(task.status == "Done" for task in phase_tasks)
        readme = readme_phases.get(phase_number)
        if not readme:
            reasons.append(f"Phase {phase_number} is missing from README.md.")
            continue
        readme_state, readme_done, readme_total = readme
        if readme_state != state:
            reasons.append(
                f"Phase {phase_number} is {state} in status.md but {readme_state} in README.md."
            )
        if (readme_done, readme_total) != (done, len(phase_tasks)):
            reasons.append(
                f"Phase {phase_number} README count is {readme_done}/{readme_total}; expected {done}/{len(phase_tasks)}."
            )

    done_tasks = [task for task in tasks if task.status == "Done"]
    ready = [task for task in tasks if task.status == "Ready"]
    active = [task for task in tasks if task.status in {"In progress", "In review"}]
    blocked = [task for task in tasks if task.status == "Blocked"]

    for task in done_tasks:
        if not all((task.implementer, task.reviewer, task.completed_at)):
            reasons.append(f"{task.task_id} is Done but completion metadata is incomplete.")
        if task.implementer == task.reviewer:
            reasons.append(f"{task.task_id} uses the same implementer and reviewer.")
        if not _latest_review_approved(task):
            reasons.append(f"{task.task_id} has no latest Approved review.")
        if not any(task.task_id in subject for subject in commit_subjects):
            reasons.append(f"{task.task_id} has no reachable Task-ID commit.")

    control = bootstrap / "ralph-loop"
    for name in ("HANDOFF.md", "KNOWLEDGE.md"):
        if not (control / name).exists():
            reasons.append(f"ralph-loop/{name} is missing.")

    if blocked:
        return Result(State.BLOCKED, blocked[0].task_id, len(done_tasks), len(tasks), git_clean, reasons)

    if len(active) > 1:
        reasons.append("More than one task is active.")
    if active:
        task = active[0]
        if readme_current != task.task_id:
            reasons.append(f"README current task is {readme_current}; active task is {task.task_id}.")
        state = State.RESUMABLE if len(active) == 1 and not reasons else State.INCONSISTENT
        return Result(state, task.task_id, len(done_tasks), len(tasks), git_clean, reasons)

    all_done = bool(tasks) and len(done_tasks) == len(tasks)
    if all_done:
        if any(state != "Done" for state in phase_states.values()) or len(phase_states) != len(readme_phases):
            reasons.append("Not every phase status file is Done and represented in README.md.")
        if any(state != "Done" for state, _, _ in readme_phases.values()):
            reasons.append("Not every README phase row is Done.")
        if readme_current or readme_next:
            reasons.append("README still names a current or next task.")
        if final_task_id not in task_by_id or task_by_id.get(final_task_id, Task("", "", "", Path(), None, None, None)).status != "Done":
            reasons.append(f"Final task {final_task_id} is not Done.")
        report = bootstrap / "completion-report.md"
        if not report.exists() or "Not started" in report.read_text(encoding="utf-8"):
            reasons.append("The completion report is not finalized.")
        if not git_clean and not allow_dirty:
            reasons.append("Git working tree is not clean.")
        state = State.COMPLETE if not reasons else State.INCONSISTENT
        return Result(state, None, len(done_tasks), len(tasks), git_clean, reasons)

    if len(ready) != 1:
        reasons.append(f"Expected exactly one Ready task, found {len(ready)}.")
        return Result(State.INCONSISTENT, None, len(done_tasks), len(tasks), git_clean, reasons)

    task = ready[0]
    if readme_current != task.task_id or readme_next != task.task_id:
        reasons.append(
            f"README current/next task does not match the Ready task {task.task_id}."
        )
    if not git_clean and not allow_dirty:
        reasons.append("Git working tree is not clean before starting a task.")
    state = State.READY if not reasons else State.INCONSISTENT
    return Result(state, task.task_id, len(done_tasks), len(tasks), git_clean, reasons)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--expected-task-count", type=int, default=28)
    parser.add_argument("--final-task-id", default="B07-03")
    parser.add_argument("--allow-dirty", action="store_true", help="Dry-run only: ignore dirty Git state.")
    args = parser.parse_args(argv)
    result = inspect_repository(
        args.repo,
        expected_task_count=args.expected_task_count,
        final_task_id=args.final_task_id,
        allow_dirty=args.allow_dirty,
    )
    print(result.to_json())
    return EXIT_CODES[result.state]


if __name__ == "__main__":
    sys.exit(main())

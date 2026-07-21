from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.dont_write_bytecode = True

TOOLS = Path(__file__).resolve().parent
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from check_state import Result, State, inspect_repository  # noqa: E402
from ralph_loop import LoopOutcome, run_loop  # noqa: E402


README = """# Bootstrap

| Phase | State | Tasks done |
|---|---|---:|
| 00 — Test | {phase_state} | {done}/{total} |

**Current task:** {current}
**Next unblocked task:** {next_task}
"""


def task_text(task_id: str, status: str) -> str:
    complete = status == "Done"
    return f"""---
id: {task_id}
status: {status}
depends_on: []
implementer_agent: {'impl' if complete else 'null'}
reviewer_agent: {'reviewer' if complete else 'null'}
started_at: {'2026-01-01T00:00:00Z' if complete else 'null'}
completed_at: {'2026-01-01T00:10:00Z' if complete else 'null'}
---

# Task
"""


class RepositoryFixture:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.bootstrap = root / ".scratch" / "bootstrap"
        self.phase = self.bootstrap / "phases" / "00-test"
        (self.phase / "tasks").mkdir(parents=True)
        (self.bootstrap / "ralph-loop").mkdir(parents=True)
        (self.bootstrap / "ralph-loop" / "HANDOFF.md").write_text("# Handoff\n", encoding="utf-8")
        (self.bootstrap / "ralph-loop" / "KNOWLEDGE.md").write_text("# Knowledge\n", encoding="utf-8")

    def add_task(self, task_id: str, status: str) -> None:
        folder = self.phase / "tasks" / task_id.lower()
        folder.mkdir(parents=True)
        (folder / "task.md").write_text(task_text(task_id, status), encoding="utf-8")
        if status == "Done":
            reviews = folder / "reviews"
            reviews.mkdir()
            (reviews / "01-review.md").write_text("**Verdict:** **Approved**\n", encoding="utf-8")

    def write_tracking(self, phase_state: str, done: int, total: int, current: str, next_task: str) -> None:
        statuses = []
        for task in sorted((self.phase / "tasks").glob("*/task.md")):
            text = task.read_text(encoding="utf-8")
            task_id = next(line.split(":", 1)[1].strip() for line in text.splitlines() if line.startswith("id:"))
            status = next(line.split(":", 1)[1].strip() for line in text.splitlines() if line.startswith("status:"))
            statuses.append(f"| {task_id} | {status} |")
        (self.phase / "status.md").write_text(
            "# Status\n\n| Task | State |\n|---|---|\n" + "\n".join(statuses) + f"\n\n**Phase state:** {phase_state}\n",
            encoding="utf-8",
        )
        (self.bootstrap / "README.md").write_text(
            README.format(phase_state=phase_state, done=done, total=total, current=current, next_task=next_task),
            encoding="utf-8",
        )

    def init_git(self, subjects: list[str]) -> None:
        subprocess.run(["git", "init", "-q"], cwd=self.root, check=True)
        subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=self.root, check=True)
        subprocess.run(["git", "config", "user.name", "Test"], cwd=self.root, check=True)
        subprocess.run(["git", "add", "."], cwd=self.root, check=True)
        subprocess.run(["git", "commit", "-qm", subjects[0]], cwd=self.root, check=True)
        for subject in subjects[1:]:
            marker = self.root / f"marker-{len(list(self.root.glob('marker-*')))}"
            marker.write_text(subject, encoding="utf-8")
            subprocess.run(["git", "add", "."], cwd=self.root, check=True)
            subprocess.run(["git", "commit", "-qm", subject], cwd=self.root, check=True)


class CheckStateTests(unittest.TestCase):
    def fixture(self) -> tuple[tempfile.TemporaryDirectory[str], RepositoryFixture]:
        temp = tempfile.TemporaryDirectory()
        return temp, RepositoryFixture(Path(temp.name))

    def test_one_ready_task_is_ready(self) -> None:
        temp, fx = self.fixture()
        with temp:
            fx.add_task("B00-01", "Done")
            fx.add_task("B00-02", "Ready")
            fx.write_tracking("Ready", 1, 2, "`B00-02`", "`B00-02`")
            fx.init_git(["complete B00-01"])
            result = inspect_repository(fx.root, expected_task_count=2, final_task_id="B00-02")
            self.assertEqual(State.READY, result.state)
            self.assertEqual("B00-02", result.task)

    def test_in_review_task_is_resumable_even_when_git_is_dirty(self) -> None:
        temp, fx = self.fixture()
        with temp:
            fx.add_task("B00-01", "In review")
            fx.write_tracking("In review", 0, 1, "`B00-01`", "`B00-01`")
            fx.init_git(["initial"])
            (fx.root / "work.txt").write_text("uncommitted", encoding="utf-8")
            result = inspect_repository(fx.root, expected_task_count=1, final_task_id="B00-01")
            self.assertEqual(State.RESUMABLE, result.state)

    def test_blocked_task_is_blocked(self) -> None:
        temp, fx = self.fixture()
        with temp:
            fx.add_task("B00-01", "Blocked")
            fx.write_tracking("Blocked", 0, 1, "`B00-01`", "`B00-01`")
            fx.init_git(["initial"])
            result = inspect_repository(fx.root, expected_task_count=1, final_task_id="B00-01")
            self.assertEqual(State.BLOCKED, result.state)

    def test_tracking_disagreement_is_inconsistent(self) -> None:
        temp, fx = self.fixture()
        with temp:
            fx.add_task("B00-01", "Ready")
            fx.write_tracking("Done", 1, 1, "None", "None")
            fx.init_git(["initial"])
            result = inspect_repository(fx.root, expected_task_count=1, final_task_id="B00-01")
            self.assertEqual(State.INCONSISTENT, result.state)
            self.assertTrue(result.reasons)

    def test_complete_requires_all_completion_signals(self) -> None:
        temp, fx = self.fixture()
        with temp:
            fx.add_task("B07-03", "Done")
            fx.write_tracking("Done", 1, 1, "None", "None")
            (fx.bootstrap / "completion-report.md").write_text("# Complete\n\nAll local gates passed.\n", encoding="utf-8")
            fx.init_git(["complete B07-03"])
            result = inspect_repository(fx.root, expected_task_count=1, final_task_id="B07-03")
            self.assertEqual(State.COMPLETE, result.state)

    def test_complete_rejects_dirty_git(self) -> None:
        temp, fx = self.fixture()
        with temp:
            fx.add_task("B07-03", "Done")
            fx.write_tracking("Done", 1, 1, "None", "None")
            (fx.bootstrap / "completion-report.md").write_text("# Complete\n", encoding="utf-8")
            fx.init_git(["complete B07-03"])
            (fx.root / "dirty.txt").write_text("dirty", encoding="utf-8")
            result = inspect_repository(fx.root, expected_task_count=1, final_task_id="B07-03")
            self.assertEqual(State.INCONSISTENT, result.state)


class RalphLoopTests(unittest.TestCase):
    def test_max_tasks_stops_after_two_successful_tasks(self) -> None:
        states = iter(
            [
                Result(State.READY, "B00-01", 0, 3, True, []),
                Result(State.READY, "B00-02", 1, 3, True, []),
                Result(State.READY, "B00-03", 2, 3, True, []),
            ]
        )
        executed: list[str] = []

        def inspect() -> Result:
            return next(states)

        def execute(task: str, session_id: str | None, repair_reasons: list[str]) -> str:
            executed.append(task)
            return f"session-{task}"

        outcome = run_loop(
            Path.cwd(),
            max_tasks=2,
            inspect_fn=inspect,
            execute_fn=execute,
            state_dir=Path(tempfile.mkdtemp()),
        )

        self.assertEqual(LoopOutcome.LIMIT_REACHED, outcome)
        self.assertEqual(["B00-01", "B00-02"], executed)

    def test_complete_stops_without_calling_codex(self) -> None:
        def inspect() -> Result:
            return Result(State.COMPLETE, None, 28, 28, True, [])

        def execute(task: str, session_id: str | None, repair_reasons: list[str]) -> str:
            self.fail("Codex should not run after completion")

        outcome = run_loop(
            Path.cwd(),
            inspect_fn=inspect,
            execute_fn=execute,
            state_dir=Path(tempfile.mkdtemp()),
        )
        self.assertEqual(LoopOutcome.COMPLETE, outcome)


if __name__ == "__main__":
    unittest.main()

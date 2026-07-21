"""Validate the structural contracts of the tracked bootstrap workspace."""

from __future__ import annotations

from pathlib import Path
import re
import sys


WORKSPACE = Path(__file__).resolve().parents[1]
TASK_PATHS = sorted(WORKSPACE.glob("phases/*/tasks/*/task.md"))
TASK_FIELDS = re.compile(r"^(id|status|depends_on):\s*(.+)$", re.MULTILINE)
FRONT_MATTER = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def main() -> int:
    errors: list[str] = []
    records: list[tuple[str, list[str], Path, str]] = []
    phase_counts: dict[str, list[int]] = {}
    phase_rows: dict[str, dict[str, str]] = {}
    phase_states: dict[str, str] = {}

    for task_path in TASK_PATHS:
        content = task_path.read_text(encoding="utf-8")
        front_matter = FRONT_MATTER.match(content)
        if front_matter is None:
            errors.append(f"{task_path}: missing YAML front matter")
            continue

        fields = dict(TASK_FIELDS.findall(front_matter.group(1)))
        task_id = fields.get("id")
        if task_id is None:
            errors.append(f"{task_path}: missing id")
            continue

        for heading in ("## What", "## Why", "## How", "## Required reading"):
            if heading not in content:
                errors.append(f"{task_path}: missing {heading}")
        if re.search(r"^## Acceptance(?: and verification)?\s*$", content, re.MULTILINE) is None:
            errors.append(f"{task_path}: missing acceptance section")

        dependencies = re.findall(r"B\d{2}-\d{2}", fields.get("depends_on", ""))
        status = fields.get("status", "")
        records.append((task_id, dependencies, task_path, status))
        phase = task_path.parents[2].name
        phase_counts.setdefault(phase, [0, 0])
        phase_counts[phase][0] += 1
        phase_counts[phase][1] += status == "Done"

    for status_path in sorted(WORKSPACE.glob("phases/*/status.md")):
        phase = status_path.parent.name
        status_text = status_path.read_text(encoding="utf-8")
        state = re.search(r"\*\*Phase state:\*\*\s*([^\r\n]+)", status_text)
        if state is None:
            errors.append(f"{status_path}: missing phase state")
        else:
            phase_states[phase] = state.group(1).strip()
        phase_rows[phase] = {
            row.group(1): row.group(2).strip()
            for row in re.finditer(
                r"^\|\s*(B\d{2}-\d{2})\s*\|\s*([^|]+?)\s*\|$",
                status_text,
                re.MULTILINE,
            )
        }

    for task_id, _, task_path, status in records:
        phase = task_path.parents[2].name
        recorded = phase_rows.get(phase, {}).get(task_id)
        if recorded != status:
            errors.append(
                f"{task_id}: task.md is {status}; phase status is {recorded or 'missing'}"
            )

    ids = [record[0] for record in records]
    if len(ids) != 28:
        errors.append(f"expected 28 task IDs, found {len(ids)}")
    for task_id in sorted(set(ids)):
        if ids.count(task_id) != 1:
            errors.append(f"duplicate ID {task_id}")

    graph = {task_id: dependencies for task_id, dependencies, _, _ in records}
    for task_id, dependencies, _, _ in records:
        for dependency in dependencies:
            if dependency not in graph:
                errors.append(f"{task_id}: unknown dependency {dependency}")

    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, trail: list[str]) -> None:
        if node in visiting:
            errors.append("dependency cycle: " + " -> ".join([*trail, node]))
            return
        if node in visited:
            return
        visiting.add(node)
        for dependency in graph[node]:
            visit(dependency, [*trail, node])
        visiting.remove(node)
        visited.add(node)

    for node in graph:
        visit(node, [])

    for markdown_path in WORKSPACE.rglob("*.md"):
        for target in MARKDOWN_LINK.findall(markdown_path.read_text(encoding="utf-8")):
            target = target.strip().strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            relative_target = target.split("#", 1)[0].split("?", 1)[0]
            if relative_target and not (markdown_path.parent / relative_target).resolve().exists():
                errors.append(
                    f"{markdown_path.relative_to(WORKSPACE)}: unresolved link {relative_target}"
                )

    dashboard = (WORKSPACE / "README.md").read_text(encoding="utf-8")
    for phase, (total, done) in phase_counts.items():
        phase_number = phase[:2]
        row = re.search(
            rf"^\| {re.escape(phase_number)} — .*? \| (.*?) \| (\d+)/(\d+) \|$",
            dashboard,
            re.MULTILINE,
        )
        if row is None:
            errors.append(f"dashboard missing phase {phase_number} row")
            continue
        dashboard_state, dashboard_done, dashboard_total = row.groups()
        if (int(dashboard_done), int(dashboard_total)) != (done, total):
            errors.append(
                f"dashboard count mismatch for phase {phase_number}: "
                f"expected {done}/{total}, found {dashboard_done}/{dashboard_total}"
            )
        if dashboard_state.strip() != phase_states.get(phase):
            errors.append(
                f"dashboard phase {phase_number} is {dashboard_state.strip()}; "
                f"phase status is {phase_states.get(phase, 'missing')}"
            )

    def dashboard_label(name: str) -> str | None:
        match = re.search(rf"(?m)^\*\*{re.escape(name)}:\*\*\s*(.+?)\s*$", dashboard)
        if match is None:
            return None
        value = match.group(1).strip().strip("`")
        return None if value.lower() in {"none", "—", "complete"} else value

    active = [task_id for task_id, _, _, status in records if status in {"In progress", "In review"}]
    ready = [task_id for task_id, _, _, status in records if status == "Ready"]
    current_task = dashboard_label("Current task")
    next_task = dashboard_label("Next unblocked task")
    if len(active) == 1:
        if current_task != active[0]:
            errors.append(
                f"dashboard current task is {current_task or 'missing'}; active task is {active[0]}"
            )
        if next_task is not None:
            errors.append(f"dashboard next task is {next_task}; an active task must have no next task")
    elif not active and len(ready) == 1 and (current_task, next_task) != (ready[0], ready[0]):
        errors.append(f"dashboard current/next task must both be Ready task {ready[0]}")

    if errors:
        print("\n".join(errors))
        return 1

    completed = sum(done for _, done in phase_counts.values())
    total = sum(total for total, _ in phase_counts.values())
    print(
        "PASS: "
        f"{len(records)} unique task IDs; required sections present; acyclic dependencies; "
        f"all Markdown links resolve; status views and dashboard task counts match ({completed}/{total})."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

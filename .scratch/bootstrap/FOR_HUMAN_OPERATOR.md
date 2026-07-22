# For the Human Operator

This is the shortest operational view of the bootstrap process.

## What is happening

The repository contains the project documentation and a complete bootstrap execution workspace. Bootstrap itself has **not** started: no application, packages, skills, or test tools were installed by the planning work.

There are 8 phases and 28 tasks. Each task is implemented by one subagent, reviewed by a different subagent, and closed by the root integrator only after checks pass.

## Current status

- Current phase: `00 — Planning and baseline`
- Current task: `B00-02 — Validate and finalize the execution workspace`
- Next unblocked task: `B00-02`
- Completed tasks: `1/28`
- External blocker: Kimi Code is unavailable, so full cross-agent compatibility cannot be declared green.
- Hosted CI: intentionally outside this bootstrap.

For detail, open [the dashboard](README.md). For governing rules, open [the protocol](protocol.md).

## Ralph-loop commands

Run these from the repository root:

```bash
# Read-only validation and intended command; no AI execution.
python .scratch/ralph-loop/tools/ralph_loop.py --dry-run

# Live AI execution until the signal is true or an operational failure occurs.
python .scratch/ralph-loop/tools/ralph_loop.py

# Bounded live AI execution.
python .scratch/ralph-loop/tools/ralph_loop.py --max-iterations 2

# Hermetic tests; never launches Hermes.
python -B -m unittest discover -s .scratch/ralph-loop/tests -p "test_ralph_loop.py" -v
```

The controller never resets the completion signal; a human must explicitly edit it from `true` to `false` for a new campaign.

## What you normally do

1. Paste the continuation prompt below into your primary coding agent.
2. Respond only when it requests approval for destructive/overwrite work, credentials, an external service, or a material scope decision.
3. Use this file and the dashboard for concise progress.

You do not need to choose details already settled by task briefs and the verification matrix.

## Short handoff prompt

```text
Read `.scratch/bootstrap/BOOTSTRAP-AGENTS.md` and execute exactly one next valid bootstrap task.
```
## Copy-paste continuation prompt

```text
Resume the Greek Essence bootstrap process from `.scratch/bootstrap/` as the root integrator. Execute no work before reconciling the recorded state with the repository.

First read:
1. root `AGENTS.md`, if it exists;
2. `.scratch/bootstrap/README.md`;
3. `.scratch/bootstrap/protocol.md`;
4. `.scratch/bootstrap/plan.md`;
5. `.scratch/bootstrap/decisions.md`;
6. `.scratch/bootstrap/dependency-map.md`;
7. `.scratch/bootstrap/verification-matrix.md`;
8. the current phase’s `phase.md` and `status.md`;
9. the active task’s `task.md`, or the selected next-ready task’s `task.md` when no task is active.

Then inspect Git status, branch, remotes, tracked and untracked files, active reports/reviews, task front matter, phase status, dashboard, and the available runtime/tools. Confirm they agree before changing anything. If a task is `In progress` or `In review`, resume that exact task rather than selecting another. Otherwise, select only the next `Ready` task whose dependencies are `Done`. Read only the project documents named in that task’s Required reading section.

Before delegated work, briefly report whether recorded state matches repository reality, the task selected or resumed, why it is eligible, the implementer/reviewer workflow, and any blocker or approval required. For every task, launch a fresh `greekimpl` Hermes profile session and record its canonical session ID; launch a different fresh `greekreview` session for independent review and record its canonical session ID. Follow the full implementation, review, response, and re-review procedure in `protocol.md`; do not replace it with ad-hoc role instructions.

Execute only that one task. Preserve unrelated work and do not begin a later task, push, deploy, change remotes, rewrite history, or perform destructive/overwrite operations without the authority and approval required by the protocol. After a task is successfully closed, create its required dedicated local commit with the task ID in the commit message before any later task begins.

At the end, update all task, phase, and dashboard records; report the task outcome, files changed, exact verification commands/results, implementer and reviewer identities, review verdict/cycles, unresolved findings or blockers, progress counts, and the next eligible task with its reason. If tracking and repository reality disagree, stop execution and repair or report the discrepancy rather than guessing. Stop after the one task unless I explicitly request continuation.
```

## Status-only prompt

```text
Read `.scratch/bootstrap/README.md`, `.scratch/bootstrap/protocol.md`, and the current phase/task records. Do not edit files or execute a bootstrap task. Briefly report: current phase, current task, completed/total tasks, blockers, latest review verdict, whether tracking matches repository reality, and the recommended next task with one-sentence reasoning.
```

## Completion meaning

Local bootstrap is complete only when Phase 07 is approved, every applicable command is green, the Reviewer Skill is green in Codex, and `completion-report.md` is finalized. Kimi remains visibly blocked until actually validated; local completion must not be presented as full cross-agent acceptance.

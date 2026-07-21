# For the Human Operator

This is the shortest operational view of the bootstrap process.

## What is happening

The repository contains the project documentation and a complete bootstrap execution workspace. Bootstrap itself has **not** started: no application, packages, skills, or test tools were installed by the planning work.

There are 8 phases and 28 tasks. Each task is implemented by one subagent, reviewed by a different subagent, and closed by the root integrator only after checks pass.

## Current status

- Current phase: `00 — Planning and baseline`
- Current task: `B00-01 — Record and protect the initial repository state`
- Next unblocked task: `B00-01`
- Completed tasks: `0/28`
- External blocker: Kimi Code is unavailable, so full cross-agent compatibility cannot be declared green.
- Hosted CI: intentionally outside this bootstrap.

For detail, open [the dashboard](README.md). For governing rules, open [the protocol](protocol.md).

## What you normally do

1. Paste the continuation prompt below into your primary coding agent.
2. Respond only when it requests approval for destructive/overwrite work, credentials, an external service, or a material scope decision.
3. Use this file and the dashboard for concise progress.

You do not need to choose details already settled by task briefs and the verification matrix.

## Copy-paste continuation prompt

```text
Resume the Greek Essence bootstrap process from `.scratch/bootstrap/`.

First read:
1. `.scratch/bootstrap/README.md`
2. `.scratch/bootstrap/protocol.md`
3. `.scratch/bootstrap/dependency-map.md`
4. the current phase `status.md`

Reconcile recorded status with the repository before changing anything. Identify the next `Ready` task whose dependencies are `Done`, briefly tell me the current status and why that task is next, then execute only that task using the implementer/reviewer protocol. Every task must use a fresh `.codex/agents/implementer.toml` instance, be reviewed by a different fresh `.codex/agents/reviewer.toml` instance, and return to the implementer for review responses and fixes. Do not begin a later task, commit, push, deploy, change remotes, or perform destructive/overwrite operations without authority and approval from the protocol.

At the end, update all relevant task, phase, and dashboard records and report: task outcome, verification results, review verdict, blockers, and next recommended task. If tracking and repository reality disagree, stop execution and repair or report the discrepancy rather than guessing.
```

## Status-only prompt

```text
Read `.scratch/bootstrap/README.md`, `.scratch/bootstrap/protocol.md`, and the current phase/task records. Do not edit files or execute a bootstrap task. Briefly report: current phase, current task, completed/total tasks, blockers, latest review verdict, whether tracking matches repository reality, and the recommended next task with one-sentence reasoning.
```

## Completion meaning

Local bootstrap is complete only when Phase 07 is approved, every applicable command is green, the Reviewer Skill is green in Codex, and `completion-report.md` is finalized. Kimi remains visibly blocked until actually validated; local completion must not be presented as full cross-agent acceptance.

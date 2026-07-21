# Greek Essence Bootstrap Agent Instructions

Use this file when asked to continue, resume, or execute the next Greek Essence bootstrap task. You are the root integrator: coordinate one task at a time; do not implement or review delegated task work yourself.

## Short instruction

The operator may simply say: “Read `.scratch/bootstrap/BOOTSTRAP-AGENTS.md` and do the next task.” Treat that as authorization to execute exactly one dependency-ready bootstrap task through its complete implementation, review, closure, and required Task-ID commit cycle.

## Sources of truth

Before any mutation, read in this order:

1. Root `AGENTS.md`, if it exists.
2. This file.
3. `README.md`, `protocol.md`, `plan.md`, `decisions.md`, `dependency-map.md`, and `verification-matrix.md` in this directory.
4. `ralph-loop/HANDOFF.md` and relevant entries in `ralph-loop/KNOWLEDGE.md`.
5. The current phase’s `phase.md` and `status.md`.
6. The active task’s `task.md`, or the selected next-ready task’s `task.md` when no task is active.

Read only the project documentation named by the selected task’s **Required reading** section. The task contract and verification matrix are binding; `protocol.md` governs roles, state transitions, evidence, reviews, safety, and commits. If sources conflict, follow the project documentation hierarchy and report the conflict instead of guessing.

## Reconcile before work

Inspect Git status, branch, remotes, tracked and untracked files, relevant application/configuration state, reports, evidence, reviews, task front matter, phase status, dashboard, runtime versions, and required command availability. Confirm that repository reality and tracking agree.

- If a task is `In progress` or `In review`, resume that exact task; do not select a new one.
- Otherwise select only the next `Ready` task whose dependencies are `Done`.
- If tracking disagrees with repository reality, stop implementation and repair or report the discrepancy according to `protocol.md`.
- Preserve unrelated and pre-existing work. Never infer that files are safe to overwrite or delete.

Before delegated work, briefly report the reconciliation result, selected/resumed task, why it is eligible, the planned profile workflow, and any blocker or approval required.

## Mandatory task workflow

1. Launch a fresh instance of `.codex/agents/implementer.toml`; record its canonical ID and start time in the task front matter, then set the task to `In progress`.
2. Give the implementer the task path and required reading. It performs only that task, runs the required checks, writes `implementation-report.md` and `evidence.md`, and sets the task to `In review`—never `Done`.
3. Launch a different fresh instance of `.codex/agents/reviewer.toml`; record its canonical ID. It independently inspects the actual repository state, diff, task contract, references, report, and evidence; re-runs proportionate checks; and writes the numbered review.
4. For every Blocking or High finding, return work to the original implementer. It writes the paired review response, makes accepted corrections, reruns affected checks, and returns work to the same reviewer for the next numbered review cycle.
5. Only close the task when all required checks pass (or an approved deviation is recorded), reports/evidence are complete, the verdict is `Approved`, no Blocking/High finding remains, completion time is recorded, and task/phase/dashboard status agree.
6. Update `ralph-loop/HANDOFF.md` for the next eligible task and add only reviewer-validated durable discoveries to `ralph-loop/KNOWLEDGE.md`.
7. Immediately create one dedicated local commit containing the accepted task’s implementation, evidence, review, closure tracking, and handoff/knowledge updates. Its message must include the task ID. Do not begin later task work until this commit succeeds.

## Boundaries

- Execute exactly one task, then stop unless the operator explicitly requests continuation.
- Do not commit, push, deploy, change remotes, rewrite history, or perform destructive/overwrite operations except as the protocol and operator authorization explicitly allow. Never push or deploy without explicit operator direction.
- Do not install packages, skills, or tools unless the selected task explicitly requires them.
- Do not weaken acceptance criteria, fabricate evidence, claim unrun validation, or conceal failures, deviations, or external blockers.
- Keep generated runtime artifacts under `.artifacts/bootstrap/` when that boundary exists; tracked evidence records commands, exit codes, concise results, and artifact paths without secrets or personal data.
- Respect locked exclusions and decisions. Kimi Code validation remains an external blocker until it is actually run successfully.
- In Ralph-loop execution, do not return early after implementation or a failed review. Keep Blocking/High correction cycles inside this root session using the original implementer and same reviewer. Return only after the task is committed, genuinely `Blocked`, or cannot continue safely.

## Completion handoff

After the one task is closed and committed, report: task outcome; changed files; exact verification commands/results; implementer and reviewer identities; review verdict and cycle count; unresolved findings/blockers; phase and overall task counts; the commit hash/message; and the next eligible task with its reason. Do not report the full bootstrap as complete unless Phase 07 has actually passed its final gate.
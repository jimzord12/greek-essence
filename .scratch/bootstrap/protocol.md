# Bootstrap Work Protocol

This document is normative for bootstrap execution. It defines roles, workflow, evidence, reviews, safety, and completion. If it conflicts with root `AGENTS.md` or project documentation under `docs/`, the higher-authority instruction governs. Technical requirements remain in each `task.md` and `verification-matrix.md`.

## Roles

### Human operator

The human operator owns scope, approvals, and exceptional decisions.

Must:

- approve destructive or overwrite operations required by repository safety rules;
- decide changes to scope, locked decisions, credentials, and external blockers;
- review deviations affecting cost, security, product scope, or Definition of Done.

Must not be expected to:

- coordinate ordinary task files or status transitions;
- interpret raw output when an agent can summarize it;
- resolve details already locked by task briefs and the verification matrix;
- approve routine reads, edits, tests, builds, or non-destructive Git inspection.

### Root integrator

The root integrator orchestrates work and preserves repository-wide consistency.

Must:

- read this protocol, the dashboard, dependency map, and current phase status;
- select only a `Ready` task whose dependencies are `Done`;
- assign one fresh instance of `.codex/agents/implementer.toml` and a different fresh instance of `.codex/agents/reviewer.toml`, recording their IDs;
- preserve unrelated and pre-existing work;
- resolve cross-task conflicts and update task, phase, and dashboard state together;
- create one task commit after each successful task closure, control phase commits, and surface blockers with exact consequences.
- update `ralph-loop/HANDOFF.md` before every task commit and promote only reviewed cross-task discoveries to `ralph-loop/KNOWLEDGE.md`.

Must not:

- implement a task assigned to a subagent or review its own work;
- mark work `Done` from an implementation report alone;
- weaken acceptance criteria to obtain green results;
- hide findings, failures, deviations, or blockers;
- push, change remotes, deploy, or expand scope without authority.

### Task implementer subagent

The implementer owns exactly one task and its accepted review fixes. For every task, the root integrator launches a fresh instance of the repository's `.codex/agents/implementer.toml` profile; it does not substitute ad-hoc implementer instructions.

Must:

- read root `AGENTS.md`, this protocol, its `task.md`, its verification row, and only its listed project references;
- confirm the task is `Ready` and dependencies are `Done`;
- record its ID/start time, set `In progress`, and inspect repository state before mutation;
- implement the smallest complete in-scope change;
- run every required check and write `implementation-report.md` and `evidence.md` with exact commands, exit codes, results, and artifact paths;
- respond to every finding, fix accepted findings, and re-run affected checks;
- stop when safety approval, missing authority, credentials, or a scope decision is required.

Must not:

- begin another task or later phase;
- change product requirements to fit an implementation;
- invent commands, versions, claims, credentials, or evidence;
- commit, push, change remotes, deploy, rewrite history, or perform unapproved destructive/overwrite operations;
- edit review files or mark its own task `Done`;
- dismiss findings without requirement- and evidence-based rationale.

### Task reviewer subagent

The reviewer independently determines whether one task satisfies its contract. For every task, the root integrator launches a fresh instance of the repository's `.codex/agents/reviewer.toml` profile; it does not substitute ad-hoc reviewer instructions.

Must:

- be fresh and different from the implementer;
- read the task, report, evidence, diff, verification row, and task-listed references;
- inspect actual changes and re-run proportionate checks;
- record severity, exact location, requirement, evidence/reproduction, correction, and verification for each finding;
- use `Blocking`, `High`, or `Non-blocking` severity and a `Blocked`, `Changes requested`, or `Approved` verdict;
- re-review responses when blocking/high findings required changes.

Must not:

- edit implementation files or fix findings directly;
- broaden scope according to preference;
- present subjective suggestions as defects without a traceable requirement;
- approve unresolved blocking/high findings or accept missing evidence as a pass;
- overwrite implementation reports or responses.

### Phase reviewer subagent

The phase reviewer validates integration after every phase task has task-level approval.

Must:

- be fresh and independent from phase implementers where practical;
- read the phase brief/status, task reports/reviews, dependency map, and integration gates;
- run integration checks, inspect task interactions, verify tracking accuracy, and assess readiness for the next phase;
- block closure when integration or the phase exit gate fails.

Must not:

- repeat every task review without an integration reason;
- implement fixes directly;
- approve an incomplete phase because individual tasks passed;
- ready future work while dependencies remain unresolved.

## Task procedure

### 1. Selection and assignment

1. Root integrator reads the dashboard, dependency map, and phase status.
2. It selects the first dependency-satisfied `Ready` task.
3. It launches a fresh `.codex/agents/implementer.toml` instance, records its canonical ID, and gives it the task path, not a rewritten brief.
4. Work remains serialized unless non-overlapping write sets are proven and the exception is recorded.

### 2. Implementation

1. Implementer performs preflight, records `started_at`, and sets `In progress`.
2. It implements within scope and runs the verification contract.
3. It completes the implementation and evidence records.
4. It sets `In review`; it does not mark `Done`.

### 3. Independent review

1. Root integrator launches a different fresh `.codex/agents/reviewer.toml` instance and records its canonical ID.
2. Reviewer writes `reviews/01-review.md` using the template.
3. `Approved` with no blocking/high findings may proceed to closure.
4. `Blocked` or `Changes requested` returns to the original implementer.

### 4. Response and re-review

1. Implementer writes `reviews/01-review-response.md` for every finding.
2. Accepted findings are fixed and affected checks repeated; rejected findings require evidence-based rationale.
3. Reviewer writes `02-review.md` when another cycle is needed; implementer uses the paired response.
4. Numbered cycles continue until no blocking/high finding remains or the task becomes `Blocked`.
5. Automation keeps this ping-pong inside the same Codex root session so corrections return to the original implementer and then the same reviewer.

### 5. Task closure

Root integrator may mark `Done` only when records are complete, required checks pass or have an approved deviation, reviewer verdict is `Approved`, no blocking/high finding remains, `completed_at` is recorded, and all status views agree. Before committing, it updates `ralph-loop/HANDOFF.md` for the next eligible task and adds only reviewed durable discoveries to `ralph-loop/KNOWLEDGE.md`. It then creates one dedicated commit containing the task implementation, evidence, review, closure tracking, and handoff/knowledge updates. The commit message must include the task ID (for example, `B00-01`); no later task may begin before that commit succeeds.

## Phase procedure

1. When every task is `Done`, root integrator sets the phase `In review`.
2. A fresh phase reviewer runs integration checks and writes the numbered phase review.
3. The phase owner responds and coordinates fixes through the owning task where possible.
4. Phase becomes `Done` only when its exit gate passes and phase review approves it; set its status file to the exact value `**Phase state:** Done`.
5. Root integrator sets that phase's README State cell to exact `Done`, updates exact task counts, and may create the phase Conventional Commit.
6. Only then may the next dependency-satisfied task become `Ready`.

## Ralph-loop automation contract

- `ralph-loop/tools/check_state.py` is the deterministic authority; model prose is not a completion signal.
- A fresh Codex root session starts only for a clean `Ready` task. An interrupted `In progress` or `In review` task resumes its saved root session.
- The loop stops on `Blocked`, inconsistent tracking, missing session identity, or exhausted repair attempts.
- `COMPLETE` requires all 28 tasks and all eight phases `Done`, README counts aligned with no current/next task, B07-03 and `completion-report.md` finalized, latest reviews approved, Task-ID commits reachable, and Git clean.
- When Phase 07 completes, the README must show `28/28` with no current or next task.

## Evidence and artifacts

- Tracked Markdown records explain exactly what ran and what happened.
- Generated screenshots, traces, reports, coverage, and downloads belong under ignored `.artifacts/bootstrap/`.
- Evidence includes exact commands, exit codes, versions, concise results, and artifact paths.
- Results must not be fabricated, inferred from file existence, or copied from an earlier run.
- Secrets, credentials, personal data, and unrelated machine information must not appear in evidence.

## Blockers, deviations, and safety

- Use `Blocked` only when safe/correct progress requires external input or state change.
- Record the condition, investigation, required decision, and affected tasks.
- A deviation names the original rule, reason, impact, approval owner, and replacement verification.
- Before destructive or overwrite operations: stop, name the exact command/targets and consequence, and wait for explicit approval.
- Kimi Code remains an external blocker; full cross-agent compatibility cannot be claimed until its controlled validations actually pass.

## Status integrity

- Dashboard, phase status, task front matter, reports, and reviews must agree.
- Use exact completed-task counts, not percentages.
- A failed re-check reopens the owning task.
- The final report states blockers and excluded scope plainly.


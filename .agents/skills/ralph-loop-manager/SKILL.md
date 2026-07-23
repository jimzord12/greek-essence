---
name: ralph-loop-manager
description: Use when the operator asks to run, resume, or monitor the project Ralph Loop for a named feature or a repository-contained directory. Fail closed on incompatible scope, campaign state, profiles, safety authority, notification readiness, or controller health; then run one bounded Ralph iteration at a time, verify durable progress, and notify by email on completed tasks or genuine escalations.
version: 1.0.0
author: Greek Essence project
license: Project-owned
metadata:
  hermes:
    tags: [ralph-loop, orchestration, compatibility, monitoring, notifications]
    related_skills: [bootstrap-next, email-notification]
---

# Ralph Loop Manager

## Overview

Manage this repository's existing Ralph controller; do not invent a second loop or replace its reasoning with Python task parsing. This skill is project-only and applies only to targets contained by the Greek Essence Git repository or to named features grounded in its authoritative project records.

The manager owns four things around the existing controller:

1. a read-only structural preflight;
2. an agent-reviewed semantic compatibility gate;
3. bounded launch and monitoring between fresh Ralph root iterations;
4. concise email notification for verified task completion, campaign completion, or genuine escalation.

A failed compatibility check is a **HARD STOP**. Do not launch Ralph, reset its completion signal, repair around the failure, or silently narrow/expand the requested scope.

## When to Use

Use when the operator says, for example:

- "Use the Ralph Loop for B06-02."
- "Run Ralph for the contact-form feature."
- "Use Ralph to finish work under `app/[locale]/quality-lab/`."
- "Resume and monitor the Greek Essence Ralph Loop."

Do not use for:

- a target outside this repository;
- a one-command or trivial edit that does not need fresh-context orchestration;
- an open-ended goal without bounded acceptance criteria;
- a second campaign while another false-signal campaign owns the Ralph state;
- generic installation of Ralph into another repository;
- work whose expected completion necessarily requires an unauthorized push, deployment, credential, system-wide change, Git history rewrite, or out-of-repository edit.

For one ordinary bootstrap task without a managed loop, use `$bootstrap-next` instead.

## Authoritative Components

Read these before making a compatibility judgment:

1. `AGENTS.md`
2. `.scratch/ralph-loop/RALPH_LOOP.md`
3. `.scratch/ralph-loop/HANDOFF.md`
4. `.scratch/ralph-loop/KNOWLEDGE.md`
5. `.scratch/ralph-loop/completion-signal.json`
6. the authoritative task, feature, phase, plan, dependency, review, and verification files for the requested target

The existing controller remains canonical:

```bash
python .scratch/ralph-loop/tools/ralph_loop.py
```

**Entrypoint selection is fail-closed and literal:** default to the canonical `ralph_loop.py` command for every run, resume, or monitor request. Use the live smoke runner only when the operator explicitly says **"smoke test"**, **"Ralph smoke test"**, or explicitly names `smoke_test.py`:

```bash
python .scratch/ralph-loop/tools/smoke_test.py
```

The smoke runner delegates to the canonical controller with a fixed `--max-iterations 2` cap and otherwise accepts the same campaign, task, tier, timeout, state-directory, and dry-run arguments. It is live AI execution, not the hermetic unit suite. Do not infer smoke mode from words such as "test," "check," "verify," "try," or "bounded run." If the request is ambiguous, stay on `ralph_loop.py` rather than selecting smoke mode.

For normal managed operation, this manager invokes `ralph_loop.py` with `--max-iterations 1` so it can inspect and notify between fresh root iterations. Do not modify the controller merely to make management more convenient.

## Phase 1 — Normalize the Request Without Mutating State

Resolve the operator's request into one target:

- **Path target:** resolve it and prove it is contained by the repository root.
- **Feature target:** map the label to authoritative files, task IDs, acceptance criteria, and dependencies. A label supported only by conversation prose is not enough.
- **Resume request:** use the active campaign described by the false completion signal and `HANDOFF.md`; do not infer a different campaign from stale chat history.

Record a short proposed campaign statement in working context:

```text
Target: <feature, task IDs, or repository-relative path>
Managed outcome: <bounded end state>
Acceptance: <authoritative files and executable gates>
Explicit exclusions: <adjacent work not owned>
Notification recipient: <explicit address or email-notification default>
```

Completion criterion: the proposed scope has one unambiguous target, a bounded end state, and traceable acceptance sources. No repository or runtime file has been changed yet.

## Phase 2 — Deterministic Structural Preflight

From the repository root run the project-owned read-only checker:

```bash
python .agents/skills/ralph-loop-manager/scripts/preflight.py \
  --repo . \
  --target "<feature label or repository-relative path>"
```

The checker never launches Hermes or Ralph and always emits JSON with `launch_performed: false`.

Interpret the result strictly:

- `STRUCTURAL_PASS` means only that deterministic prerequisites passed. Continue to the semantic gate.
- `HARD_STOP` means stop immediately and report every item in `hard_stops` with its remediation.
- A `DIRTY_WORKTREE` warning is unresolved until every changed and untracked path is attributed to the requested campaign. Unrelated or ambiguous dirtiness becomes a semantic HARD STOP.
- A feature label requires semantic mapping even though it can pass structural path validation.

Do not bypass failed email checks for a live managed run. The operator requested email progress/escalation notification as part of this workflow.

Completion criterion: the command exits `0`, returns `STRUCTURAL_PASS`, and every warning has an evidence-backed disposition.

## Phase 3 — Semantic Compatibility Gate

All checks below must pass. If any answer is no or uncertain, HARD STOP.

### A. Scope and campaign identity

- The target is inside this repository or is a named feature represented by authoritative repository files.
- The goal is finite and testable; "improve," "clean up," or "work on this directory" without a bounded outcome is incompatible.
- Fresh root sessions can recover the target and next action from durable files rather than chat memory.
- The target either matches the explicit active false-signal campaign in `HANDOFF.md`, or the false-signal state is provably unclaimed and the operator's current request explicitly establishes this target.
- Treat a false signal as **provably unclaimed** only when there is no live lock, no in-progress or blocked work owned by another scope, and no handoff/task/dependency evidence of another active campaign. Uncertainty is a HARD STOP.
- A narrower target will not cause `isEverythingDone: true` to falsely close a broader campaign.
- A broader target will not silently absorb unrelated work.

If the completion signal is `true`, HARD STOP. A human must explicitly define/rearm a new campaign and reset it to `false` as required by `RALPH_LOOP.md`. The skill never resets it.

If the completion signal is `false` and `HANDOFF.md` describes a different active campaign, HARD STOP. Explain the conflict and ask the operator whether to finish, abandon, or formally replace that campaign; do not overwrite it.

If the completion signal is `false` and no campaign identity exists, the explicit operator request may establish the campaign only when the state is provably unclaimed under the criteria above. Phase 4 must then write that identity before launch. If existing durable state is ambiguous, HARD STOP rather than treating silence as permission.

### B. Durable orchestration state

- The task/feature state identifies dependencies, owner status, acceptance, verification, and done/block conditions.
- `HANDOFF.md` can state the managed target, current state, next action, decisive evidence, and genuine human blockers.
- Required review and evidence records have stable repository paths.
- Completion can be proven by repository state, reviews, gates, and commits—not model prose alone.

### C. Executability and safety

- Required commands and profiles are available and pinned as stated by `RALPH_LOOP.md`.
- The expected path to completion stays within current repository-local authority.
- Missing credentials, remote changes, push/deploy, history rewriting, system changes, unrelated deletion, and out-of-repository work are stop-and-ask boundaries.
- The worktree is clean or every existing change is intentionally owned by the active campaign. Preserve all unrelated work.
- There is no live competing Ralph lock.

### D. Notification readiness

Load the installed `email-notification` skill through the current agent's skill mechanism and follow its invocation contract. Then load its `scripts/send_notification.py` support file and run the exact resolved script path with `--dry-run` for the intended recipient and a harmless progress preview.

Do not copy credentials into commands, prompts, repository files, logs, or email content. `RESEND_API_KEY` and `RESEND_FROM_EMAIL` must be present in the executing environment. Preflight checks only non-secret key shape and sender syntax and rejects obvious placeholders. A valid dry-run proves rendering and recipient validation; neither check proves that Resend will accept the key/domain or deliver a future message. Record that limitation and treat only a real event's successful API response as "accepted by Resend."

If the skill, sender script, recipient, sender, or API environment is unavailable, HARD STOP before Ralph launch.

Completion criterion: every A–D statement is supported by live evidence and the notification dry-run exits `0` for the intended recipient.

## HARD STOP Contract

Return the failure before any launch using this exact structure:

```text
RALPH HARD STOP
Target: <requested target>
Failed check: <stable code or semantic gate name>
Evidence: <observed path, status, command result, or conflict>
Why Ralph cannot run safely: <specific consequence>
Required remediation: <smallest concrete operator or repository action>
Ralph launched: no
Email notification: <not sent | accepted by Resend with message ID | unavailable and why>
```

List multiple independent failures separately. Never say merely "incompatible" or "configuration issue."

When the preflight failure itself is a genuine escalation and email is operational, invoke `email-notification` once with event `blocked`. If email readiness is the failure, report that fact in chat; do not pretend an email was sent.

## Phase 4 — Prepare an Already-Compatible Campaign

Only after Phases 1–3 pass, reconcile durable state so the next fresh root can recover the exact campaign:

- update `HANDOFF.md` with the target, managed outcome, current state, next action, decisive commands/results, exclusions, and genuine human blockers;
- keep durable non-obvious discoveries in `KNOWLEDGE.md`, not routine progress;
- preserve valid task/dependency/review history;
- do not reset the completion signal;
- do not begin implementation in the manager session.

If preparing the handoff would replace a different active campaign, this phase is not authorized: return to HARD STOP.

Capture a baseline before launch:

- current commit and branch;
- porcelain worktree status;
- active/ready/blocked task state;
- dashboard counts/current-next pointers;
- completion signal;
- handoff contents;
- latest runtime event-log path, if any.

Completion criterion: a fresh `greekroot` session can identify the exact target and done condition from repository files alone, and all baseline facts are recorded in manager context.

## Phase 5 — Run One Observable Iteration

Launch the selected entrypoint as a tracked background process. Unless the operator explicitly requested the smoke test, use the canonical script bounded to one fresh root iteration. Pass the already-resolved campaign identity, task identity, and engineering tier explicitly so controller-owned renewal/retry counters remain bound to the same task across fresh processes:

```bash
python .scratch/ralph-loop/tools/ralph_loop.py \
  --max-iterations 1 \
  --campaign-id "<campaign-id>" \
  --task-id "<task-id>" \
  --resolved-tier "<resolved tier>"
```

For an explicit smoke-test request, use the smoke runner and do not add another `--max-iterations` argument; its two-iteration cap is fixed internally:

```bash
python .scratch/ralph-loop/tools/smoke_test.py \
  --campaign-id "<campaign-id>" \
  --task-id "<task-id>" \
  --resolved-tier "<resolved tier>"
```

The default root lease is 60 minutes. At 45 minutes the controller launches one fresh read-only `greekreview` **Diagnosis A Check** (session timer reset assessment). Diagnosis A has a 20-minute execution budget. Only exact `{"should_extend": true}` renews the lease, with at most three successful renewals per task. Its stdout contains only the model response—session-ID trailers are disabled so valid JSON is not rejected. Invalid, failed, timed-out, uncertain, completed, or hard-stopped assessments do not renew. Counters and assessor logs live under `%LOCALAPPDATA%\hermes\ralph\greek-essence\`, outside Git.

After timeout, the controller kills only the launched root's Windows process tree, runs a fresh read-only `greekreview` **Diagnosis B Check** (work-session retry assessment) with the same 20-minute budget, and permits at most one same-task retry after mandatory preflight. The diagnosis output is exactly `{"should_retry": true, "steering": "..."}` or `{"should_retry": false, "steering": null}`. Both diagnosis prompts prioritize the smallest authoritative evidence set, prohibit broad exploration and repeated checks, and require a prompt decision once decisive evidence is clear. Invalid diagnosis, failed preflight, a second timeout, completion, ambiguous surviving children, or exhausted limits fail closed. Retry preserves the campaign, task, resolved tier, existing completion signal, and extension count; it may not begin the next task.

Use the agent's background-process tool with completion notification enabled. Retain the returned process/session identifier. Do not wrap the command in `nohup`, `start`, shell `&`, or another untracked launcher.

Interpret exit behavior:

| Result | Meaning | Manager action |
|---|---|---|
| exit `0`, `COMPLETE` | Signal is true | Verify campaign completion before email/reporting |
| exit `2`, `LIMIT_REACHED` | One root iteration ended while signal stayed false | Inspect durable progress, notify if applicable, then decide whether to run another iteration |
| `HERMES_FAILED` | Root process failed | Inspect cited log; retry only if the cause is unambiguous and safe |
| `TIMEOUT` | Iteration exceeded timeout | Inspect cited log and child cleanup; usually escalate |
| `INVALID_SIGNAL` | Signal is malformed/missing | HARD STOP |
| `LOCK_CONFLICT` | Another loop owns the lock | HARD STOP and monitor the existing owner |
| exit `7`, `HARD_STOP` | Retry was denied, controller state was malformed, or process-tree cleanup was ambiguous | Preserve cited evidence and HARD STOP; do not retry automatically |
| `INTERRUPTED`/`ERROR` | Controller stopped abnormally | Inspect evidence, preserve state, and escalate when unresolved |

Do not treat expected `LIMIT_REACHED` exit `2` as a failed task. It is the observation boundary between iterations.

Completion criterion: the bounded process has exited, its outcome and event-log path are captured, and no second controller was launched concurrently.

## Phase 6 — Verify Progress and Notify

After every bounded iteration, independently reconcile live repository state. Do not trust the child summary alone.

Compare against the baseline:

- new commits and their task identity;
- changed/untracked files;
- task, phase, dashboard, dependency, evidence, review, and handoff state;
- required command results and artifacts;
- completion signal;
- genuine blockers and exact requested human action.

Classify exactly one outcome:

### Verified task completion

A task is complete only when its acceptance and required gates pass, required independent review approves, synchronized tracking is correct, and the dedicated task commit exists. Invoke `email-notification` once with:

- `event: progress` for an individual task completed within a continuing campaign;
- `task: Ralph — <Task ID/name>`;
- a concise summary with commit and decisive gates;
- a stable idempotency key such as `ralph-<campaign>-<task-id>-completed-<commit>`.

Then continue only if the campaign remains compatible and the signal is false.

### Genuine escalation/block

Notify with `event: blocked` only when user action or authority is truly required—for example credentials, push/deploy, history rewriting, system change, out-of-repository scope, destructive unrelated work, contradictory authority, or an unresolved acceptance decision. Include the exact decision/input needed and a stable idempotency key.

A routine review-required handoff, expected correction cycle, or ordinary test failure that the authorized Luna/Terra workflow can resolve is not a human escalation and must not generate a blocked email.

Stop after a genuine escalation. Do not keep launching iterations that cannot make authorized progress.

### Operational failure

After reasonable safe diagnosis, preserve the event-log path and report the failure in chat and durable handoff state. Do not send an operational-failure email unless the evidence also identifies a genuine escalation requiring precise user action; in that case use `event: blocked` and state the exact decision/input needed. Avoid blind retries after ambiguous email outcomes.

### Campaign completion

Even when the controller reports `COMPLETE`, independently confirm the target's bounded acceptance, final required gates, tracking consistency, clean/attributed worktree, and truthful handoff. Then invoke `email-notification` once with:

- `event: completed`;
- `task: Ralph — <campaign>`;
- verified result and final commit(s);
- stable idempotency key `ralph-<campaign>-completed-<final-commit>`.

Report API success as "accepted by Resend" with the message ID, not "delivered," unless delivery was independently verified.

### Continuing progress

If durable progress exists but no task completed and no escalation occurred, update the manager baseline and run Phase 2 again before another bounded iteration. Do not send routine email.

### Stalled loop

If one iteration produces no attributable task, commit, tracking, handoff, review, evidence, or meaningful gate progress, record one stall observation. If the next iteration also produces no durable progress, HARD STOP as `STALLED_CAMPAIGN`; do not burn unlimited fresh contexts. Use `event: blocked` only when the evidence identifies a precise human decision or input that can unblock the campaign. Otherwise report the terminal stall in chat and durable handoff state without sending email or inventing a user action.

Completion criterion: the iteration has one evidence-backed classification, any required email was attempted exactly once, and the manager either stops or has a fresh compatible baseline for the next iteration.

## Monitoring Rules

- Keep the background Ralph process tracked through the process tool.
- Use the controller's cited event log for root-process evidence; do not scrape unrelated session history.
- Never launch a second process while a live lock exists.
- Re-run deterministic preflight before each new bounded invocation.
- Continue monitoring until `COMPLETE`, a genuine escalation, an unrecoverable operational failure, a two-iteration stall, user cancellation, or loss of safe authority.
- If the manager session itself is about to end, do not claim monitoring continues. Record the process ID, runtime lock/log path, repository state, and exact resume command in `HANDOFF.md`, then tell the user that active agent-level email monitoring requires a live manager session.

## Common Pitfalls

1. **Treating structural pass as full compatibility.** The script cannot decide campaign semantics or authority. Complete the semantic gate.
2. **Using a directory as an unbounded goal.** A path identifies location, not acceptance. Require a finite managed outcome.
3. **Overwriting a false-signal campaign.** HARD STOP on campaign identity conflict.
4. **Resetting the signal automatically.** Only a human may rearm a completed campaign.
5. **Launching the unbounded controller and losing task-level observation.** Use one bounded iteration at a time under this skill.
6. **Calling routine review blocking an escalation.** Email only when user action is genuinely required.
7. **Trusting a child completion claim.** Verify review, gates, tracking, and commit from live files.
8. **Sending duplicate emails.** Use stable idempotency keys and one event per verified transition.
9. **Claiming email delivery.** An API success means accepted by Resend.
10. **Claiming monitoring after session loss.** Persist a truthful handoff and disclose the limitation.
11. **Inferring smoke mode from a generic test request.** Only explicit smoke-test wording or `smoke_test.py` selects the live two-iteration runner; otherwise use `ralph_loop.py`.

## Verification Checklist

- [ ] Target is repository-contained or mapped to authoritative feature records
- [ ] Managed outcome and acceptance are bounded and executable
- [ ] Structural preflight returns `STRUCTURAL_PASS`
- [ ] Every warning has an evidence-backed disposition
- [ ] Active campaign and requested target are compatible
- [ ] Completion signal was not reset by the agent
- [ ] Worktree is clean or every path is attributed
- [ ] Required profiles and controller dry-run pass
- [ ] `email-notification` is loaded and its intended-recipient dry-run passes
- [ ] Ralph is launched only as one tracked bounded iteration
- [ ] Entrypoint is `ralph_loop.py` unless the operator explicitly requested the live smoke test
- [ ] Each iteration outcome is independently reconciled
- [ ] Completion/escalation email uses a stable idempotency key
- [ ] Final completion is verified before the completed email
- [ ] No push, deployment, remote change, history rewrite, credential disclosure, or out-of-repository action occurred without explicit authority

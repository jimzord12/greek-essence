# Ralph Context-Refresh Loop Implementation Plan

> **For Hermes:** Implement this plan task-by-task. Preserve unrelated work and do not push, deploy, alter remotes, rewrite history, or modify files outside this repository.

**Goal:** Replace the bootstrap-specific deterministic Ralph state machine with a small, project-level context-refresh loop whose only semantic stop condition is `.scratch/ralph-loop/completion-signal.json` containing `{ "isEverythingDone": true }`.

**Architecture:** Move Ralph from `.scratch/bootstrap/ralph-loop/` to `.scratch/ralph-loop/`. The Python harness will only launch fresh `gpt-5.6-sol`/low root-agent iterations, retain operational safeguards, and stop when the completion Boolean becomes true. Sol owns orchestration and filesystem-derived state; it delegates substantial implementation to `gpt-5.6-luna`/high and review to `gpt-5.6-terra`/high while conserving its own context through repository-written reports and compact child summaries.

**Tech stack:** Python standard library, Hermes CLI/profile sessions, Markdown handoff files, JSON completion signal, `unittest`, Git.

---

## Decisions and invariants

1. Ralph exists at `.scratch/ralph-loop/`, outside the bootstrap namespace, because it is a general work-management tool.
2. Each iteration starts a fresh Sol root session. Session resumption is intentionally removed; `HANDOFF.md`, `KNOWLEDGE.md`, Git, and the structured workspace provide continuity.
3. The root prompt provides exactly three explicit entry points:
   - `.scratch/ralph-loop/RALPH_LOOP.md`
   - `.scratch/ralph-loop/HANDOFF.md`
   - `.scratch/ralph-loop/KNOWLEDGE.md`
4. The agent may inspect other repository files discovered through those entry points. Root `AGENTS.md` remains automatically injected by Hermes.
5. The only semantic stop signal is:

   ```json
   {
     "isEverythingDone": false
   }
   ```

6. The controller reads the signal before every iteration. `true` means successful termination; `false` means launch another fresh root agent.
7. Missing, unreadable, malformed, schema-invalid, or non-Boolean completion state is an operational error. The controller stops rather than guessing.
8. The JSON object must contain exactly one property: `isEverythingDone`.
9. Only Sol may change the completion signal to `true`, and only after all managed work and final quality gates have succeeded.
10. Python does not count tasks, parse task/phase Markdown, inspect reviews, infer Git completion, choose work, resume task sessions, or repair repository state.
11. Retained operational safeguards are: one-process lock, stale-lock recovery, per-iteration timeout, bounded iteration count, child cleanup, logs, nonzero-exit handling, and final process outcome.
12. No `CONTINUE`, `BLOCKED`, or textual `COMPLETE` model signals are introduced.

---

## Target layout

```text
.scratch/
└── ralph-loop/
    ├── RALPH_LOOP.md
    ├── HANDOFF.md
    ├── KNOWLEDGE.md
    ├── completion-signal.json
    ├── profiles/
    │   ├── README.md
    │   ├── greekroot-SOUL.md
    │   ├── greekimpl-SOUL.md
    │   └── greekreview-SOUL.md
    ├── tools/
    │   └── ralph_loop.py
    └── tests/
        └── test_ralph_loop.py
```

Runtime-only locks and logs remain outside Git at:

```text
%LOCALAPPDATA%\hermes\ralph\greek-essence\
```

---

### Task 1: Relocate Ralph under `.scratch/`

**Objective:** Establish the project-level Ralph namespace without changing behavior yet.

**Files:**

- Move: `.scratch/bootstrap/ralph-loop/` → `.scratch/ralph-loop/`
- Rename: `.scratch/ralph-loop/RALPH-LOOP.md` → `.scratch/ralph-loop/RALPH_LOOP.md`
- Update references in: `.scratch/bootstrap/BOOTSTRAP-AGENTS.md`
- Update references in: `.scratch/bootstrap/protocol.md`
- Update references in: `.scratch/bootstrap/README.md`
- Update any other tracked file returned by `git grep -n "bootstrap/ralph-loop\|ralph-loop/"`

**Steps:**

1. Run `git status --short` and preserve any pre-existing work.
2. Use `git mv` for the directory and Markdown rename so history remains traceable.
3. Search all tracked files for old paths.
4. Change references to `.scratch/ralph-loop/...`; do not rewrite historical evidence whose purpose is to record an exact command/path unless that evidence is intended as live operating documentation.
5. Run the old Ralph tests from their relocated path before behavioral changes to establish the migration baseline.
6. Run `git diff --check`.

**Expected result:** No live documentation or executable import refers to `.scratch/bootstrap/ralph-loop/`.

---

### Task 2: Add the single completion signal

**Objective:** Create a strict, durable, machine-readable stop condition.

**Files:**

- Create: `.scratch/ralph-loop/completion-signal.json`
- Modify: `.scratch/ralph-loop/tools/ralph_loop.py`
- Create/modify: `.scratch/ralph-loop/tests/test_ralph_loop.py`

**Steps:**

1. Add the tracked initial file:

   ```json
   {
     "isEverythingDone": false
   }
   ```

2. Write failing tests for a `read_completion_signal(repo: Path) -> bool` function:
   - exact Boolean `false` returns `False`;
   - exact Boolean `true` returns `True`;
   - missing file raises a clear configuration error;
   - malformed JSON raises a clear configuration error;
   - array/string/null input is rejected;
   - missing property is rejected;
   - extra properties are rejected;
   - non-Boolean values such as `1` and `"true"` are rejected.
3. Implement the smallest strict reader using Python’s `json` module.
4. Keep the controller read-only with respect to this file. Agents—not Python—own the false-to-true transition.
5. Run:

   ```bash
   python -m unittest .scratch/ralph-loop/tests/test_ralph_loop.py -v
   ```

**Expected result:** Completion is represented by one exact Boolean and invalid state fails closed.

---

### Task 3: Replace the deterministic state machine with a context-refresh loop

**Objective:** Make the controller responsible only for fresh-session iteration and operational safety.

**Files:**

- Modify: `.scratch/ralph-loop/tools/ralph_loop.py`
- Delete: `.scratch/ralph-loop/tools/check_state.py`
- Delete or replace: relocated checker/state-machine tests
- Modify: `.scratch/ralph-loop/tests/test_ralph_loop.py`
- Remove: `.scratch/ralph-loop/tools/test_ralph_loop.py` live two-task wrapper, or replace it with a clearly named non-test executable if a bounded smoke runner is still useful

**Steps:**

1. Write failing loop tests proving:
   - `true` at startup returns success without launching Hermes;
   - `false` launches one fresh Sol iteration;
   - if that iteration changes the file to `true`, the next loop check exits successfully without launching another agent;
   - every `false` iteration launches a new session and never adds `--resume`;
   - hitting `--max-iterations` stops with a distinct non-success outcome;
   - a Hermes nonzero exit stops and reports the log path;
   - timeout terminates the child and stops safely;
   - the existing lock prevents concurrent loops and stale locks recover;
   - malformed completion JSON prevents agent launch.
2. Remove imports and concepts from `check_state.py`: `State`, `Result`, `inspect_repository`, task counts, repair reasons, phase review handling, resumable sessions, and deterministic completion.
3. Reduce `run_loop` to:

   ```text
   acquire operational lock
   for each bounded iteration:
       read completion-signal.json
       if true: return COMPLETE
       launch one fresh Sol root agent
       require clean process exit
   return LIMIT_REACHED
   ```

4. Preserve per-iteration event logs, but use iteration number/timestamp rather than task ID because Python no longer knows the task.
5. Remove profile database session discovery and runtime `state.json`; no root session is resumed.
6. Add a real `--iteration-timeout` option and enforce it with child termination/cleanup.
7. Rename `--max-tasks` to `--max-iterations`.
8. Keep `--dry-run`, but redefine it to validate and print only the completion signal and intended root command without launching an agent.
9. Ensure Ctrl+C and exceptions release the lock and terminate any active child.
10. Run the focused tests and `git diff --check`.

**Expected result:** The harness contains no project-state reasoning and starts one fresh root context per false completion check.

---

### Task 4: Define Sol’s orchestration contract

**Objective:** Move task selection, reconciliation, delegation, closure, and completion judgment into the root agent and Hermes harness.

**Files:**

- Rewrite: `.scratch/ralph-loop/RALPH_LOOP.md`
- Rewrite: `.scratch/ralph-loop/profiles/greekroot-SOUL.md`
- Modify: `.scratch/bootstrap/BOOTSTRAP-AGENTS.md`
- Modify: `.scratch/bootstrap/protocol.md`

**Steps:**

1. Make `RALPH_LOOP.md` the root’s operational entry point. It must instruct Sol to:
   - read `HANDOFF.md` and `KNOWLEDGE.md` first;
   - inspect repository reality and structured work files itself;
   - select or resume the highest-priority coherent work unit;
   - conserve context by delegating detailed work and having children write durable reports/evidence directly to the repository;
   - request compact child summaries containing verdict, findings, changed files, commands/results, and next action;
   - update `HANDOFF.md` before ending every iteration;
   - add only durable, reviewed discoveries to `KNOWLEDGE.md`;
   - preserve unrelated work and remain within existing safety authority;
   - set `isEverythingDone` to `true` only after all managed work and final gates succeed.
2. Pin the root profile contract to `gpt-5.6-sol`, provider `openai-codex`, reasoning `low`.
3. Remove wording that makes Python or `check_state.py` authoritative.
4. Remove the “exactly one bootstrap task because controller selected it” assumption. Sol may finish one coherent work unit per context and must leave a precise handoff for the next fresh Sol iteration.
5. Keep the repository’s structured task, review, evidence, and phase files as working memory—not as Python-parsed state.
6. Update completion language so Sol, not a script, verifies the project’s Definition of Done before flipping the Boolean.

**Expected result:** A fresh Sol agent can enter through the three files, determine current reality, orchestrate useful progress, and leave enough durable context for its successor.

---

### Task 5: Configure Luna/high implementation and Terra/high review

**Objective:** Make model routing explicit and reproducible.

**Files:**

- Modify: `.scratch/ralph-loop/profiles/README.md`
- Modify: `.scratch/ralph-loop/profiles/greekimpl-SOUL.md`
- Modify: `.scratch/ralph-loop/profiles/greekreview-SOUL.md`
- Modify: `.scratch/ralph-loop/profiles/greekroot-SOUL.md`
- Modify: `.scratch/ralph-loop/RALPH_LOOP.md`

**Required routing:**

| Role                    | Profile       | Model           | Reasoning |
| ----------------------- | ------------- | --------------- | --------- |
| Root orchestrator       | `greekroot`   | `gpt-5.6-sol`   | low       |
| Substantial implementer | `greekimpl`   | `gpt-5.6-luna`  | high      |
| Independent reviewer    | `greekreview` | `gpt-5.6-terra` | high      |

**Steps:**

1. Update tracked profile documentation and SOUL templates with the routing above.
2. Keep profile-bound Hermes subprocesses because they provide different pinned models/reasoning and independent contexts.
3. Update the root instructions to launch Luna for substantial implementation and Terra for review, wait for real completion, and verify filesystem output rather than trusting prose.
4. During implementation, inspect the installed Hermes CLI/config schema before documenting exact profile-setting commands; do not guess unsupported config keys. Verify final live profiles with:

   ```bash
   hermes profile show greekroot
   hermes profile show greekimpl
   hermes profile show greekreview
   ```

5. Confirm all three use this repository as working directory and `openai-codex` as provider.
6. Keep child prompts standalone and scoped so the root does not need to ingest entire task documents, diffs, or logs.

**Expected result:** Every unattended run uses the intended model/reasoning assignment and fresh child contexts.

---

### Task 6: Implement Sol’s simple-fix policy

**Objective:** Avoid unnecessary agent churn while keeping substantial work independently implemented and reviewed.

**Files:**

- Modify: `.scratch/ralph-loop/RALPH_LOOP.md`
- Modify: `.scratch/ralph-loop/profiles/greekroot-SOUL.md`
- Modify: `.scratch/bootstrap/BOOTSTRAP-AGENTS.md`
- Modify: `.scratch/bootstrap/protocol.md`

**Steps:**

1. Define a simple fix as all of:
   - mechanical and unambiguous;
   - localized to one or two files;
   - no architecture, dependency, security/privacy, schema, migration, or broad behavior change;
   - acceptance can be proven by existing relevant quality gates;
   - no expansion beyond the reviewer’s cited finding.
2. After Terra returns a review with only simple findings, allow Sol to apply those fixes directly.
3. Require Sol to run every relevant quality gate cited by the task/reviewer.
4. If all gates pass, allow Sol to close the task without another Terra review.
5. If any gate fails, the fix expands in scope, or uncertainty appears, Sol must stop self-fixing and delegate the failed state to Terra for review. Terra may direct substantial corrective implementation back to Luna.
6. Preserve independent Terra review for the original substantial Luna implementation. The no-extra-review exception applies only to Sol’s narrowly scoped simple corrections validated by objective green gates.
7. Update old protocol statements that categorically prohibit all root implementation or require every correction to return to the original implementer.
8. Add examples to `RALPH_LOOP.md`: typo/stale metadata/small assertion/config correction are potentially simple; architecture, dependency, security, broad test redesign, and unclear failures are not.

**Expected result:** Sol can cheaply finish safe mechanical corrections, while failed or expanding fixes return to high-reasoning review/orchestration.

---

### Task 7: Migrate handoff and knowledge ownership

**Objective:** Ensure context survives fresh root sessions without a Python-owned state database.

**Files:**

- Modify: `.scratch/ralph-loop/HANDOFF.md`
- Modify: `.scratch/ralph-loop/KNOWLEDGE.md`
- Modify: `.scratch/ralph-loop/RALPH_LOOP.md`

**Steps:**

1. Preserve current B06-02-ready bootstrap facts during relocation.
2. Add a concise HANDOFF template containing:
   - last completed work;
   - active/resumable work;
   - current repository/worktree facts;
   - next recommended action and why;
   - child session IDs only when a current iteration needs them;
   - decisive commands/results;
   - blockers requiring human action.
3. Keep HANDOFF mutable and current; do not turn it into an append-only log.
4. Keep KNOWLEDGE limited to durable, non-obvious discoveries. Progress, temporary failures, and task status remain in HANDOFF or task records.
5. Remove references to controller runtime `state.json` and session resumption.
6. State that interrupted work is recovered from Git status, diffs, structured task files, reports, and HANDOFF by the next fresh Sol agent.

**Expected result:** Killing the loop between iterations loses no essential decision context, and an interrupted iteration remains recoverable from repository reality.

---

### Task 8: Update commands, tests, and operating documentation

**Objective:** Make the simplified loop safe and unambiguous to run.

**Files:**

- Modify: `.scratch/ralph-loop/RALPH_LOOP.md`
- Modify: `.scratch/ralph-loop/profiles/README.md`
- Modify: `.scratch/bootstrap/README.md`
- Modify all remaining live references identified by path/model/state-machine searches

**Steps:**

1. Document canonical commands from the repository root:

   ```bash
   python .scratch/ralph-loop/tools/ralph_loop.py --dry-run
   python .scratch/ralph-loop/tools/ralph_loop.py
   python .scratch/ralph-loop/tools/ralph_loop.py --max-iterations 2
   python -m unittest .scratch/ralph-loop/tests/test_ralph_loop.py -v
   ```

2. Clearly label bounded real runs as live AI execution. Do not retain a file named `test_ralph_loop.py` that secretly launches two real agents.
3. Document how to reset the completion signal for a new managed campaign: explicit human edit from `true` to `false`; the controller never resets it automatically.
4. Document operational outcomes separately from semantic completion: success, iteration limit, Hermes process failure, timeout, invalid signal, and lock conflict.
5. Search for stale model assignments (`terra` implementer, `sol` reviewer, medium root reasoning), old Ralph paths, `check_state.py`, `--max-tasks`, `--resume`, and deterministic-authority wording.
6. Run all Ralph unit tests and relevant bootstrap workspace validation as advisory checks. The advisory validator must not control Ralph’s loop.
7. Run `git diff --check` and inspect `git status --short`.

**Expected result:** Operators cannot confuse tests with live execution, and all documentation describes the new model consistently.

---

### Task 9: End-to-end smoke verification

**Objective:** Prove the harness behavior without consuming real bootstrap work accidentally.

**Files:**

- Test only; do not change unrelated application files.

**Steps:**

1. Run the unit suite and verify all completion-signal, loop, lock, timeout, and command-construction tests pass.
2. In a temporary fixture repository or with an injected fake executor:
   - start with `false`;
   - simulate one successful root iteration changing it to `true`;
   - verify the next check exits and no second root starts.
3. Verify `true` at startup launches no Hermes process.
4. Verify invalid JSON launches no Hermes process and returns a nonzero error.
5. Verify generated root command pins `greekroot`, `gpt-5.6-sol`, `openai-codex`, and starts a fresh session without `--resume`.
6. Run `--dry-run` in the real repository and confirm it performs no mutation.
7. Verify only intended Ralph/documentation files changed.
8. Create a dedicated local commit for the Ralph refactor only after all focused tests pass. Do not push.

---

## Acceptance criteria

- Ralph lives at `.scratch/ralph-loop/`; no live path remains under `.scratch/bootstrap/ralph-loop/`.
- `completion-signal.json` contains exactly one Boolean property, `isEverythingDone`.
- Python checks that Boolean before each iteration and performs no project-state inference.
- A true signal prevents any further agent launch.
- Every false iteration starts a fresh Sol/low root session.
- Sol receives the three explicit entrypoint files and owns orchestration/state judgment.
- Luna/high handles substantial implementation; Terra/high handles independent review.
- Sol may complete simple review fixes directly when all relevant quality gates pass.
- A failed or expanding Sol fix is delegated to Terra rather than repeatedly self-repaired.
- Locks, stale-lock recovery, bounded iterations, timeout, cleanup, logs, and nonzero-exit handling remain.
- Session discovery/resumption, `check_state.py`, task counting, phase parsing, repair attempts, and textual loop signals are removed.
- Unit tests are hermetic and never launch live Hermes agents.
- Documentation and profile templates agree with the final behavior.
- Git diff is scoped, tests pass, and no push/deploy/remote/history-rewrite action occurs.

## Risks and mitigations

- **Erroneous `true` written by Sol:** This design intentionally trusts the agent. Mitigate through a strong RALPH contract, final quality-gate checklist, and visible one-line JSON diff—not duplicate Python reasoning.
- **Infinite repetition while work is blocked:** Use bounded iterations and fail on repeated process errors/timeouts. HANDOFF must record human blockers clearly; there is still only one semantic completion signal.
- **Fresh-agent rediscovery cost:** Keep HANDOFF concise and current, KNOWLEDGE durable, and child details in repository-owned reports.
- **Root context growth:** Require compact child summaries and direct-to-filesystem evidence; Sol reads detailed artifacts only when reconciling uncertainty.
- **Model-routing drift:** Pin and verify the three Hermes profiles before unattended execution.
- **Interrupted child process:** Terminate on timeout, preserve logs and repository state, and let the next fresh Sol reconcile from the filesystem.

## Non-goals

- Building a generic task database or scheduler.
- Reimplementing task/phase/review validation in Python.
- Adding multiple model-emitted control signals.
- Automatically resetting completion for new projects.
- Changing bootstrap product requirements or completing remaining bootstrap tasks as part of this refactor.
- Pushing, deploying, changing remotes, rewriting Git history, or modifying user/system scope beyond explicitly configuring the three existing Hermes profiles during implementation.

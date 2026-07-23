# Deterministic Ralph Campaign Transition Implementation Plan

> **For Hermes:** Execute this plan under Sol as root integrator. Delegate substantial implementation to a fresh `greekimpl` Luna session and independent review to a fresh `greekreview` Terra session. Do not launch a managed Ralph campaign for this work.

**Goal:** Add an explicit project-owned command that safely and deterministically archives one declared completed Ralph controller identity and initializes a declared new identity without reading or resetting the semantic completion signal.

**Architecture:** Add a narrow transition operation beside the existing controller state primitives in `.scratch/ralph-loop/tools/ralph_loop.py`, exposed through a separate CLI wrapper so the established live-controller CLI remains backward compatible. The operation acquires the existing external runtime lock, strictly validates the completed state and absence of any recorded/live owned root, creates a collision-free timestamped archive outside Git, atomically replaces `controller-state.json` with a fully zeroed new state, emits bounded lifecycle events, and releases the lock on every handled path. Tests use only `TemporaryDirectory` state roots and mocked process/time/write boundaries.

**Tech stack:** Python 3 standard library (`argparse`, `dataclasses`, `datetime`, `json`, `os`, `pathlib`, `shutil`/byte I/O, `unittest`, `unittest.mock`); existing Ralph controller and lifecycle logger.

**Resolved depth:** Tier 2 — Prototype from `AGENTS.md`, with fail-closed integrity behavior explicitly required by `NEXT.md`.

---

## Verified planning baseline (read-only inspection, 2026-07-23)

- `main` and `origin/main` both resolve to `35b141d7da12ba43755cd8be6be0ee5358b6f119`; primary worktree was clean before this plan file was written.
- A separate worktree exists at `C:/Users/jimzord12/Documents/GitHub/greek-essence-ralph-analytics` on `feature/ralph-loop-analytics`; it must not be touched.
- Live Ralph runtime has no `ralph.lock`. `controller-state.json` strictly identifies `bootstrap-b07-03` / `B07-03` / tier `2`, has `current_root_pid: null`, and retains `current_iteration: 1`.
- The tracked completion signal is exactly `{"isEverythingDone": true}` and must remain byte-for-byte untouched by this task.
- No controller-owned root PID is recorded. General Hermes/Desktop processes exist, so process checks must be scoped to the recorded PID rather than broad process-name matching.
- Existing state logic lives in `.scratch/ralph-loop/tools/ralph_loop.py`: strict JSON/schema validation, `ControllerState`, atomic temp-plus-`os.replace` writes, lifecycle logging, PID liveness, and lock acquisition/release.
- Existing Ralph tests are `.scratch/ralph-loop/tests/test_ralph_loop.py`, `test_ralph_supervision.py`, and `test_ralph_manager_preflight.py`.
- `NEXT.md` remains compatible with this design. The task is the transition gap only; K-002 Job Objects/orphan recovery, asset work, product work, and completion-signal authorization remain out of scope.

## Fixed interface and invariants

Expose this explicit command from the repository root:

```bash
python .scratch/ralph-loop/tools/transition_campaign.py \
  --completed-campaign-id bootstrap-b07-03 \
  --completed-task-id B07-03 \
  --completed-resolved-tier 2 \
  --new-campaign-id <explicit-new-campaign> \
  --new-task-id <explicit-new-task> \
  --new-resolved-tier <explicit-resolved-tier>
```

Optional test/operations arguments:

- `--state-dir PATH`: defaults to the existing `%LOCALAPPDATA%\hermes\ralph\greek-essence` location; tests always pass a temporary directory.
- `--archive-timestamp YYYYMMDDTHHMMSSffffffZ`: optional deterministic/test hook. Normal operation generates a UTC timestamp including microseconds. It never selects identity.

Rules:

1. All six identity flags are required and trimmed non-empty strings. No defaults, prose parsing, Git inspection, TODO inference, or model judgment.
2. Completed and new campaign IDs must differ, and completed and new task IDs must differ. The tier may remain equal, but both declared tiers must be explicit and the completed tier must exactly match state.
3. Acquire/hold the existing `ralph.lock` before reading or writing state. A live owner fails with `LOCK_CONFLICT`; stale-lock behavior remains the existing controller behavior. Holding the lock closes the race with a controller launch.
4. Strictly load the existing state; do not create it when absent. Malformed, missing, duplicate-key, wrong-schema, or identity-mismatched state fails closed.
5. Require `current_root_pid is None`. A non-null recorded PID fails closed whether currently live or dead: the command is a campaign transition, not orphan/stale-root recovery. If a PID is present, report only the PID and whether liveness was observed; never inspect or log unrelated command lines.
6. New state is exactly `ControllerState(new_campaign, new_task, new_tier)` so supervision counters are `0` and iteration/root/log fields are `None`.
7. Archive path is `state_dir/archive/controller-state-<sanitized-completed-campaign>-<sanitized-completed-task>-<UTC timestamp>.json`. Sanitize only for the filename; retain exact identities inside JSON/events. Create the archive with exclusive-create semantics and fail on collision.
8. Crash-safe sequence while holding the lock:
   - serialize and write the new state to a unique same-directory temporary file; flush and `os.fsync` it;
   - exclusively create the archive from the original controller-state bytes; flush and `os.fsync` it;
   - atomically `os.replace` the prepared new-state temporary over `controller-state.json`;
   - best-effort fsync the containing directory where supported;
   - clean a prepared temporary on handled failure, but never delete/overwrite the original state or an archive whose preservation is uncertain.
     A crash before replacement leaves the old current state intact (possibly with a preserved archive); a crash after replacement leaves complete new state plus archive. No partial JSON becomes current.
9. Emit privacy-bounded events such as `campaign_transition_start`, `campaign_transition_validation_complete`, `campaign_transition_archive_complete`, `campaign_transition_state_replace_complete`, `campaign_transition_complete`, and `campaign_transition_failed`. Include only identities, tier, bounded path, PID/liveness when relevant, and exception type—not prompts, credentials, unrelated command lines, or raw state content.
10. Never read, write, or reset `.scratch/ralph-loop/completion-signal.json` in the transition code.

---

### Task 1: Establish the task branch and immutable baseline evidence

**Objective:** Start implementation from the verified main commit without disturbing the other worktree or runtime state.

**Files:**

- Existing plan: `.hermes/plans/2026-07-23_152431-ralph-campaign-transition.md`
- No runtime files modified.

**Steps:**

1. Re-run `git fetch --prune origin`, `git status --short --branch`, `git rev-parse HEAD`, `git rev-parse origin/main`, and `git worktree list --porcelain`.
2. Require HEAD and `origin/main` to remain `35b141d7da12ba43755cd8be6be0ee5358b6f119` unless a new upstream commit is inspected and reconciled before proceeding.
3. Confirm `.scratch/ralph-loop/completion-signal.json` is true and capture its SHA-256 for later unchanged-file verification.
4. Read the external lock/state read-only again. Stop if a live lock, recorded root, malformed state, or unexpected identity now exists.
5. Create `task/ralph-campaign-transition` from the verified `main`. Do not create or use a new worktree, and do not touch `feature/ralph-loop-analytics`.
6. Record exact commands, exit codes, and concise results in implementation evidence/PR notes; do not place runtime IDs or logs in tracked docs.

Expected: branch is based on verified `main`; only the plan file may be initially untracked/modified; live runtime remains untouched.

### Task 2: Delegate the RED transition contract to Luna

**Objective:** Add focused failing tests defining all authorized success and fail-closed behavior before production code.

**Files:**

- Create: `.scratch/ralph-loop/tests/test_ralph_transition.py`
- No production-code edits in this RED step.

**Luna brief requirements:** Include the objective, resolved Tier 2, exact command contract/invariants above, live-state prohibition, other-worktree warning, and requirement to run tests only against temporary state directories.

**Tests to write:**

1. `test_success_archives_exact_completed_bytes_and_writes_zeroed_new_state`
   - create valid completed state with nonzero counters and no root;
   - invoke the transition core with a fixed timestamp;
   - assert one exact archive exists, original bytes are preserved, current state has new exact identity and zero/`None` supervision fields, lock is released, and no completion-signal path is touched.
2. `test_live_lock_owner_fails_without_state_or_archive_change` using the current test PID/mocked liveness.
3. `test_non_null_recorded_root_fails_whether_pid_is_live_or_dead` with subtests for both liveness results; assert no process termination call occurs.
4. `test_completed_identity_and_tier_mismatch_fail_closed` with campaign, task, and tier subtests.
5. `test_missing_or_malformed_controller_state_fails_closed`, including strict duplicate key/wrong schema.
6. `test_incomplete_or_inappropriately_same_new_identity_is_rejected` for whitespace values, same campaign, and same task; same tier remains allowed.
7. `test_archive_name_collision_preserves_current_state` using a fixed timestamp and pre-created archive.
8. `test_new_state_temp_write_or_fsync_failure_preserves_old_state_and_no_archive`.
9. `test_archive_write_or_fsync_failure_preserves_old_current_state_and_no_partial_archive` (or asserts any exclusively created failed artifact is never treated as success).
10. `test_atomic_replace_failure_preserves_old_current_state_and_complete_archive` and cleans the prepared temp best-effort.
11. `test_cli_requires_all_six_identities_and_returns_structured_nonzero_failure`.
12. `test_transition_events_are_bounded_and_contain_no_prompt_command_or_raw_state`.

**RED command:**

```bash
python -B -m unittest .scratch.ralph-loop.tests.test_ralph_transition -v
```

Because hyphenated package paths may not import portably, use this canonical focused command instead if needed:

```bash
python -B -m unittest discover -s .scratch/ralph-loop/tests -p "test_ralph_transition.py" -v
```

Expected: exit `1`, failures/import errors only because the transition API/CLI does not yet exist. Confirm existing suites were not edited to fake RED.

**Commit:** Do not commit a knowingly failing standalone state unless needed for review history; Luna does not commit under the repository protocol. Sol verifies RED output before authorizing GREEN.

### Task 3: Implement the minimal transition core and explicit CLI

**Objective:** Make the focused contract pass without changing ordinary Ralph loop behavior.

**Files:**

- Modify: `.scratch/ralph-loop/tools/ralph_loop.py`
- Create: `.scratch/ralph-loop/tools/transition_campaign.py`
- Modify as test feedback requires: `.scratch/ralph-loop/tests/test_ralph_transition.py`

**Production API shape:**

```python
@dataclass(frozen=True)
class CampaignIdentity:
    campaign_id: str
    task_id: str
    resolved_tier: str

@dataclass(frozen=True)
class TransitionResult:
    archive_path: Path
    state_path: Path


def transition_campaign_state(
    state_dir: Path,
    completed: CampaignIdentity,
    new: CampaignIdentity,
    *,
    timestamp_utc: str | None = None,
    pid_is_running_fn: Callable[[int], bool] = _pid_is_running,
    replace_fn: Callable[[Path, Path], None] = os.replace,
) -> TransitionResult:
    ...
```

Implementation constraints:

- Reuse `_strict_json`, `_validated_controller_state`, `_acquire_lock`, `ControllerState`, `LifecycleLogger`, and the existing default state directory.
- Add a strict existing-state loader rather than calling `load_controller_state`, because transition must not initialize missing state.
- Factor atomic serialization only as much as needed to share correct same-directory temp writing; preserve existing `save_controller_state` behavior and diagnostics.
- Use dependency injection only at hard-to-test time/replace/PID boundaries; do not add a framework or recovery subsystem.
- The CLI prints one JSON result containing `outcome`, old/new identity, and archive path. Map lock conflict distinctly and all other rejected transitions to structured nonzero outcomes without stack traces.
- No `subprocess` process killing, completion-signal access, task inference, Git calls, or Job Object behavior.
- Release the acquired lock in `finally`, preserving the existing lifecycle release diagnostics.

**GREEN commands:**

```bash
python -B -m unittest discover -s .scratch/ralph-loop/tests -p "test_ralph_transition.py" -v
python -B -m unittest discover -s .scratch/ralph-loop/tests -p "test_*.py" -v
```

Expected: both exit `0`.

### Task 4: Document the command and preserve operational boundaries

**Objective:** Make the explicit entry point discoverable without implying semantic authorization or automatic campaign selection.

**Files:**

- Modify: `.scratch/ralph-loop/RALPH_LOOP.md`
- Do not yet reconcile: `NEXT.md`, `TODO.md`, `.scratch/ralph-loop/HANDOFF.md` (closure occurs only after review/merge).

**Documentation changes:**

- Add the exact transition command under canonical commands.
- State that all six identity values are human-declared, the command does not reset/read the completion signal, and it does not launch Hermes.
- State fail-closed prerequisites and archive location/shape.
- State that a non-null recorded root requires separate authorized recovery; transition never kills it.
- Keep K-002 explicitly out of scope.

**Verification:**

```bash
python .scratch/ralph-loop/tools/transition_campaign.py --help
python .scratch/ralph-loop/tools/ralph_loop.py --dry-run
```

Expected: both exit `0`; dry-run behavior remains unchanged and does not mutate runtime files.

### Task 5: Perform isolated runtime-file acceptance verification

**Objective:** Exercise the real CLI and filesystem sequence without touching `%LOCALAPPDATA%` Ralph state.

**Files:**

- Temporary directory only; no live runtime mutation.

**Steps:**

1. Create a temporary state directory using Python `tempfile.TemporaryDirectory`.
2. Write a valid completed `controller-state.json` there with nonzero supervision counters and `current_root_pid: null`.
3. Invoke the real wrapper with `--state-dir <temp>` and six explicit identities.
4. Assert exit `0`, structured success JSON, exact archive contents, fresh zeroed state, bounded lifecycle events, and absent lock/temp artifacts.
5. Repeat one real CLI call with a mismatched completed task; assert nonzero exit and byte-identical current state.
6. Compare the real completion-signal SHA-256 with Task 1 and confirm live `%LOCALAPPDATA%` `controller-state.json` metadata/content hash is unchanged from the pre-implementation observation.

Expected: isolated success and failure behave exactly as documented; real live state and completion signal are unchanged.

### Task 6: Sol verification and task commit

**Objective:** Independently verify Luna’s filesystem output and all required gates before review.

**Files:** All task-owned changed files only.

**Commands:**

```bash
python -B -m unittest discover -s .scratch/ralph-loop/tests -p "test_ralph_transition.py" -v
python -B -m unittest discover -s .scratch/ralph-loop/tests -p "test_*.py" -v
git diff --check
git status --short
git diff -- .scratch/ralph-loop/tools/ralph_loop.py .scratch/ralph-loop/tools/transition_campaign.py .scratch/ralph-loop/tests/test_ralph_transition.py .scratch/ralph-loop/RALPH_LOOP.md .hermes/plans/2026-07-23_152431-ralph-campaign-transition.md
```

Also run any affected-file checks identified by Luna. Do not run `smoke_test.py`, launch Ralph, reset completion, or use live runtime as a fixture.

Expected: all test/check commands exit `0`; diff is bounded; no unrelated/concurrent files are staged.

**Commit:**

```bash
git add .hermes/plans/2026-07-23_152431-ralph-campaign-transition.md \
  .scratch/ralph-loop/tools/ralph_loop.py \
  .scratch/ralph-loop/tools/transition_campaign.py \
  .scratch/ralph-loop/tests/test_ralph_transition.py \
  .scratch/ralph-loop/RALPH_LOOP.md
git commit -m "feat(ralph): add deterministic campaign transition"
```

### Task 7: Independent Terra review and corrections

**Objective:** Obtain independent spec, safety, and code-quality approval before PR/merge.

**Terra review brief:** Provide the verified base/head SHAs, full task contract, resolved tier, changed files, exact test outputs, isolated CLI evidence, and explicit prohibitions. Require Terra to inspect the actual diff and rerun proportionate tests.

**Required review focus:**

- exact explicit identity contract and no inference;
- lock/race behavior;
- recorded/live root fail-closed semantics;
- strict state schema/identity/tier matching;
- archive collision and preservation;
- crash/atomic-write failure behavior on Windows-compatible filesystems;
- zeroed fresh state;
- lifecycle privacy bounds;
- completion signal and live state untouched;
- preservation of existing controller diagnostics and tests;
- no K-002/general orphan-recovery expansion.

**Correction loop:**

- Blocking/High or substantive findings go back to Luna with the exact findings and inherited tier.
- Sol may apply only a mechanical one/two-file simple fix under the repository simple-fix policy, followed by all cited gates.
- Re-run focused/full tests and `git diff --check` after every correction; obtain renewed Terra approval for substantive changes.
- Commit accepted fixes with a normal additional commit; do not amend/rewrite history.

Expected: explicit Terra `Approved` verdict with no unresolved Blocking/High findings.

### Task 8: Push, PR, CI/review reconciliation, and normal merge

**Objective:** Complete the authorized substantial-work workflow with independently verified evidence.

**Steps and commands:**

```bash
git push -u origin task/ralph-campaign-transition
gh pr create --base main --head task/ralph-campaign-transition \
  --title "feat(ralph): add deterministic campaign transition" \
  --body-file <prepared-pr-body.md>
gh pr checks <PR-number> --watch
gh pr view <PR-number> --json state,mergeable,reviewDecision,statusCheckRollup,headRefOid,baseRefOid
gh pr merge <PR-number> --merge
```

PR body must summarize behavior, safety invariants, exact commands/results, isolated runtime evidence, unchanged completion/live state, and Terra verdict. If CI or review finds a defect, fix on the same branch, rerun gates, push, and re-review as required.

Do not use squash/rebase merge and do not delete the branch.

Expected: PR merged by a normal merge commit; no unresolved checks/reviews.

### Task 9: Reconcile tracked handoff/backlog after merge

**Objective:** Record only durable closure and leave later dependency nodes unauthorized.

**Files:**

- Modify: `NEXT.md`
- Modify: `TODO.md`
- Modify: `.scratch/ralph-loop/HANDOFF.md`
- Modify `KNOWLEDGE.md` only if review establishes a durable non-obvious discovery; do not close or broaden K-002.

**Steps:**

1. On the task branch before final merge if feasible—or in a small follow-up branch/PR if merge evidence is required—remove/reconcile the completed transition node from `TODO.md`.
2. Update `NEXT.md` to state transition completion and identify the reviewed sequential asset prompt pack as the next dependency **without authorizing its execution** unless the operator separately promotes it.
3. Update Ralph handoff with durable current campaign status only; exclude process IDs, raw logs, session IDs, or detailed runtime state.
4. Rerun `git diff --check` and relevant Ralph unit tests for any code-adjacent correction.
5. Commit/push/review/normal-merge this reconciliation through the same PR when possible. If PR is already merged, use a bounded follow-up PR rather than direct unreviewed substantial changes.

### Task 10: Final main-state verification and stop

**Objective:** Prove the accepted implementation is on `main` and stop at the authorized boundary.

**Commands:**

```bash
git switch main
git pull --ff-only origin main
git status --short --branch
git log -5 --oneline --decorate
python -B -m unittest discover -s .scratch/ralph-loop/tests -p "test_*.py" -v
git diff --check
gh pr view <PR-number> --json state,mergedAt,mergeCommit,headRefName,baseRefName
```

Final assertions:

- `main` equals `origin/main` and contains the normal merge commit.
- Worktree is clean.
- Complete Ralph suite and diff check exit `0`.
- Terra approval and PR merge are verified from source, not agent prose.
- Completion signal hash remains unchanged and true.
- Live Ralph state was never transitioned for demonstration.
- Branch remains available for operator deletion.
- Asset prompt pack, documentation-review node, and P1 planning have not begun.

Stop once these gates pass.

---

## Likely changed files

- `.scratch/ralph-loop/tools/ralph_loop.py`
- `.scratch/ralph-loop/tools/transition_campaign.py` (new)
- `.scratch/ralph-loop/tests/test_ralph_transition.py` (new)
- `.scratch/ralph-loop/RALPH_LOOP.md`
- `.hermes/plans/2026-07-23_152431-ralph-campaign-transition.md` (this plan)
- Closure only after approval: `NEXT.md`, `TODO.md`, `.scratch/ralph-loop/HANDOFF.md`

## Risks and mitigations

- **Two-artifact atomicity:** A filesystem cannot atomically create an archive and replace current state together. Mitigate by fully preparing/fsyncing new state, exclusively preserving/fsyncing old bytes, then atomically replacing current state. Every crash point preserves at least one complete authoritative copy and never exposes partial current JSON.
- **Controller launch race:** Mere lock inspection is insufficient. Acquire and hold the same `ralph.lock` for the entire transition.
- **Stale recorded PID:** Do not reinterpret or clear it. Any non-null recorded root blocks transition, regardless of observed liveness, preserving K-002’s fail-closed boundary.
- **Archive collision:** Microsecond timestamps reduce probability; exclusive creation and deterministic collision tests prevent overwrite.
- **Windows filesystem behavior:** Keep temp and target on the same state volume; avoid POSIX-only rename assumptions; test injected fsync/open/replace failures.
- **Lifecycle logger failure:** Preserve existing non-fatal logger behavior unless Terra demonstrates the transition contract requires otherwise; state safety must not depend on log success.
- **Plan file dirties main:** Create the authorized task branch before any implementation edit and carry this plan into the task commit; do not commit it directly to `main` outside the PR workflow.

## Open questions

None requiring operator input. The plan intentionally resolves “appropriately different” as both campaign ID and task ID changing, while allowing the explicitly declared tier to remain the same. If repository tests or Terra identify a conflicting existing contract, stop and escalate that contract conflict rather than silently weakening validation.

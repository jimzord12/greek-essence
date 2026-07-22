# Project Handoff

## Purpose

`NEXT.md` is the durable handoff for the next project agent. Every agent must inspect this file at startup and follow it when it contains instructions. Keep it current, concise, and repository-grounded. Ralph-specific orchestration state remains in `.scratch/ralph-loop/HANDOFF.md`.

## Current work: debug Ralph controller process ownership

The active engineering task is to diagnose the repeated Windows lifecycle failure in which the tracked Ralph controller disappears while its launched `hermes.exe` root remains alive.

### Observed evidence

- First incident: controller PID `44988` disappeared while Hermes root PID `33596` survived.
- Second incident: controller PID `43772` disappeared while Hermes root PID `10172` survived.
- In both incidents, `ralph.lock` and `controller-state.json.current_root_pid` remained stale, proving normal controller cleanup did not finish.
- The outer Hermes background tracker reported exit code `0` because it tracks a Git Bash wrapper around the Python controller; that does not prove the complete Windows process tree exited.
- Archived incident records are under `%LOCALAPPDATA%\hermes\ralph\greek-essence\`.
- Durable issue details are in `.scratch/ralph-loop/KNOWLEDGE.md`, entry `K-002`.

### Current scope

1. Add diagnostic PID/process-lifecycle events to `.scratch/ralph-loop/tools/ralph_loop.py` and focused tests.
2. Capture controller PID/parent PID, root PID, command identity, launch/poll/exit status, state writes that set or clear `current_root_pid`, lock lifecycle, exception/return/finally paths, cleanup boundaries, and final controller outcome.
3. Keep diagnostic data in the existing runtime event log outside Git; do not record credentials, prompt contents, or unrelated process command lines.
4. Do not implement broad automatic process termination or Windows Job Objects until the new evidence identifies the failing boundary or the operator expands scope.

### Safety and attribution

- Do not launch another Ralph controller while debugging this issue.
- No live Ralph controller/root or active lock was present when this handoff was written.
- Preserve the existing B07-01 task-owned modification:
  `.scratch/bootstrap/phases/07-final-verification/tasks/01-clean-room-verification/task.md`.
  It records the interrupted implementer session and must not be reset, discarded, or included accidentally in the controller-debugging commit.
- Preserve all unrelated and user-owned changes.
- Do not push, deploy, rewrite history, modify remotes, expose credentials, or make system-wide changes.

### Verification

Use test-first development. Run the focused Ralph controller tests, then the full Ralph unit suite, followed by `git diff --check`. Record what each new diagnostic test proves. Do not claim the lifecycle defect fixed merely because instrumentation tests pass; a later controlled live reproduction is required to identify the cause.

### Completion/update rule

Current implementation status on branch `fix/ralph-controller-pid-logging`:

- `AGENTS.md` now requires every project agent to inspect and follow non-empty `NEXT.md`.
- The controller writes a dedicated JSONL lifecycle log under `%LOCALAPPDATA%\hermes\ralph\greek-essence\logs\controller-lifecycle-<timestamp>-pid-<pid>.jsonl`.
- Logged boundaries include controller/parent identity, lock acquire/release, root launch identity and PID, state writes, supervision poll/wait outcomes, assessments/extensions, exception/finally paths, root PID clearing, loop return, and controller exit.
- Lifecycle events intentionally omit prompts and full commands; they record only bounded root identity fields.
- Focused supervision tests and the full Ralph suite pass (`63` tests). Lifecycle-log I/O is fail-open so diagnostic failures cannot prevent controller cleanup.
- Independent review identified post-`Popen` state-write and cleanup-exception orphan boundaries. The executor now establishes cleanup immediately after launch, terminates the root when the initial state write fails, preserves the primary exception when state clearing or process termination also fails, records cleanup failure as an exception note/lifecycle event, and has regression tests for these boundaries and end-to-end lifecycle-log I/O failure.

Next action: the exact staged diff passed final independent review with no security concerns, logic errors, or suggestions. Commit only `NEXT.md`, `AGENTS.md`, the controller, and its two test files; then run a separately authorized controlled live reproduction. Do not include the existing B07-01 task-status modification in the debugging commit and do not claim the underlying lifecycle defect fixed until live evidence identifies the terminating boundary.

Keep this file current with review findings, commits, decisive live evidence, remaining uncertainty, and exact next action. Do not delete or empty project handoff context unless the operator explicitly requests it or all recorded work has been durably reconciled elsewhere.

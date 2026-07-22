# Ralph Context-Refresh Loop — Independent Review 01

**Reviewer canonical session_id:** `20260722_120723_498b9c`
**Reviewed implementation session_id:** `20260722_115237_90b6f0`
**Verdict:** Changes requested

## Scope reviewed

Reviewed the complete live worktree implementation of `.hermes/plans/2026-07-22_114158-simplify-ralph-loop-context-refresh.md`, including all relocated, added, modified, and deleted Ralph/bootstrap files. The pre-existing untracked `.hermes/` directory was preserved; the assigned plan remains present at `.hermes/plans/2026-07-22_114158-simplify-ralph-loop-context-refresh.md`.

## Findings

1. **High — documented required unit-test command is not executable on the supported Windows/Python environment.**
   - **Location:** `.scratch/ralph-loop/RALPH_LOOP.md:29-32`; `.scratch/bootstrap/FOR_HUMAN_OPERATOR.md:36-39`.
   - **Violated requirement:** Plan Task 2 step 5 and Task 8 step 1 require the focused `python -m unittest .scratch/ralph-loop/tests/test_ralph_loop.py -v` command; Task 8 requires safe, unambiguous operating commands and the acceptance criteria require passing hermetic unit tests and consistent documentation.
   - **Evidence/reproduction:** From the repository root, `python -m unittest .scratch/ralph-loop/tests/test_ralph_loop.py -v` exited `1` before test loading with `ValueError: Empty module name` under the installed Windows Python 3.11. The same invalid command is presented as the primary hermetic-test command in both operating documents. A working direct invocation and unittest discovery each ran all 16 tests successfully, so this is command/documentation correctness rather than a test failure.
   - **Required correction:** Make one runnable Windows-safe invocation the canonical focused test command in every live operating document, and remove the failing `-m unittest` path-form invocation as a purported standard command. Record the necessary compatibility deviation from the plan's impossible path-form command rather than presenting an expected failure as a normal command.
   - **Verification:** Run the selected canonical command from the repository root and confirm all 16 tests pass; rerun `git diff --check`; verify neither live operating document retains the failing command as canonical.

## Verified acceptance evidence

- `.scratch/ralph-loop/` exists, `.scratch/bootstrap/ralph-loop/` is absent, and the plan is preserved.
- `completion-signal.json` has exactly `{"isEverythingDone": false}`. Hermetic tests cover strict object/Boolean validation including duplicate properties; an independent temporary-repository probe returned `COMPLETE` with a true signal without launching Hermes and returned `INVALID_SIGNAL`/exit `3` for invalid JSON.
- The controller is read-only with respect to the signal, checks it before each iteration, has no project-state parser/state writer, and its active command has no `--resume`. The focused suite passed 16/16, including fresh command construction, true/false behavior, lock/stale-lock handling, timeout termination, cleanup, and nonzero-exit reporting.
- Real-repository `--dry-run` exited `0`, printed the fresh `greekroot`/`gpt-5.6-sol`/`openai-codex` command and false signal, and left the worktree unchanged.
- Live profile verification confirms `greekroot` Sol/low, `greekimpl` Luna/high, and `greekreview` Terra/high, all with `openai-codex` and repository `terminal.cwd`.
- `python -B .scratch/bootstrap/tools/validate_workspace.py` passed (28 task IDs; dashboard status 23/28); `git diff --check HEAD` and `git diff --check` passed. Live stale-reference hits are confined to preserved historical evidence and the implementation report, not live executable/controller behavior.

## Next action

Return this one High finding to the original implementer. Do not commit or begin bootstrap task B06-02 until a re-review approves the corrected operating command/documentation.

# Greek Essence Ralph Loop

The Ralph loop repeatedly runs one complete `$bootstrap-next` task until the deterministic checker reports `COMPLETE`.

## Commands

Dry run without Codex:

```bash
python .scratch/bootstrap/ralph-loop/tools/ralph_loop.py --dry-run
```

Run continuously:

```bash
python .scratch/bootstrap/ralph-loop/tools/ralph_loop.py
```

Run at most two completed tasks:

```bash
python .scratch/bootstrap/ralph-loop/tools/test_ralph_loop.py
```

Run unit tests:

```bash
python .scratch/bootstrap/ralph-loop/tools/test_check_state.py -v
```

## Contract

- One Codex root session owns one task through implementation, review, corrections, closure, handoff updates, and commit.
- Blocking/High findings return to the original implementer and then the same reviewer.
- An interrupted `In progress` or `In review` task resumes its saved Codex session.
- A fresh Codex session starts only after the previous task is committed and tracking is consistent.
- `check_state.py`, not the model's final message, decides whether to continue, resume, stop, or complete.
- The loop fails closed on `Blocked`, inconsistent tracking, missing session identity, or exhausted repair attempts.
- It never pushes, deploys, changes remotes, rewrites history, or approves destructive/overwrite operations.

## Completion

`COMPLETE` requires all 28 tasks and all eight phases to be `Done`, README counts to agree, B07-03 and the completion report to be finalized, latest reviews to be approved, Task-ID commits to exist, and Git to be clean.

## Runtime state

Session IDs, locks, and logs are stored outside Git under:

```text
%LOCALAPPDATA%\hermes\ralph\greek-essence\
```

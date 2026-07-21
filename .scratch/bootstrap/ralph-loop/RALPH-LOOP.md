# Greek Essence Ralph Loop

The Ralph loop repeatedly runs one complete task or phase-review work unit with Hermes until the deterministic checker reports `COMPLETE`.

## Commands

Dry run without an AI execution:

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

- One `greekroot` Hermes session owns one task or phase-review gate through review, corrections, closure, handoff updates, and commit.
- Blocking/High findings return to the original implementer and then the same reviewer.
- An interrupted `In progress` or `In review` task or phase gate resumes its saved Hermes session.
- A fresh Hermes session starts only after the previous work unit is committed and tracking is consistent.
- `check_state.py`, not the model's final message, decides whether to continue, resume, stop, or complete.
- The loop fails closed on `Blocked`, inconsistent tracking, missing session identity, or exhausted repair attempts.
- It never pushes, deploys, changes remotes, rewrites history, or performs unrelated destructive operations.

Ralph invokes Hermes non-interactively with `--yolo`. Standing authority is limited to task-owned repository-local changes explicitly required by the active contract or reviewer findings; all external, unrelated, credential, system, remote, push, deploy, and history-rewrite boundaries remain fail-closed.

Profiles are pinned as reusable context shells: `greekroot` (`gpt-5.6-sol`, high reasoning), `greekimpl` (`gpt-5.6-terra`, medium), and `greekreview` (`gpt-5.6-sol`, medium), all through `openai-codex`. Their reproducible configuration and SOUL templates are in [profiles/README.md](profiles/README.md).

## Completion

`COMPLETE` requires all 28 tasks and all eight phases to be `Done`, README counts to agree, B07-03 and the completion report to be finalized, latest reviews to be approved, Task-ID commits to exist, and Git to be clean.

## Runtime state

Session IDs, locks, and logs are stored outside Git under:

```text
%LOCALAPPDATA%\hermes\ralph\greek-essence\
```

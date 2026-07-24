# Git Workflow

## Status and authority

This document is the repository's **mandatory master Git workflow**. Every agent and human contributor must read it before modifying files, creating or switching branches, creating worktrees, delegating implementation, staging changes, committing, pushing, opening or merging a pull request, resolving conflicts, or cleaning up Git state.

Root [`AGENTS.md`](../AGENTS.md) makes this a required start-of-task read. A feature-local `AGENTS.md`, task contract, or delegated-agent brief may impose stricter rules, but it must not weaken this workflow. Direct operator instructions remain authoritative; any approved exception must be explicit, narrow, and recorded truthfully.

## Core model

For implementation work:

> **One task = one dedicated branch = one isolated worktree = one clear owner.**

A branch records one line of work. A worktree gives that branch a separate physical directory. Separate worktrees let agents work concurrently without switching branches underneath another process or mixing unrelated files.

Do not perform implementation in a shared dirty worktree when an isolated worktree can be used. Do not switch the branch of a worktree owned by another agent or active process.

## Mandatory lifecycle

1. Inspect live repository and remote state.
2. Create a dedicated branch and isolated worktree from current `origin/main`.
3. Record task ownership, path, branch, scope, exclusions, and Git permissions.
4. Implement and verify only the assigned task.
5. Stage explicit task-owned paths and inspect the staged snapshot.
6. Commit, push, and open a focused pull request.
7. Complete required checks and independent reviews.
8. Resolve straightforward conflicts safely; escalate ambiguous semantic conflicts.
9. Merge with a normal merge commit.
10. Verify the merge on remote `main` and verify required post-merge checks.
11. Confirm the task worktree is clean, then delete its worktree and local/remote branch.

Cleanup is part of completion, but it happens only after the remote merge is proven.

## 1. Preflight: inspect before changing anything

From any existing repository worktree:

```bash
git fetch origin
git status --short --branch
git worktree list
git branch --show-current
git remote -v
```

Also inspect the live task/frontier documents required by root and feature-level `AGENTS.md`.

Before mutation, determine:

- the selected task or issue;
- the branch name;
- the absolute isolated-worktree path;
- the base commit (`origin/main` by default);
- expected owned paths;
- concurrent agents, worktrees, branches, and excluded paths;
- whether the agent may commit, push, open a PR, merge, or clean up.

Never assume a handoff still describes current Git state. Never reset, stash, clean, overwrite, or absorb existing work merely because it is unfamiliar.

## 2. Create the branch and isolated worktree

Use current remote `main`, not a possibly stale local branch:

```bash
git fetch origin
git worktree add \
  -b feat/short-description \
  ../greek-essence-short-description \
  origin/main
```

Typical branch prefixes:

- `feat/` — new behavior;
- `fix/` — defect repair;
- `docs/` — documentation;
- `test/` — test-only work;
- `refactor/` — behavior-preserving restructuring;
- `chore/` — bounded maintenance.

Use a short task-specific name. Do not reuse a branch or dirty worktree for unrelated work.

### Ownership record

The task handoff or agent brief should state:

```text
Task: <issue or objective>
Branch: <branch>
Worktree: <absolute path>
Base: origin/main at <commit>
Owned paths: <expected paths or subsystem>
Excluded concurrent work: <paths/branches/worktrees>
Git permissions: <edit only | commit | push | PR | merge | cleanup>
```

An implementation subagent must receive the worktree path and branch explicitly. A review agent normally receives read-only Git permissions and must not change branches or lifecycle state.

## 3. Work only inside the assigned worktree

Inside the task worktree:

```bash
git branch --show-current
git status --short --branch
```

Confirm both match the brief before editing.

Rules:

- Do not switch branches inside another agent's worktree.
- Do not edit through the original shared worktree when assigned an isolated one.
- Do not copy, stage, or commit concurrent agents' work.
- Preserve unfamiliar edits until ownership is established.
- Keep generated logs, caches, browser CLI state, credentials, and temporary artifacts out of commits unless the contract explicitly requires sanitized evidence.
- If an agent discovers that the assigned branch/worktree is wrong, stop mutation and correct the isolation first.

## 4. Stage deliberately

Avoid broad staging in repositories with concurrent work:

```bash
# Avoid by default
git add .
git add -A
```

Prefer explicit task-owned paths:

```bash
git add \
  app/example/page.tsx \
  components/example-card.tsx \
  tests/example.spec.ts
```

Then inspect the exact staged snapshot:

```bash
git diff --cached --name-only
git diff --cached
git diff --cached --check
git status --short
```

Before committing, compare the staged path list to the declared ownership and exclusion lists. If an unrelated path appears, unstage it without discarding its content:

```bash
git restore --staged path/to/unrelated-file
```

Do not use destructive cleanup commands to solve staging mistakes.

## 5. Verify before commit

A commit must represent a known, truthfully verified state. Run:

- focused tests during implementation;
- applicable format, lint, type, content, and build checks;
- required browser, accessibility, performance, or security gates;
- task-contract verification;
- required independent code and visual reviews.

Record commands, exit codes, decisive counts, and residual risks. Never describe a failing gate as passing. If the operator authorizes an exception after bounded evidence-backed attempts, preserve the gate and document the exception in the implementation report and PR.

Before commit:

```bash
git diff --cached --check
git status --short --branch
```

## 6. Commit and push

Use a conventional, task-focused commit message:

```bash
git commit -m "feat(scope): concise outcome"
git push -u origin HEAD
```

Pushing publishes the branch; it does not change `main`.

Do not commit or push unless the task brief or operator authorizes it. Do not rewrite shared history with force-push, rebase, or commit amendment after another party may depend on it unless explicitly authorized.

## 7. Open a focused pull request

Open a PR from the task branch to `main`. The description should include:

- summary and user-visible outcome;
- task/issue scope;
- exact verification results;
- code and visual review status when required;
- residual risks or explicit exceptions;
- excluded concurrent work;
- deployment or credential boundaries.

Example:

```bash
gh pr create \
  --base main \
  --head feat/short-description \
  --title "feat(scope): concise outcome" \
  --body-file pr-body.md
```

A PR is ready to merge only when it is mergeable, mandatory checks and reviews are acceptable, and its evidence matches the final commit.

## 8. Conflict handling

A conflict means Git cannot decide how two lines of work should combine.

### Straightforward conflicts

The agent may resolve a conflict when the correct result is mechanical and unambiguous, for example:

- adjacent documentation additions;
- import ordering;
- generated timestamps or status fields with a clear current value;
- two independent entries that should both remain.

After resolving:

1. inspect both original intentions;
2. stage only the resolved task-owned files;
3. rerun affected checks;
4. inspect the full staged diff;
5. update the PR truthfully.

### Semantic or ownership conflicts

Stop and escalate when the intended combined behavior is unclear, for example:

- both branches change the same business logic differently;
- one branch removes an API or component required by the other;
- status ledgers claim contradictory workflow states;
- resolving the conflict would modify another agent's owned work;
- architecture or product meaning must be chosen.

Never pick a side merely to make Git report a clean merge.

### Updating from main

For a shared feature branch, preserve history by merging current remote `main` into the task branch rather than rebasing:

```bash
git fetch origin
git merge origin/main
```

Resolve approved conflicts, rerun affected verification, then push the updated branch.

## 9. Merge strategy

The default strategy is a **normal merge commit**:

```bash
gh pr merge <number> --merge
```

Do not squash or rebase by default. Normal merge commits preserve task commits, PR boundaries, and references used by concurrent agents.

Do not delete the branch as part of the merge command. Verification comes first; cleanup comes afterward.

## 10. Verify remote merge and post-merge state

A successful local command is not sufficient. Verify GitHub and `origin/main`:

```bash
gh pr view <number> --json state,mergedAt,mergeCommit,url
git fetch origin
git log -1 --oneline origin/main
git branch -r --contains <merge-commit>
```

Confirm:

- PR state is `MERGED`;
- the expected merge commit exists;
- `origin/main` contains it;
- required CI/deployment checks completed successfully;
- no unrelated concurrent work entered the PR;
- the task's final artifacts and status are present on remote `main`.

If post-merge verification fails, do not clean up yet. Diagnose or report the exact discrepancy.

## 11. Cleanup after verified merge

First ensure the task worktree has no uncommitted or untracked task-owned content:

```bash
git -C ../greek-essence-short-description status --short
```

If output is non-empty, inspect it. Do not force-remove the worktree blindly.

After the remote merge and checks are proven:

```bash
git worktree remove ../greek-essence-short-description
git branch -d feat/short-description
git push origin --delete feat/short-description
git worktree prune
git worktree list
```

The preferred order is:

1. verify PR and `origin/main`;
2. verify task worktree is clean;
3. remove task worktree;
4. delete local branch;
5. delete remote branch;
6. prune and inspect worktree metadata.

Never delete another agent's branch or worktree. Cleanup authority belongs to the task owner or an explicitly authorized orchestrator.

## Concurrent-agent safeguards

When several agents work in the repository:

- each implementation task gets a separate branch and worktree;
- every brief names ownership and exclusion paths;
- agents never switch another agent's branch or worktree;
- agents use explicit staging allowlists;
- review agents are read-only unless a repair task explicitly authorizes edits;
- shared status files are updated only by the authorized workflow owner;
- no task PR may include another task's files merely because they were visible in a dirty worktree;
- if isolation was not established at task start, establish it before commit by creating a clean worktree from `origin/main` and transferring only verified task-owned paths.

## Delegation requirement

Every implementation-agent brief must include:

```text
Mandatory master read: read root AGENTS.md and docs/GIT_WORKFLOW.md before modifying files or Git state. Work only in the supplied isolated worktree and branch. Preserve concurrent work. Do not switch branches. Do not stage, commit, push, open or merge a PR, or clean up unless this brief explicitly authorizes that action.
```

Every review-agent brief must include:

```text
Read root AGENTS.md and docs/GIT_WORKFLOW.md. Treat Git as read-only: do not edit implementation, switch branches, stage, commit, push, merge, or remove worktrees unless the brief explicitly authorizes a repair.
```

An orchestrator must verify these requirements are present before dispatching an agent.

## Emergency and exception rules

Potentially destructive or history-rewriting actions require explicit operator authorization, including:

- `git reset --hard`;
- `git clean`;
- force-push;
- rebasing a shared branch;
- deleting an unmerged branch;
- force-removing a dirty worktree;
- discarding or overwriting another agent's changes.

When an exception is authorized, record its scope and reason. An exception for one task does not silently change the repository default.

## Completion checklist

Before declaring Git delivery complete, verify:

- [ ] Mandatory master Git workflow was read.
- [ ] Dedicated branch and isolated worktree were used.
- [ ] Branch/worktree ownership and exclusions were explicit.
- [ ] Only task-owned paths were staged and committed.
- [ ] Required checks and reviews were completed truthfully.
- [ ] PR was opened against `main` with accurate evidence.
- [ ] Conflicts, if any, were reviewed and affected checks rerun.
- [ ] PR used a normal merge commit.
- [ ] Remote `origin/main` contains the merge commit.
- [ ] Required post-merge checks succeeded.
- [ ] Task worktree was clean before removal.
- [ ] Task worktree and local/remote branch were deleted.
- [ ] Concurrent agents' work remained untouched.

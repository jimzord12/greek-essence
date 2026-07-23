# Project Handoff

## Current state

The bootstrap campaign is complete and merged to `main`: all 28 tasks and all 8 phases are `Done`, final task/phase reviews are approved, and local quality gates are green. Kimi Code remains unavailable and must not be represented as green.

During the B07-02 → B07-03 handoff, the next controller launch failed closed because external `controller-state.json` still retained the completed B07-02 campaign/task identity. There was no live lock or surviving root; the completed state was archived manually and B07-03 then ran successfully. This exposed a deterministic campaign-transition gap rather than a task or process-cleanup failure.

## Active work: deterministic Ralph campaign transition

Design and implement the smallest project-owned mechanism that safely transitions external Ralph controller state from one verified completed campaign/task to a newly authorized campaign/task without agent judgment.

### Required behavior

1. Provide an explicit deterministic command or controller entry point; do not infer the next campaign from prose or Git state.
2. Fail closed unless:
   - no live `ralph.lock` owner exists;
   - no controller-owned root process is recorded or alive;
   - existing state is valid and exactly matches the declared completed campaign, task, and resolved tier;
   - the new campaign/task/tier identity is complete and differs appropriately;
   - the archive destination is collision-free.
3. Preserve the completed state as a timestamped archive outside Git, initialize fresh zeroed supervision counters atomically, and emit privacy-bounded lifecycle transition events.
4. Never reset `.scratch/ralph-loop/completion-signal.json`; campaign semantic authorization remains human-owned.
5. Keep runtime files and process data outside Git. Do not record credentials, prompts, unrelated command lines, or stale process IDs in tracked documentation.

### Verification

Use test-first development. Add focused tests for successful transition, active lock, recorded/live root, identity/tier mismatch, malformed state, archive collision, and interrupted or failed atomic writes. Run the focused tests, the complete Ralph unit suite, and `git diff --check`. Preserve existing lifecycle and fail-closed behavior.

### Workflow and safety

- Work from current `main` on a dedicated task branch.
- Use the repository-owned Ralph/controller documentation and tests as authority; inspect live state before mutation.
- Use a substantial-work branch → PR → independent review/fix → normal merge workflow; preserve the merged branch for the operator to delete.
- Push/PR/normal merge are authorized for this task after verification and review.
- Do not deploy, expose credentials, rewrite history, change remotes, perform destructive/unverified process recovery, edit unrelated product scope, or read the external asset-plan file as part of this task.
- The abrupt Windows controller-termination/orphan cause remains separately unresolved in `.scratch/ralph-loop/KNOWLEDGE.md` K-002; do not broaden this transition task into Job Objects or general orphan termination.

### Completion and next dependency

When implementation, focused/full tests, independent review, PR, and normal merge pass, reconcile this handoff and `TODO.md`. The next planned node is the reviewed sequential asset prompt pack, but it is not authorized automatically by completion of this task.

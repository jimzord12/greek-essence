# Project Handoff

## Current state

The bootstrap campaign is complete and merged to `main`: all 28 tasks and all 8 phases are `Done`, final task/phase reviews are approved, and local quality gates are green. Kimi Code remains unavailable and must not be represented as green.

During the B07-02 → B07-03 handoff, the next controller launch failed closed because external `controller-state.json` still retained the completed B07-02 campaign/task identity. There was no live lock or surviving root; the completed state was archived manually and B07-03 then ran successfully. This exposed a deterministic campaign-transition gap rather than a task or process-cleanup failure.

The deterministic Ralph campaign-transition command is implemented, independently approved, and awaiting normal PR merge under the authorized task workflow.

The next planned dependency is the reviewed sequential asset prompt pack. It is not active or authorized for execution; the operator must promote it separately after this transition task is merged and verified.

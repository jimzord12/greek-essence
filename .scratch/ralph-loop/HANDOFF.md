# Ralph Handoff

This file is mutable working memory for the next fresh Sol context. It is not an append-only log.

## Last completed work

The deterministic Ralph campaign-transition command is implemented and independently approved. Focused transition tests, the complete Ralph unit suite, isolated real-CLI acceptance, repository quality gates, and diff checks passed. The tracked completion signal and external live Ralph controller state remained unchanged.

## Current repository/worktree facts

- The transition work is on `task/ralph-campaign-transition` for normal PR merge.
- Independent review verdict: `Approved`, with no findings.
- The command requires explicit completed/new campaign, task, and tier identities; it never reads or resets the completion signal and never performs stale-root recovery.
- K-002 remains open and out of scope.

## Active campaign

None. The bootstrap campaign is complete. Do not reset `.scratch/ralph-loop/completion-signal.json` automatically; a human must explicitly set it false to authorize a new managed campaign.

## Next required action

Complete the authorized normal PR merge and final main-state verification for the transition task. The reviewed sequential asset prompt pack remains only the next planned dependency and is not authorized automatically.

## Blockers requiring human action

- Kimi Code CLI/authentication must become available before full cross-agent compatibility can be claimed.

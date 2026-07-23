# Project Handoff

## Current state

The bootstrap campaign, deterministic Ralph campaign-transition mechanism, and reviewed 18-record prototype asset-prompt pack are complete and merged to `main`. Bootstrap tooling and the bilingual fixture scaffold are complete; product prototype implementation remains pending. The asset pack remains at the operator visual-direction checkpoint: image generation and visual review are deferred until the operator returns to them. Historical bootstrap compatibility probes and pnpm 10 runtime observations remain factual, clearly non-normative records; they are not current requirements, blockers, or gates. The current development contract uses standalone pnpm `11.17.0`. K-002 remains open and out of scope. No managed Ralph campaign is active; do not reset `.scratch/ralph-loop/completion-signal.json` automatically.

## Next operator checkpoint

Return to the operator visual-direction checkpoint for the reviewed asset-prompt pack. Do not begin image generation or visual review, P1 planning, or product implementation automatically. Any new managed Ralph campaign requires explicit operator promotion and must preserve the completion-signal boundary.

## Scope and safety boundaries

- Preserve the reviewed asset pack and defer image work until the operator promotes it.
- Keep K-002 open and out of scope.
- Do not launch Ralph, reset or mutate `.scratch/ralph-loop/completion-signal.json`, or alter external Ralph runtime state automatically.
- Do not begin product implementation or P1 planning from this handoff.

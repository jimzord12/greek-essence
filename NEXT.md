# Project Handoff

## Current state

The bootstrap campaign and deterministic Ralph campaign-transition mechanism are complete and merged to `main`. All 28 bootstrap tasks and all 8 phases are `Done`; transition-focused tests, the complete Ralph unit suite, isolated CLI verification, independent Terra review, PR checks, and normal merge passed. Kimi Code remains unavailable and must not be represented as green.

The transition mechanism is available through the explicit project-owned command documented in `.scratch/ralph-loop/RALPH_LOOP.md`. It preserves completed controller state outside Git, initializes zeroed new controller state, fails closed on incompatible lock/root/state conditions, and never reads or resets the semantic completion signal.

## Current continuation

No project work is currently active. The next planned dependency is the reviewed sequential asset prompt pack, but it is not authorized automatically. The operator must separately promote it before any agent reads the external asset-plan file or begins planning, delegation, or execution.

K-002 remains open and out of scope. Do not launch a managed Ralph campaign or reset `.scratch/ralph-loop/completion-signal.json` without separate human authorization.

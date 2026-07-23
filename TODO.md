# Project TODO

`TODO.md` is the operator-managed backlog and idea inbox for work that must be remembered but is not currently active.

It is not an execution queue, task contract, project-status ledger, or agent handoff. [`NEXT.md`](NEXT.md) remains the single source for the immediate project continuation. An item appearing here does not authorize an agent to implement it.

## Workflow

```text
New idea or pending work
        ↓
TODO.md — Inbox
        ↓
Clarified and prioritized
        ↓
Formal plan or task contract
        ↓
NEXT.md when it becomes active
        ↓
Completed and removed or reconciled into durable project history
```

## Rules

- The operator controls priority and promotion into active work.
- Agents may add a clearly attributable item when new pending work emerges, clarify an existing item without changing its intent, or mark an item blocked when supported by evidence.
- Agents must not implement, delegate, schedule, or start an item merely because it appears here.
- Before implementation, promote the item into the appropriate plan, issue, or task contract. Put only the immediate continuation in `NEXT.md`.
- Keep entries concise: desired outcome, useful source/reference, and any known decision or blocker.
- Do not store runtime state, process IDs, session IDs, raw logs, secrets, credentials, or detailed execution evidence here.
- Remove completed items once their outcome is reconciled into Git history, task records, or another durable source of truth. This file is not a changelog.

## Inbox

<!-- New unprioritized items go here before entering the planned dependency graph. -->

## Planned

- [ ] Turn the Terra prototype asset report into a reviewed, sequential ChatGPT image-generation prompt pack for manual use.
  - **Depends on:** Deterministic Ralph campaign transition.
  - **Source:** `C:\Users\jimzord12\Documents\greek-essence-prototype-asset-plan.md`
  - **Desired outcome:** One self-contained, copy-ready prompt per must-have image, ordered so the operator can paste prompts manually into the ChatGPT app one by one.
  - **Prompt contents:** Asset ID, subject/location, photographic direction, composition and text-safe area, aspect ratio and target dimensions, responsive crop intent, EN/EL text-overlay prohibition, accessibility intent, geographic/brand accuracy constraints, negative prompt, and any continuity instructions shared with the asset family.
  - **Workflow:** Begin with a small visual-direction test set; record operator feedback; revise the shared style guidance; then prepare the remaining prompts without generating or submitting images automatically.
  - **Notes:** Preserve licensing review requirements and clearly label inferred scenes or provisional people/journey content. The deliverable is the prompt list only; the operator performs every ChatGPT submission manually. Reading the source outside the repository requires explicit authority at execution time.

- [ ] Review and update authoritative project documentation after the asset prompt pack.
  - **Depends on:** Reviewed asset prompt pack and operator visual-direction feedback.
  - **Desired outcome:** Reconcile approved asset/visual decisions into the correct documentation owners, repair affected traceability, and leave an implementation-ready P1 baseline without silently changing product scope.
  - **Scope:** Documentation review and approved updates only; do not begin product implementation in this task.

- [ ] Plan the first product implementation phase (P1 — Visual and content foundation).
  - **Depends on:** Documentation review and update.
  - **Desired outcome:** A bounded, dependency-ordered implementation plan and task contracts grounded in the PRD, prototype specification, technical design, design system, and reconciled asset direction.
  - **Scope:** Planning only unless the operator separately authorizes implementation tasks.

## Dependency graph

```text
Deterministic Ralph campaign transition
        ↓
Reviewed sequential asset prompt pack
        ↓
Authoritative documentation review and update
        ↓
P1 visual and content foundation planning
```

Only the first node is active through `NEXT.md`. Completion of one node does not automatically authorize its successor; reconcile evidence and explicitly promote the next node first.

<!-- Agreed and prioritized work that is not active yet. Link its plan/task when available. -->

## Blocked / awaiting decision

<!-- Items that require operator input or an external dependency before planning. -->

## Later / ideas

<!-- Uncommitted possibilities that should remain visible but need clarification. -->

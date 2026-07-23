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

- [ ] Convert the Terra prototype asset inventory into a reviewed ChatGPT image-generation prompt pack.
  - **Source:** `C:\Users\jimzord12\Documents\greek-essence-prototype-asset-plan.md`
  - **Desired outcome:** Detailed prompts for the 18 must-have prototype images, followed by a small visual-direction test set before full generation.
  - **Notes:** Preserve geographic accuracy, responsive crop requirements, text-safe composition, accessibility intent, licensing review, and the report's negative constraints.

## Planned

<!-- Agreed and prioritized work that is not active yet. Link its plan/task when available. -->

## Blocked / awaiting decision

<!-- Items that require operator input or an external dependency before planning. -->

## Later / ideas

<!-- Uncommitted possibilities that should remain visible but need clarification. -->

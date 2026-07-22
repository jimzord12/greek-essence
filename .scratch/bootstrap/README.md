# Greek Essence Bootstrap Workspace

This tracked workspace coordinates repository bootstrap only. It does not authorize implementation of Greek Essence product pages, content, forms, email delivery, authentication, analytics, or deployment.

## Current status

| Phase | State | Tasks done |
|---|---|---:|
| 00 — Planning and baseline | Done | 2/2 |
| 01 — Agent tooling | Done | 7/7 |
| 02 — Application scaffold | Done | 3/3 |
| 03 — Code hygiene | Done | 4/4 |
| 04 — Bilingual fixtures | Done | 3/3 |
| 05 — Automated tests | In review | 3/3 |
| 06 — Quality review | Pending | 0/3 |
| 07 — Final verification | Pending | 0/3 |

**Current task:** `None`
**Next unblocked task:** `None`
**Known external blockers:** Kimi Code is unavailable, so cross-agent validation cannot become fully green. The former B01-03 source blocker is resolved by BD-015.

## Entry points

- [Bootstrap agent instructions](BOOTSTRAP-AGENTS.md)
- [Human operator guide](FOR_HUMAN_OPERATOR.md)
- [Work protocol](protocol.md)
- [Execution plan](plan.md)
- [Dependency map](dependency-map.md)
- [Locked decisions](decisions.md)
- [Verification matrix](verification-matrix.md)
- [Completion report template](completion-report.md)
- [Ralph-loop automation](ralph-loop/RALPH-LOOP.md)
- [Current Ralph handoff](ralph-loop/HANDOFF.md)
- [Durable bootstrap knowledge](ralph-loop/KNOWLEDGE.md)
- [Artifact templates](templates/)
- [Phases](phases/)

## Operating rules

The normative procedure and role boundaries are in [`protocol.md`](protocol.md). In summary:

- The root integrator selects dependency-ready work, delegates it, reconciles repository-wide state, updates tracking, creates one dedicated Task-ID commit after each successful task closure, and controls phase commits. It does not implement delegated tasks or review its own work.
- A fresh implementer owns exactly one task, its evidence, report, and accepted review fixes. It does not commit, broaden scope, modify review files, or mark its work `Done`.
- A different fresh task reviewer independently checks the diff and evidence and re-runs proportionate verification. It does not edit implementation or approve unresolved blocking/high findings.
- A fresh phase reviewer validates integration and the phase exit gate after task reviews pass. It does not substitute phase review for missing task review.
- The human operator handles destructive/overwrite approvals, credentials, scope changes, and material exceptions—not routine coordination.
- Generated evidence belongs in ignored `.artifacts/bootstrap/`; tracked `evidence.md` files record commands and results.

Every participating agent must read the protocol first.

Ralph-loop completion is deterministic: every phase row must use exact `Done`, the total must be `28/28`, B07-03 and the completion report must be finalized, and no current or next task may remain.

Allowed states: `Pending`, `Ready`, `In progress`, `In review`, `Blocked`, `Done`, `Deferred`.

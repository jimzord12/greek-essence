---
id: B05-01
status: Done
depends_on: [B04-03]
implementer_agent: 20260722_082947_f3ea6c
reviewer_agent: 20260722_083707_aea86f
started_at: 2026-07-22T08:30:18+03:00
completed_at: 2026-07-22T08:44:32+03:00
---

# Configure focused unit and component tests

## What

Add Vitest and the minimum React test support required by bootstrap fixtures.

## Why

Locale helpers, message completeness, and small interaction contracts should fail quickly without full browser startup.

## How

- Isolate test types from application-global types.
- Test locale helpers, message parity, and the lab interaction contract.
- Avoid broad snapshots and artificial coverage targets.
- Prove failure detection with a temporary failing case, then remove it.

## Required reading

- `docs/03_technical_design/18_testing_and_quality_gates.md`
- `docs/03_technical_design/05_routing_rendering_and_localization.md`

## Bootstrap verification contract

Apply verification row B05-01 and all relevant locked defaults from [the Bootstrap Verification Matrix](../../../../verification-matrix.md). Record exact commands, exit codes, and artifact paths in evidence.md.

## Acceptance

Focused unit tests pass deterministically, failure detection is proven, and coverage or generated output remains ignored.

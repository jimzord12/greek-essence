---
id: B07-02
status: Done
depends_on: [B07-01]
implementer_agent: 20260723_123245_7b0dbd
reviewer_agent: 20260723_125017_a99633
started_at: 2026-07-23T12:33:52+03:00
completed_at: 2026-07-23T12:59:11+03:00
---

# Run the aggregate quality gate

## What

Execute every authoritative bootstrap command in the primary workspace.

## Why

Individual task success does not prove integrated success.

## How

Run frozen install, format check, lint, typecheck, unit tests, build, E2E, axe, Unlighthouse, and `check:all`. Inspect console/network results, tracked artifacts, secrets, prohibited tools, and deferred dependencies.

## Required reading

- `docs/03_technical_design/18_testing_and_quality_gates.md`
- `docs/05_agent_skills/16_acceptance_criteria.md`
- `docs/05_agent_skills/17_required_completion_report.md`

## Bootstrap verification contract

Apply verification row B07-02 and all relevant locked defaults from [the Bootstrap Verification Matrix](../../../../verification-matrix.md). Record exact commands, exit codes, and artifact paths in evidence.md.

## Acceptance

Every aggregate verification command exits zero, no prohibited dependency, secret, or tracked runtime artifact exists, and all task and phase reviews are resolved.

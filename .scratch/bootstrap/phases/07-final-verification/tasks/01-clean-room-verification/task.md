---
id: B07-01
status: Done
depends_on: [B06-03]
implementer_agent: 20260722_232706_b03315
reviewer_agent: 20260723_013332_c5307d
started_at: 2026-07-22T23:28:28+03:00
completed_at: 2026-07-23T11:51:09+03:00
---

# Verify a clean-room installation

## What

Install and test an isolated copy without relying on the working dependency tree or prior build output.

## Why

A green primary workspace does not prove reproducibility.

## How

- Copy tracked state to a temporary directory without deleting or resetting the primary workspace.
- Run the pinned toolchain and frozen install.
- Run fast checks, build, browser tests, axe, and Unlighthouse.
- Record versions and cache assumptions.

## Required reading

- `docs/03_technical_design/03_technology_stack_and_version_policy.md`
- `docs/03_technical_design/18_testing_and_quality_gates.md`
- `docs/05_agent_skills/16_acceptance_criteria.md`

## Bootstrap verification contract

Apply verification row B07-01 and all relevant locked defaults from [the Bootstrap Verification Matrix](../../../../verification-matrix.md). Record exact commands, exit codes, and artifact paths in evidence.md.

## Acceptance

The fresh isolated copy starts without `node_modules` or `.next`, installs from the frozen lockfile without changing it, and passes every applicable local gate. Normal pnpm content-addressed cache reuse is allowed; package versions and integrity remain governed by `pnpm-lock.yaml`.

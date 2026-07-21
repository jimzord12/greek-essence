---
id: B07-01
status: Pending
depends_on: [B06-03]
implementer_agent: null
reviewer_agent: null
started_at: null
completed_at: null
---

# Verify a clean-room installation

## What

Install and test an isolated copy without relying on the working dependency tree.

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

The isolated copy installs from the frozen lockfile and passes every applicable local gate without relying on the primary workspace dependency tree or caches.

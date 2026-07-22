---
id: B03-04
status: Ready
depends_on: [B03-03]
implementer_agent: null
reviewer_agent: null
started_at: null
completed_at: null
---

# Define scripts and environment safety

## What

Create stable pnpm command contracts, `.env.example`, and artifact/secret ignores.

## Why

Every later agent and quality gate needs predictable cross-platform entry points.

## How

- Define `dev`, `build`, `start`, lint, typecheck, format, unit, E2E, axe, Unlighthouse, `check`, and `check:all` scripts.
- Keep `check` fast; reserve browser/performance work for `check:all`.
- Add only bootstrap-used public environment values.
- Ignore secrets and generated evidence; do not add fake Resend configuration.

## Required reading

- `docs/03_technical_design/17_configuration_and_environments.md`
- `docs/03_technical_design/18_testing_and_quality_gates.md`
- `docs/03_technical_design/16_analytics_and_observability.md`

## Bootstrap verification contract

Apply verification row B03-04 and all relevant locked defaults from [the Bootstrap Verification Matrix](../../../../verification-matrix.md). Record exact commands, exit codes, and artifact paths in evidence.md.

## Acceptance

Every locked package script exists and is cross-platform, check scripts are non-mutating, secrets/artifacts are ignored, and no deferred service is required.

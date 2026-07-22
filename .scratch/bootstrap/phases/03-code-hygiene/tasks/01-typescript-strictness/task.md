---
id: B03-01
status: Done
depends_on: [B02-03]
implementer_agent: 20260722_055345_61990f
reviewer_agent: 20260722_055752_8c1034
started_at: 2026-07-22T02:54:02Z
completed_at: 2026-07-22T03:00:46Z
---

# Strengthen TypeScript

## What

Configure maintainable TypeScript 6 strictness.

## Why

Safe defaults must exist before project code accumulates.

## How

- Retain `strict` and Next.js-required settings.
- Enable `noUncheckedIndexedAccess`, `exactOptionalPropertyTypes`, `noImplicitOverride`, `noFallthroughCasesInSwitch`, `noUncheckedSideEffectImports`, and `useUnknownInCatchVariables`.
- Scope test types to test configuration.
- Avoid experimental or disproportionately noisy flags.

## Required reading

- `docs/03_technical_design/03_technology_stack_and_version_policy.md`
- `docs/03_technical_design/04_project_and_file_architecture.md`

## Bootstrap verification contract

Apply verification row B03-01 and all relevant locked defaults from [the Bootstrap Verification Matrix](../../../../verification-matrix.md). Record exact commands, exit codes, and artifact paths in evidence.md.

## Acceptance

Type checking passes and a temporary negative fixture proves the configured strictness before that fixture is removed.

---
id: B03-02
status: Ready
depends_on: [B03-01]
implementer_agent: null
reviewer_agent: null
started_at: null
completed_at: null
---

# Configure ESLint and Prettier

## What

Create flat ESLint configuration and deterministic formatting.

## Why

Linting is an explicit gate and must complement rather than fight TypeScript and formatting.

## How

- Use Next.js core-web-vitals and TypeScript recommendations.
- Add only high-value rules for imports, promises, and framework correctness.
- Configure generated/artifact ignores.
- Add Prettier and Tailwind class sorting when compatible.
- Do not add Stylelint or a competing formatter.

## Required reading

- `docs/03_technical_design/03_technology_stack_and_version_policy.md`
- `docs/03_technical_design/18_testing_and_quality_gates.md`

## Bootstrap verification contract

Apply verification row B03-02 and all relevant locked defaults from [the Bootstrap Verification Matrix](../../../../verification-matrix.md). Record exact commands, exit codes, and artifact paths in evidence.md.

## Acceptance

Lint and format check/fix commands pass, remain mutually compatible, and do not rewrite ignored or generated output.

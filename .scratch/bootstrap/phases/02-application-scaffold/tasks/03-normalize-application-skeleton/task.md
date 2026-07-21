---
id: B02-03
status: Pending
depends_on: [B02-02]
implementer_agent: null
reviewer_agent: null
started_at: null
completed_at: null
---

# Normalize the application skeleton

## What

Align generator output with the approved shallow root architecture.

## Why

Preset defaults must not silently redefine the project structure or component boundaries.

## How

- Use root-level `app/`, not `src/`, and retain `@/*` aliases.
- Keep only directories needed by bootstrap fixtures and configuration.
- Default pages/layouts to Server Components; isolate necessary interaction.
- Remove generator marketing content without beginning the actual Home page.
- Preserve preset semantic tokens as bootstrap infrastructure.
- Review and normalize generator-owned root `README.md` and `.gitignore`; link the documentation and bootstrap entry points, preserve required generated ignores, and add `.artifacts/bootstrap/` without removing unrelated rules.

## Required reading

- `docs/03_technical_design/01_confirmed_technical_decisions.md`
- `docs/03_technical_design/04_project_and_file_architecture.md`
- `docs/04_design/05_token_hierarchy_and_source_of_truth_rules.md`

## Bootstrap verification contract

Apply verification row B02-03 and all relevant locked defaults from [the Bootstrap Verification Matrix](../../../../verification-matrix.md). Record exact commands, exit codes, and artifact paths in evidence.md.

## Acceptance

Development startup and production build pass with the approved root architecture, normalized README and ignore rules, and no product implementation.

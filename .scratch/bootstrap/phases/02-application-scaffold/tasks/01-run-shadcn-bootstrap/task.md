---
id: B02-01
status: Pending
depends_on: [B01-07]
implementer_agent: null
reviewer_agent: null
started_at: null
completed_at: null
---

# Run the prescribed shadcn bootstrap

## What

Generate the application with `pnpm dlx shadcn@latest init --preset b27GcrRo --template next --pointer`.

## Why

The preset and command are owner-mandated bootstrap inputs.

## How

- Reconfirm current CLI help and record the resolved shadcn version.
- Inventory prospective targets and existing files.
- Run the command exactly in the repository root only when it will not overwrite existing files.
- If overwrite is proposed, stop and request approval for the exact paths; never add `--force`.
- Capture output and inspect the complete diff.

## Required reading

- `docs/03_technical_design/03_technology_stack_and_version_policy.md`
- `docs/03_technical_design/04_project_and_file_architecture.md`
- `docs/04_design/36_theme_structure.md`
- `docs/05_agent_skills/13_safe_installation_and_review_rules.md`

## Bootstrap verification contract

Apply verification row B02-01 and all relevant locked defaults from [the Bootstrap Verification Matrix](../../../../verification-matrix.md). Record exact commands, exit codes, and artifact paths in evidence.md.

## Acceptance

The exact prescribed command completes without unauthorized overwrites, existing documentation remains intact, and the generated application starts.

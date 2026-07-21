---
id: B01-01
status: Pending
depends_on: [B00-02]
implementer_agent: null
reviewer_agent: null
started_at: null
completed_at: null
---

# Create repository-level guidance

## What

Create only the pre-generator-safe governance files: concise root `AGENTS.md`, `.editorconfig`, and `.gitattributes`.

## Why

Humans and agents need stable authority, constraints, and entry points before generated files appear.

## How

- Link to `docs/README.md` and `.scratch/bootstrap/README.md` from `AGENTS.md`.
- State authority, package manager, architecture boundaries, locales, approved skills, browser policy, commands, and Definition of Done.
- Use exact modular documentation paths.
- Prohibit deferred capabilities and unapproved browser-agent tools.
- Do not create root `README.md` or `.gitignore`; the shadcn generator may own those paths. They are reviewed and normalized in B02-03.

## Required reading

- `docs/05_agent_skills/05_root_agents_md.md`
- `docs/05_agent_skills/01_approved_tooling_baseline.md`
- `docs/03_technical_design/01_confirmed_technical_decisions.md`
- `docs/03_technical_design/18_testing_and_quality_gates.md`

## Bootstrap verification contract

Apply verification row B01-01 and all relevant locked defaults from [the Bootstrap Verification Matrix](../../../../verification-matrix.md). Record exact commands, exit codes, and artifact paths in evidence.md.

## Acceptance

Root guidance passes every requirement in the agent-tooling acceptance checklist and all documentation links resolve.

---
id: B01-06
status: Ready
depends_on: [B01-05]
implementer_agent: null
reviewer_agent: null
started_at: null
completed_at: null
---

# Create the Greek Essence quality-review skill

## What

Create the project-owned reviewer skill and five focused reference checklists.

## Why

The final bootstrap must be reviewed against project-specific quality requirements using real browser evidence.

## How

- Implement required metadata, triggers, review behavior, anti-patterns, and output order.
- Reference exact modular source documents instead of copying requirements.
- Require Playwright CLI evidence for browser claims.
- Permit irrelevant review sections to be omitted with a scope explanation.

## Required reading

- `docs/05_agent_skills/10_project_owned_quality_review_skill.md`
- `docs/05_agent_skills/15_how_agents_must_use_the_tooling.md`
- `docs/04_design/40_workflow.md`

## Bootstrap verification contract

Apply verification row B01-06 and all relevant locked defaults from [the Bootstrap Verification Matrix](../../../../verification-matrix.md). Record exact commands, exit codes, and artifact paths in evidence.md.

## Acceptance

The project skill and all five required reference files pass structural review; live rendered validation remains assigned to B06-03.

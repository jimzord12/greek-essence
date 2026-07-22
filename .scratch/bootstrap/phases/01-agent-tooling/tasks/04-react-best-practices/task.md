---
id: B01-04
status: Done
depends_on: [B01-03]
implementer_agent: greekimpl
reviewer_agent: greekreview
session_id: 20260722_034457_9f8463
reviewer_session_id: 20260722_035028_ae84c9
started_at: 2026-07-22T00:45:38Z
completed_at: 2026-07-22T00:53:26Z
---

# Install Vercel React best practices

## What

Install only `vercel-react-best-practices` at its canonical repository path.

## Why

Fixture components must demonstrate disciplined rendering and Client Component boundaries.

## How

Use the isolated inspection, revision pinning, license preservation, and normalization process from B01-03.

## Required reading

- `docs/05_agent_skills/08_vercel_react_best_practices.md`
- `docs/05_agent_skills/13_safe_installation_and_review_rules.md`
- `docs/05_agent_skills/12_agents_readme.md`

## Bootstrap verification contract

Apply verification row B01-04 and all relevant locked defaults from [the Bootstrap Verification Matrix](../../../../verification-matrix.md). Record exact commands, exit codes, and artifact paths in evidence.md.

## Acceptance

The canonical React skill is present without unrelated Vercel skills or duplicated agent-specific copies.

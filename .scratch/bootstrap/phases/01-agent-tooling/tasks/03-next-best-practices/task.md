---
id: B01-03
status: Pending
depends_on: [B01-02]
implementer_agent: null
reviewer_agent: null
started_at: null
completed_at: null
---

# Install Vercel next-best-practices

## What

Install only `next-best-practices` at its canonical repository path.

## Why

App Router setup needs current framework-specific guidance.

## How

- Verify the official Skills CLI command and source revision.
- Stage, inspect, license-check, and normalize only this skill.
- Do not install the full Vercel skill collection or plugin bundle.

## Required reading

- `docs/05_agent_skills/07_vercel_next_best_practices.md`
- `docs/05_agent_skills/13_safe_installation_and_review_rules.md`
- `docs/05_agent_skills/12_agents_readme.md`

## Bootstrap verification contract

Apply verification row B01-03 and all relevant locked defaults from [the Bootstrap Verification Matrix](../../../../verification-matrix.md). Record exact commands, exit codes, and artifact paths in evidence.md.

## Acceptance

Only the requested canonical Next.js skill and its required supporting files are present; the broader Vercel collection is absent.

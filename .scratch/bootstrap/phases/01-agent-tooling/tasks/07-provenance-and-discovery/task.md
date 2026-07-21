---
id: B01-07
status: Pending
depends_on: [B01-06]
implementer_agent: null
reviewer_agent: null
started_at: null
completed_at: null
---

# Complete provenance and agent discovery records

## What

Populate `.agents/README.md` and validate every skill with Codex.

## Why

Files existing on disk do not prove provenance, discovery, or correct use.

## How

- Record source, revision, command, date, license, included/excluded files, modifications, and update procedure.
- Run each documented controlled prompt in Codex and record evidence.
- Record Kimi as blocked because the executable/authentication is unavailable.
- Do not create duplicated skill copies to simulate compatibility.

## Required reading

- `docs/05_agent_skills/11_cross_agent_compatibility.md`
- `docs/05_agent_skills/12_agents_readme.md`
- `docs/05_agent_skills/16_acceptance_criteria.md`
- `docs/05_agent_skills/17_required_completion_report.md`

## Bootstrap verification contract

Apply verification row B01-07 and all relevant locked defaults from [the Bootstrap Verification Matrix](../../../../verification-matrix.md). Record exact commands, exit codes, and artifact paths in evidence.md.

## Acceptance

Codex discovery and controlled use pass for all five skills, while Kimi is explicitly and honestly recorded as an external blocker.

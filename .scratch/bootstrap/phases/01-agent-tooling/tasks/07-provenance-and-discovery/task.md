---
id: B01-07
status: Done
depends_on: [B01-06]
implementer_agent: 20260722_042302_c11331
reviewer_agent: 20260722_043148_cb427a
started_at: 2026-07-22T04:23:50+03:00
completed_at: 2026-07-22T04:36:01+03:00
---

# Complete provenance and agent discovery records

## What

Populate `.agents/README.md` and validate every skill with Codex.

## Why

Files existing on disk do not prove provenance, discovery, or correct use.

## How

- Record source, revision, command, date, license, included/excluded files, modifications, and update procedure.
- Run each documented controlled prompt in Codex and record evidence.
- Do not create duplicated skill copies to simulate compatibility.

## Required reading

- `docs/05_agent_skills/11_cross_agent_compatibility.md`
- `docs/05_agent_skills/12_agents_readme.md`
- `docs/05_agent_skills/16_acceptance_criteria.md`
- `docs/05_agent_skills/17_required_completion_report.md`

## Bootstrap verification contract

Apply verification row B01-07 and all relevant locked defaults from [the Bootstrap Verification Matrix](../../../../verification-matrix.md). Record exact commands, exit codes, and artifact paths in evidence.md.

## Acceptance

Codex discovery and controlled use pass for all five skills. Historical second-agent probe results remain outside the current acceptance contract.

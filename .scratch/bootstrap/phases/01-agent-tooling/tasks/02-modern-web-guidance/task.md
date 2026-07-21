---
id: B01-02
status: Done
depends_on: [B01-01]
implementer_agent: greekimpl
session_id: 20260722_014730_908786
reviewer_agent: greekreview
reviewer_session_id: 20260722_020416_c5fa1e
started_at: 2026-07-21T22:48:01Z
completed_at: 2026-07-21T23:24:01Z
---

# Install Modern Web Guidance

## What

Install only the core skill at `.agents/skills/modern-web-guidance/`.

## Why

It is part of the locked tooling baseline for platform, accessibility, compatibility, privacy, and security guidance.

## How

- Verify current official source and installer help.
- Generate in an isolated temporary directory.
- Inspect `SKILL.md`, referenced files, scripts, network calls, license, and revision.
- Copy only required core files and record excluded disciplines.

## Required reading

- `docs/05_agent_skills/06_google_chrome_modern_web_guidance.md`
- `docs/05_agent_skills/13_safe_installation_and_review_rules.md`
- `docs/05_agent_skills/12_agents_readme.md`

## Bootstrap verification contract

Apply verification row B01-02 and all relevant locked defaults from [the Bootstrap Verification Matrix](../../../../verification-matrix.md). Record exact commands, exit codes, and artifact paths in evidence.md.

## Acceptance

The canonical core skill and its required references exist, provenance and license are recorded, and no optional discipline was silently installed.

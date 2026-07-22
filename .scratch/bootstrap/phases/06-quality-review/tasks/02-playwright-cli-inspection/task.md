---
id: B06-02
status: Done
depends_on: [B06-01]
implementer_agent: 20260722_165408_e78a72
reviewer_agent: 20260722_171958_b5891d
started_at: 2026-07-22T16:54:37+03:00
completed_at: 2026-07-22T17:50:42+03:00
---

# Validate interactive Playwright CLI inspection

## What

Use the canonical Playwright CLI skill against the running fixtures.

## Why

Automated tests do not replace observed browser behavior and evidence collection.

## How

- Inspect both routes in both locales at compact and wide viewports.
- Exercise language switching, keyboard focus, and the interactive primitive.
- Record route, locale, viewport, state, console/network results, and artifact paths.
- Convert repeatable defects into permanent tests.

## Required reading

- `docs/05_agent_skills/09_playwright_cli_and_official_agent_skill.md`
- `docs/05_agent_skills/15_how_agents_must_use_the_tooling.md`
- `docs/02_prototype_specification/04_global_layout_and_responsive_model.md`

## Bootstrap verification contract

Apply verification row B06-02 and all relevant locked defaults from [the Bootstrap Verification Matrix](../../../../verification-matrix.md). Record exact commands, exit codes, and artifact paths in evidence.md.

## Acceptance

Interactive CLI evidence is reproducible for both routes and locales, and no blocking browser, console, network, keyboard, or responsive defect remains.

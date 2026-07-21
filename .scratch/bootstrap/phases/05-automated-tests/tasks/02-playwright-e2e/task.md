---
id: B05-02
status: Pending
depends_on: [B05-01]
implementer_agent: null
reviewer_agent: null
started_at: null
completed_at: null
---

# Configure Playwright Test

## What

Add Chromium E2E projects for compact, medium-targeted, and wide validation.

## Why

Permanent browser tests are required separately from interactive Playwright CLI inspection.

## How

- Install only Chromium.
- Add an exact-pinned project-level `@playwright/test` and, when officially supported, `@playwright/cli`; record the relationship to the global CLI validated in B01-05.
- Configure 390×844 and 1440×1024 projects plus targeted 834×1112 coverage.
- Use `baseURL` `http://127.0.0.1:3100`; Playwright `webServer` runs `pnpm dev --port 3100`, reuses an existing server only outside final verification, waits 120 seconds, and uses zero local retries.
- Use a 30-second test timeout, zero local retries, `trace: retain-on-failure`, `screenshot: only-on-failure`, and `video: retain-on-failure`.
- Test locales, switch, interaction, root redirect, invalid locale, metadata, keyboard focus, console, and critical requests.
- Use role/label locators.

## Required reading

- `docs/03_technical_design/18_testing_and_quality_gates.md`
- `docs/02_prototype_specification/04_global_layout_and_responsive_model.md`
- `docs/05_agent_skills/02_responsibilities_of_each_approved_item.md`

## Bootstrap verification contract

Apply verification row B05-02 and all relevant locked defaults from [the Bootstrap Verification Matrix](../../../../verification-matrix.md). Record exact commands, exit codes, and artifact paths in evidence.md.

## Acceptance

All configured Chromium projects pass reliably with the locked server, timeout, retry, locator, and failure-artifact policies.

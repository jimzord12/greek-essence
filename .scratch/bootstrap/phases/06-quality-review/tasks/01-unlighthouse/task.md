---
id: B06-01
status: In review
depends_on: [B05-03]
implementer_agent: 20260722_094928_de39e3
reviewer_agent: 20260722_125717_83e18a
started_at: 2026-07-22T06:50:03Z
completed_at: null
---

# Configure Unlighthouse

## What

Add an exact-pinned local Unlighthouse production-build gate.

## Why

Bootstrap needs a repeatable whole-site Lighthouse budget rather than an informal spot check.

## How

- Scan only the four explicit localized fixture URLs.
- Run mobile production audits with three samples.
- Enforce performance 90, accessibility 100, best practices 95, and SEO 95.
- Store output under `.artifacts/bootstrap/unlighthouse`.
- Make the script CI-ready but add no CI workflow.

## Required reading

- `docs/03_technical_design/08_media_assets_and_performance.md`
- `docs/03_technical_design/14_seo_architecture.md`
- `docs/03_technical_design/18_testing_and_quality_gates.md`

## Bootstrap verification contract

Apply verification row B06-01 and all relevant locked defaults from [the Bootstrap Verification Matrix](../../../../verification-matrix.md). Record exact commands, exit codes, and artifact paths in evidence.md.

## Acceptance

Every explicit localized fixture URL passes performance 90, accessibility 100, best practices 95, and SEO 95 against the production build.

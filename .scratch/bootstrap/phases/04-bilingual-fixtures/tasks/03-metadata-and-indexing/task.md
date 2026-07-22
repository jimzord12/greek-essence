---
id: B04-03
status: Done
depends_on: [B04-02]
implementer_agent: 20260722_075846_a50993
reviewer_agent: 20260722_080347_d09e15
started_at: 2026-07-22T04:59:02Z
completed_at: 2026-07-22T05:06:25Z
---

# Add fixture metadata and indexing safety

## What

Add localized metadata, equivalents, and `noindex, nofollow`.

## Why

SEO plumbing needs a test surface, but fixtures must never be presented as production content.

## How

- Add unique localized titles/descriptions and equivalent-route alternates.
- Use the configured local site URL for canonicals.
- Mark all bootstrap fixtures `noindex, nofollow`.
- Add no production structured data or organization claims.

## Required reading

- `docs/03_technical_design/14_seo_architecture.md`
- `docs/01_prd/20_trust_and_credibility_requirements.md`

## Bootstrap verification contract

Apply verification row B04-03 and all relevant locked defaults from [the Bootstrap Verification Matrix](../../../../verification-matrix.md). Record exact commands, exit codes, and artifact paths in evidence.md.

## Acceptance

Rendered titles, descriptions, canonicals, and alternates are localized and correct, and every bootstrap fixture is noindex and nofollow.

---
id: B04-03
status: Ready
depends_on: [B04-02]
implementer_agent: null
reviewer_agent: null
started_at: null
completed_at: null
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

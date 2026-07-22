---
id: B04-01
status: Ready
depends_on: [B03-04]
implementer_agent: null
reviewer_agent: null
started_at: null
completed_at: null
---

# Configure next-intl routing

## What

Add explicit English and Greek locale routing and minimal messages.

## Why

Localization infrastructure and route equivalence must be proven before product pages exist.

## How

- Support exactly `en` and `el`; redirect `/` to `/en`.
- Add routing, request, and navigation helpers.
- Set localized document language.
- Unknown locales return not-found.
- Keep messages limited to fixture interface strings.

## Required reading

- `docs/03_technical_design/05_routing_rendering_and_localization.md`
- `docs/03_technical_design/09_navigation_and_language_switching.md`
- `docs/02_prototype_specification/03_information_architecture_and_sitemap.md`

## Bootstrap verification contract

Apply verification row B04-01 and all relevant locked defaults from [the Bootstrap Verification Matrix](../../../../verification-matrix.md). Record exact commands, exit codes, and artifact paths in evidence.md.

## Acceptance

Both locale shells render statically, equivalent language switching works, root redirection is deterministic, and invalid locales return an honest not-found response.

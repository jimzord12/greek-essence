---
id: B04-02
status: Ready
depends_on: [B04-01]
implementer_agent: null
reviewer_agent: null
started_at: null
completed_at: null
---

# Create minimal quality-fixture pages

## What

Create `/[locale]` and `/[locale]/quality-lab`.

## Why

The routes provide a real target for i18n, shadcn/Base UI, responsive, keyboard, Playwright, axe, and performance checks without beginning product work.

## How

- Landing: skip link, landmarks, one H1, bootstrap status, locale switch, and lab link.
- Lab: one approved interactive primitive with localized labels and visible states.
- Keep the Client Component boundary minimal.
- Use no business claims, real travel content, forms, analytics, or trust assertions.

## Required reading

- `docs/03_technical_design/07_design_system_components_responsive_behavior_and_motion.md`
- `docs/03_technical_design/13_accessibility_implementation.md`
- `docs/04_design/22_universal_visual_states.md`
- `docs/04_design/35_wcag_2_2_aa_visual_rules.md`

## Bootstrap verification contract

Apply verification row B04-02 and all relevant locked defaults from [the Bootstrap Verification Matrix](../../../../verification-matrix.md). Record exact commands, exit codes, and artifact paths in evidence.md.

## Acceptance

Both fixture routes work in English and Greek at 320, 390, 834, and 1440 widths with keyboard-only use, reduced motion, and 200 percent zoom.

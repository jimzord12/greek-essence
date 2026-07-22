---
id: B05-03
status: In review
depends_on: [B05-02]
implementer_agent: 20260722_090930_f3cf8d
reviewer_agent: 20260722_125220_95d73e
started_at: 2026-07-22T06:09:52Z
completed_at: null
---

# Add axe accessibility gates

## What

Integrate `@axe-core/playwright` across both routes and locales.

## Why

Automated accessibility detection complements required manual keyboard, zoom, reflow, target-size, and reduced-motion review.

## How

- Use current WCAG A/AA tags through WCAG 2.2 where supported.
- Require zero violations and attach full JSON on failure.
- Do not suppress rules or exclude components to manufacture green results.
- Keep manual acceptance checks separately recorded.

## Required reading

- `docs/03_technical_design/13_accessibility_implementation.md`
- `docs/02_prototype_specification/11_accessibility_and_inclusive_interaction.md`
- `docs/04_design/35_wcag_2_2_aa_visual_rules.md`

## Bootstrap verification contract

Apply verification row B05-03 and all relevant locked defaults from [the Bootstrap Verification Matrix](../../../../verification-matrix.md). Record exact commands, exit codes, and artifact paths in evidence.md.

## Acceptance

All four localized route variants report zero axe violations, controlled failure detection is proven, and no rule suppression is introduced.

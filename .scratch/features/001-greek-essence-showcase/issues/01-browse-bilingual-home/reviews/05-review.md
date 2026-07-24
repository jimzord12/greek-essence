# Issue Review 05: Browse a complete bilingual Home through the shared showcase foundation

Date: 2026-07-24
Reviewer: fresh independent code-review agent (attempt 05)
Issue: `01-browse-bilingual-home`
Verdict: `PASS with operator-authorized performance exception`
Route: `fresh visual review; remain in-review`

## Scope

Reviewed the complete current tracked and untracked issue-owned snapshot against root and feature `AGENTS.md`, `NEXT.md`, approved feature `SPEC.md`, current `issue.md` and `change-contract.md`, immutable code review 03, immutable visual review 04, reconciled `implementation-report.md`, and the relevant responsive/accessibility implementation guidance. Inspected the VIS-04-01 source and regression-test repair in full and re-evaluated Standards and every issue #01 SPEC/contract axis for regressions from that source change.

Concurrent unrelated `.agents/skills/ralph-loop-manager/**`, `.scratch/ralph-loop/**`, `.hermes/plans/**`, and generated `.playwright-cli/**` changes were preserved and excluded from the issue verdict and focused formatting scope. Issue #02 was not inspected.

Reviews 03 and 04 remain unchanged: their SHA-256 values are respectively `ea8cfb742ba1189c87d42010ffd4fbf3fa5d97202bdf168b3b81301a2fbb3c29` and `f1490ce4b623b3c73565d30cb53503cdb7333e488fb95f662583298be7f0a2b9`; their path-specific working-tree diff was empty before this report was written.

## Standards Verdict

`PASS with operator-authorized performance exception`. The VIS-04-01 repair is narrow, CSS-first, responsive, readable, and accessible. At and below `20rem`, Home shells receive an exact viewport-derived gutter width and Home headings/paragraphs receive `overflow-wrap: break-word`. The rules are not global, do not alter ordinary compact or wide typography, and introduce no `overflow` hiding, clipping, line clamping, ellipsis, fixed height, content reduction, or truncation. Existing semantic structure, focus behavior, reduced-motion behavior, light-only tokens, static rendering, localized navigation, media fallback, security headers, and minimal client boundary remain intact.

**Accepted residual risk — strict performance gate remains technically RED:** the unchanged Home LCP ceiling is `<=2500ms`. The latest reported post-repair measurement is EN `2547.223ms`; the implemented assertion correctly exits nonzero. Direct operator authority permits workflow progression, but this review does not call the metric or aggregate performance gate a technical PASS. No threshold, samples, routes, audits, mobile profile, category budget, or measurement rationale was weakened.

## Spec And Contract Verdict

`PASS with operator-authorized performance exception`. VIS-04-01 is repaired without a new code blocker:

- A fresh production-runtime probe at exact `195 × 844` measured document and body `195/195` for both `/en` and `/el`, with zero internally over-wide descendants.
- The same independent probe measured document/body exact equality and zero over-wide descendants for both locales at `320`, `321`, `390`, and `1440` CSS-pixel widths. This verifies the media-query boundary as well as no degradation at required compact/wide frames.
- Computed `overflow-wrap` was `break-word` at `195` and `320`, and returned to `normal` at `321`, `390`, and `1440`, confirming the repair is scoped to `max-width: 20rem`.
- Main shell widths were `155px` at a `195px` viewport, `280px` at `320px`, `281px` at `321px`, `350px` at `390px`, and `1280px` at `1440px`; shell overflow remained `visible`.
- Main headings and paragraphs retained visible overflow and `text-overflow: clip` rather than hiding or ellipsizing content. The slight scroll/client-height differences observed on some headings were normal line-box rounding with all text visible, not fixed-height clipping.
- Both locales still rendered exactly six direct Home sections in every runtime probe. Focused compact/wide Playwright and axe runs remained green.
- The regression helper asserts exact document/body `scrollWidth === clientWidth` and enumerates every descendant whose internal `scrollWidth` exceeds `clientWidth` by more than one pixel or whose right edge exceeds the viewport. It directly covers both locale routes at the exact `195px` regression width and would reproduce the original Greek `205/195` failure. Source inspection complements the test by proving the repair does not hide overflow. This is proportionate and strong for the observed defect.

The source change does not regress the exact bilingual composition, locale-aware route identity, content/message/media validation, approved-media fail-closed behavior, metadata and private-prototype policy, complete CSS token foundation, semantic landmarks/headings, keyboard/focus/reduced-motion behavior, security/privacy boundaries, static-first architecture, or issue scope.

## Blocking Findings

None other than the unchanged strict LCP gate, which remains a prominent technically failing gate and is accepted solely as the operator-authorized residual risk for workflow progression.

## Non-Blocking Findings

- The focused regression test itself checks the exact `195px` failure boundary, while the fresh independent production probe supplied the additional `320/321/390/1440` boundary evidence. A later test expansion could encode the `321px` scope boundary, but the current regression test plus narrowly readable CSS and ordinary compact/wide suites are sufficient for this Tier-2 repair.
- The prior visual-review observation that Greek display fallback is heavier than English remains a visual-polish matter for the mandatory fresh visual reviewer, not a source blocker.

## Verification Considered

- Focused formatting over the complete issue-owned production, content, validation, configuration, unit/E2E, and implementation-report paths — `PASS`; all matched files use Prettier style. Global formatting was intentionally not required for unrelated Ralph/plan/generated Playwright YAML files.
- `pnpm lint` — `PASS`.
- `pnpm typecheck` — `PASS`.
- `pnpm validate:content` — `PASS`; Zod-backed EN/EL validation with media approval checks.
- `pnpm test:unit` — `PASS`, 7 files / 29 tests.
- `pnpm build` — `PASS`; `/en` and `/el` remain statically generated, with no application Route Handler introduced.
- `pnpm exec playwright test --project=chromium-compact tests/e2e/localization-and-quality.spec.ts tests/e2e/accessibility.spec.ts` — `PASS`, 12/12, including the exact two-locale `195px` regression assertion.
- `pnpm exec playwright test --project=chromium-wide tests/e2e/localization-and-quality.spec.ts tests/e2e/accessibility.spec.ts` — `PASS`, 11 passed / 1 expected compact-only skip.
- Independent production server on `127.0.0.1:4174` — ready in 167ms; runtime DOM probes covered `/en` and `/el` at `195 × 844`, `320 × 844`, `321 × 844`, `390 × 844`, and `1440 × 1024`; all document/body and descendant-overflow checks passed. The review-owned server was stopped afterward.
- `git diff --check` — `PASS`.
- Review immutability checks — `PASS`; reviews 03/04 path diff empty and hashes recorded above.
- Strict performance evidence — `FAIL` as designed and authorized: latest reported EN LCP `2547.223ms` exceeds `2500ms`, so `pnpm quality:unlighthouse` and therefore `pnpm check:all` cannot truthfully be called fully green.
- Persisted lifecycle evidence — issue remains `in-review`; no lifecycle mutation was performed.

## Required Route

Proceed to a **fresh independent visual review** of the final `/en` and `/el` Home at `195 × 844`, `390 × 844`, and `1440 × 1024`, including the repaired Greek reflow, complete readable content, compact/wide shell and navigation, localized current state, pending-media fallback, keyboard focus, and reduced-motion presentation. Keep issue #01 `in-review`; do not mark it `done` unless that fresh visual review passes. Carry the technically failing strict `<=2500ms` LCP gate forward unchanged as the operator-authorized residual risk, and do not begin or inspect issue #02 from this verdict.

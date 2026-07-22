---
task: B06-01
reviewer_agent: 20260722_125717_83e18a
implements_review: 04-review.md
verdict: Changes requested
---

# Review 05 — B06-01 strict remediation re-review

## 1. Scope and methodology

Reviewed Review 04, its response, updated task evidence/report, the complete current diff, raw current Lighthouse reports and captured Unlighthouse logs, the verification matrix and required technical-design sections, and installed `@unlighthouse/core@0.18.0`/Lighthouse `12.6.1` source. Prior records remain unchanged.

The locked B06-01 contract requires mobile audits, three samples, four explicit URLs, and the stated budgets; the installed Lighthouse mobile default is part of the meaning of that contract, not an optional implementation detail. `core/config/constants.js:60-64` sets mobile `throttling: mobileSlow4G` and `throttlingMethod: "simulate"`. `core/computed/metrics/metric.js:84-93` computes simulated metrics only for `simulate` and observed metrics for `provided`; `core/lib/emulation.js:82-95` clears network throttling unless the method is `devtools`.

## 2. F-06 — High — Remains open: `provided` weakens the locked mobile performance methodology

- Location: `unlighthouse.config.ts:12-15`; current raw reports at `.artifacts/bootstrap/unlighthouse/reports/**/lighthouse.json`.
- Violated requirement: `task.md:23-26,41`, `verification-matrix.md:29,51,63`, and `docs/03_technical_design/08_media_assets_and_performance.md:13-29` require a meaningful mobile production-performance gate, not merely textually mobile report metadata and score thresholds.
- Evidence/reproduction: the exact current gate, `env -u NEXT_PUBLIC_SITE_URL pnpm quality:unlighthouse`, exited 0 with four 1.00 category results. Raw reports nevertheless identify `formFactor: "mobile"` and `throttlingMethod: "provided"`, with observed host-local LCP values only 70.337–126.152 ms. The configured mobileSlow4G values remain printed in the report but do not turn the observed local-host measurement into simulated mobile performance.
- Methodology analysis: changing the default from `simulate` to `provided` changes the measured metric type from Lighthouse's simulated mobileSlow4G model to host-dependent observed measurements. It therefore weakens the locked mobile acceptance semantics even though device, route list, samples, and budgets remain textually unchanged. The current all-1.00 result is not comparable to the original default-mobile result and cannot resolve F-06.
- Controlled A/B: after a fresh successful production build, the reviewer created a temporary ignored config identical to the gate but omitting `throttlingMethod`, ran `env -u NEXT_PUBLIC_SITE_URL pnpm exec unlighthouse-ci --config-file .artifacts/bootstrap/b06-01-review-simulated.config.ts` against the same production server, and removed both temporary config and output afterward. It exited 0 with raw `throttlingMethod: "simulate"` reports: `/el` 0.93, `/el/quality-lab` 0.92, `/en` 0.93, and `/en/quality-lab` 0.93 performance; accessibility, best practices, and SEO were 1.00 for every route. This proves a valid correction does not need the methodology change.
- Required correction: remove `lighthouseOptions.throttlingMethod: "provided"`; retain the boundary correction, locked three-sample behavior, routes, budgets, and audit scope; then refresh evidence from the restored default simulated-mobile gate.
- Verification: from a fresh production build, `env -u NEXT_PUBLIC_SITE_URL pnpm quality:unlighthouse` exits 0; all raw reports state `throttlingMethod: "simulate"`, the four exact paths meet the existing budgets, and captured output has no server, console, locale, or critical-request failure.

## 3. QualityLabToggle boundary — verified as the effective default-methodology correction

`app/[locale]/quality-lab/page.tsx:4,71-75` limits the new boundary to the existing toggle. `components/quality-lab-toggle.tsx:1-14` is a client-only dynamic import with `ssr: false`; the page remains a statically generated SSG route in the reviewer build. This is a small, non-critical interaction boundary rather than a conversion of page content or locale/metadata work to client rendering.

The controlled default-simulated A/B result above shows that the boundary improves the previously failing mobile methodology: both quality-lab routes now pass at 0.92/0.93 without changing Lighthouse method, device, samples, routes, or budgets. No High SSR/static-first, accessibility, or interaction defect was found. On the production build, Playwright CLI at 390x844 exercised English and Greek quality-lab pages via Tab/Space: each button received keyboard focus, changed `aria-pressed` from `false` to `true`, and updated its localized polite live region. The browser reported zero console errors. `pnpm exec playwright test tests/e2e/localization-and-quality.spec.ts` exited 0 with 15 passing tests, including its browser console/network guards and localized toggle journey.

## 4. F-04 — Non-blocking — Unchanged accepted technical debt

- Location: `app/[locale]/layout.tsx:10-16` (unchanged in this remediation).
- Disposition: unchanged from Review 04. The absent-public-origin fallback is not an original B06-01 acceptance failure and remains documented Non-blocking technical debt; no metadata policy change was made or required for F-06.
- Verification: Review 04's English/Greek production-rendered canonical evidence remains applicable; this re-review found no change to that source or behavior.

## 5. Reviewer commands and results

- `env -u NEXT_PUBLIC_SITE_URL pnpm build` — exit 0; generated `/en`, `/el`, `/en/quality-lab`, `/el/quality-lab`, and `/robots.txt` as static/SSG routes.
- Exact current `env -u NEXT_PUBLIC_SITE_URL pnpm quality:unlighthouse` — exit 0; current provided-method report contains four required paths and all categories at 1.00, but fails the methodology assessment above.
- Controlled temporary default-simulated Unlighthouse run — exit 0; four required routes, all budgets passed, performance 0.92–0.93; temporary config/output removed.
- `pnpm exec playwright test tests/e2e/localization-and-quality.spec.ts` — exit 0; 15 passed.
- `git diff --check` — exit 0.

## 6. Verdict and task-status disposition

Changes requested.

F-06 remains High because `throttlingMethod: "provided"` weakens the locked mobile performance acceptance semantics. F-04 remains Non-blocking. B06-01 stays `In review`; no Blocking finding is present, and it cannot return to `Done` until F-06 is corrected and re-reviewed.

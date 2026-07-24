# Issue Review 03: Browse a complete bilingual Home through the shared showcase foundation

Date: 2026-07-24
Reviewer: fresh independent code-review agent (attempt 03)
Issue: `01-browse-bilingual-home`
Verdict: `PASS with operator-authorized performance exception`
Route: `mandatory fresh visual review; remain in-review`

## Scope

Reviewed the complete current tracked and untracked issue-owned snapshot against root and feature `AGENTS.md`, `NEXT.md`, approved `SPEC.md`, current `issue.md` and `change-contract.md`, immutable reviews 01/02, the reconciled `implementation-report.md`, live JZ validation/completion expectations, and relevant design, token, responsive, accessibility, Home, and media/performance sources. Inspected the complete issue #01 production, content, validation, test, build, route, header, and Unlighthouse wiring. Re-evaluated all Standards and SPEC/contract axes, not only review-02 deltas. Issue #02 implementation was not inspected.

Reviews 01 and 02 remain unchanged: their SHA-256 values are respectively `0ce89383d2a109e6972fd09b86d0c7ac79134cac55001357ad6751cbf4a6e9fe` and `db829a6baa7c04ac12c40cab5534f58fd27f10fc10cc897a7d26d02b5f0f095d`; the path-specific working-tree diff for both was empty before this report was written.

## Standards Verdict

`PASS with operator-authorized performance exception`. The retained implementation is bounded, static-first, explicit-locale, predominantly server-rendered, strict-TypeScript, CSS-first and light-only. It introduces no successor surface or dynamic server boundary, renders editorial data through React rather than raw HTML, preserves the approved locale-aware navigation/provider boundary, fails closed for unapproved media, and retains the required security headers. Focused validation, unit, lint, type, and production-build checks are green.

**Accepted residual risk — strict performance gate remains technically RED:** the unchanged Home LCP ceiling is `<=2500ms`; the implemented gate correctly exits nonzero for the latest bounded baseline EN measurements of `2521.378–2524.444ms`. Direct operator authority on 2026-07-24 permits workflow progression after the bounded investigation, but does not make this gate technically pass. The later `2577.9ms` EN / `2612.368ms` EL artifact came from a reverted font experiment and is not representative of retained source, while still remaining truthful failing evidence.

## Spec And Contract Verdict

`PASS with operator-authorized performance exception`. Review-02 repairs are otherwise acceptable:

- The complete documented semantic color names and exact mappings are present in the Tailwind CSS v4 `@theme inline` source and asserted exhaustively, including surface-subtle, accent-hover, links, disabled, status/subtle pairs, overlay, hero foreground, and hero scrim. Primitive palette and the documented typography, spacing, container/gutter, radius, elevation, easing, focus, and shared-state foundation remain centralized in CSS with no dark or TypeScript theme branch.
- Controlled fixtures reject empty editorial copy, unknown route IDs, unknown media IDs, and EN/EL structural drift. The Zod-backed command validates live locale structure and media references.
- Approved media requires approved set/source/operator status, allow-listed provenance, approved rights, non-provisional state, localized non-empty alt, valid focal coordinates, positive geometry, an approved master/crop role, and file existence. Pending live media continues to return the intentional fallback. The rendering path consumes approved resolution through responsive `next/image` and does not infer approval in components.
- `scripts/assert-unlighthouse-lcp.mjs` reads the actual EN/EL Lighthouse report files, rejects missing/non-finite reports, accepts the exact `2500ms` boundary, rejects `2500.001ms` for either locale, and is chained after `unlighthouse-ci` inside the real `pnpm quality:unlighthouse` command. Samples, routes, mobile profile, audits, category budgets, and the documented DevTools-throttling rationale remain unchanged.
- The exact six-section bilingual Home, shell, metadata/alternates/noindex, route identities, pending-media fallback, response headers, compact-menu behavior, focus/current/reduced-motion behavior, responsive/zoom coverage, static generation, browser guards, and accessibility evidence remain consistent with the issue contract.

The sole unresolved contract failure is the explicitly accepted strict LCP result above. It is not reinterpreted or erased.

## Blocking Findings

None other than the strict LCP gate, which remains a prominent technically failing gate and is accepted solely as the operator-authorized residual risk for workflow progression.

## Non-Blocking Findings

- The controlled media unit table directly mutates pending source approval, arbitrary source provenance, provisional status, and invalid crop role. Other fail-closed clauses (set/operator approval, rights, alt, focal coordinates, dimensions, and file existence) are plainly conjoined in the reviewed implementation and standalone validator, but do not each have a separately named mutation row in the final table. Given the existing approved happy path, incomplete approval table, live validator, and Tier-2 scope, this is not a remaining blocker.
- Cormorant Garamond has no supported Greek subset in the installed font API, so Greek headings use the declared serif fallback. This remains appropriate for inspection during mandatory visual review.
- The issue front matter and persisted issue ledger remain `in-review`; the persisted phase remains `red` after two review reopens. No lifecycle state was changed by this review.

## Verification Considered

- Fresh focused unit command: `pnpm test:unit -- tests/unit/content/showcase-content.test.ts tests/unit/design/showcase-token-contract.test.ts tests/unit/quality/unlighthouse-lcp.test.ts tests/unit/routes/showcase-routes.test.ts` — `PASS`, 7 files / 29 tests (Vitest script runs the repository unit suite).
- Fresh `pnpm validate:content` — `PASS`, Zod-backed EN/EL and media approval validation.
- Fresh `pnpm lint` — `PASS`.
- Fresh `pnpm typecheck` — `PASS`.
- Fresh `pnpm build` — `PASS`; `/en` and `/el` remain statically generated, with no new application Route Handler.
- Fresh `git diff --check` — `PASS`.
- Fresh review immutability checks — `PASS`: reviews 01/02 path diff empty; SHA-256 values recorded in Scope.
- Supplied post-review-02 browser evidence — compact `12/12`, wide `11 passed/1 compact-only skip`, full E2E `34 passed/2 compact-only skips`, and axe `12/12`.
- Supplied strict performance evidence — `FAIL` as required by the implemented gate: retained-source baseline EN `2521.378–2524.444ms` exceeds `2500ms`. `pnpm check:all` therefore cannot truthfully be called green. This is the operator-authorized exception, not a technical PASS.
- Persisted lifecycle evidence — issue `in-review`; authorized frontier `review-issue`. No lifecycle mutation was performed.

## Required Route

Proceed only to the feature-local mandatory fresh independent visual review of `/en` and `/el` at `390 × 844` and `1440 × 1024`, including localized current/selected navigation, compact/wide shell, pending-media fallbacks, keyboard focus, and reduced-motion presentation. Keep issue #01 `in-review`; do not mark it `done` unless visual review passes. Carry the strict failing `<=2500ms` LCP gate forward prominently as the operator-authorized accepted residual risk. Do not begin issue #02 from this verdict.

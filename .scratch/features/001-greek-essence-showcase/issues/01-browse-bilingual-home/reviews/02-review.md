# Issue Review 02: Browse a complete bilingual Home through the shared showcase foundation

Date: 2026-07-24
Reviewer: fresh independent code-review agent (attempt 02)
Issue: `01-browse-bilingual-home`
Verdict: `FAIL`
Route: `red`

## Scope

Reviewed the complete tracked and untracked issue-owned snapshot against root `AGENTS.md` and `NEXT.md`, feature `AGENTS.md`, approved `SPEC.md`, current `issue.md` and reopen history, `change-contract.md`, immutable `reviews/01-review.md`, reconciled `implementation-report.md`, live non-fast `jz-implement-contract` validation/completion/contract-cage references, the repository-local Greek Essence quality-review skill, and relevant `docs/04_design` token, Home, responsive, motion, and accessibility sources. Re-reviewed the Home routes and shared shell, Zod/content/media boundaries, route helpers and `next-intl` navigation, provider behavior, metadata/headers, CSS token foundation, rendering, tests, quality configuration, and supplied performance artifacts. Issue #02 was not inspected.

## Standards Verdict

`FAIL`. The implementation remains static-first, localized, predominantly server-rendered, free of raw HTML, and bounded to issue #01. Focused unit/content checks, compact/wide browser checks, response headers, menu behavior, current/focus/reduced-motion/zoom checks, and the supplied direct-throttled EN/EL performance measurements are green. However, the CSS-first design-system contract is still materially incomplete, and the tests that claim completeness do not enumerate the documented semantic token inventory or several named invalid-validation cases. These are acceptance-case test defects, so Standards do not pass.

## Spec And Contract Verdict

`FAIL`. Prior blockers F-03 and F-04 are substantially repaired: Home rendering receives `resolveMedia` results, pending records remain neutral fallbacks, controlled approved media uses `next/image` with alt, intrinsic dimensions, focal position, `sizes`, and hero priority; `@/i18n/navigation` again exports `createNavigation(routing)`, all reviewed links use that boundary, explicit locale URLs are not duplicated, `NextIntlClientProvider` is restored, and prefetch is disabled only for deferred unavailable successor routes. F-05's observed measurements now pass the unchanged numerical budgets: EN LCP 2377.826 ms and EL LCP 2460.344 ms, with performance 94/93, all other categories 100, CLS 0, unchanged route/sample/score settings, and documented direct mobile DevTools throttling rationale.

F-01 and F-02 are not fully resolved. The implementation report is therefore inaccurate where it states that the complete documented token inventory exists and that F-01 through F-05 are all repaired. Review 01 remains unchanged; its current SHA-256 is `0ce89383d2a109e6972fd09b86d0c7ac79134cac55001357ad6751cbf4a6e9fe`, and `git diff -- reviews/01-review.md` is empty.

## Blocking Findings

### F-01: Token completeness and invalid-validation tests remain materially weak

`tests/unit/design/showcase-token-contract.test.ts` asserts only a selected subset of primitive/layout tokens and checks shared-state names without values. It does not test the complete documented semantic inventory in `docs/04_design/06_color_philosophy.md`, including `--color-surface-subtle`, `--color-accent-hover`, `--color-link`, `--color-link-hover`, disabled foreground/background, success/warning/destructive/info subtle pairs, overlay, hero foreground, and hero scrim. The content tests exercise live valid content, pending media, one controlled approved record, and one incomplete approved record, but do not provide controlled invalid Zod fixtures for empty editorial fields, unknown route IDs, unknown media IDs, or EN/EL structural drift. The standalone validator is now genuinely Zod-backed and checks current structure/media, and route/header/menu/responsive checks are present, but the named invalid acceptance cases and full exact token inventory are not proven. The required route remains `red`.

### F-02: The documented CSS-first semantic token inventory is still incomplete

`app/globals.css` contains the primitive palette, type-size roles, spacing, containers, radii, shadows, motion/easing, focus, and generic state aliases, and the retained dark branches were removed. But its `@theme inline` block omits or renames many required semantic tokens from `docs/04_design/06_color_philosophy.md`: it defines `--color-surface-muted` rather than documented `--color-surface-subtle`, `--color-accent-active` rather than `--color-accent-hover`, and omits the documented link, disabled, warning, subtle status, overlay, hero foreground, and hero-scrim mappings. Consequently Tailwind semantic utilities do not resolve from the complete documented source-of-truth inventory required by FR-016/DEC-013. This directly contradicts the implementation report's “complete” claim.

### F-03: Approved-media validation does not prove the full approval contract

`resolveMediaFromManifest` requires approved rights/status, localized alt, focal data, dimensions, and a file check, and the rendering path now consumes the result correctly. However, the declared `MediaManifest` drops the manifest's `provisional` and per-file role/crop metadata, and neither runtime validation nor the standalone validator verifies a non-pending approved source/provenance state. The controlled test uses arbitrary `source: "operator-generated"` while approval succeeds solely from `approvalStatus` and `rightsStatus`. The SPEC requires complete source/rights approval before rendering. Add a precise controlled invalid fixture for missing/pending source approval and make the validator fail closed at that seam without promoting the live pending manifest.

### F-04: The separate strict LCP ceiling is evidence-only, not enforced by the quality gate

The supplied final artifact passes F-05 numerically, and the DevTools throttling rationale is documented without lowering scores, routes, audits, or samples. Nevertheless, `unlighthouse.config.ts` enforces only category scores; `pnpm quality:unlighthouse` can exit 0 when Home LCP exceeds 2500 ms, as review 01 already demonstrated. No test or post-processing gate deterministically fails the command on the separate strict Home LCP ceiling. The contract and review-01 repair route explicitly require retaining a gate for that threshold. Add a deterministic assertion over both Home locale reports while preserving the current mobile profile, three samples, direct-throttling rationale, route set, audits, and score budgets.

## Non-Blocking Findings

- Compact menu Escape closes and returns focus; outside activation closes; locale navigation closes by route transition. The contract does not require outside-click focus return, and the current behavior is acceptable.
- `getRoutePathname` derives locale-neutral pathnames by stripping `/en`, but links still pass those pathnames through `createNavigation(routing)` and focused E2E proves no duplicate locale prefix on Home switching. This is acceptable for the fixed route boundary.
- The existing note about Cormorant Garamond lacking a Greek subset remains appropriate for mandatory visual review; it is not a code-review blocker because the installed font API does not expose a Greek subset and the CSS provides a serif fallback.
- Even after a future code-review PASS, leave the issue `in-review`; the feature-local fresh visual review remains mandatory.

## Verification Considered

- `pnpm validate:content` - `PASS`: real Zod parse, recursive current EN/EL shape comparison, referenced-media checks, and approval/file checks completed for the live content.
- `pnpm test:unit -- tests/unit/content/showcase-content.test.ts tests/unit/design/showcase-token-contract.test.ts tests/unit/routes/showcase-routes.test.ts` - `PASS`: Vitest ran 6 files and 17 tests; coverage gaps remain as F-01 describes.
- `pnpm exec playwright test --project=chromium-compact tests/e2e/localization-and-quality.spec.ts` - `PASS`: 8/8, including metadata, headers, menu interactions, focus/current/reduced-motion, responsive overflow, and 195 px zoom-equivalent coverage.
- `pnpm exec playwright test --project=chromium-wide tests/e2e/localization-and-quality.spec.ts` - `PASS`: 7 passed and 1 compact-only skip.
- `git diff --check` - `PASS`.
- `git diff -- .scratch/features/001-greek-essence-showcase/issues/01-browse-bilingual-home/reviews/01-review.md` - `PASS`: empty; review 01 unchanged.
- Supplied final `pnpm check:all` / Unlighthouse artifact - `PASS` for the observed run: EN 94/100/100/100, LCP 2377.826 ms, CLS 0; EL 93/100/100/100, LCP 2460.344 ms, CLS 0; DevTools mobile throttling, three samples, unchanged score budgets/routes/audits. The command still lacks deterministic enforcement of the separate LCP ceiling as F-04 describes.
- Persisted lifecycle files - `PASS`: issue status is `in-review`; the authorized frontier remains `review-issue`. No lifecycle mutation was performed.

## Required Route

Reopen at `red`. Add failing tests for the complete documented semantic token inventory and exact mappings, the named invalid Zod/content/media fixtures including source approval, and deterministic EN/EL Home LCP ceiling enforcement. Then repair only those in-contract seams, reconcile `implementation-report.md`, rerun affected/full gates, and create a new immutable code-review attempt. Do not mark the issue done; after a future code-review PASS, mandatory fresh visual review is still required.

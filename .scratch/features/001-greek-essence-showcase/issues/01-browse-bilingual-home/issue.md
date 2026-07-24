Status: done
Method: tdd-solo
Complexity: 5
BlockedBy: none
Milestone: explore-bilingual-showcase
Phase: green
Reopens: 3

# Browse a complete bilingual Home through the shared showcase foundation

Deliver the first complete static discovery slice: a visitor can browse the six-section Home in English or Greek, use the shared responsive shell, switch to the equivalent localized Home, follow localized calls to action, and see meaningful editorial content even while provisional media remains unapproved. Establish the complete documented reusable Tailwind CSS v4 token foundation as part of this consumed Home slice, without adding unused wider-product components or a parallel theme representation.

## Acceptance criteria

- [ ] English and Greek Home routes render the exact six-section composition and shared shell, with complete natural locale content, localized links, no unsupported business claims, and no mixed-language fallback (FR-001, DEC-001, DEC-008, SUBDEC-004).
- [ ] The locale switch preserves Home route identity through the approved locale-aware navigation boundary, and static explicit-locale routing remains intact (FR-003, DEC-010).
- [ ] Build-time content and shared-message validation enforces locale structure/key parity, stable media IDs, non-empty localized editorial content, and fail-closed approved-media metadata (FR-013, NFR-007).
- [ ] Pending QUE-003 media renders the intentional neutral fallback with all meaning retained in adjacent content; no unapproved image is promoted and no approval question is reopened.
- [ ] Home emits non-empty localized title/description, self-canonical URL, `en`/`el`/`x-default` alternates, and private-prototype `noindex,nofollow`, with no PII in URL or metadata (FR-015, NFR-004).
- [ ] The complete documented reusable foundation—colors, typography, spacing, layout, responsive modes, shape, elevation, motion/easing, focus, and shared interaction/status states—is centralized through Tailwind CSS v4 semantic theme variables and consumed by Home; appearance is light-only, no parallel TypeScript theme exists, and component tokens/variants are limited to showcase consumers (FR-016, DEC-011, DEC-013, NFR-008).
- [ ] The shared static shell and Home use semantic landmarks/headings, keyboard-operable controls, visible focus, reduced-motion behavior, responsive image/fallback handling, and minimal client JavaScript; server-only/dynamic functionality is not introduced (NFR-001, NFR-002, NFR-003, DEC-010).
- [ ] Shared rendering treats editorial content as data rather than raw HTML, introduces no user-derived HTML, and applies the SPEC's route-wide CSP, `nosniff`, referrer, permissions, and frame-denial headers without weakening Next/font or local-image behavior (NFR-005).
- [ ] Focused automated checks prove route/content/message parity, Home metadata, locale switching, token-contract completeness, and safe media fallback behavior.
- [ ] Home is exercised at the required compact and wide Playwright viewports with browser guards, axe checks, responsive/zoom spot checks, and preserved Unlighthouse plus documented transfer, image, JavaScript, CSS, LCP, INP, and CLS budgets; failures are fixed in this slice without weakening gates (DEC-012).

Traces: FR-001, FR-003, FR-013, FR-015, FR-016; NFR-001, NFR-002, NFR-003, NFR-004, NFR-005, NFR-007, NFR-008; DEC-001, DEC-008, DEC-010, DEC-011, DEC-012, DEC-013, SUBDEC-004.

## Reopen History

### 2026-07-24 — review failed → restart at red (tests)
# Issue Review 01: Browse a complete bilingual Home through the shared showcase foundation

Date: 2026-07-24
Reviewer: fresh independent code-review agent
Issue: `01-browse-bilingual-home`
Verdict: `FAIL`
Route: `red`

## Scope

Reviewed the complete current tracked and untracked issue-owned working snapshot against root `AGENTS.md`, `NEXT.md`, `docs/README.md`, feature `AGENTS.md`, the approved feature `SPEC.md`, `issue.md`, `change-contract.md`, draft `implementation-report.md`, the live `jz-implement-contract` validation/completion rules, the repository-local Greek Essence quality-review skill, and the relevant design-system token specifications. The review covered the Home routes and shared shell, content/schema/media boundaries, route helpers and navigation, metadata/security configuration, fonts, CSS/token foundation, tests, quality configuration, and reported verification evidence. Issue #02 implementation was not inspected.

## Standards Verdict

`FAIL`. The snapshot is small and predominantly static/server-rendered, keeps explicit locale static params, introduces no dynamic server boundary, uses escaped React rendering rather than raw HTML, and adds the required response headers. However, the implementation does not meet the repository's required test depth or its CSS-first design-system contract. The content validation command is not a real validation of the exported Zod schema or media approval contract, the test suite omits contract-named seams, and the claimed full token foundation is materially partial. The use of `throttlingMethod: "devtools"` is plausibly motivated by a reproduced Windows Lantern defect and does not change the numeric score thresholds, but it does change the measurement model; more importantly, the resulting measured Home LCP values still exceed the unchanged explicit 2.5-second gate, so the performance acceptance cannot be reported as passing.

## Spec And Contract Verdict

`FAIL`. The six Home sections, EN/GR content, static route generation, localized metadata, pending-media fallback presentation, and baseline security headers are present. The following contract requirements are not proven or not implemented:

- The approved locale-aware navigation boundary is bypassed. `SiteHeader`, `SiteFooter`, and `HomeSections` import raw `next/link`, and `quality-lab` was changed from `@/i18n/navigation` to raw string-built `next/link` paths. Centralizing strings in `getLocalizedHref` avoids ad-hoc replacement for showcase routes, but it is not the contract-preserved `createNavigation(routing)` boundary. Removing `NextIntlClientProvider` may be a valid static-first optimization only after the locale-aware navigation helpers and all client consumers are proven to work without it; the current implementation avoids that proof by replacing the helpers.
- All Home media is rendered unconditionally as `MediaFallback`; `resolveMedia` is never consumed by the rendering path. Pending media looks correct today, but a valid approved record would still never render, contrary to the fail-closed approved-media/responsive-image contract.
- The foundational token inventory is incomplete and in places contradicts documented values. Missing examples include the full type-role scale, `space-0/5/10/20/32/40`, named container set and responsive gutter modes, `radius-xs/xl/2xl/3xl/full`, `shadow-none/xs/sm/md/lg`, emphasized/exit easing, and semantic hover/selected/disabled/loading/error/success/unavailable state tokens. Existing radius values also do not match the documented 8/10/12/16/20/24 px system, the focus offset is 3 px rather than 2 px, and retained `dark:` variants in `components/ui/button.tsx` contradict the required light-only/no-dark-branch inspection.
- Disabling prefetch on every Home link is not justified by the contract. Avoiding speculative fetches to successor routes that intentionally do not exist yet is reasonable, but disabling prefetch on self/Home and locale links is blanket behavior and appears to mask unavailable-target/browser-guard pressure rather than preserve the normal navigation boundary.
- The reported EN/EL LCP values, 2529.7 ms and 2558.0 ms, are both above the unchanged `LCP <= 2.5 s` requirement. A green Unlighthouse score-budget exit does not supersede this separate hard gate.
- Inter correctly requests Greek glyphs and both families disable preload, but Cormorant Garamond is loaded only with `latin`; Greek headings therefore fall through to Georgia. The SPEC allows Greek subsets only where supported, so this is not independently blocking without proof that the installed Next font exposes a Greek subset, but the preload/subset trade-off needs explicit browser evidence in the later visual/performance review rather than a blanket completion claim.

## Blocking Findings

### F-01: Contract-required tests and validation seams are missing or materially weak

The change contract explicitly requires `tests/unit/design/*.test.ts`, controlled invalid content/media fixtures, complete route-helper cases, response-header checks, compact-menu Escape/outside/navigation and focus-return behavior, reduced-motion/focus/current-state checks, and responsive/zoom evidence. No design-token test exists. `showcase-routes.test.ts` checks only Home rather than Paros, Plan My Trip, and confirmation identities. `showcase-content.test.ts` checks only current valid content and two pending fallbacks, not approved records or invalid approved metadata/files. `scripts/validate-content.mjs` does not import/run `showcaseContentSchema`, inspect media IDs/files/approval metadata, enforce recursive EN/GR structure parity, or reject the named invalid cases; it only checks that EN is a non-empty object and compares top-level `home` keys. E2E does not assert the required headers or menu close/focus behaviors. These are acceptance-case test defects, so the required route is `red`.

### F-02: The complete foundational token contract is neither implemented nor testable

`app/globals.css` contains only a subset of the documented reusable inventory and several incompatible values, while `components/ui/button.tsx` retains dark-mode branches. This contradicts FR-016, DEC-011/013, the theme hard wall, and the implementation report's statement that the consumed light-only design foundation is complete. Add the missing red token-contract tests first; then make the CSS implementation satisfy the approved inventory without introducing unused component systems.

### F-03: The rendering path bypasses the approved media-resolution behavior

`HomeSections` always emits a generic `MediaFallback` and never receives or calls `resolveMedia`. Therefore current pending records happen to fail closed, but the controlled-approved acceptance case cannot render an approved localized image with manifest geometry/alt/focal data. Add a failing rendering/boundary test for both pending and approved resolutions before correcting the implementation.

### F-04: Locale navigation no longer uses the approved locale-aware navigation boundary

The contract says to keep `i18n/navigation.ts` / `createNavigation(routing)` as the public locale-aware boundary. The snapshot instead uses raw `next/link` throughout new Home code and changes `quality-lab` from the approved helper to interpolated explicit paths. Existing E2E proves one Home locale click, not adherence to or behavior of the approved boundary. Add focused tests at the locale-aware seam (including both directions and fixed route identities) before restoring compliant navigation. Provider removal is not itself rejected, but it must not be achieved by bypassing the locked navigation interface.

### F-05: The unchanged Home LCP gate is failing

The implementation report records direct-throttled LCP of 2529.7 ms for EN and 2558.0 ms for EL, both greater than the contract's `<= 2.5 s` budget. `throttlingMethod: "devtools"` can be a legitimate correction for the reproduced Windows Lantern defect, but it cannot reinterpret a numeric gate or convert over-budget measurements into PASS. Keep the measurement-method rationale and numeric score budgets explicit, add/retain a gate for the separate LCP threshold, and produce passing evidence.

## Non-Blocking Findings

- `implementation-report.md` is still correctly marked pending review, but its verification narrative is not fully accurate: it calls the over-budget LCP result `PASS`, claims `git diff --check` passes after removal of a trailing blank line while the current command reports `issue.md:25: new blank line at EOF`, and describes the token foundation as complete despite the omissions above. It must be reconciled only after repairs and a later passing review.
- The reported transient accessibility dev-server 404 cascade is not treated as a product failure because the immediate clean rerun passed 12/12; the report states this accurately.
- The current CSP includes `'unsafe-eval'` and broad websocket allowances. These may be needed for Next development, and the contract asks for Next compatibility, so this review does not block on them; production-header tightening can be considered only if it remains proportionate and does not break the approved build/runtime.
- Font preload is disabled for both families. That can reduce unused preload pressure but may delay above-fold text; validate actual EN/GR font requests, fallback behavior, and LCP in the required visual/performance follow-up.

## Verification Considered

- `pnpm validate:content` - `PASS`: exits 0 for current EN/EL files, but the command is too weak to prove the contract's invalid-fixture/media conditions.
- `pnpm test:unit -- tests/unit/content/showcase-content.test.ts tests/unit/routes/showcase-routes.test.ts` - `PASS`: Vitest ran the full five-file suite; 5 files and 6 tests passed. Coverage remains insufficient as described in F-01.
- `git diff --check` - `FAIL`: reports a new blank line at EOF in `issue.md`, contradicting the draft report's claim.
- Reported `pnpm format:check`, `pnpm lint`, `pnpm typecheck`, `pnpm build` - `PASS`: considered as supplied implementation evidence.
- Reported compact exact Playwright run - `PASS`: 9 tests.
- Reported wide exact Playwright run - `PASS`: 9 tests.
- Reported `pnpm test:e2e` - `PASS`: 27 tests across compact, medium, and wide.
- Reported `pnpm test:a11y` - `PASS`: clean 12/12 rerun after one transient dev-server 404 cascade.
- Reported `pnpm quality:unlighthouse` - `FAIL` for the complete contract despite command exit 0: score budgets passed at EN 93/100/100/100 and EL 92/100/100/100 using DevTools throttling, but recorded LCP was 2529.7/2558.0 ms against the unchanged 2500 ms Home gate; CLS was 0 and transfer was approximately 0.70–0.73 MiB.
- Reported `pnpm check:all` - `PASS` as a command exit, but it does not cover the missing contract tests and does not enforce the separate LCP ceiling.
- `features-cli progress --feature greek-essence-showcase --json` - `FAIL` to execute because the installed global CLI points to a missing package source path. Persisted issue state independently shows `in-review`; no lifecycle mutation was attempted.

## Required Route

Reopen at `red`. The primary failure is missing/weak contract coverage at named seams. Add the failing token, content/media, route/navigation, header, interaction, responsive, and performance-gate tests first; then repair the implementation findings under the existing contract and submit a new immutable code-review attempt. Do not mark the issue done. After a future code-review PASS, the feature-local fresh independent visual review is still mandatory before completion.

### 2026-07-24 — review failed → restart at red (tests)
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

### 2026-07-24 — review failed → restart at green (code)
# Visual Review 04: Browse a complete bilingual Home through the shared showcase foundation

Date: 2026-07-24
Reviewer: fresh independent visual-review agent
Issue: `01-browse-bilingual-home`
Verdict: `FAIL`
Route: `implementation repair → fresh code review if source changes → fresh visual review; remain in-review`

## Scope

Reviewed the final rendered production application for issue #01 only. Read root and feature `AGENTS.md`, `NEXT.md`, approved feature `SPEC.md`, `issue.md`, `change-contract.md`, code review `reviews/03-review.md`, `implementation-report.md`, the repository-local `greek-essence-quality-review` and Playwright CLI skills/checklists, and relevant approved Home, responsive, typography, media, motion, and accessibility guidance. Started `pnpm start --hostname 127.0.0.1 --port 4173` from the existing production build, verified `/en` returned HTTP 200, inspected only `/en` and `/el`, and stopped the server after review.

Rendered review covered both locales at exact `390 × 844` and `1440 × 1024`, full-page six-section composition, wide selected/current navigation, compact menu closed/open, locale switching, keyboard-visible focus, Escape/focus return, reduced-motion presentation, pending-media fallback, footer, long Greek wrapping, an `834 × 1112` transition state, and a `195 px` CSS viewport used as the 200%-zoom equivalent. Screenshots contain only public synthetic showcase content.

## Visual Verdict

`FAIL`. The ordinary compact, medium, and wide Home presentation is polished and coherent: all six sections are visible in the intended order; the warm-ivory/deep-Aegean palette, hierarchy, restrained surfaces, editorial spacing, CTA prominence, neutral pending-media fallback, and footer read intentionally; EN/GR content is locale-pure apart from the brand/proper names and language controls; compact and wide focus/current/menu states are clear; and the reviewed production session showed no console errors, warnings, broken assets, or failed critical requests.

However, the required 200%-zoom-equivalent Greek state has real horizontal overflow. At `195 px`, `document.documentElement.scrollWidth` and `document.body.scrollWidth` are `205 px` while `clientWidth` is `195 px`. Long Greek display and card text exposes intrinsic over-width descendants. This violates the explicit no-horizontal-overflow/reflow acceptance boundary and blocks visual approval.

The strict Home LCP `<=2500ms` gate remains technically RED and is carried unchanged as the operator-authorized **nonvisual residual risk** from code review 03. This visual review does not reinterpret it as passing and does not use it to determine the visual verdict.

## Blocking Findings

### VIS-04-01 — Greek 200%-zoom-equivalent state horizontally overflows

- Severity: blocking
- Category: responsive / accessibility / visual reflow
- Route: `/el`
- Viewport/state: `195 × 844` CSS viewport, 200%-zoom equivalent, full page
- Evidence: `evidence/04-visual/el-195x844-zoom200-equivalent-full.png`
- Observed: the page is visually forced into extremely narrow wrapping and exposes a 10 px horizontal overflow (`scrollWidth: 205`, `clientWidth: 195`). DOM inspection identified over-wide descendants in the promise section, How It Works headings/body copy, and trust section; examples included a `155 px`-wide H2 with `185 px` scroll width and `107 px`-wide H3s with up to `130 px` scroll width.
- Expected: all meaningful Greek content, navigation, CTAs, section headings, cards, and footer reflow at 200% zoom without horizontal page scrolling or clipped critical text.
- Required repair: remove the intrinsic text overflow at this supported narrow/reflow state without hiding overflow or truncating content; rerun the 195 px/200% equivalent in both locales, affected responsive/browser/accessibility gates, and obtain the required fresh reviews.

## Non-Blocking Findings

### NVIS-04-01 — Greek display fallback is visibly heavier than English

Greek headings remain readable, correctly accented, and unclipped at 390, 834, and 1440 widths, but the available serif fallback has a materially heavier, less delicate character than the English Cormorant Garamond headings. The presentation remains coherent and acceptable for this pending-media Tier-2 prototype, so this is a polish observation rather than an independent blocker. Evidence: `el-390x844-compact-closed-full.png`, `el-834x1112-medium-transition-full.png`, and `el-1440x1024-wide-current-nav-full.png`.

No other visual defect was found in the required ordinary compact/wide states. Compact visible controls measured at least 44 px high in the initial viewport; focus rings were visible and unclipped; Escape closed the menu, restored focus to the trigger, and set `aria-expanded="false"`; reduced-motion emulation produced `0s` transition/animation durations on the sampled controls; and the pending media presented as a clean, fixed-aspect neutral gradient with no broken-image icon or misleading decorative label.

## Evidence

All paths are relative to `reviews/evidence/04-visual/`.

- `en-390x844-compact-closed-full.png` — full six-section English compact Home and footer.
- `el-390x844-compact-closed-full.png` — full six-section Greek compact Home, long wrapping, fallback, and footer.
- `en-390x844-compact-menu-open.png` — compact English menu open/current state.
- `en-390x844-compact-menu-keyboard-focus.png` — visible keyboard focus in open menu.
- `en-390x844-compact-menu-escape-focus-return.png` — closed menu with visible trigger focus after Escape.
- `el-390x844-reduced-motion-menu-open.png` — localized compact menu under reduced-motion emulation.
- `en-1440x1024-wide-current-nav-full.png` — full English wide Home with selected/current navigation.
- `el-1440x1024-wide-current-nav-full.png` — full Greek wide Home with selected/current navigation.
- `el-1440x1024-wide-current-nav-header.png` — focused evidence of wide Greek navigation.
- `en-1440x1024-wide-keyboard-focus-header.png` — visible wide header keyboard focus and selected Home state.
- `el-834x1112-medium-transition-full.png` — intermediate responsive composition.
- `el-195x844-zoom200-equivalent-full.png` — full Greek 200%-zoom-equivalent state and blocking overflow context.

Every listed principal screenshot was visually inspected, not treated as self-certifying automation evidence.

## Verification Considered

- Production server: `pnpm start --hostname 127.0.0.1 --port 4173` — ready in 155 ms; `/en` returned HTTP 200.
- Playwright CLI only was used for browser interaction, per repository policy.
- Locale switch: `/en` → `/el` and `/el` → `/en` preserved Home route identity and updated document language/title.
- Section count: six rendered `main section` elements at wide inspection.
- Ordinary overflow checks: `390/390` and `1440/1440` scroll/client widths in reviewed states; the `834 × 1112` screenshot was visually inspected for clipping and overflow.
- Blocking reflow check: `/el` at 195 px returned `scrollWidth 205` vs `clientWidth 195`.
- Compact target sampling: visible brand link `139 × 44`, menu `73 × 45.98`, primary CTA `133 × 52.39`, and secondary CTA `241 × 52.39` CSS px.
- Keyboard: focus was visibly outlined; compact Escape returned focus to `Menu` with `aria-expanded="false"`.
- Reduced motion: sampled links/buttons reported `transition-duration: 0s` and `animation-duration: 0s`.
- Console/network: zero console errors or warnings; reviewed static document, CSS, JS, fonts, favicon, and RSC requests returned 200; no broken asset was visible.
- Pending media: visually intentional warm neutral gradient, stable aspect ratio, no broken-image affordance, meaning retained in adjacent text.
- EN/GR parity: complete localized shell and six-section copy; no mixed-language fallback beyond brand/proper names and the deliberate opposite-language control.
- Issue #02 routes were not opened or reviewed.
- Nonvisual residual risk: strict Home LCP `<=2500ms` remains technically failing but operator-authorized for workflow progression, exactly as recorded by code review 03.

## Required Route

Keep issue #01 `in-review`. Route `VIS-04-01` to in-contract implementation repair. Because correcting responsive CSS/source materially changes implementation, run the affected/full verification and obtain a fresh independent code-review attempt before a new immutable fresh visual-review attempt. Do not mark the issue done, do not begin issue #02, and do not treat the operator-authorized LCP exception as a technical performance pass.

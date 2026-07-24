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

# Change Contract — Browse a complete bilingual Home through the shared showcase foundation

Issue: `01-browse-bilingual-home` · Method: `tdd-solo` · Milestone: `explore-bilingual-showcase`

## Goal / postcondition

After this slice, a visitor can browse the exact six-section Greek Essence Home at `/en` or `/el`, use an accessible responsive shared shell, switch to the equivalent localized Home, and follow localized Home calls to action. Editorial content and metadata are complete and locale-pure; provisional unapproved media produces an intentional neutral fallback without losing meaning. The Home consumes the complete documented light-only Tailwind CSS v4 foundation, remains static-first with minimal client JavaScript, and is proven at compact and wide surfaces. Because this is user-visible work, later implementation completion also requires the feature-local fresh visual-review gate for both locales and both required viewport sizes; visual review is not performed by this contract task.

## Traces

FR-001, FR-003, FR-013, FR-015, FR-016; NFR-001, NFR-002, NFR-003, NFR-004, NFR-005, NFR-007, NFR-008; DEC-001, DEC-008, DEC-010, DEC-011, DEC-012, DEC-013, SUBDEC-004.

## Soft scope — edit freely

| Path | Create / edit | Reason & pattern to match |
| --- | --- | --- |
| `package.json` | edit | Add only the dependency/script needed for schema-backed content validation in this slice; preserve the pinned standalone pnpm and existing quality-command contract. |
| `pnpm-lock.yaml` | edit | Lock the corresponding package change through pnpm 11.17.0; do not hand-edit. |
| `app/[locale]/layout.tsx` | edit | Add the approved fonts and shared document/shell semantics while preserving its existing locale validation, `generateStaticParams`, `dynamicParams = false`, provider, and `setRequestLocale` pattern. |
| `app/[locale]/page.tsx` | edit | Replace the fixture Home with the six-section server-rendered composition and localized metadata; preserve the current canonical/hreflang/noindex metadata shape and `setRequestLocale` pattern. |
| `app/globals.css` | edit | Replace the bootstrap grayscale theme with the complete documented reusable Tailwind CSS v4 `@theme`/semantic foundation and consumed Home states; retain one CSS source of truth and light-only behavior. |
| `next.config.ts` | edit | Add the SPEC-required CSP, `nosniff`, referrer, permissions, and frame-denial response headers while preserving `allowedDevOrigins` and the next-intl wrapper. |
| `i18n/navigation.ts` | edit if needed | Keep `createNavigation(routing)` as the locale-aware public navigation boundary; only extend it if the fixed Home route helper genuinely requires it. |
| `messages/en.json` | edit | Add complete English shared-shell/navigation/state labels while retaining fixture keys still consumed by `quality-lab`. |
| `messages/el.json` | edit | Add the identical message-key structure with natural Greek labels and no mixed-language fallback. |
| `content/en/showcase.json` | create | Add English Home editorial data matching the SPEC `ShowcaseContent` structure; directory `content/` exists and content must reference stable media IDs rather than physical paths. |
| `content/el/showcase.json` | create | Add structurally equivalent natural Greek Home editorial data with comparable hierarchy and depth. |
| `content/schemas/showcase.ts` | create | Define the strict showcase content contract; mirror the repository's strict TypeScript and JSON-import patterns. |
| `content/shared/media.json` | reuse; edit only if explicitly approved | Existing stable media-ID and approval source. QUE-003 defaults to fallback; this contract does not authorize promoting or inventing approval metadata. |
| `lib/content.ts` | create | Provide the sole typed content-loading and media-resolution boundary described by the SPEC; `lib/` exists and already holds shared utilities. |
| `lib/routes.ts` | create | Centralize fixed Home/destination/form route identities and localized href generation so metadata and navigation do not duplicate raw replacements. |
| `scripts/validate-content.mjs` | create | Add the build/CLI content validation entry point beside the existing asset-prompt validator pattern in `scripts/validate-prototype-asset-prompts.mjs`. |
| `components/layout/site-header.tsx` | create | Shared wide/compact shell header using locale-aware navigation and the SPEC's accessible compact-menu behavior; `components/` exists. |
| `components/layout/site-footer.tsx` | create | Bounded prototype footer without invented contact/legal destinations. |
| `components/layout/language-switcher.tsx` | create | Public route-identity-preserving locale switch; use helpers from `i18n/navigation.ts`, never string replacement. |
| `components/sections/*.tsx` | create | Add only Home-consumed hero, promise/editorial, Paros feature, three-step, trust/story, and final-CTA section primitives; no wider-product component library. |
| `tests/unit/content/*.test.ts` | create | Test public schema/loader/media-resolution outcomes with EN/GR and invalid fixtures; follow existing Vitest alias/import conventions. |
| `tests/unit/routes/*.test.ts` | create | Test fixed localized href outputs through the public route helper. |
| `tests/unit/design/*.test.ts` | create | Contract-test the documented global token inventory/mappings and absence of dark/parallel TypeScript theme behavior. |
| `tests/unit/messages/parity.test.ts` | edit | Extend the existing recursive key-path parity seam from fixture messages to the shared showcase labels. |
| `tests/e2e/localization-and-quality.spec.ts` | edit | Extend the existing metadata, locale-switch, keyboard, browser-guard, and invalid-locale patterns to the completed Home without removing still-needed quality-lab coverage. |
| `tests/e2e/accessibility.spec.ts` | edit | Add EN/GR Home axe coverage using the existing WCAG 2.2 A/AA and browser-guard pattern. |
| `tests/e2e/browser-guards.ts` | edit only if required | Preserve the existing zero unexpected console/page/request/HTTP failure seam; small targeted adjustments are allowed only for legitimate Home behavior. |
| `playwright.config.ts` | edit only if required | Preserve named compact `390 × 844`, medium `834 × 1112`, and wide `1440 × 1024` projects and retained failure artifacts. |
| `unlighthouse.config.ts` | edit | Keep all score budgets unchanged while retaining Home locale routes in the representative scan set. |

Small neighbouring files under these same Home/content/layout/test concerns may be added without approval when they preserve these patterns and do not introduce a second feature concern.

## Hard walls — STOP if hit

- **Explicit locale-routing interface** — `routing.locales` remains exactly `en`/`el`, locale prefixes remain mandatory, `/` continues to resolve to `/en`, unsupported locales remain 404, and `app/[locale]/layout.tsx` remains statically parameterized with `dynamicParams = false` (DEC-010; SPEC §§4.3, 5.3, 12.5).
- **Static-first boundary** — this issue may not add a Route Handler, Server Action, runtime content API, database, CMS, or other dynamic server boundary; Home/content remain build-time/static and minimal client code is limited to necessary shell interaction (DEC-010; SPEC §§0, 5.1, 10).
- **Stable media-ID and approval boundary** — page content references `content/shared/media.json` IDs, never physical paths; pending records resolve to `fallback`, and rendering an image requires complete localized alt, rights/source approval, focal coordinates, dimensions, and an existing file. QUE-003 is not reopened (FR-013; SPEC §§2.3, 6.3, 7.3).
- **Exact Home composition** — shared header, hero, promise, one Paros-led feature, compact three-step How It Works, one truthful trust/story block, final CTA, and footer are the complete slice. Extra catalogues, broader pages, unsupported claims, booking/pricing/availability/contact/legal destinations, or wider-product components require a new contract (DEC-001; SPEC §§2.5, 5.4, 12.3).
- **Bilingual parity boundary** — every Home section, shell label, CTA, metadata value, interaction, fallback, focus/selected state, and compact-menu state has complete natural EN/GR presentation with canonical values untranslated and no mixed-language fallback (DEC-008/SUBDEC-004; SPEC §§2.1, 7.3).
- **Theme source-of-truth invariant** — the complete documented reusable primitive/semantic color, typography, spacing, container/gutter, responsive, radius, border, surface, shadow, motion/easing, focus, and shared state inventory is centralized through Tailwind CSS v4 CSS-first variables. No dark mode, parallel TypeScript theme object, partial ad-hoc palette, or unused component system (DEC-011/013; FR-016; SPEC §§2.1, 7.1, 13.1).
- **Security/privacy and claims boundary** — no user-derived/raw HTML, PII, credentials, analytics, external tracking, invented business facts, or weakened response headers may enter content, metadata, logs, screenshots, fixtures, or artifacts (NFR-004/005; SPEC §§7.2, 9).
- **Quality budgets and viewport interfaces** — do not lower Playwright dimensions, axe expectations, Unlighthouse scores (performance ≥90, accessibility 100, best practices ≥95, SEO ≥95), or documented Home transfer/image/JS/CSS/LCP/INP/CLS budgets to obtain green checks (DEC-012; SPEC §§3.3, 13–14).
- **Successor-issue surfaces** — do not implement the Paros detail page, Plan My Trip form/draft, submission API/email, or confirmation. Links may point to their fixed public routes, but issue #02 and later milestones own those surfaces (SPEC milestone coverage and §12.3).
- **Feature-local visual-review completion gate** — implementation cannot mark this user-visible issue `done` until normal code review passes and then a fresh independent visual review reports `PASS` for `/en` and `/el` at `390 × 844` and `1440 × 1024`, including the ordinary Home in its live pending-media fallback state, compact/wide header navigation, localized current/selected Home navigation state, locale switch, keyboard focus, and reduced-motion presentation. Evidence must be sanitized and immutable; crossing a contract wall to fix a finding requires escalation (`.scratch/features/001-greek-essence-showcase/AGENTS.md`).

## Seams to test

- **`getShowcaseContent(locale)` and content-validation command** — public build-time content boundary exposes complete typed EN/GR Home data and fails on structural, locale-parity, or media-reference defects.
- **`resolveMedia(id)`** — public media boundary returns either a fully approved localized media record or the intentional pending-approval fallback; components never infer approval themselves.
- **`showcaseRoutes` / `getLocalizedHref(routeId, locale)`** — public route identity boundary returns fixed explicit-locale paths consumed by links and metadata.
- **Rendered Home route (`GET /en`, `GET /el`)** — browser-observable page composition, localized metadata, landmarks/headings, links, locale switching, response headers, static behavior, and browser guards.
- **Global CSS/Tailwind theme contract** — emitted source/styles expose the complete documented light-only semantic foundation and shared focus/motion/state mappings, without a parallel TypeScript theme.
- **User-visible responsive/visual surface** — rendered Home shell, six sections, neutral media fallbacks, locale-specific copy, compact menu, focus, and reduced-motion behavior at required compact/wide viewports; automated checks prepare evidence, while the later mandatory fresh visual reviewer supplies the final visual verdict.
- **Repository quality gates** — public command outcomes preserve formatting, lint, type, content, unit, build, compact/wide Playwright, axe, full E2E, Unlighthouse, and aggregate contracts without reducing thresholds.

## Triangulating acceptance cases

**Seam: `getShowcaseContent(locale)` and content-validation command**

- [ ] Locale `en` → Home data contains exactly hero, promise, Paros feature, three How It Works steps, one trust story, and final CTA with non-empty English prose (FR-001; SPEC §§5.4, 7.3).
- [ ] Locale `el` → identical structural keys and exactly three How It Works steps, with Greek-script prose rather than copied English except brand names (DEC-008; SPEC §7.3).
- [ ] A fixture with an unknown route ID, unknown media ID, empty heading, or EN/GR structure drift → validation exits non-zero instead of falling back or dropping the field (FR-013; SPEC §7.3).
- [ ] Static editorial review of the actual EN/GR Home fixtures → rejects any price, availability/booking guarantee, response-time promise, award, partner, review, or credential claim; automated validation remains limited to deterministic structural/allow-listable rules (SPEC §7.3).

**Seam: `resolveMedia(id)`**

- [ ] `home-aegean-human-arrival-01` with the live manifest defaults still pending and localized alt/focal data null → `{ kind: "fallback", id: "home-aegean-human-arrival-01", reason: "pending-approval" }` (QUE-003; live `content/shared/media.json`).
- [ ] `destination-paros-antiparos-primary-01` under the same pending defaults → the same fallback shape with that distinct ID, proving the result is not hardcoded to the hero (live manifest; SPEC §7.3).
- [ ] A controlled approved record with valid file, dimensions, EN/GR alt, approved rights/source, and `xPercent`/`yPercent` within 0–100 → `kind: "approved"` with the requested locale's alt and manifest geometry (SPEC §7.3).
- [ ] A record marked approved but missing a file, localized alt, approval metadata, dimensions, or valid focal coordinates → content validation fails; it is never rendered as approved (FR-013; SPEC §7.3).

**Seam: `showcaseRoutes` / `getLocalizedHref(routeId, locale)`**

- [ ] `home` + `en` → `/en`; `home` + `el` → `/el` (ASM-001; SPEC §5.3).
- [ ] `paros` + `en` → `/en/destinations/paros-antiparos`; `paros` + `el` → `/el/destinations/paros-antiparos` (ASM-001; SPEC §5.3).
- [ ] `plan-my-trip` + `en` → `/en/plan-my-trip`; `confirmation` + `el` → `/el/plan-my-trip/confirmation`, proving route identity and locale are independently mapped even though those target pages are successor work (SPEC §5.3).

**Seam: rendered Home route (`GET /en`, `GET /el`)**

- [ ] `/en` → `<html lang="en">`, exact six Home sections in DEC-001 order, English shell/content/CTAs, Home canonical `/en`, alternates `en=/en`, `el=/el`, `x-default=/en`, and `noindex,nofollow` (FR-001/015; SPEC §§3.2, 5.4).
- [ ] `/el` → `<html lang="el">`, the same section hierarchy with natural Greek shell/content/CTAs, canonical `/el`, and the same route-pair alternates without English fallback (DEC-008; FR-015).
- [ ] Activate the Home language control from `/en` → `/el`; activate it from `/el` → `/en`, preserving Home identity through `next-intl` navigation rather than string replacement (FR-003; existing `i18n/navigation.ts`).
- [ ] `/` → `/en`, while `/invalid` → 404 and both explicit locale pages remain statically generated (DEC-010; existing routing tests/patterns).
- [ ] EN and EL Home responses → CSP compatible with Next/font/local images plus `X-Content-Type-Options: nosniff`, `Referrer-Policy: strict-origin-when-cross-origin`, `Permissions-Policy: camera=(), microphone=(), geolocation=()`, and `X-Frame-Options: DENY`; page has no unexpected console/page/critical-request/HTTP failure (NFR-005; SPEC §12.2; browser guards).

**Seam: global CSS/Tailwind theme contract**

- [ ] Token inventory inspection → every documented reusable color, type role, spacing, container/gutter, responsive mode, radius, border, surface, shadow, motion/easing, focus, and shared interaction/status token is mapped through CSS/Tailwind v4, including fixed Home-critical colors `#FAF6ED`, `#FFFCF6`, `#F1EDE3`, `#E6DFD2`, `#17475F`, `#103348`, `#0B2433`, `#34767A`, `#275F63`, `#172126`, `#59666B`, `#A13B39`, `#F7E3E1`, `#2F6B4F`, `#E1EFE7`, and `#FFFFFF` (FR-016; SPEC §7.1; `docs/04_design`).
- [ ] Repository scan → no dark theme selector/token branch and no TypeScript theme object; semantic CSS remains the single source of truth (DEC-013; SPEC §§2.1, 7.1).
- [ ] Keyboard focus on header links, locale control, and CTAs → a visible 2 px focus treatment with at least 3:1 boundary contrast; selected/current states do not rely on color alone (NFR-002; SPEC §§3.3, 7.1).
- [ ] `prefers-reduced-motion: reduce` → optional motion is removed or reduced and no content/action is delayed; normal mode remains brief and restrained (SPEC §§7.1, 13.3).

**Seam: user-visible responsive/visual surface**

- [ ] `/en` and `/el` at `390 × 844` → one-column Home, operable compact menu, all six sections and neutral fallbacks readable with no clipping/horizontal overflow; Greek maintains comparable hierarchy (NFR-001/007; feature visual gate).
- [ ] `/en` and `/el` at `1440 × 1024` → wide shared navigation and selective multi-column Home composition retain hierarchy, spacing, fallback aspect ratios, and localized CTA prominence (DEC-011/012; feature visual gate).
- [ ] Compact menu open/close, keyboard focus, locale switch, and current/selected Home navigation state in both locales → visible, localized interaction states that do not rely on color alone; Escape/outside/navigation close behavior returns focus appropriately and produces no console or critical request failure (SPEC §7.1; feature visual gate).
- [ ] Pending hero/Paros media plus reduced-motion mode at both widths/locales → intentional limestone fallback carries no broken-image icon/decorative text, adjacent copy preserves all meaning, and no animation delays content/actions (QUE-003; SPEC §§7.1, 7.3).
- [ ] After implementation and code review, a fresh independent visual reviewer inspects the final screenshots/application—including sanitized compact/wide evidence of the localized current/selected Home navigation state—and records immutable `reviews/<NN>-visual-review.md` with `PASS`; automated screenshots alone do not satisfy completion (feature `AGENTS.md`).

**Seam: repository quality gates**

- [ ] Focused unit/content/message/token tests and `pnpm validate:content` → exit 0 for valid EN/GR content and fail controlled invalid fixtures (FR-013/016; SPEC §§13.1, 14).
- [ ] Compact and wide Home Playwright/axe runs → both locales pass browser guards, metadata, locale switch, keyboard/focus, no-overflow, and zero selected WCAG A/AA violations at `390 × 844` and `1440 × 1024` (DEC-012; SPEC §§13.2–14).
- [ ] The full suite retains the `834 × 1112` regression project, and manual or automated Home spot checks cover 320 px, an intermediate/landscape width, and 200% zoom in both locales where copy expansion affects layout → no clipping or horizontal overflow (issue acceptance; NFR-001; SPEC §§3.3, 13.2–13.3).
- [ ] `pnpm build` → exit 0 with Home routes static and no new server-dynamic boundary (DEC-010; SPEC §14).
- [ ] `pnpm quality:unlighthouse` → exit 0 with performance ≥90, accessibility 100, best practices ≥95, SEO ≥95; Home also respects LCP ≤2.5 s, INP ≤200 ms, CLS ≤0.1, critical-route JS ≤150 KiB gzip, critical CSS ≤40 KiB gzip, cold mobile transfer ≤1.8 MiB, and hero image normally ≤400 KiB (NFR-003; SPEC §§3.3, 13.4).
- [ ] Full exact validation sequence in SPEC §14, ending with `pnpm check:all` → every applicable command exits 0 without lowering or bypassing a gate.

## Method / risk

`tdd-solo` — the public seams are clear, but bilingual parity, complete token coverage, fail-closed media approval, metadata/headers, and responsive accessibility can regress silently; one implementer must carry each seam through an explicit red→green→refactor loop.

## Escalation — what forces a ScopeExpansionRequest

- A correct solution requires implementing or editing a feature concern outside the Home/content/layout/theme/test soft scope, including the Paros page, form/draft, API/email, confirmation, deployment, credentials, or remote Git state.
- A required change would cross any hard wall: explicit locale/static routing, stable media IDs/approval, exact six-section scope, bilingual parity, CSS-only light theme source of truth, privacy/security/claims, quality thresholds, successor-issue ownership, or the mandatory visual-review gate.
- The implementation needs an architectural change not anticipated here, such as runtime content fetching, a CMS/database, a generalized page builder/component system, dark mode, or a parallel theme representation.
- A red test or later code/visual review implies behavior that differs from the issue or approved SPEC, including a missing locale/state/surface or a visual fix that requires crossing a wall.
- Completing required sanitized compact/wide EN/GR visual evidence is impossible inside the accepted user-visible surfaces and states.

Small in-scope neighbour additions under the same Home/content/layout/theme/testing concerns do **not** need a request.

## ScopeExpansionRequest (fill only if a hard wall is hit)

- **What was discovered:** <the file/interface/invariant the plan didn't anticipate>
- **Why the current contract is insufficient:** <what can't be done inside it>
- **Proposed change:** <files to add to soft scope, or wall to renegotiate>
- **Risk if ignored:** <low | medium | high>

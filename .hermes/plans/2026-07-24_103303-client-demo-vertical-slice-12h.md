# Greek Essence 12-Hour Client-Demo Vertical Slice Implementation Plan

> **For Hermes:** Implement only after explicit operator approval. Use bounded staged delivery with Sol as integrator, Luna for implementation stages, and Terra for independent acceptance review. Stop when the acceptance gates pass.

**Goal:** Deliver a polished bilingual meeting artifact that tells one coherent story—**inspiration → destination expertise → conversion**—through Home, Paros & Antiparos detail, a four-step local-only Plan My Trip flow, and an honest confirmation.

**Architecture:** Extend the existing static-first Next.js 16 App Router scaffold. Editorial facts live in locale JSON under `content/`; small interface strings remain in `messages/`; typed Server Components render pages; only the form state, compact navigation, and language-safe local draft behavior use Client Components. No API route, email, database, CMS, CRM, analytics, booking, or production infrastructure is introduced.

**Tech stack:** Next.js 16.2.6, React 19.2.4, TypeScript 6 strict, next-intl 4.13.3, Tailwind CSS 4, Base UI/shadcn primitives, Vitest, Playwright, axe, Unlighthouse, standalone pnpm 11.17.0.

**Implementation depth:** Tier 2 — Prototype.

**Hard ceiling:** 12:00 elapsed working time, including review, fixes, optional preview deployment, and rehearsal. The reviewed plan reserves 1:45 of explicit contingency; feature packages may not consume it by default.

---

## 1. Live baseline and authority resolution

### Verified repository state (2026-07-24)

- Branch: `main`.
- `HEAD`: `f768007302c740275afb57c994cf68e34ed71df5`.
- `origin/main`: `f768007302c740275afb57c994cf68e34ed71df5`.
- Worktree: only an intentional unstaged `NEXT.md` promotion diff; preserve it and never stage it with implementation work.
- Application: bilingual fixture routes only (`app/[locale]/page.tsx`, `app/[locale]/quality-lab/page.tsx`); no product routes.
- Product components/content: no product section/layout/form directories; only fixture toggles and `components/ui/button.tsx`.
- Tests: bootstrap localization, responsive, accessibility, and primitive tests only.
- Deployment: no tracked `vercel.json`; preview deployment can use Vercel’s repository defaults only after operator authorization.
- Tooling mismatch to close during implementation: `AGENTS.md` and Technical Design require `pnpm validate:content`, but `package.json` currently has no `validate:content` script and no general product-content schema dependency. The implementation must add the smallest deterministic product-content validation path; it must not claim the gate already exists.
- Quality budgets in `unlighthouse.config.ts`: performance 90, accessibility 100, best practices 95, SEO 95. Never lower them.

### Authority decisions for this bounded slice

1. Direct operator instruction overrides lower-level prototype breadth for this session: only the named routes/components are planned.
2. PRD content outcomes remain mandatory, but representative modules may contain fewer cards/items than the eventual complete site.
3. The local-only demo form intentionally does **not** satisfy Technical Design’s production-like email/Route Handler DoD. Its success screen must say no request was transmitted. This is an explicit slice limitation, not a false production success.
4. Unknown response time, price/budget ranges, partners, awards, team identities, property relationships, services, legal status, and operational commitments are omitted—not invented.
5. The `NEXT.md` diff and `TODO.md` Unlighthouse stability item remain untouched.

---

## 2. Asset readiness gate

### Pre-clock prerequisite (currently unsatisfied)

The operator must supply/freeze approved Home and Paros hero imagery plus the representative EN/EL copy set **before the 12-hour implementation clock starts**. This is an external dependency, not work that can be recovered through coding speed. The clocked implementation begins with a **fail-closed 30-minute re-verification/scope gate**. Final imagery is an assumed implementation input, but the live inspection currently proves only the following set exists:

| Asset ID                              | Live path                                                                                                          | Dimensions / orientation | Format / size    | Prompt mapping and crop                                                          | Current approval/licensing evidence                                                              |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------ | ---------------- | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| `home-aegean-human-arrival-01` master | `C:\Users\jimzord12\Downloads\home-aegean-human-arrival-01-image-set\home-aegean-human-arrival-01-master-16x9.png` | 2560×1440, landscape     | PNG, 4,557,998 B | Exact ID; 16:9 master; left DOM-copy safe zone and center-right subject required | File exists, but repository record still says unlicensed planning-only / pending visual feedback |
| same, medium crop                     | `...\home-aegean-human-arrival-01-3x2.jpg`                                                                         | 2160×1440, landscape     | JPEG, 671,839 B  | Exact ID; 3:2 derivative                                                         | Same unresolved approval/licensing state                                                         |
| same, compact crop                    | `...\home-aegean-human-arrival-01-4x5.jpg`                                                                         | 1152×1440, portrait      | JPEG, 402,197 B  | Exact ID; 4:5 derivative                                                         | Same unresolved approval/licensing state                                                         |

No final Home destination cards, Paros detail/editorial/gallery images, experience cards, or journey imagery were found in the repository, Desktop, Documents, Downloads, or Pictures using their expected asset IDs. Bootstrap screenshots under `.artifacts/` are test evidence, not product imagery.

### Required asset intake before coding

For every selected file, record in an implementation checklist (not authoritative docs): absolute source path, byte size, width/height, orientation, format, prompt asset ID, intended route/section, focal point, required crops, alt-text facts, creator/source, release requirement, web/prototype/derivative rights, and operator approval state.

**Preferred image set (7 masters, derivatives where specified):**

1. `home-aegean-human-arrival-01` (existing 16:9 + 3:2 + 4:5).
2. `destination-paros-antiparos-primary-01` (Home card + detail hero; 4:3 master and approved 16:9/3:2/4:5/3:4 crops).
3. Two of Athens/Mykonos/Santorini destination-primary assets for secondary Home cards (4:3).
4. `paros-antiparos-editorial-culture-food-01` (4:5 plus approved crop).
5. One of `paros-antiparos-editorial-hospitality-01` or `paros-antiparos-editorial-local-moment-01`.
6. One approved experience image.
7. One approved journey image whose route/copy is verified and explicitly described as customizable inspiration.

**Reviewed default for the 12-hour build:** keep the Home hero and Paros hero; show four priority destinations but allow only Paros and one secondary card to be image-led; use one Paros rich-story image and omit the gallery; render three experience themes as concise text-led cards; use one text-led customizable journey card. The preferred seven-master treatment is an upgrade only if every asset is already approved and the implementation is at least 45 minutes ahead at the 04:00 checkpoint. Never substitute unrelated stock or test screenshots.

**Stop condition:** if the prerequisite is not met before the scheduled implementation day, declare `ASSET-BLOCKED` and do not start the 12-hour clock. If re-verification fails by minute 30, stop implementation; do not spend the day building around placeholders.

---

## 3. Demonstrated routes and narrative

| Story beat            | English route                                                                                  | Greek route             | Meeting purpose                                                                                                                  |
| --------------------- | ---------------------------------------------------------------------------------------------- | ----------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Inspiration           | `/en`, `/el`                                                                                   | locale equivalents      | Establish tailored Greece, human/local expertise, calm premium character, and a clear but unforced CTA                           |
| Destination expertise | `/en/destinations/paros-antiparos`, `/el/destinations/paros-antiparos`                         | equivalent page context | Explain character, fit, experiences, local texture, combinations, and planning value without exclusivity claims                  |
| Conversion            | `/en/plan-my-trip?destination=paros-antiparos`, `/el/plan-my-trip?destination=paros-antiparos` | equivalent context      | Demonstrate visible editable prefill, four short steps, validation, persistence, and explicit local-only completion              |
| Confirmation          | `/en/plan-my-trip/confirmation`, `/el/plan-my-trip/confirmation`                               | equivalent context      | Confirm the **demo was completed**, explicitly state nothing was sent, provide correction/restart and inspirational onward paths |

### Exact operator click path (target: 5–6 minutes)

1. Open `/en` at 1440 px. State the proposition from the opening screen; briefly show brand promise.
2. Scroll to featured destinations; open the strategically emphasized Paros & Antiparos card.
3. On destination detail, show traveler fit, one rich local story, combination guidance, and the contextual `Plan My Trip` CTA.
4. Open the prefilled form; point out “Four short steps” and local-demo disclosure.
5. Step 1: retain/edit Paros & Antiparos and flexible dates. Step 2: enter two adults and trip type. Step 3: choose culture/gastronomy and balanced pace. Step 4: use representative fake data and acknowledge demo privacy notice.
6. Submit locally and show confirmation: “Demo completed—no request was sent.” Use “Review or correct details” to prove safe recovery, then return to Home.
7. Switch to Greek on the equivalent route (preferably destination or form) to prove context preservation and responsive Greek layout.
8. Resize/open the prepared 390 px view and show mobile menu, stacked destination narrative, and form progress/error behavior.

### Demo recovery

- Keep a production build running locally on port 3101 and pre-open the same EN/EL routes.
- Keep a static meeting checklist with exact local URLs and representative fake inputs.
- If preview connectivity fails, switch to local build without changing the narrative.
- If the form state is stale, use the visible “Start over / Clear demo” action and replay with prepared inputs.
- If a late image is rejected, use only the approved reduced image set; never show unapproved media as final.

---

## 4. Requirements-to-slice matrix

| Area                 | Mandatory slice behavior                                                                                                                                                                   | Evidence authority                                                                                    | Acceptance proof                                                                                                                                 |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Home                 | Hero; brand promise; four priority destinations represented; experience themes; compact How It Works; one customizable journey example; honest trust/service promise; contextual final CTA | PRD `17_page_inventory_and_product_requirements.md` §17.1; Prototype `07_page_specifications.md` §7.1 | At opening + first section, user identifies Greece, tailored planning, human/local expertise, audience, and CTA; page cannot read as marketplace |
| Paros detail         | Breadcrumb, precise hero/location, intro, why visit, traveler fit, signature experiences, culture/gastronomy, service style, combinations, related journey/experience, contextual CTA      | PRD §17.3; Prototype §7.3                                                                             | Answers why special, who it suits, planning value, combinations; no unsupported access/exclusivity                                               |
| Form                 | Minimal header/escape/language, `Request a Custom Itinerary`, four steps, text progress, Back/Continue, editable context prefill, current-step validation, preserved valid data            | PRD §18; Prototype §§7.13 and 9                                                                       | Keyboard-completable; multiple-error summary; focus goes to summary/invalid field; Back never clears; local demo disclosure persistent           |
| Confirmation         | Unambiguous demo completion, no-transmission disclosure, next step framed as prototype behavior, correction/restart route, onward inspiration                                              | Prototype §§7.14 and 9.11, adjusted by direct local-only instruction                                  | Focus moves to heading; status announced once; no submitted personal payload shown; not a dead end                                               |
| Shared layout        | Header, footer, language switch preserving equivalent context, skip link, one H1, landmarks                                                                                                | Prototype §§4, 8.1, 11                                                                                | Full EN/EL navigation at 1440; fit-based compact menu; 44×44 target goal; 200% zoom works                                                        |
| Bilingual            | Complete editorial and UI copy for every demonstrated route; no mixed-language fallback; locale-aware metadata/hreflang/canonical                                                          | AGENTS; Prototype §§8.1, 11.4                                                                         | Message parity test; direct navigation and switch on each route; Greek labels do not truncate                                                    |
| Responsive           | 390 compact, 834 medium, 1440 wide; inspect 320 and 200% zoom; semantic stack order; no horizontal overflow                                                                                | Prototype §4                                                                                          | Screenshots and manual review at all reference widths; form errors/actions never obscured                                                        |
| Accessibility        | WCAG 2.2 AA interaction target; text-over-image crop contrast; keyboard/focus/error semantics; reduced motion; meaningful alt                                                              | Prototype §§9.12, 11; Design §35                                                                      | axe smoke, full keyboard click path, zoom/reflow, contrast and reduced-motion checks; accessibility score 100                                    |
| Performance          | Static-first; `next/image`; art-directed responsive source sizes; minimal client bundle; final representative media                                                                        | Technical Design §18; current budgets                                                                 | Three clean Unlighthouse runs after a fresh build; every route meets 90/100/95/95; any outlier investigated, not retried away                    |
| Claims/content       | Approved facts only; provisional demo wording explicit; omit unsupported people/partners/awards/pricing/timing/legal/licensing claims                                                      | PRD §§19–20; Design §§4,43                                                                            | Content review checklist records each visible claim and asset status                                                                             |
| Deployment/rehearsal | Authorized Vercel Preview only; representative fake data; local fallback; no production launch/domain/credentials mutation                                                                 | Technical Design §19 narrowed by direct instruction                                                   | Preview smoke checks + local production checks; links recorded; rehearsal completed twice                                                        |

---

## 5. Minimum reusable component set

Create only these slice-owned components:

1. `SiteHeader` — header, compact menu, skip-link integration.
2. `SiteFooter` — reduced truthful navigation; no unapproved contact/legal claims.
3. `LanguageSwitcher` — equivalent locale path; no flags.
4. `Hero` — Home and destination variants only.
5. `SectionHeader`.
6. `DestinationCard` — featured and compact-related variants.
7. `ExperienceCard` — text/image outcome-led variant.
8. `JourneyCard` — one representative customizable route variant.
9. `RichStory`.
10. `HowItWorks` — three-step compact version using provisional, non-committal language.
11. `BrandPromise` — also serves the honest trust/value block; do not build credentials/team components.
12. `PrimaryCta`.
13. `TripRequestForm` plus internal field/progress/error/confirmation-status helpers colocated under `components/forms/trip-request/`.

`Gallery` is removed from the reviewed baseline. A single image inside `RichStory` satisfies the bounded local-story treatment; no gallery, carousel, modal, or viewer is planned.

**Explicitly remove from the likely list:** no separate generic “Trust Credentials” component; no award/logo/team treatment. Trust is represented by approved brand/process copy through `BrandPromise` and `HowItWorks`.

---

## 6. Dependency-ordered 12-hour schedule

All times are hard elapsed ceilings. Sol owns integration/scope; Luna owns bounded implementation stages; Terra performs independent reviews. There is one critical path because the routes share content/layout and form links.

| Clock       |  Duration | Owner            | Work package                                                                                    | Depends on                        | Critical?  |
| ----------- | --------: | ---------------- | ----------------------------------------------------------------------------------------------- | --------------------------------- | ---------- |
| 00:00–00:30 |      0:30 | Sol + operator   | Re-verify pre-frozen scope/assets/copy; branch preflight                                        | pre-clock prerequisite + approval | Yes        |
| 00:30–01:45 |      1:15 | Luna, Sol verify | Tokens/fonts, content validation/loader, shared layout, locale-safe navigation, route skeletons | asset gate                        | Yes        |
| 01:45–03:45 |      2:00 | Luna             | Polished reduced Home baseline                                                                  | foundation                        | Yes        |
| 03:45–05:15 |      1:30 | Luna             | Paros & Antiparos detail + contextual CTA, no gallery                                           | shared components/content         | Yes        |
| 05:15–07:00 |      1:45 | Luna             | Four-step local form + honest guarded confirmation                                              | routes/i18n/content IDs           | Yes        |
| 07:00–07:45 |      0:45 | Luna + Sol       | Greek, responsive, image crop and 200% zoom pass                                                | all pages                         | Yes        |
| 07:45–09:15 |      1:30 | Sol + Terra      | Automated/manual QA and bounded fixes                                                           | integrated slice                  | Yes        |
| 09:15–10:15 |      1:00 | Sol + operator   | Local rehearsal; authorized preview only if green; deployed smoke if available                  | all gates green                   | Yes        |
| 10:15–12:00 |      1:45 | Sol              | Protected contingency for evidence-backed fixes, preview variance, and second rehearsal         | accepted baseline                 | No—reserve |
| **Total**   | **12:00** |                  |                                                                                                 |                                   |            |

The 1:45 contingency begins at 10:15 and may be used only for acceptance defects, performance variance, preview variance, or rehearsal recovery—not new features or richer assets. If a preceding package misses its cutoff, apply the cuts in §9 immediately. The reviewed feasibility verdict is **conditional**: feasible only with the pre-clock prerequisite satisfied and this reduced baseline; not feasible from the current live asset/copy state.

---

## 7. Implementation tasks

### Task 0 — Approval and implementation preflight (00:00–00:30)

**Objective:** Freeze truthful inputs and prevent asset/copy uncertainty from reaching code.

**Files:**

- Do not modify source during the intake.
- Preserve unstaged: `NEXT.md`.
- Later copy approved assets into: `public/images/home/`, `public/images/destinations/paros-antiparos/`, `public/images/experiences/`, `public/images/journeys/`.

**Steps / acceptance:**

1. Re-run `git branch --show-current`, `git rev-parse HEAD`, `git rev-parse origin/main`, `git status --short --branch`, and `git diff -- NEXT.md`.
2. Create an implementation branch only after operator approval; never include `NEXT.md` in staging.
3. Inventory selected assets with dimensions/bytes and inspect each crop visually at 320, 390, 834, and 1440.
4. Require operator status for each: final/approved, provisional demo, or omit. Record rights/release state; “file exists” is not approval.
5. Confirm the pre-frozen EN/EL copy sheet uses only approved or visibly provisional claims; do not author unresolved business copy inside this clock.
6. Confirm the cut level (full preferred or reduced asset fallback).

**Gate:** Home hero + Paros hero approved; exact selected files and copy statuses known; otherwise stop `ASSET-BLOCKED`.

### Task 1 — Foundation, content contract, and shared shell (00:30–01:45)

**Objective:** Establish the smallest typed bilingual foundation and route shell shared by all pages.

**Files:**

- Modify: `package.json`, `pnpm-lock.yaml`, `app/globals.css`, `app/[locale]/layout.tsx`, `messages/en.json`, `messages/el.json`, `unlighthouse.config.ts`.
- Create: `content/schemas/site-content.ts`, `content/shared/media.json`, `content/en/pages/home.json`, `content/el/pages/home.json`, `content/en/destinations/paros-antiparos.json`, `content/el/destinations/paros-antiparos.json`, `lib/content.ts`, `lib/seo.ts`, `scripts/validate-content.mjs`.
- Create: `components/layout/site-header.tsx`, `components/layout/site-footer.tsx`, `components/layout/language-switcher.tsx`, `components/layout/locale-path.ts`.
- Create route shells: `app/[locale]/destinations/paros-antiparos/page.tsx`, `app/[locale]/plan-my-trip/page.tsx`, `app/[locale]/plan-my-trip/confirmation/page.tsx`.
- Tests: `tests/unit/content/content.test.ts`, `tests/unit/i18n/locale-path.test.ts`, update `tests/unit/messages/parity.test.ts`.

**Implementation constraints:**

- Add only the smallest schema dependency justified by the documented content boundary (prefer `zod`); do not add a CMS layer.
- Import Cormorant Garamond and Inter using `next/font` with only needed weights; no remote runtime font dependency.
- Keep shared shell server-rendered; isolate only menu interaction if necessary.
- `messages/` owns interface strings only; editorial copy stays in `content/`.
- Locale switch preserves the exact equivalent route and query context.

**Acceptance:**

- `pnpm validate:content` exists and fails on invalid locale parity/relationships/media IDs.
- Direct route generation succeeds for both locales.
- One H1 remains page-owned; shell has skip link, landmarks, visible focus.
- Unlighthouse include list covers all eight demonstrated route URLs (four per locale).

**Verification:**

```bash
pnpm validate:content
pnpm test:unit -- tests/unit/content/content.test.ts tests/unit/i18n/locale-path.test.ts tests/unit/messages/parity.test.ts
pnpm typecheck
```

### Task 2 — Home narrative (01:45–03:45)

**Objective:** Build the polished inspiration page without expanding into full site breadth.

**Files:**

- Replace: `app/[locale]/page.tsx`.
- Create: `components/sections/hero.tsx`, `section-header.tsx`, `destination-card.tsx`, `experience-card.tsx`, `journey-card.tsx`, `how-it-works.tsx`, `brand-promise.tsx`, `primary-cta.tsx`.
- Modify: Home locale JSON, media manifest, `app/globals.css`.
- Test: `tests/e2e/vertical-slice-home.spec.ts`.

**Exact page order:** global header → cinematic hero → lower-intensity brand promise → featured destinations (Paros emphasized, all four priorities represented) → 3 curated experience themes → compact 3-step How It Works → 1 honest customizable journey → brand/service reassurance (no credentials) → deep-blue final CTA → footer.

**Acceptance:**

- 1440 opening screen communicates Greece, tailored planning, local/human expertise, premium-but-not-status positioning, and `Plan My Trip`.
- 390 and 320 crops preserve focal subject and text contrast; media failure leaves proposition complete.
- Cards are distinguishable by text and never show pricing, availability, booking, ratings, or exclusivity.
- Static Server Components except compact menu behavior.

**Verification:**

```bash
pnpm test:e2e -- tests/e2e/vertical-slice-home.spec.ts --project=chromium-wide --project=chromium-compact
```

### Task 3 — Paros & Antiparos destination expertise (03:45–05:15)

**Objective:** Build one locally grounded, credible destination detail that converts contextual interest.

**Files:**

- Implement: `app/[locale]/destinations/paros-antiparos/page.tsx`.
- Create: `components/layout/breadcrumbs.tsx`, `components/sections/rich-story.tsx`.
- Modify: Paros EN/EL JSON, media manifest, relevant shared cards/styles.
- Test: `tests/e2e/vertical-slice-destination.spec.ts`.

**Exact page order:** breadcrumbs → destination hero/location/contextual CTA → editorial intro → why visit + traveler fit → 3 signature experiences → culture/gastronomy Rich Story → service/accommodation style without listings → 2 destination-combination cues → 1 related customizable journey + 1 related experience → contextual CTA → footer.

**Acceptance:**

- Copy differentiates Paros and Antiparos without blending geography or naming an unverified village, venue, property, maker, partner, inclusion, or access.
- One approved Rich Story image carries local texture; no gallery/carousel/modal JS.
- CTA links to locale form with visible editable `destination=paros-antiparos` context.
- Mobile stacking keeps heading/text/action before supporting media unless media establishes necessary context.

**Verification:**

```bash
pnpm test:e2e -- tests/e2e/vertical-slice-destination.spec.ts --project=chromium-wide --project=chromium-compact
```

### Task 4 — Four-step local Plan My Trip demo (05:15–07:00)

**Objective:** Demonstrate qualification UX and recovery without transmitting data or implying operational receipt.

**Files:**

- Implement: `app/[locale]/plan-my-trip/page.tsx`, `app/[locale]/plan-my-trip/confirmation/page.tsx`.
- Create: `components/forms/trip-request/trip-request-form.tsx`, `trip-progress.tsx`, `error-summary.tsx`, `fields.tsx`, `demo-draft.ts`, `demo-schema.ts`.
- Modify: `messages/en.json`, `messages/el.json`, `app/globals.css`.
- Tests: `tests/unit/forms/demo-schema.test.ts`, `tests/unit/forms/demo-draft.test.ts`, `tests/e2e/vertical-slice-form.spec.ts`.

**Step fields (bounded representative subset):**

1. **Trip basics:** destination or Help me choose; estimated arrival/departure; flexible dates. Require destination intent; validate date order.
2. **Travelers/type:** adults; children count + conditional child ages; trip type; first Greece visit.
3. **Preferences:** interests; pace; optional context/access needs invitation without soliciting unnecessary sensitive data.
4. **Budget/contact:** **do not invent ranges**; use an optional free-text planning-budget context or “Discuss with planner” demo choice, explicit flights clarification, full name, email, country, optional WhatsApp, preferred contact, required demo privacy acknowledgement.

**Local behavior:**

- Persist in `localStorage` under a versioned demo key with a tested 72-hour expiry and visible manual clear action, matching the documented prototype contract. Back/Continue, refresh, and locale switch preserve the draft. Store no more data than the demonstrated fields require.
- Never put personal values in URL/query, logs, screenshots, analytics, or confirmation.
- Final action label: `Complete Demo` / accurate Greek equivalent—not `Send`.
- On complete, set only a non-sensitive session completion flag and navigate to confirmation.
- Confirmation requires the non-sensitive session completion flag. Direct navigation without that flag must show an honest `No demo request has been completed` recovery state or return to the form; it must never fabricate success. A valid confirmation says no request was sent and offers Review/correct, Start over, Paros detail, and Home.
- No `app/api/trip-request/route.ts`, email templates, Resend, CAPTCHA, rate limiter, or provider dependencies.

**Accessibility acceptance:** persistent labels, Optional labels, native semantics, `Step X of 4`, current title, error summary links, focus correction, `aria-describedby`, no color-only status, 44×44 target goal, keyboard and 200% zoom completion, confirmation heading receives focus and status is announced once.

**Verification:**

```bash
pnpm test:unit -- tests/unit/forms/demo-schema.test.ts tests/unit/forms/demo-draft.test.ts
pnpm test:e2e -- tests/e2e/vertical-slice-form.spec.ts --project=chromium-wide --project=chromium-compact
```

### Task 5 — Greek, responsive, media, and metadata pass (07:00–07:45)

**Objective:** Treat Greek and compact layouts as first-class, not post-hoc translations.

**Files:** adjust only files created/modified in Tasks 1–4 plus existing metadata tests; no new features.

**Checks:**

1. Every demonstrated route has complete EN/EL editorial copy and UI strings; a script/test enforces keys and IDs.
2. Language switch preserves Home, Paros, each form step/draft, and confirmation context.
3. Test at 320, 390, 834, 1440 and 200% zoom; no clipped Greek, overflow, obscured sticky controls, or breakpoint-only success.
4. Use `next/image` with accurate `sizes`, priority only for the current LCP hero, explicit dimensions/aspect ratio, and art-directed crops where approved.
5. One logical H1, canonical, EN/EL hreflang, localized title/description, and prototype noindex behavior remains deliberate.
6. Reduced motion removes non-essential transitions.

**Gate at 07:45:** no more content modules or visual features after this point.

### Task 6 — QA, independent review, and bounded fixes (07:45–09:15)

**Objective:** Prove the coherent slice and fix only acceptance failures.

**Files:** focused test/config/source corrections only; no refactors unrelated to failures.

**Automated order:**

```bash
pnpm format:check
pnpm lint --max-warnings=0
pnpm typecheck
pnpm validate:content
pnpm test:unit
pnpm build
pnpm test:e2e
pnpm test:a11y
pnpm quality:unlighthouse
```

**Manual checks:**

- Full EN click path and Greek equivalent; direct-load every route.
- Keyboard-only navigation/form; focus visibility/order; compact menu; error summary; confirmation focus.
- 320 width, 390/834/1440 frames, 200% zoom, reduced motion, image unavailable behavior.
- Browser console and network: zero console errors and no failed critical requests.
- Claims/assets ledger: each visible claim and image approved/provisional; no personal data in artifacts.
- Contrast across every hero crop and form state.

**Performance stability protocol:**

1. Fresh `pnpm build`.
2. Run Unlighthouse three clean times against the same build, preserving reports.
3. Every included route must satisfy performance ≥90, accessibility 100, best practices ≥95, SEO ≥95 on all three runs.
4. Any sub-budget result is a failure requiring route/audit diagnosis (LCP image, font, JS, CLS, request timing). Do not lower budgets or treat an immediate retry as resolution.

**Independent Terra acceptance review:** verify authority alignment, exclusions, EN/EL parity, narrative, accessibility, client-only JS boundaries, route/content truthfulness, asset rights labels, and 12-hour scope. Sol fixes only supported P0/P1 acceptance findings within the QA box.

### Task 7 — Local-first rehearsal and optional authorized preview (09:15–10:15, then contingency if needed)

**Objective:** Produce a dependable meeting path with local recovery.

**Prerequisite:** explicit operator authorization to push/open PR/deploy; credentials are operator-controlled. Planning approval alone does not authorize deployment.

**Steps:**

1. Run local production build at port 3101 and smoke all eight URLs.
2. Commit implementation on its approved feature branch without `NEXT.md`; push/open PR under the normal workflow.
3. Use Vercel Preview only if all local acceptance gates are green by 09:15 and operator authorization/credentials already exist. Preview is optional; no custom domain, production launch, DNS, environment-secret, or email configuration.
4. If preview exists, smoke it at 1440 and 390 for EN Home → Paros → form → confirmation; switch Greek on Paros and form; inspect console/network.
5. Rehearse twice locally; if preview exists, replace the first local rehearsal with preview. Target 5–6 minutes and use representative fake data.
6. Record any preview URL, local commands, exact demo URLs, cut level, known prototype limitations, and recovery sequence in the PR/implementation report—not authoritative product docs.

**Acceptance:** operator can complete the narrative without improvisation; local fallback is pre-opened; no request is transmitted; preview and local behavior match.

---

## 8. Desktop and mobile acceptance criteria

### Wide (1440×1024)

- Header shows fit-tested full navigation, language access, and one primary CTA without compression.
- Home hero uses approved wide crop; copy block stays in safe area and passes contrast.
- Destination collections use up to 3–4 columns but preserve Paros emphasis and readable card measure.
- Paros alternating editorial layouts remain semantically ordered.
- Form stays within 720–880 px, with stable progress/title and consistent Back/Continue hierarchy.

### Medium (834×1112)

- Navigation condenses based on fit; no Greek truncation.
- Cards reflow to two columns where useful; editorial split remains balanced or stacks early.
- No assumptions that 834 behaves like reduced desktop.

### Compact (390×844; also inspect 320)

- One-column priority; menu has labeled control, focus containment/return, Escape close, and 44×44 target goal.
- Hero uses approved portrait crop; actions stack primary first.
- How It Works and route combinations are ordered vertical text sequences.
- Form count/title take priority over all step labels; actions never cover content/errors/system UI.
- No horizontal viewport scroll at 320 or 200% zoom.

---

## 9. Time-triggered cuts and stopping rules

Cuts preserve the core story, bilingual behavior, accessibility, and budgets.

| Trigger                               | Mandatory cut                                                                                 |       Time recovered | Never cut                                                          |
| ------------------------------------- | --------------------------------------------------------------------------------------------- | -------------------: | ------------------------------------------------------------------ |
| Pre-clock prerequisite absent         | Do not start the implementation day                                                           |   prevents sunk cost | approved Home + Paros heroes and frozen EN/EL copy                 |
| Re-verification not complete by 00:30 | Stop if either core hero/copy set fails; do not source assets inside build window             |   prevents sunk cost | core input approval                                                |
| Foundation not green by 01:45         | Drop decorative motif and transparent-to-solid header transition; use solid responsive header |            20–30 min | locale routing/content validation                                  |
| Home not accepted by 03:45            | Reduce experience cards 3→2; keep one text journey; remove all reveal transitions             |            20–30 min | hero, promise, all priority destinations represented, process, CTA |
| Paros not accepted by 05:15           | Combinations become text links; related module 2→1                                            |            15–20 min | traveler fit, local story, contextual CTA                          |
| Form Step 3 not working by 06:15      | Remove optional context textarea; use native controls only                                    |            15–20 min | four steps, validation, 72-hour draft, confirmation truth          |
| Integrated slice not ready by 07:00   | Freeze visual work; remove optional motion and secondary card imagery                         |            30–45 min | Greek/responsive/a11y QA reserve                                   |
| Quality gates not green by 09:15      | Skip preview; spend contingency on acceptance defects and rehearse local only                 |           up to 1:45 | no budget reduction or false pass                                  |
| Preview unavailable by 09:50          | Stop deployment troubleshooting; use local production fallback                                | 25 min + contingency | rehearsal and recovery path                                        |

**Stop-at-acceptance rule:** once routes, narrative, EN/EL, responsive/accessibility checks, quality budgets, and rehearsal pass, stop. Do not polish other pages, quality-lab visuals, tooling history, K-002, legal, or production gaps.

---

## 10. Files likely to change during approved implementation

**Modify:**

- `package.json`, `pnpm-lock.yaml`
- `app/[locale]/layout.tsx`, `app/[locale]/page.tsx`, `app/globals.css`
- `messages/en.json`, `messages/el.json`
- `unlighthouse.config.ts`
- focused existing tests/config only where route expectations legitimately change

**Create:**

- `app/[locale]/destinations/paros-antiparos/page.tsx`
- `app/[locale]/plan-my-trip/page.tsx`
- `app/[locale]/plan-my-trip/confirmation/page.tsx`
- `components/layout/{site-header,site-footer,language-switcher,locale-path,breadcrumbs}.tsx` (use `.ts` for non-React `locale-path`)
- `components/sections/{hero,section-header,destination-card,experience-card,journey-card,rich-story,how-it-works,brand-promise,primary-cta}.tsx`
- `components/forms/trip-request/{trip-request-form,trip-progress,error-summary,fields}.tsx`
- `components/forms/trip-request/{demo-draft,demo-schema}.ts`
- `content/schemas/site-content.ts`, `content/shared/media.json`
- `content/{en,el}/pages/home.json`
- `content/{en,el}/destinations/paros-antiparos.json`
- `lib/content.ts`, `lib/seo.ts`, `scripts/validate-content.mjs`
- approved media under `public/images/...`
- `tests/unit/content/content.test.ts`, `tests/unit/i18n/locale-path.test.ts`, `tests/unit/forms/{demo-schema,demo-draft}.test.ts`
- `tests/e2e/{vertical-slice-home,vertical-slice-destination,vertical-slice-form}.spec.ts`

**Do not create:** API route, email templates, provider integration, analytics, CMS/database/CRM, filters, hero video, gallery modal, legal pages, all destination/index routes, or generalized 30-component system.

---

## 11. Risks, tradeoffs, and approval decisions

1. **Asset blocker (current):** only the Home hero set is live and even it remains unlicensed/pending in the repository record. Implementation is conditional on operator-approved Home + Paros heroes; the preferred seven-master set is not currently verified.
2. **Content validator gap:** the handoff calls the content gate operational, but live `package.json` does not expose `validate:content`. The plan includes the smallest honest repair.
3. **Form DoD conflict:** repository Technical Design expects live controlled email, but direct scope explicitly excludes it. The slice must be described as a local interaction demo, with no receipt claim.
4. **Trust content:** Home requirements ask for trust/hospitality evidence, while live approval is unresolved. Use approved process/value wording only; omit credentials, team, partner marks, awards, reviews, and operational timing.
5. **Twelve-hour realism and independent review:** Terra’s first verdict was **not feasible as written** because the current core-asset gate fails, the first schedule had zero contingency, and implementation packages were underestimated. After correction, feasibility is **conditional** on approved Home/Paros heroes and frozen EN/EL copy before the clock, the reduced no-gallery baseline, optional preview, strict cutoffs, native controls, and a protected 1:45 contingency after 10:15. If those conditions are not met, do not start.

## Operator approval gate

Approve one of the following before implementation:

1. **Recommended — approve the plan conditionally:** implementation may start only after the 45-minute gate verifies approved Home and Paros heroes plus truthful copy; use the preferred set if all assets are available and the documented cuts otherwise.
2. Approve only after all seven preferred masters and their rights/status are supplied.
3. Request plan revisions; do not implement.

No branch, code, test, content, asset, configuration, commit, push, PR, or deployment work is authorized by this plan alone.

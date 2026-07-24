---
spec_id: greek-essence-showcase-SPEC-001
title: Greek Essence Bilingual Client Showcase
status: approved
revision: 1.1.0
created_at: 2026-07-24
updated_at: 2026-07-24T10:59:39Z
repo: C:/Users/jimzord12/Documents/GitHub/greek-essence
base_branch: main
implementation_depth: 2
source_inputs:
  - .scratch/features/001-greek-essence-showcase/PRD.md
  - .scratch/features/001-greek-essence-showcase/DECISIONS.md
  - .scratch/features/001-greek-essence-showcase/GRILL_SESSION.md
  - .scratch/features/001-greek-essence-showcase/GLOSSARY.md
  - .scratch/features/001-greek-essence-showcase/contracts/*.md
  - AGENTS.md
  - repository prototype, technical, and design documentation
  - live codebase reconnaissance at f768007302c740275afb57c994cf68e34ed71df5
output_path: .scratch/features/001-greek-essence-showcase/SPEC.md
intended_implementer: fresh AI implementation agent with repository access but no chat history
---

# Greek Essence Bilingual Client Showcase Implementation SPEC

## 0. How to Use This SPEC

This SPEC is the complete implementation contract for the bounded Greek Essence client showcase. The implementation agent must:

1. Read this file fully before coding. Also obey repository-root `AGENTS.md` for repository operating safety; it does not add feature behavior beyond the architecture, scope, and gates reproduced here.
2. Preserve unrelated working-tree changes and treat the decision ledger as non-negotiable.
3. Implement only the English/Greek Home, Paros & Antiparos, Plan My Trip, confirmation, and submission surfaces described here.
4. Keep the build static-first; `POST /api/trip-request` is the only dynamic server boundary.
5. Prefer the smallest maintainable solution that fits the strict 12-hour Tier-2 implementation target.
6. Run the exact validation commands in §14 and stop when all acceptance criteria pass.
7. Ask for human input only for runtime email values or asset approval; neither permits broadening the feature.

Source files named in this SPEC provide provenance, not missing implementation instructions. All feature behavior needed to implement the showcase is stated here. If a source file later changes and contradicts this approved SPEC, stop and reconcile the authority conflict rather than silently changing scope. In particular, this feature has no budget, residence, first-visit, accommodation-preference, marketing-consent, or visible saved-draft messaging; agency-notification acceptance, not acknowledgement acceptance, is the successful-submission boundary.

## 1. Executive Summary

### Goal

Deliver a polished bilingual demonstration of inspiration → destination expertise → conversion: a visitor can move from Home to a Paros & Antiparos editorial page, open a four-step Plan My Trip request with editable destination context, retain progress across refresh and language switching, submit through Resend, and reach an honest confirmation state.

### Outcome

The application exposes four equivalent route types in English and Greek, works at 390 × 844 and 1440 × 1024, uses the approved warm-ivory/deep-Aegean/muted-teal visual direction, persists one canonical browser draft for 72 hours, sends a structured agency email with a UTF-8 JSON attachment, attempts a localized visitor acknowledgement, and preserves recoverability without claiming booking, price, availability, or response-time commitments.

### Scope Classification

- Feature type: new vertical-slice feature
- Engineering depth: Tier 2 — Prototype
- Primary surfaces: static Next.js pages, one client form island, one Route Handler, local JSON content, transactional email templates, focused tests
- Risk level: medium because the form handles PII and external email, but there is no database, account, payment, booking, or production operations
- Timebox: strict 12 implementation hours after approved runtime credentials are available

This is one coherent vertical slice. Splitting page, form, and email behavior into separate SPECs would weaken the end-to-end demonstration and add coordination overhead.

## 2. Decision Ledger

### 2.1 Locked Decisions

| ID | Source | Source ID | Decision | Implementation impact |
|---|---|---|---|---|
| DEC-001 | `DECISIONS.md` | D-001 | Home uses hero, promise, Paros-led destination module, compact How It Works, one trust/story block, and final CTA. | Do not import the broader Home hierarchy or extra catalogues. |
| DEC-002 | `DECISIONS.md` | D-001 | Paros & Antiparos uses hero, editorial character, traveler fit, signature experiences with culture/gastronomy, one combinations block, and final CTA. | No separate accommodation or sample-journey section. |
| DEC-003 | `DECISIONS.md` | D-002 | The form has exactly four steps: Trip, Travelers, Preferences, Contact. | Field grouping and progression are fixed. |
| DEC-004 | `DECISIONS.md` | D-003 | One canonical draft is shared by English and Greek, saved after 1000 ms and on blur, expires 72 hours after meaningful update, and is silent. | Use one locale-neutral storage key; no save/restore/expiry UI. |
| DEC-005 | `DECISIONS.md` | D-003 | Start Over requires confirmation; failures preserve the draft; only confirmed Start Over or accepted submission clears it. | Reset and submission state transitions are fixed. |
| DEC-006 | `DECISIONS.md` | D-004 | Agency notification includes every accepted field, grouped HTML, and a UTF-8 JSON attachment. | Server mapping and email tests must prove exact field parity. |
| DEC-007 | `DECISIONS.md` | D-004 | Agency-notification acceptance is the success boundary; acknowledgement failure must not invite resubmission. | Return success after agency acceptance and report acknowledgement as non-blocking. |
| DEC-008 | `DECISIONS.md` | D-005 | Every section, interaction, message, state, confirmation, and acknowledgement has full English/Greek parity. | Missing locale content is a build/test defect; no mixed-language fallback. |
| DEC-009 | `PRD.md` | §9 | Delivery is a strict 12-hour Tier-2 showcase. | Prefer shallow modules and focused tests; no speculative infrastructure. |
| DEC-010 | root `AGENTS.md` | Architecture | Static local schema-validated content renders public pages; the form Route Handler is the sole dynamic boundary. | No database, CMS, server actions, or runtime content API. |
| DEC-011 | design docs | visual direction | Warm ivory, deep Aegean, muted teal, Cormorant Garamond, Inter, cinematic stills, restrained motion, light appearance only. | Replace bootstrap grayscale tokens and do not add dark mode. |
| DEC-012 | technical docs | testing | Critical Playwright flows run at 390 px and 1440 px; repository budgets are not lowered. | Preserve compact/wide projects and Unlighthouse thresholds. |
| DEC-013 | `DECISIONS.md` | D-006 | Implement the complete documented foundational token system through Tailwind CSS v4 CSS-first theme variables, while creating component-level tokens and primitives only for showcase consumers. | Centralize the full reusable foundation; do not ship a partial ad hoc palette, parallel TypeScript theme, dark mode, or unused wider-product component system. |

Normative subordinate contracts:

| ID | Source | Source ID | Contract |
|---|---|---|---|
| SUBDEC-001 | `contracts/D-002-showcase-form-fields.md` | D-002 | Step fields, omissions, validation timing, Back behavior, dependent child ages, and canonical locale-neutral values are binding. |
| SUBDEC-002 | `contracts/D-003-draft-persistence.md` | D-003 | Versioned record, expiry, autosave/flush, silent cleanup, confirmed reset, and success-only clearing are binding. |
| SUBDEC-003 | `contracts/D-004-showcase-emails.md` | D-004 | Two-email content, attachment, styling, omission, plain-text fallback, and acceptance boundary are binding. |
| SUBDEC-004 | `contracts/D-005-bilingual-parity.md` | D-005 | Route, state, field, option, recovery, content, and email-language parity are binding. |

The rows above are provenance. Their complete operative behavior is reproduced in §§3, 5, 6, 7, 8, and 13; an implementer does not need to open the contract files to discover additional feature requirements.

### 2.2 Rejected Alternatives

| ID | Source ID | Rejected direction | Reason |
|---|---|---|---|
| REJ-001 | R-001 | Full broader page hierarchy | It jeopardizes the 12-hour target and form/email polish. |
| REJ-002 | R-002 | Ultra-lean conversion-only pages | It does not demonstrate editorial depth or destination expertise. |
| REJ-003 | D-003 rejection | Per-locale or persistent-forever drafts | It breaks bilingual continuity or privacy-conscious expiry. |
| REJ-004 | D-004 rejection | Internal-only email or success requiring both emails | It fails the visitor experience or creates duplicate-resubmission risk. |
| REJ-005 | D-005 rejection | Reduced Greek coverage | Full parity is part of the demonstrated product capability. |

### 2.3 Assumptions

| ID | Assumption | Why reasonable | Verification |
|---|---|---|---|
| ASM-001 | The showcase route pairs are `/en`, `/el`; `/en/destinations/paros-antiparos`, `/el/destinations/paros-antiparos`; `/en/plan-my-trip`, `/el/plan-my-trip`; `/en/plan-my-trip/confirmation`, `/el/plan-my-trip/confirmation`. | Existing routing requires explicit locale prefixes, and a shared stable slug minimizes complexity for one destination. | Routing unit tests and Playwright route matrix. |
| ASM-002 | Canonical option IDs are English-like kebab-case identifiers and are never translated. | `next-intl` and the accepted draft contract require locale-neutral values. | Schema and language-switch E2E tests. |
| ASM-003 | Omitted optional scalar values serialize as `null`; omitted multi-select values serialize as `[]`. | This gives the required stable JSON attachment representation. | Email mapper unit test and attachment snapshot. |
| ASM-004 | Form limits in §6 are implementation policy for safe bounded input, not business claims. | The accepted decisions require validation but do not fix technical limits. | Shared-schema unit tests. |
| ASM-005 | Generated media remains provisional. Assets may render only after their manifest records have non-null localized alt text, focal metadata, source/rights status, and operator approval; otherwise the component uses its designed neutral fallback. | Current `content/shared/media.json` explicitly marks approval metadata pending. | Content validation and representative-media manual check. |
| ASM-006 | Local and automated tests use an injected email transport mock; controlled Resend smoke testing is a separate operator-run gate with approved addresses. | Credentials and recipients must remain outside Git. | Route tests run without network; controlled smoke evidence is recorded separately. |
| ASM-007 | No direct contact fallback is shown in this showcase because no monitored channel is approved. Failure copy offers Retry; confirmation offers Home, Paros, and Start a New Request. | Repository authority prohibits invented operational channels. | Failure and confirmation E2E tests. |

### 2.4 Open Questions / Required Human Inputs

No design question blocks implementation. These runtime inputs are required only to exercise real delivery:

| ID | Input | Blocking? | Behavior until supplied |
|---|---|---|---|
| QUE-001 | `RESEND_API_KEY`, verified `RESEND_FROM`, and `GREEK_ESSENCE_LEADS_TO` | blocks real email smoke only | Build and automated tests use the transport mock; production-mode endpoint fails closed with a generic 503. |
| QUE-002 | Approved controlled visitor test address | blocks real acknowledgement smoke only | Do not send to arbitrary or real visitor addresses during testing. |
| QUE-003 | Final approval metadata for generated showcase media | does not block functional implementation | Render the intentional neutral media fallback for unapproved records. |

### 2.5 Non-Goals

- Full sitemap, destination catalogue, experiences, journeys, About, FAQ, Contact, or legal-page implementation.
- Booking, reservations, pricing, budget collection, availability, payments, accounts, dashboards, CRM, CMS, database, analytics, marketing automation, or production lead operations.
- Country of residence, first-visit status, accommodation preference, separate considered-destinations field, duplicate notes, file uploads, or marketing consent.
- Advanced animation, hero video, maps, destination filters, generic page builders, generalized form frameworks, queues, durable idempotency stores, delivery tracking, or background retries.
- Deployment, credential provisioning, public launch, production legal approval, or production-grade anti-abuse controls.

## 3. User and Product Behavior

### 3.1 Core Scenarios

```gherkin
Scenario: English destination-led request
  Given the visitor is on /en/destinations/paros-antiparos
  When they choose Plan My Trip
  Then /en/plan-my-trip opens at Step 1 with Paros & Antiparos visibly selected and editable

Scenario: Greek journey parity
  Given the visitor follows the showcase through /el
  When they visit the destination, complete all four steps, and submit
  Then every page, label, option, validation message, pending state, failure state, and confirmation is Greek

Scenario: Draft recovery and locale continuity
  Given the visitor has entered meaningful canonical values on Step 3
  When 1000 ms passes, a field blurs, the page refreshes, or the visitor switches locale
  Then the current step and values are restored from the same canonical record and rendered with labels in the active locale

Scenario: Agency delivery failure
  Given the final payload is valid
  When Resend rejects the agency notification
  Then the endpoint returns a generic recoverable failure, the form and draft remain intact, and retry reuses the submission ID

Scenario: Acknowledgement-only failure
  Given Resend accepts the agency notification
  When the visitor acknowledgement fails
  Then the visitor still reaches confirmation, the draft is cleared, and the UI does not ask for resubmission
```

### 3.2 Functional Requirements

| ID | Requirement | Acceptance criteria | Implementation target | Test idea |
|---|---|---|---|---|
| FR-001 | Render the six fixed Home sections plus shared header/footer in both locales. | Section order matches DEC-001; CTA paths are localized; copy is complete and contains no unsupported claims. | `app/[locale]/page.tsx`, `components/layout/*`, `components/sections/*`, showcase content JSON | E2E section/CTA assertions for `/en` and `/el`. |
| FR-002 | Render the six fixed Paros & Antiparos sections plus shared shell in both locales. | Page explains character, fit, experiences, culture/gastronomy, combinations, and planning CTA without extra broad sections. | `app/[locale]/destinations/paros-antiparos/page.tsx`, shared sections, content JSON | E2E route and heading matrix. |
| FR-003 | Preserve equivalent routes through the language switcher. | Switching on all four route types keeps the route type; Plan My Trip also keeps step and canonical values. | `components/layout/language-switcher.tsx`, `i18n/navigation.ts`, form draft module | Routing unit test plus E2E switches on destination and Step 3. |
| FR-004 | Implement exactly four form steps and the accepted fields. | Continue/Submit validates the active step; correction then validates inline; Back neither validates nor clears. | `components/forms/trip-request-form.tsx`, step components, shared schema | Component/unit tests and keyboard E2E. |
| FR-005 | Handle children and child ages without silent loss. | Ages appear and are required when children > 0; reducing count with populated removed ages requires confirmation or preserves values until confirmed. | travelers step/reducer | Unit state test and mobile E2E. |
| FR-006 | Persist one canonical 72-hour draft. | Meaningful change saves after 1000 ms and flushes on blur and step/language navigation; valid drafts restore; corrupt, incompatible, unreadable, and expired drafts are silently removed. | `lib/form-draft.ts`, form hook | Fake-timer unit tests and E2E refresh/expiry/language switch. |
| FR-007 | Provide confirmed Start Over. | Cancel leaves all state intact; confirm clears storage and values, returns to Step 1, and retains route-implied Paros context only on destination-context entry. | form component/reset dialog | Component and E2E tests. |
| FR-008 | Submit only a server-validated canonical payload. | JSON-only endpoint rejects malformed, oversized, invalid, unsupported-locale, disallowed-option, honeypot, and cross-site requests without returning PII/provider details. | `app/api/trip-request/route.ts`, `lib/trip-request-schema.ts` | Route integration tests. |
| FR-009 | Send the agency notification first. | Email has structured HTML/text, every accepted field, locale, submission ID, and identical canonical JSON attachment; optional values follow ASM-003. | `emails/agency-notification.ts`, `lib/email-payload.ts`, transport | Mapper/template unit tests and mocked route test. |
| FR-010 | Attempt a localized visitor acknowledgement after agency acceptance. | English or Greek email confirms receipt without booking, response-time, price, or availability claims and excludes unnecessary sensitive details. | `emails/visitor-acknowledgement.ts`, route | Locale template snapshots and mocked route test. |
| FR-011 | Apply the agency acceptance boundary. | Agency failure returns failure and preserves draft; acknowledgement-only failure returns accepted success with `acknowledgement: "failed"`; no duplicate agency send occurs on same idempotency key. | route and Resend transport | Mocked failure matrix and retry integration test. |
| FR-012 | Show an accessible localized confirmation route. | Successful client navigation reaches `/{locale}/plan-my-trip/confirmation`, focuses the success heading, contains no submitted PII in URL or page, and refresh/direct access yields the generic safe receipt-orientation copy defined in §7.1. | confirmation page and client navigation | E2E happy path, refresh, and direct-access assertions. |
| FR-013 | Validate bilingual content and messages at build time. | Required structural content and message keys exist in both locales; referenced media IDs exist; required approved media metadata is complete before rendering. | content schemas/loader/validator, parity tests | `pnpm validate:content` and unit parity tests. |
| FR-014 | Preserve clean failure/retry behavior. | Pending disables only Submit; all values stay visible; retry is explicit; no automatic background retry or false success. | form submit state | E2E intercepted 503 then 200. |
| FR-015 | Generate localized metadata for each route pair. | Each route has non-empty localized title/description, self-canonical, `en`/`el`/`x-default` alternates, and `noindex,nofollow` while the private prototype policy remains active. | page `generateMetadata` helpers | Metadata E2E route matrix. |
| FR-016 | Implement the complete documented foundational token system for the showcase. | All reusable primitive and semantic colors, typography roles, spacing, containers/gutters, responsive modes, radii, borders, surfaces, shadows, motion/easing, focus, and shared interaction/status states defined by `docs/04_design` are centralized through Tailwind CSS v4 `@theme` / `@theme inline` in global CSS or an imported token stylesheet. Documented provisional values are the baseline; light-only behavior, semantic utilities, and one CSS source of truth are preserved. Component tokens, variants, and primitives exist only where an accepted showcase component consumes them. | global CSS/theme foundation and consumed component variants | Token contract test/static inspection plus compact/wide EN/GR visual, contrast, focus, reduced-motion, and representative-component checks. |

### 3.3 Non-Functional Requirements

| ID | Requirement | Target |
|---|---|---|
| NFR-001 | Responsiveness | Complete journey at 390 × 844 and 1440 × 1024; usable at 320 px, 834 × 1112, intermediate widths, landscape, and 200% zoom; no horizontal overflow. |
| NFR-002 | Accessibility | Semantic headings/landmarks, keyboard completion, persistent labels, 44 × 44 minimum interactive target where practical, visible 2 px focus ring, associated errors, error-summary focus, reduced-motion support, and zero axe A/AA violations on key routes. |
| NFR-003 | Performance | Preserve Unlighthouse budgets: performance ≥90, accessibility 100, best practices ≥95, SEO ≥95. Also enforce Home LCP ≤2.5 s, INP ≤200 ms, CLS ≤0.1, critical-route JS ≤150 KiB gzip, form-route JS ≤200 KiB gzip, critical CSS ≤40 KiB gzip, cold mobile Home transfer ≤1.8 MiB, and hero image normally ≤400 KiB; use responsive `next/image` and avoid unnecessary client components/remote-image dependency. |
| NFR-004 | Privacy | No PII in URLs, metadata, logs, console, analytics, screenshots, provider error responses, or repository fixtures; free-text warns against passports, payment, health, or other sensitive data. |
| NFR-005 | Security | Server-only secrets, JSON/body limits, allow-listed enums/IDs, origin/fetch-site checks, honeypot, plain-text escaping, safe HTML escaping, generic correlation ID on server failure, no raw user HTML. |
| NFR-006 | Reliability | Draft survives supported failures; retries are user initiated; one submission ID and deterministic keys cover immediate retry; acknowledgement failure cannot trigger duplicate-resubmission messaging. |
| NFR-007 | Localization | Natural, complete, layout-realistic English and Greek; canonical values remain untranslated; no silent mixed-language fallback. |
| NFR-008 | Maintainability | Strict TypeScript, shallow feature modules, one content loader, one shared submission schema, no global state library, no parallel TypeScript theme object, and no speculative abstraction or component-token API beyond accepted showcase consumers named in §5.3. |

## 4. Current Codebase Map

### 4.1 Repository Snapshot

- Runtime: Node `v24.18.0`; package contract Node `>=24 <25`.
- Package manager: standalone pnpm `11.17.0`.
- Framework: Next.js `16.2.6` App Router, React `19.2.4`, TypeScript `6.0.3`, Tailwind `4.3.3`, `next-intl` `4.13.3`.
- Current UI base: shadcn `4.13.1`, Base UI `1.6.0`.
- Tests: Vitest `4.1.10`, Playwright `1.61.1`, axe Playwright `4.12.1`, Unlighthouse `0.18.0`.
- Current application: localized bootstrap fixture only; product showcase is not implemented.
- Live branch at reconnaissance: `main` at `f768007302c740275afb57c994cf68e34ed71df5`, matching `origin/main`, with unrelated dirty documentation/content/assets and feature-workspace changes that must be preserved.

### 4.2 Relevant Existing Files

| Path | Current responsibility / symbol | Evidence and implementation relevance |
|---|---|---|
| `app/[locale]/layout.tsx` | `generateStaticParams`, `dynamicParams = false`, locale validation/provider | Preserve explicit static locale generation and `setRequestLocale`; add fonts/shared shell without weakening locale validation. |
| `app/[locale]/page.tsx` | localized fixture Home and metadata | Replace fixture composition with showcase Home and preserve canonical/hreflang/noindex semantics. |
| `i18n/routing.ts` | `locales: ["en", "el"]`, always-prefixed default English | Fixed locale contract and root redirect behavior. |
| `i18n/navigation.ts` | locale-aware `Link`, router, pathname | Required route-preserving language switching. |
| `proxy.ts` | `/` → `/en`; localized middleware; API exclusion | Preserve API exclusion and invalid-locale behavior. |
| `messages/en.json`, `messages/el.json` | small interface translation namespace | Replace/extend with parity-preserved navigation, form, state, validation, and confirmation keys; editorial copy belongs in content JSON. |
| `app/globals.css` | Tailwind/shadcn bootstrap grayscale tokens | Replace with approved Greek Essence semantic tokens; retain focus/base layers and light-only policy. |
| `content/shared/media.json` | stable media IDs, files, dimensions, pending metadata | Reuse IDs, never physical paths in page content; fail closed for unapproved media and support neutral fallback. |
| `tests/unit/messages/parity.test.ts` | recursive locale message key parity | Extend unchanged pattern to complete showcase message parity. |
| `tests/e2e/localization-and-quality.spec.ts` | localized metadata, locale switching, keyboard interaction, browser guards | Replace fixture route matrix with showcase route pairs and preserve browser-failure assertions. |
| `tests/e2e/accessibility.spec.ts` | axe WCAG 2.2 A/AA smoke matrix | Expand to Home, destination, each form state, confirmation in both locales. |
| `tests/e2e/browser-guards.ts` | catches console, page, request, and HTTP failures | Reuse in every critical journey; explicitly allow mocked expected API failures only in the test that asserts them. |
| `playwright.config.ts` | compact 390, medium 834, wide 1440 projects | Critical flow gates target compact and wide; medium remains regression coverage when full suite runs. |
| `unlighthouse.config.ts` | fixed budgets and fixture include list | Change includes to Home, destination, Plan My Trip, confirmation route samples without lowering scores. |
| `docs/03_technical_design/04_project_and_file_architecture.md` | shallow app/components/content/emails/lib boundaries | Target structure in §5.3 follows this repository contract, narrowed to the showcase. |
| `docs/03_technical_design/18_testing_and_quality_gates.md` | Playwright-led test strategy | Governs exact gates in §13–14. |

### 4.3 Existing Patterns to Preserve

1. **Static localized App Router pages.** Every locale page calls `setRequestLocale`, resolves local content/messages, and emits route-specific metadata. Locale parameters are generated statically and unsupported locales return 404.
2. **Locale-aware navigation.** Use helpers from `i18n/navigation.ts`, not raw string replacement. Equivalent fixed route pairs are selected by route identity; form values come from the canonical draft.
3. **Editorial/interface separation.** Put page prose and media references under `content/en` and `content/el`; put short labels, validation, navigation, and statuses under `messages`.
4. **Stable media IDs.** Content references `content/shared/media.json` IDs. A loader resolves approved files/dimensions/alt/focal data; UI does not hard-code asset paths.
5. **Browser guards.** Critical E2E tests install guards before navigation and fail on unexpected console errors, page errors, failed requests, or HTTP errors.
6. **Message parity.** Recursive key-set comparison prevents locale drift. Extend this test rather than creating an unrelated translation mechanism.
7. **Minimal client JavaScript.** Page composition and content remain Server Components. Header menu, language switching where route state matters, form, and reset confirmation are the only client islands.

### 4.4 Constraints and Current Gaps

- `react-hook-form`, `zod`, and `resend` are not currently installed even though technical authority selects shared Zod validation and a React Hook Form client. Add only these runtime dependencies. Do not add React Email; two small typed render functions returning escaped email-safe HTML/text are proportionate and satisfy the accepted email contract.
- `package.json` currently lacks `validate:content`; implementation must add the script before claiming repository gates.
- No form, email, content schema/loader, showcase pages, or API route currently exists.
- Current media records are provisional and have null alt/focal fields. Do not silently promote them to approved runtime assets.
- Unrelated dirty files and generated assets already exist. Implementation must edit only files required by this SPEC and never overwrite concurrent work blindly.

## 5. Target Design

### 5.1 Architecture

Use one static content projection and one client form island:

1. Build-time loaders validate locale-specific showcase JSON and media references with Zod.
2. A centralized Tailwind CSS v4 token foundation maps the complete documented reusable design system to semantic utilities; server page components compose typed shared sections and route metadata from that foundation.
3. A small client header handles compact navigation; the fixed-route language switcher preserves equivalent path identity.
4. `TripRequestForm` owns React Hook Form state, a four-state step reducer, canonical draft persistence, and submit/retry state.
5. Shared Zod schemas validate the same canonical values in browser and Route Handler.
6. `POST /api/trip-request` performs security checks, parses/validates, maps one canonical email model, sends agency notification first, then attempts visitor acknowledgement.
7. Browser clears the draft and navigates to localized confirmation after agency acceptance, independent of acknowledgement outcome.

### 5.2 Alternatives

| Option | Benefits | Costs | Decision |
|---|---|---|---|
| Native uncontrolled form | fewer dependencies | harder conditional fields, step validation, reset, and persistence | rejected; repository technical decision selects React Hook Form |
| Server Actions | concise mutation syntax | violates the one explicit Route Handler boundary and complicates testable HTTP contract | rejected |
| React Email package | component syntax | additional dependency and build surface for two templates | rejected for this Tier-2 timebox; escaped typed render functions are sufficient |
| Database/queue | durable storage and delivery orchestration | out of scope and impossible within target | rejected |
| Generic content/page builder | flexible future pages | speculative abstraction and schema complexity | rejected; use showcase-specific typed schemas |

### 5.3 Component and Module Boundaries

| Module/file | Responsibility | Public interface | Consumers |
|---|---|---|---|
| `content/{en,el}/showcase.json` | Complete locale editorial content and stable media IDs for Home/Paros. | JSON conforming to `ShowcaseContent`. | `lib/content.ts` |
| `content/schemas/showcase.ts` | Zod schema and inferred content types. | `showcaseContentSchema`, `ShowcaseContent` | loader and validator |
| `lib/content.ts` | Only public content-loading/media-resolution boundary. | `getShowcaseContent(locale)`, `resolveMedia(id)` | page routes/sections |
| `lib/routes.ts` | Fixed route identities and equivalent localized hrefs. | `showcaseRoutes`, `getLocalizedHref(routeId, locale)` | metadata, header, switcher, tests |
| `components/layout/site-header.tsx` | Logo/Home, primary destination link, Plan My Trip, compact menu, language control. | `{locale, routeId}` | three public page layouts |
| `components/layout/site-footer.tsx` | Bounded prototype footer without invented contact/legal links. | `{locale}` | all showcase pages |
| `components/layout/language-switcher.tsx` | Switch fixed equivalent route; flush form draft through callback when used in form. | `{locale, routeId, onBeforeNavigate?}` | header/form shell |
| `components/sections/*` | Typed visual sections: hero, editorial split, card row, steps, trust story, combinations, CTA. | Explicit content props; no filesystem reads. | Home and destination routes |
| `lib/trip-request-schema.ts` | Canonical values, per-step schemas, final submission schema, normalization. | types and `validateStep`, `tripRequestSubmitSchema` | client form, route, email mapper |
| `lib/form-draft.ts` | Parse, load, save, expire, clear version-1 draft. | `loadDraft`, `saveDraft`, `clearDraft`, `DRAFT_KEY`, `DRAFT_VERSION` | form hook/tests |
| `components/forms/trip-request-form.tsx` | Four-step state, validation, persistence, submit/retry, reset. | `{locale, initialDestinationId?}` | Plan My Trip route |
| `components/forms/steps/*.tsx` | Render one accepted field group each. | React Hook Form context plus localized option labels. | `TripRequestForm` only |
| `lib/email-payload.ts` | Map validated submission to exact canonical email model and attachment bytes. | `toEmailModel(submit)`, `toJsonAttachment(model)` | route/templates/tests |
| `emails/agency-notification.ts` | Escaped branded HTML/text for agency. | `renderAgencyEmail(model)` → `{subject, html, text}` | route |
| `emails/visitor-acknowledgement.ts` | Escaped localized receipt email without sensitive repetition. | `renderVisitorAcknowledgement(model)` → `{subject, html, text}` | route |
| `lib/resend.ts` | Server-only transport and deterministic idempotency keys. | `sendAgency(model)`, `sendAcknowledgement(model)` | Route Handler only |
| `app/api/trip-request/route.ts` | HTTP/security/validation/orchestration boundary. | `POST(Request)` | browser/tests |
| `app/[locale]/plan-my-trip/confirmation/page.tsx` | Generic localized success/recovery page with no PII. | route component | browser navigation |

No module above is public outside the repository. Functions must return typed results rather than expose provider response objects.

`showcaseRoutes` is the complete route contract:

```ts
const showcaseRoutes = {
  home: (locale: Locale) => `/${locale}` as const,
  paros: (locale: Locale) => `/${locale}/destinations/paros-antiparos` as const,
  "plan-my-trip": (locale: Locale) => `/${locale}/plan-my-trip` as const,
  confirmation: (locale: Locale) => `/${locale}/plan-my-trip/confirmation` as const,
}
function getLocalizedHref(routeId: RouteId, locale: Locale): string
```

Each localized page follows the fully stated pattern: export `generateMetadata({params})`; await/validate locale against `routing.locales`; call `setRequestLocale(locale)` in the page; load locale content through `getShowcaseContent`; emit a self-canonical URL, `en`/`el`/`x-default` alternates using `showcaseRoutes`, and `robots: {index:false, follow:false}`. The locale layout alone exports `generateStaticParams` for `en` and `el` and `dynamicParams = false`.

### 5.4 Page Composition

**Home:** shared header → cinematic hero → concise brand promise → one Paros-led destination module → compact three-step How It Works → one truthful trust/story narrative using provisional copy, not credentials → deep-blue final CTA → footer.

**Paros & Antiparos:** shared header → destination hero → editorial introduction/defining character → traveler-fit block → signature experiences including culture/gastronomy → one destination-combinations block → contextual final CTA → footer.

**Plan My Trip:** minimal header with Home/language/safe exit → localized title `Request a Custom Itinerary` → concise four-step/privacy/value orientation → stable progress → active step → Back/Continue/Submit → Start Over → compact footer. No help/contact/legal route is invented; the inline privacy acknowledgement in §6.1 is the complete provisional notice for this showcase. Storage operation remains invisible.

**Confirmation:** minimal shared shell → focused heading → honest receipt orientation → no promised response window → Home, Paros, and Start a New Request links. Immediately after accepted navigation the heading is “Request received” / “Το αίτημά σας ελήφθη”. Direct access or refresh may show the same generic statement because it contains no request data and causes no side effect; supporting copy says the page records no booking and instructs a visitor who did not just submit to return to Plan My Trip. No contact channel is shown because none is approved for this showcase.

## 6. Data, Types, and Contracts

### 6.1 Canonical Domain Model

```ts
type Locale = "en" | "el"
type DestinationId = "paros-antiparos" | "help-me-choose"
type TripType = "couple" | "honeymoon" | "family" | "friends" | "solo" | "other"
type InterestId =
  | "beaches"
  | "culture"
  | "history"
  | "gastronomy"
  | "nightlife"
  | "nature"
  | "wellness"
  | "local-life"
  | "relaxation"
type Pace = "relaxed" | "balanced" | "active"
type ContactMethod = "email" | "phone" | "whatsapp"

type EditableTripRequestValues = {
  destinationIds: DestinationId[]
  flexibleTiming: boolean
  arrivalDate: string              // empty or in-progress YYYY-MM-DD text
  departureDate: string
  adults: string                   // numeric input text; clean default "2"
  children: string                 // numeric input text; clean default "0"
  childAges: string[]              // may be incomplete while editing
  tripType: TripType | null
  interests: InterestId[]
  pace: Pace | null
  notes: string
  fullName: string
  email: string
  phone: string
  preferredContactMethod: ContactMethod | null
  privacyAcknowledged: boolean
}

type TripRequestValues = {
  destinationIds: DestinationId[]
  flexibleTiming: boolean
  arrivalDate: string | null       // YYYY-MM-DD
  departureDate: string | null     // YYYY-MM-DD
  adults: number                   // integer 1..12
  children: number                 // integer 0..8
  childAges: number[]              // each integer 0..17; length === children
  tripType: TripType
  interests: InterestId[]          // at least one
  pace: Pace
  notes: string | null             // trimmed, max 1500 code points
  fullName: string                 // trimmed, 2..100 code points
  email: string                    // trimmed/lowercased, max 254
  phone: string | null             // trimmed, 7..40 when present; permissive international characters
  preferredContactMethod: ContactMethod
  privacyAcknowledged: true
}

type TripRequestSubmit = {
  submissionId: string             // UUID
  submissionCreatedAt: string      // stable ISO instant created with UUID and reused for retry
  locale: Locale
  form: TripRequestValues
  context: { type: "destination"; id: "paros-antiparos" } | null
  honeypot: string                 // must be empty
}

type TripRequestDraftV1 = {
  version: 1
  updatedAt: string
  expiresAt: string
  currentStep: 1 | 2 | 3 | 4
  values: EditableTripRequestValues
  context: TripRequestSubmit["context"]
  submissionId: string | null      // populated for a failed attempt and reused until meaningful edit/success/reset
  submissionCreatedAt: string | null
}
```

Step ownership, defaults, controls, and fixed interface labels are:

| Step | Field | Clean default | Control | English label | Greek label |
|---|---|---|---|---|---|
| 1 Trip | `destinationIds` | direct entry: `["help-me-choose"]`; contextual entry: `["paros-antiparos"]` | checkbox choice cards; at least one | Destination | Προορισμός |
| 1 Trip | `flexibleTiming` | `true` | checkbox/switch with native semantics | My dates are flexible | Οι ημερομηνίες μου είναι ευέλικτες |
| 1 Trip | `arrivalDate` | `""` | native date input | Approximate arrival | Περίπου ημερομηνία άφιξης |
| 1 Trip | `departureDate` | `""` | native date input | Approximate departure | Περίπου ημερομηνία αναχώρησης |
| 2 Travelers | `adults` | `"2"` | numeric input with keyboard entry | Adults | Ενήλικες |
| 2 Travelers | `children` | `"0"` | numeric input with keyboard entry | Children | Παιδιά |
| 2 Travelers | `childAges` | `[]` | one numeric input per child | Child N age | Ηλικία παιδιού N |
| 2 Travelers | `tripType` | `null` | radio group | Trip type | Τύπος ταξιδιού |
| 3 Preferences | `interests` | `[]` | checkbox chips; at least one | Interests | Ενδιαφέροντα |
| 3 Preferences | `pace` | `null` | radio group | Preferred pace | Προτιμώμενος ρυθμός |
| 3 Preferences | `notes` | `""` | textarea | Anything else we should know? (Optional) | Κάτι άλλο που θα θέλατε να γνωρίζουμε; (Προαιρετικό) |
| 4 Contact | `fullName` | `""` | text input, `autocomplete="name"` | Full name | Ονοματεπώνυμο |
| 4 Contact | `email` | `""` | email input, `autocomplete="email"` | Email | Email |
| 4 Contact | `phone` | `""` | tel input, `autocomplete="tel"` | Phone or WhatsApp (Optional) | Τηλέφωνο ή WhatsApp (Προαιρετικό) |
| 4 Contact | `preferredContactMethod` | `null` | radio group; phone/WhatsApp disabled until phone is usable | Preferred contact method | Προτιμώμενος τρόπος επικοινωνίας |
| 4 Contact | `privacyAcknowledged` | `false` in editable state; submission requires literal `true` | checkbox | I acknowledge that Greek Essence will use these details to review and respond to this request. | Αναγνωρίζω ότι η Greek Essence θα χρησιμοποιήσει αυτά τα στοιχεία για να εξετάσει και να απαντήσει σε αυτό το αίτημα. |

Fixed option labels:

- Destination: `paros-antiparos` → “Paros & Antiparos” / “Πάρος & Αντίπαρος”; `help-me-choose` → “Help me choose” / “Βοηθήστε με να επιλέξω”.
- Trip type: couple → Couple / Ζευγάρι; honeymoon → Honeymoon / Ταξίδι του μέλιτος; family → Family / Οικογένεια; friends → Friends / Παρέα φίλων; solo → Solo / Ατομικό ταξίδι; other → Other / Άλλο. No extra “other” text field is collected.
- Interests: beaches → Beaches / Παραλίες; culture → Culture / Πολιτισμός; history → History / Ιστορία; gastronomy → Gastronomy / Γαστρονομία; nightlife → Nightlife / Νυχτερινή ζωή; nature → Nature / Φύση; wellness → Wellness / Ευεξία; local-life → Local life / Τοπική ζωή; relaxation → Relaxation / Χαλάρωση.
- Pace: relaxed → Relaxed / Χαλαρός; balanced → Balanced / Ισορροπημένος; active → Active / Δραστήριος.
- Contact method: email → Email / Email; phone → Phone / Τηλέφωνο; whatsapp → WhatsApp / WhatsApp.

Rules:

- Exact dates are required only when `flexibleTiming` is false. When supplied, both must parse as real `YYYY-MM-DD` calendar dates and departure must be on/after arrival; same-day and past dates are accepted because this showcase does not define an operational booking calendar.
- `destinationIds` has at least one unique allow-listed value. `help-me-choose` and `paros-antiparos` are mutually exclusive destination choices.
- Reducing `children` below populated `childAges.length` requires confirmation before truncation. Increasing adds empty age controls that block Continue until complete.
- `preferredContactMethod` is always allowed as `email`; `phone` or `whatsapp` requires a non-null phone value.
- Phone accepts only Unicode-trimmed ASCII digits, spaces, `+`, `(`, `)`, `-`, `.`, and `/`, contains 7–20 digits, and is at most 40 code points. It is not reformatted beyond trimming.
- Notes are plain text. Helper copy explicitly asks visitors not to enter passport, payment, health, or similarly sensitive details.
- Optional scalars normalize to `null`; lists normalize to deduplicated arrays in display order.
- All text limits count Unicode code points with `Array.from(value).length`, not UTF-16 code units. Whitespace-only optional values normalize to `null`; required text is trimmed before length checks. Text is preserved in Unicode form without normalization so names are not silently rewritten.
- `editableTripRequestSchema` is structural and permits incomplete values: empty strings, null unchosen radio values, empty interests, `privacyAcknowledged: false`, and `childAges.length !== parsed children`. It rejects unknown keys, non-allow-listed selected IDs, non-string editable scalar values, and any individual editable string over 1,500 code points. `normalizeAndValidateSubmission(editable)` trims/transforms numeric strings and optional empty strings, applies every canonical invariant above, and returns `{success:true, data:TripRequestValues}` or `{success:false, fieldErrors, formErrors}`. Only its success data may enter `TripRequestSubmit` or email mapping.

### 6.2 Context Transport and Initialization

- The Paros CTA links to `/{locale}/plan-my-trip?destination=paros-antiparos`. This query contains only an allow-listed public destination ID and no PII.
- Direct Plan My Trip navigation has no destination query and starts with `help-me-choose`.
- Initialization order is: valid draft → valid query context → clean direct defaults. A valid draft wins so a returning visitor is never overwritten by a CTA.
- Before the first autosave, refresh is recoverable because the public query remains in the URL.
- Language switching preserves only the allow-listed `destination` query and drops unknown query keys; it preserves a hash only when that hash names an existing static section anchor. On the form it flushes the draft first.
- Contextual entry provenance is `context: {type:"destination", id:"paros-antiparos"}` in form state/draft. Confirmed Start Over restores Paros only when this context exists; direct entry resets to `help-me-choose`.
- Changing destination values does not erase provenance. The submitted `context` records where the flow began while `form.destinationIds` records the visitor's final editable choice.

### 6.3 Meaningful Changes and Draft Contract

- Key: `greek-essence.trip-request-draft.v1`.
- Save only in browser code after hydration.
- A meaningful change is a change to the JSON-serializable `EditableTripRequestValues`, `currentStep`, or route-entry `context` compared with the last saved snapshot. Validation/error state, submission pending/error state, acknowledgement status, and blur without such a difference are not meaningful changes.
- `expiresAt = updatedAt + 72 hours`; every meaningful change updates both timestamps.
- Debounce value changes by exactly 1000 ms. Blur, Back, Continue, language switch, and `pagehide` synchronously flush a pending meaningful state before navigation.
- Loading catches all storage/JSON/schema errors. Invalid data is removed inside a second guarded operation; failure to remove remains silent and the clean defaults render.
- Draft structural validity uses `editableTripRequestSchema`, not final submission validity, so incomplete/invalid user progress restores exactly. `updatedAt`, `expiresAt`, and non-null `submissionCreatedAt` must be canonical ISO instants parseable by `Date`; `expiresAt` must equal `updatedAt + 72 hours` exactly in epoch milliseconds; `updatedAt` cannot be more than five minutes after injected `now`; and `now >= expiresAt` is expired. `submissionId` and `submissionCreatedAt` must either both be null or both be valid. Any violation triggers silent cleanup.
- No toast, status row, restored banner, expiry warning, or cleanup message is rendered.
- On first Submit, create `submissionId` and `submissionCreatedAt = new Date().toISOString()` together before the request and flush both into the draft. A failed submission retains both. A subsequent editable form-field change or locale switch clears both and the next Submit creates a new pair because either changes the email payload; step-only movement, blur, and route refresh do not invalidate them. A direct retry without field edits or locale change reuses the identical pair while it is under 24 hours old; at 24 hours the client atomically replaces both before retry because provider idempotency is no longer guaranteed.
- Successful agency acceptance and confirmed Start Over clear the key.

Typed draft interface:

```ts
type DraftLoadResult =
  | { kind: "empty" }
  | { kind: "restored"; draft: TripRequestDraftV1 }

function loadDraft(
  storage: Pick<Storage, "getItem" | "removeItem">,
  now: Date
): DraftLoadResult
function saveDraft(
  storage: Pick<Storage, "setItem">,
  draft: TripRequestDraftV1
): boolean
function clearDraft(storage: Pick<Storage, "removeItem">): boolean
```

The boolean is `false` only when storage throws; callers silently continue in memory. `loadDraft` never throws and returns `empty` after guarded cleanup of an invalid record.

### 6.4 HTTP Contract

`POST /api/trip-request`

Request requirements:

- Accepted `Content-Type` values, after trimming outer whitespace and ASCII-case-folding, are exactly `application/json` or `application/json;charset=utf-8`; optional whitespace around the single semicolon is allowed. Quoted charset values, duplicate charset, additional parameters, or another charset return 415.
- Body maximum is 32,768 bytes measured from the raw UTF-8 request bytes before JSON parsing; exactly 32,768 bytes is accepted and 32,769 is rejected.
- Reject `Sec-Fetch-Site: cross-site`. When `Origin` is present it must equal `new URL(NEXT_PUBLIC_SITE_URL).origin`; absence of both headers is not itself a rejection because non-browser test clients may omit them.
- Empty honeypot and allow-listed locale/context/options.
- Valid UUID submission ID and canonical ISO `submissionCreatedAt`. The timestamp must be no more than five minutes in the future and no more than 24 hours old relative to injected server `now`; otherwise return 422 `invalid` on `submissionCreatedAt`. No minimum-interaction timer or rate limiter is implemented in this Tier-2 slice; body limits, origin/fetch-site checks, strict schema validation, and honeypot are the complete prototype controls.
- Complete server validation and normalization through `tripRequestSubmitSchema`.

Responses:

```ts
type AcceptedResponse = {
  ok: true
  submissionId: string
  acknowledgement: "accepted" | "failed"
}

type FieldErrorCode =
  | "required"
  | "invalid"
  | "out_of_range"
  | "date_order"
  | "age_count"
  | "contact_channel"

type InvalidResponse = {
  ok: false
  code: "INVALID_REQUEST"
  reference: string
  fieldErrors: Record<string, FieldErrorCode[]> // dot/index paths such as childAges.0
  formErrors: FieldErrorCode[]
}

type FailureResponse = {
  ok: false
  code:
    | "UNSUPPORTED_MEDIA_TYPE"
    | "PAYLOAD_TOO_LARGE"
    | "FORBIDDEN"
    | "DELIVERY_UNAVAILABLE"
    | "MISCONFIGURED"
    | "INTERNAL_ERROR"
  reference: string
}
```

Every non-200 response gets a new opaque `crypto.randomUUID()` reference. The client localizes error codes; the server never sends visitor-facing prose.

| Status | Condition | Browser behavior |
|---:|---|---|
| 200 | Agency notification accepted; acknowledgement accepted or failed | Clear draft and navigate to localized confirmation. |
| 400 | Malformed JSON/request envelope | Generic localized invalid-request message; preserve data. |
| 413 | Body exceeds 32,768 bytes | Generic localized invalid-request message; preserve data. |
| 415 | Unsupported content type | Generic localized invalid-request message; preserve data. |
| 422 | Canonical validation failure | Map safe dot/index paths and codes, focus summary, preserve data. Date-order maps to both date controls plus one form error; age-count maps to the children group; contact-channel maps to phone and preferred-contact controls. |
| 403 | Origin/fetch-site/honeypot check fails | Generic failure with no signal detail; preserve data. |
| 500 | Unexpected internal error | Generic recoverable failure and reference; preserve data. |
| 503 | Missing server config or agency transport failure | Generic delivery unavailable; preserve data and reuse submission ID. |

Never return provider IDs, sender/recipient addresses, raw exceptions, configuration, submitted PII, or acknowledgement error details.

Server configuration validation requires `NEXT_PUBLIC_SITE_URL` to be an absolute `http:` URL in local/test or `https:` URL in prototype production, plus non-empty valid `RESEND_API_KEY`, mailbox-shaped `RESEND_FROM`, and mailbox-shaped `GREEK_ESSENCE_LEADS_TO`. Missing/malformed configuration returns 503 `MISCONFIGURED` before provider calls. Origin comparison uses this validated URL.

### 6.5 Email Model

```ts
type TripRequestEmailModel = {
  submissionId: string
  submittedAt: string
  locale: Locale
  context: { type: "destination"; id: "paros-antiparos" } | null
  form: TripRequestValues
}
```

`submittedAt` is exactly the validated `submissionCreatedAt`, not a new route-time timestamp. Every retry using the same deterministic idempotency key therefore has byte-identical email model/attachment content. A form-field edit creates a new ID/timestamp pair and a new payload/key.

Agency subject is exactly `Greek Essence trip request — ${submissionId}`. English visitor subject is `We received your Greek Essence request`; Greek visitor subject is `Λάβαμε το αίτημά σας στη Greek Essence`.

The agency HTML and text group fields under Trip, Travelers, Preferences, and Contact in the canonical field order from §6.1. Every row displays an English operational field label followed by its canonical value. Enum/ID values display `English label [canonical-id]`; dates display canonical `YYYY-MM-DD`; booleans display `Yes`/`No`; child ages display an ordered comma-separated list or `None`; `null` displays `Not provided`; `[]` displays `None`. HTML and text use the same formatter, so parity is testable. The attachment filename is `greek-essence-trip-request-${submissionId}.json`, UTF-8 `application/json`, pretty-printed with two spaces and one trailing newline. It contains exactly `TripRequestEmailModel`; it excludes storage timestamps/version, honeypot, environment values, provider metadata, and secrets.

Agency send uses deterministic key `trip-request:${submissionId}:agency`. Acknowledgement uses `trip-request:${submissionId}:acknowledgement`. The route never calls acknowledgement before agency acceptance. Provider acceptance is transport acceptance, not guaranteed inbox delivery.

Visitor acknowledgement always uses a neutral localized greeting (“Hello” / “Γεια σας”) and never derives a first name. It names no response timeframe, booking, price, availability, guaranteed arrangement, award, partner, or credential. It includes a concise non-sensitive next-step orientation and plain-text fallback.

### 6.6 State Transitions

| From | Event | To | Side effect |
|---|---|---|---|
| clean | valid stored draft loads | editing(step N) | restore canonical values silently |
| editing | meaningful change | editing | schedule save; invalidate failed-attempt ID/timestamp only for editable form-field changes; locale switching flushes then invalidates the pair before the next submission |
| editing | blur/navigation/pagehide | editing or next route | flush pending save |
| editing(step N) | Continue with invalid data | editing(step N,error) | focus error summary; no step change |
| editing(step N) | Continue valid | editing(step N+1) | flush draft |
| editing(step N) | Back | editing(step N-1) | no validation; flush draft |
| editing | Start Over cancel | editing | no change |
| editing | Start Over confirm | clean(step 1) | clear draft and reset values/context per entry route |
| editing(step 4) | Submit valid | submitting | disable Submit; retain values |
| submitting | agency failure | failure | preserve draft/submission ID; enable explicit retry |
| submitting | agency accepted, acknowledgement accepted/failed | accepted | clear draft; navigate to confirmation |
| confirmation | refresh | confirmation | render generic safe receipt state |

## 7. Surface-Specific Design

### 7.1 Frontend and UI

- Replace bootstrap fixture copy; keep `/[locale]/quality-lab` only if still required by bootstrap regression tests, but remove it from showcase navigation and performance route sets.
- Header wide mode shows logo/Home, Paros & Antiparos, language control, and dominant Plan My Trip. Compact mode uses an explicit button with `aria-expanded`, closes on Escape/outside/navigation, traps no focus, and returns focus to its trigger.
- Use Cormorant Garamond 500/600 only for display headings and Inter 400/500/600 for body/UI via `next/font/google`, including Greek subsets where supported. No third family.
- Use these fixed primitive tokens: ivory canvas `#FAF6ED`, brightest surface `#FFFCF6`, limestone surface `#F1EDE3`, border `#E6DFD2`, deep Aegean primary `#17475F` (hover `#103348`, active `#0B2433`), muted teal accent/focus `#34767A` (active `#275F63`), primary text `#172126`, secondary text `#59666B`, error `#A13B39` on `#F7E3E1`, success `#2F6B4F` on `#E1EFE7`, and white `#FFFFFF` only for controlled contrast. Map these to semantic CSS variables; photography carries saturation. Normal text contrast is at least 4.5:1 and UI/focus boundaries at least 3:1.
- Treat the preceding fixed values as the feature-critical subset of the complete `docs/04_design` foundation, not as permission to implement only a partial palette. Centralize every documented reusable primitive/semantic color, type role, spacing, container/gutter, responsive mode, radius, border, surface, shadow, motion/easing, focus, and shared interaction/status token through Tailwind CSS v4 `@theme` / `@theme inline` in `app/globals.css` or a stylesheet imported there. Use documented provisional values as the baseline and tune only with visual/accessibility evidence; keep semantic names stable, keep appearance light-only, and do not create a second theme object in TypeScript.
- Component-level tokens and variants are demand-driven: add them only for accepted showcase components that consume them. Design-system completeness does not authorize galleries, filters, wider-product cards, or other unused component implementations.
- Use one-column compact, selective two-column medium, and generous wide compositions. No horizontal carousel is required.
- Form container is 720–880 px. Controls are at least 48 px high; textarea at least 128 px; labels persist; optional fields say Optional; selected/invalid/current states never rely on color alone.
- Progress on compact shows `Step X of 4`, current step name, and bar. Medium/wide may show all four numbered labels; future steps are noninteractive until prerequisites pass.
- Validation occurs on Continue/Submit, then affected invalid controls validate during correction. Multiple errors produce a focusable summary with links. Each field has label, `aria-invalid`, and `aria-describedby`.
- Pending submission applies the disabled attribute only to Submit and changes its label/status. Back and Start Over are temporarily not rendered while the request is in flight, preventing ambiguous state changes without presenting additional disabled controls; all fields remain visible and readable.
- Hero meaning survives image failure; final text-over-image crops require contrast testing and a scrim, not text shadow alone.
- Motion is optional, brief, and disabled under `prefers-reduced-motion`; content/actions are never delayed by animation.

### 7.2 Backend and Configuration

Required server-only variables:

```text
RESEND_API_KEY
RESEND_FROM
GREEK_ESSENCE_LEADS_TO
```

Existing public variables remain:

```text
NEXT_PUBLIC_SITE_URL
NEXT_PUBLIC_DEFAULT_LOCALE
```

Add the server variables to `.env.example` as empty documented names, never values. Validate them lazily inside the email transport so static page build and mocked tests do not require secrets. In production-mode real transport, missing config returns typed `MISCONFIGURED`; it never falls back to a real default address.

`lib/resend.ts` is server-only and imports `resend`. Tests inject a transport interface:

```ts
type ProviderStatusClass = "configuration" | "authentication" | "rate-limit" | "provider-4xx" | "provider-5xx" | "network" | "unknown"
type EmailSendResult =
  | { ok: true }
  | { ok: false; statusClass: ProviderStatusClass }

type EmailTransport = {
  send(input: {
    from: string
    to: string[]
    replyTo?: string
    subject: string
    html: string
    text: string
    attachments?: Array<{ filename: string; content: Buffer; contentType: string }>
    idempotencyKey: string
  }): Promise<EmailSendResult>
}

type RouteDependencies = {
  transport: EmailTransport
  now: () => Date
  randomUUID: () => string
  logFailure: (event: { reference: string; code: string; providerStatusClass?: ProviderStatusClass }) => void
}

function createTripRequestPostHandler(dependencies: RouteDependencies): (request: Request) => Promise<Response>
```

`route.ts` exports `POST = createTripRequestPostHandler(productionDependencies)`. Tests call the factory with deterministic clock/UUID, fake transport, and an in-memory logger. `sendAgency` and `sendAcknowledgement` return `Promise<EmailSendResult>` and never throw; the transport adapter catches provider/network errors and maps them to the status classes above. Injected `now()` validates the stable client-created submission timestamp; it does not replace it. `toJsonAttachment` returns `Buffer.from(serializedJson, "utf8")`. Agency `Reply-To` is the validated visitor email; visitor acknowledgement has no visitor-derived reply-to. Subject selection is fixed by locale for the visitor and one English operational subject for the agency.

### 7.3 Content and Media

`ShowcaseContent` has exact locale-aligned structural keys:

```ts
type NonEmptyArray<T> = readonly [T, ...T[]]
type RouteId = "home" | "paros" | "plan-my-trip" | "confirmation"

type PageMetadata = { title: string; description: string }
type CtaContent = { label: string; routeId: RouteId; destinationContext: "paros-antiparos" | null }
type HeroContent = {
  eyebrow: string | null
  title: string
  summary: string
  mediaId: string | null
  primaryCta: CtaContent
  secondaryCta: CtaContent | null
}
type EditorialContent = { eyebrow: string | null; heading: string; body: readonly string[]; mediaId: string | null }
type CardContent = { id: string; title: string; summary: string; cta: CtaContent | null }
type MediaCardContent = CardContent & { mediaId: string }
type StepContent = { title: string; summary: string }

type ShowcaseContent = {
  home: {
    metadata: PageMetadata
    hero: HeroContent
    promise: EditorialContent
    parosFeature: MediaCardContent
    howItWorks: { heading: string; steps: [StepContent, StepContent, StepContent] }
    trustStory: EditorialContent
    finalCta: CtaContent
  }
  paros: {
    metadata: PageMetadata
    hero: HeroContent
    introduction: EditorialContent
    travelerFit: { heading: string; items: NonEmptyArray<CardContent> }
    signatureExperiences: { heading: string; items: NonEmptyArray<MediaCardContent> }
    combinations: { heading: string; items: NonEmptyArray<CardContent> }
    finalCta: CtaContent
  }
}

type ResolvedMedia = {
  id: string
  src: string
  width: number
  height: number
  alt: string
  focalPoint: { xPercent: number; yPercent: number }
}
type MediaResolution =
  | { kind: "approved"; media: ResolvedMedia }
  | { kind: "fallback"; id: string; reason: "pending-approval" }
```

Both locale files must have identical structure and referenced stable IDs. The validator rejects empty headings/copy, unknown route IDs, unknown media IDs, missing dimensions/files, and locale structure drift. A known media record with pending approval is valid content but resolves to `fallback`; it is not rendered as an image. An approved record must have localized non-empty alt text, source/rights approval, focal coordinates from 0–100, and an existing file; otherwise validation fails. The fallback is a fixed-aspect limestone surface with no broken-image icon, no decorative text, and adjacent content carrying all meaning.

Exact final editorial wording is intentionally provisional under the accepted PRD. Implementation owns writing complete, natural English and Greek copy directly in the two JSON files; this is routine scope, not a human blocker. Copy acceptance is deterministic in structure and claims: every required field is non-empty; Greek text contains Greek-script prose rather than copied English except brand names; no text contains a price, availability, booking guarantee, response-time promise, award, partner, review, or credential claim. Final content review confirms natural phrasing and comparable section depth in both locales.

### 7.4 Omitted Template Sections

- Native/mobile platform section is omitted because this is a responsive web application with no native modules or permissions.
- Background jobs section is omitted because all sends occur synchronously inside one Route Handler and background retries are prohibited.
- Authentication/authorization is omitted because the showcase has no accounts or protected user surfaces; same-origin and abuse checks remain in §6.3 and §9.

## 8. Error Handling and Recovery

| Case | Expected behavior | Location | Test |
|---|---|---|---|
| Missing/invalid locale | localized routing rejects unsupported locale with 404 | layout/proxy | E2E `/invalid` |
| Missing required localized content | validator/build fails; no mixed fallback | content loader/validator | unit/script failure fixture |
| Unapproved/missing media | use designed neutral fallback while preserving text/layout; validator blocks accidental approved rendering | media resolver/component | unit + manual visual |
| Corrupt/expired/incompatible local draft | silently remove and show clean Step 1 | `lib/form-draft.ts` | unit and E2E seeded storage |
| Storage API throws | continue with in-memory form; no storage UI/error | draft module/form | unit mocked exception |
| Dates reversed or exact dates missing | localized group error; values retained | shared schema/form | unit/component |
| Child age mismatch | block Continue and identify missing age; never silently truncate populated ages | schema/reducer | unit/E2E |
| Preferred phone/WhatsApp without phone | localized contact-method error | schema/form | unit/component |
| Multiple step errors | focus linked summary; inline errors remain associated | form | keyboard E2E |
| Double Submit | second activation blocked while pending | form | component/E2E |
| Offline/fetch failure | preserve form/draft; localized retry; same submission ID | form | E2E route abort |
| Invalid server response | generic delivery failure; preserve data | form | integration |
| Agency Resend failure | 503, no acknowledgement attempt, explicit retry | route | mocked route test |
| Acknowledgement failure after agency acceptance | 200 success, confirmation, no resubmit prompt | route/form | mocked route + E2E |
| Confirmation refresh/direct visit | generic localized receipt/recovery message, no PII | confirmation page | E2E |
| Retry after field edit | generate new submission ID; old deterministic keys are not reused | form draft/state | unit |

## 9. Security, Privacy, and Abuse Boundaries

- Treat trip preferences, travel dates, party composition, name, email, phone, and notes as personal data.
- Local storage is intentionally bounded to one 72-hour draft. Do not store provider responses, error bodies, environment values, CAPTCHA values, or rendered email.
- Do not log request bodies or form values. Correlation references are random and contain no user information.
- Escape every user value before HTML interpolation; text output is plain; JSON uses `JSON.stringify` on validated canonical values.
- Accept JSON only, cap at 32 KiB, reject unknown keys through strict Zod objects, normalize Unicode-safe trimmed text, and use allow-listed option/context IDs.
- Honeypot and same-origin/fetch-site checks are prototype friction, not a claim of production bot protection. Do not add a paid challenge or durable distributed store.
- No analytics, session replay, ad pixels, or non-essential cookies.
- Privacy acknowledgement is required notice acknowledgement, not marketing consent. Do not add mailing-list behavior.
- Secrets remain server-only and outside Git. Client bundles must not import `lib/resend.ts` or server config.
- Real smoke tests use controlled addresses and sanitized synthetic values; no personal/client values enter screenshots, fixtures, logs, or artifacts.

## 10. Performance and Reliability

- Static-render Home, Paros, Plan My Trip shell, and confirmation. The form is the only substantial client island.
- Use `next/image` with intrinsic dimensions, `sizes`, priority only for the active above-fold hero, and art-directed approved crops where manifest data supports them.
- Do not ship all editorial JSON or both locales to the client; server components project only needed props.
- Keep form option arrays small and local; no global state library or runtime content fetch.
- Local storage writes are debounced; blur/navigation flushes prevent race loss. Guard stale debounce callbacks with cleanup/version checks.
- Submission has one in-flight request. Immediate retries reuse deterministic keys; edits generate a new submission ID.
- The lack of durable storage means Resend idempotency is only a prototype mitigation. Do not represent it as permanent deduplication.
- Acknowledgement is best-effort after agency acceptance. There is no queue or later replay.

## 11. Migration, Compatibility, and Rollback

- There is no production user database or public API migration.
- Existing bootstrap locale routes become showcase routes; preserve `/en`, `/el`, root redirect, invalid-locale 404, message parity, metadata, and browser guards.
- Draft record version starts at 1. Any incompatible future record is silently discarded; no migration machinery is needed.
- Existing fixture drafts do not exist. Storage key is new and isolated.
- Rollback is a normal source revert. Since no server data is persisted, rollback cleanup is limited to the browser draft key, which naturally expires within 72 hours.
- Do not remove `quality-lab` or bootstrap tests unless implementation proves they are obsolete and updates their explicit consumers in the same bounded change; keeping the unlinked route is acceptable.

## 12. Implementation Blueprint

### 12.1 Files to Create

- `app/[locale]/destinations/paros-antiparos/page.tsx`
- `app/[locale]/plan-my-trip/page.tsx`
- `app/[locale]/plan-my-trip/confirmation/page.tsx`
- `app/api/trip-request/route.ts`
- `components/layout/site-header.tsx`, `site-footer.tsx`, `language-switcher.tsx`
- focused `components/sections/*.tsx` for only the shared sections in §5.4
- `components/forms/trip-request-form.tsx` and four `components/forms/steps/*.tsx`
- `content/en/showcase.json`, `content/el/showcase.json`, `content/schemas/showcase.ts`
- `lib/content.ts`, `lib/routes.ts`, `lib/trip-request-schema.ts`, `lib/form-draft.ts`, `lib/email-payload.ts`, `lib/resend.ts`
- `emails/agency-notification.ts`, `emails/visitor-acknowledgement.ts`
- `scripts/validate-content.mjs`
- focused unit files under `tests/unit/content`, `tests/unit/forms`, `tests/unit/email`, `tests/unit/api`
- focused E2E file `tests/e2e/showcase-journey.spec.ts`

### 12.2 Files to Modify

| Path | Required change |
|---|---|
| `package.json`, `pnpm-lock.yaml` | Add `react-hook-form`, `zod`, `resend`; add `validate:content`; keep pinned pnpm contract. |
| `.env.example` | Add empty server-only variable names and comments; no values. |
| `app/[locale]/layout.tsx` | Install two fonts and shared page semantics while preserving locale validation/static params. |
| `app/[locale]/page.tsx` | Replace bootstrap Home with static showcase composition and localized metadata. |
| `app/globals.css` | Apply approved tokens, typography mappings, focus, form, layout, and reduced-motion base rules. |
| `next.config.ts` | Preserve `allowedDevOrigins`; add route-wide `Content-Security-Policy` compatible with Next/font/local images/Resend-free client code, `X-Content-Type-Options: nosniff`, `Referrer-Policy: strict-origin-when-cross-origin`, `Permissions-Policy: camera=(), microphone=(), geolocation=()`, and `X-Frame-Options: DENY`. |
| `messages/en.json`, `messages/el.json` | Add complete equal interface namespaces and remove fixture-only copy only when no longer consumed. |
| `tests/unit/messages/parity.test.ts` | Rename fixture description and retain recursive key parity. |
| `tests/e2e/localization-and-quality.spec.ts` | Replace/extend route metadata, switching, and keyboard matrices. |
| `tests/e2e/accessibility.spec.ts` | Cover showcase routes/states in both locales. |
| `unlighthouse.config.ts` | Scan representative Home, Paros, Plan My Trip, confirmation paths; preserve budgets. |

### 12.3 Explicitly Out of Scope Files/Areas

- Do not add routes for broader destinations, experiences, journeys, About, FAQ, Contact, legal pages, sitemap expansion, deployment, analytics, CRM, or CMS.
- Do not edit `.scratch/ralph-loop/completion-signal.json` or launch Ralph.
- Do not alter credentials, remote Git state, deployment configuration, or existing unrelated asset/content work except targeted manifest fields required after explicit asset approval.

### 12.4 Suggested Implementation Order

1. Add dependencies, content schema/loader/validator, route identities, locale content, and message parity.
2. Establish the complete documented foundational token system and fonts, then build the shared shell and six-section Home/Paros static pages using semantic utilities and only consumed component variants.
3. Define canonical form schema, draft module, four-step form, reset, and localized route continuity.
4. Add email model/templates/transport and the Route Handler with mocked integration tests.
5. Connect submission states and confirmation route, then add compact/wide end-to-end coverage.
6. Run focused tests, all repository gates, controlled email smoke when authorized, manual accessibility/media checks, and stop.

### 12.5 Stable Interfaces

- `routing.locales`, always-prefixed locale URLs, `/` → `/en`, and unsupported locale 404.
- `content/shared/media.json` stable ID boundary; page JSON never imports physical asset paths.
- `greek-essence.trip-request-draft.v1` version-1 shape for the lifespan of this showcase.
- `POST /api/trip-request` request/response shapes in §6.3.
- Agency acceptance boundary in DEC-007.
- Existing Unlighthouse score budgets and compact/wide Playwright viewport dimensions.

## 13. Test Strategy

### 13.1 Unit and Component Tests

| Requirements | Target test | Cases |
|---|---|---|
| FR-003, FR-013, FR-015 | routes/content/messages | fixed equivalent paths; locale key/structure parity; missing content/media rejected; metadata pairs. |
| FR-016 | foundational token contract | complete documented primitive/semantic/type/spacing/layout/shape/elevation/motion/state inventory; Tailwind v4 semantic mappings; no dark tokens or parallel TypeScript theme; only consumed component variants; compact/wide EN/GR visual, contrast, focus, and reduced-motion checks. |
| FR-004, FR-005, FR-008 | trip schema/reducer | editable structural schema accepts incomplete defaults/drafts; normalization to canonical values; every step valid/invalid boundary; date order including same-day/past acceptance; integer strings/counts; child-age mismatch; allow-listed options; contact dependency; privacy required; strict unknown keys; Unicode code-point limits; phone character/digit limits. |
| FR-006, FR-007 | form draft | 1000 ms debounce; blur flush; exactly-before/at/after 72-hour expiry; exact timestamp relationship; future/corrupt/version/storage exceptions; structurally valid incomplete restore; clear confirmation; submission-ID reuse/invalidation. |
| FR-009, FR-010 | email mapper/templates | exact subject; canonical field order; enum label+ID; null/empty/child-age formatting; HTML escaping; JSON filename/content/UTF-8; EN/GR acknowledgement; prohibited-claim regression strings. |
| FR-008, FR-011 | Route Handler | accepted/rejected Content-Type grammar; 32,768/32,769-byte boundary; absent/present/cross-site headers; missing/malformed config; malformed JSON; 422 dot/index paths; agency failure with no acknowledgement call; full success; acknowledgement-only failure; safe response/logging. |
| FR-014 | form component | pending button guard, retained values, safe retry, focus summary, Back behavior. |

### 13.2 Playwright Critical Flows

Run every critical flow in `chromium-compact` and `chromium-wide`:

1. EN Home → Paros → contextual Plan My Trip → complete four steps → mocked accepted response → EN confirmation.
2. GR equivalent complete journey with Greek labels/messages and acknowledgement locale in intercepted payload.
3. Enter through Paros, edit destination, reach Step 3, switch language, and verify equivalent route, step, values, and translated labels.
4. Refresh after pending-debounce flush and verify restored values; seed expired/corrupt draft and verify silent clean form.
5. Mobile family flow with children and ages; verify confirmation before destructive count reduction.
6. Validation journey using keyboard: linked summary, associated messages, focus movement, Back without validation, 200% zoom spot check.
7. Intercept agency-style 503: data/draft remain, retry uses same submission ID, then 200 clears draft and confirms.
8. Intercept accepted response with `acknowledgement: "failed"`: confirmation remains success and contains no resubmit direction.
9. Metadata/canonical/hreflang/noindex matrix for all eight localized page URLs.
10. Browser guards report zero unexpected console, page, request, or HTTP failures and no horizontal overflow.

`chromium-medium` remains in the full suite for responsive regression but is not a duplicate critical-flow sign-off requirement.

### 13.3 Accessibility and Manual Validation

- Axe WCAG 2.2 A/AA on EN/GR Home, Paros, Step 1, Step 4 error state, and confirmation at compact/wide.
- Keyboard-only complete form, compact menu Escape/focus return, locale switch, Start Over cancel/confirm, error-summary links, and submission retry.
- Manual 320 px, 390 px, 834 px, 1440 px, landscape, 200% zoom, reduced motion, and forced colors where supported.
- Confirm 44 × 44 targets where practical, 4.5:1 body contrast, 3:1 UI/focus boundaries, hero crop/scrim readability, Greek glyphs, and no clipped/overflowing Greek copy.
- Inspect Network/Console for PII exposure, failed critical resources, duplicate submissions, and unexpected requests.
- Controlled Resend smoke with synthetic values: agency inbox receives readable HTML/text plus correct JSON attachment; controlled visitor receives the correct locale acknowledgement. Record only sanitized outcome, never addresses or payload.

### 13.4 Performance and Media

- Unlighthouse must preserve performance ≥90, accessibility 100, best practices ≥95, SEO ≥95.
- Check Home, Paros, and Plan My Trip with final representative approved media. Confirmation is included for route/metadata/accessibility, not used as the only performance sample.
- Verify responsive source selection, intrinsic dimensions, no avoidable layout shift, one prioritized hero per page, and meaningful fallback with media disabled.

## 14. Validation Commands

Run from repository root with standalone pnpm 11.17.0:

```bash
pnpm format:check
pnpm lint
pnpm typecheck
pnpm validate:content
pnpm test:unit
pnpm build
pnpm exec playwright test --project=chromium-compact tests/e2e/showcase-journey.spec.ts tests/e2e/localization-and-quality.spec.ts tests/e2e/accessibility.spec.ts
pnpm exec playwright test --project=chromium-wide tests/e2e/showcase-journey.spec.ts tests/e2e/localization-and-quality.spec.ts tests/e2e/accessibility.spec.ts
pnpm test:e2e
pnpm test:a11y
pnpm quality:unlighthouse
pnpm check:all
```

Expected outcomes:

- Every command exits 0.
- Content validation reports complete English/Greek structures and valid approved media references.
- Compact and wide critical flows pass with no unexpected browser failures.
- Full E2E includes medium responsive regression.
- Axe reports no selected WCAG A/AA violations.
- Unlighthouse meets existing budgets without configuration reductions.
- Build remains static for public routes with only `/api/trip-request` dynamic.

The controlled real Resend smoke is an operator-authorized manual gate after these commands and is not encoded with real recipients in scripts.

## 15. Observability and Debugging

- No analytics or external monitoring is added.
- Server failures may log `{reference, code, providerStatusClass}` only. Never log payload, address, provider body, attachment, or rendered email.
- Client failure UI shows only a localized generic message and correlation reference when returned.
- Debug sequence:
  1. Validation errors: inspect `tripRequestSubmitSchema` issue mapping and localized message key.
  2. Draft recovery: inspect the single storage key in a local synthetic session, record version/timestamps, and fake-timer tests.
  3. Delivery: inspect sanitized server code/reference and Resend dashboard only with operator authorization.
  4. Locale mismatch: compare message key parity, content structure validation, route identity, and canonical option IDs.
  5. Browser failure: use retained Playwright trace/screenshot/video under existing artifact paths, ensuring fixtures contain no real PII.

## 16. Risks and Mitigations

| Risk | Impact | Likelihood | Mitigation |
|---|---:|---:|---|
| Scope imports broader prototype pages/fields | high | medium | Fixed section/field lists, explicit non-goals, strict 12-hour stop. |
| Accepted feature decisions conflict with broader docs | high | high | Feature decisions explicitly override only narrowed choices; conflicts are listed in §0. |
| PII leaks to logs/artifacts | high | low | Strict logging contract, synthetic tests, no body/provider output, review Network/Console/artifacts. |
| Duplicate agency email on uncertain retry | medium | medium | Stable submission ID and deterministic provider key for immediate retries; disclose prototype limitation internally. |
| Acknowledgement failure causes duplicate request | high | low | Agency acceptance is final browser success; acknowledgement outcome is non-blocking. |
| Local storage loses or exposes draft | medium | medium | Version/schema/expiry, guarded writes, silent cleanup, Start Over, 72-hour limit; no claim of private-device security. |
| Greek layout is treated as secondary | high | low | Structural/message parity gates and full Greek critical journey. |
| Provisional media is rendered as approved | medium | medium | Manifest approval fields required for render; neutral fallback and content validator. |
| External fonts/media harm performance | medium | low | Two families/limited weights, `next/font`, responsive local images, preserved budgets. |
| Missing runtime config blocks build | medium | medium | Lazy server validation; static build/tests use injected transport; endpoint fails closed at runtime. |

## 17. Traceability Matrix

| Requirement/Decision | Implemented by | Tested by | Evidence |
|---|---|---|---|
| DEC-001, FR-001 | Home route/content/sections | Home E2E, content validation | `DECISIONS.md:22-48`; current `app/[locale]/page.tsx` |
| DEC-002, FR-002 | Paros route/content/sections | destination E2E, visual checks | `DECISIONS.md:35-48`; prototype page spec destination detail |
| DEC-003, SUBDEC-001, FR-004/005 | form schema/reducer/steps | schema/component/E2E | form contract lines 5-49 |
| DEC-004/005, SUBDEC-002, FR-006/007 | draft module/form | fake-timer + persistence E2E | draft contract lines 5-34 |
| DEC-006/007, SUBDEC-003, FR-009/010/011 | email mapper/templates/route | template/route/failure E2E | email contract lines 5-43 |
| DEC-008, SUBDEC-004, FR-003/013/015 | content/messages/routes/switcher | parity/metadata/GR journey | bilingual contract lines 5-37 |
| DEC-010 | content loader + static pages + one API route | build output/route tests | root `AGENTS.md:11-17`; technical decisions lines 5-18 |
| DEC-011/013, FR-016, NFR-001/002/003 | complete global token foundation, fonts, consumed components, and media | token contract plus visual/a11y/performance checks | design token/theme/color/type/spacing/layout/state docs |
| DEC-012 | Playwright/Unlighthouse configs | exact commands in §14 | `playwright.config.ts:27-39`; `unlighthouse.config.ts:15-21` |
| NFR-004/005/006 | schema/draft/route/transport | security/failure tests and manual inspection | technical privacy lines 3-33 |

## 18. Handoff Checklist

- [x] Locked decisions and normative contracts are represented.
- [x] Safe assumptions and runtime-only human inputs are explicit.
- [x] Current code paths, versions, gaps, and dirty-worktree constraint are mapped.
- [x] Proposed modules have named purposes, interfaces, and consumers.
- [x] Every functional requirement has implementation, acceptance, and test targets.
- [x] Error, degraded, privacy, security, retry, and acknowledgement-partial-failure behavior is defined.
- [x] File boundaries and implementation order are explicit.
- [x] Validation commands and expected outcomes are exact.
- [x] No chat history is required.

## Appendix A — Evidence Index

| ID | Source | Relevant lines/symbols | What it proves |
|---|---|---|---|
| EVD-001 | `AGENTS.md` | 9-17, 19-33, 77-91 | Authority, static-first architecture, proportional Tier-2 scope, approved gates. |
| EVD-002 | `package.json` | 6-27, 30-70 | Runtime/tool versions, existing scripts, absent form/email dependencies. |
| EVD-003 | `app/[locale]/layout.tsx` | `generateStaticParams`, `dynamicParams`, provider | Existing static explicit-locale boundary. |
| EVD-004 | `i18n/routing.ts` | `defineRouting` | Exact `en`/`el`, default EN, always-prefixed URLs. |
| EVD-005 | `app/[locale]/page.tsx` | `generateMetadata` | Existing canonical/hreflang/noindex pattern. |
| EVD-006 | `content/shared/media.json` | schema/defaults/assets | Stable IDs/files/dimensions and pending approval metadata. |
| EVD-007 | `tests/unit/messages/parity.test.ts` | `collectKeyPaths` | Existing recursive locale parity pattern. |
| EVD-008 | `tests/e2e/browser-guards.ts` | `installBrowserGuards` | Existing no-console/network/page-error gate. |
| EVD-009 | `playwright.config.ts` | projects | 390, 834, and 1440 viewport contracts. |
| EVD-010 | `unlighthouse.config.ts` | `ci.budget` | Existing score budgets. |
| EVD-011 | `docs/03_technical_design/04_project_and_file_architecture.md` | boundary rules | Shallow route/component/content/lib/email boundaries. |
| EVD-012 | `docs/03_technical_design/18_testing_and_quality_gates.md` | 3-42 | Playwright-led coverage and client-presentation gates. |
| EVD-013 | feature `DECISIONS.md` and four contracts | all accepted decisions | Narrow authoritative showcase behavior. |

## Appendix B — Conflict Resolution Record

1. Broader technical/form docs include budget, residence, first visit, accommodation preference, marketing consent, and visible saved-draft notices. Accepted D-002/D-003 remove those for this showcase; they are not implemented.
2. Broader technical docs require both emails before success. Accepted D-004 makes agency acceptance the boundary; acknowledgement-only failure remains success.
3. Broader technical architecture names React Email and a lightweight rate-limit module. For this strict showcase, escaped typed HTML/text functions are sufficient, and any in-memory request guard must not be represented as durable protection.
4. Broader Home/destination hierarchies contain extra catalogues and sections. D-001 narrows both pages to the exact six-section compositions in §5.4.

## Appendix C — Glossary

| Term | Meaning |
|---|---|
| Showcase | Bounded bilingual four-route Tier-2 client demonstration, not the full product or production site. |
| Plan My Trip | Site-wide CTA entering the request flow; it does not create a booking. |
| Request a Custom Itinerary | Form page title for human follow-up qualification. |
| Demo request | Server-validated prototype trip-planning submission accepted through the agency email boundary. |
| Draft | One versioned canonical 72-hour localStorage record shared across locales. |
| Agency acceptance | Resend accepts the agency notification request with its JSON attachment; this is browser success. |

<!-- milestone-plan:start -->

## Milestones

> Milestone plan for greek-essence-showcase-SPEC-001. Each milestone is a demoable, end-to-end increment; its slug becomes the `Milestone:` tag on the issues stage 3 writes. Generated by `jz-spec-to-milestones`.

### 1. Explore the bilingual showcase — `explore-bilingual-showcase`

- **Decomposed:** 2026-07-24T11:32:24.956Z
- **Demo:** A visitor browses Home and Paros & Antiparos in English or Greek, switches locale without losing the equivalent route, and sees complete responsive editorial pages with safe media fallbacks and localized metadata.
- **DependsOn:** none
- **Delivers:** FR-001, FR-002, FR-003 (Home and destination route equivalence), FR-013 (editorial content and shared-message parity), FR-015 (Home and destination metadata), FR-016; NFR-001, NFR-002, NFR-003, NFR-004, NFR-005, NFR-007, NFR-008; DEC-001, DEC-002, DEC-008, DEC-010, DEC-011, DEC-012, DEC-013, SUBDEC-004
- **Carries:** QUE-003 (default: render the intentional neutral fallback until generated media has complete approval metadata)
- **Scope:** Deliver the polished static-first discovery journey and its localized navigation, content validation, metadata, accessibility, responsiveness, and performance proof. Establish the complete documented reusable token foundation through Tailwind CSS v4 semantic utilities, while creating component-level tokens and variants only for showcase consumers; keep all editorial meaning available when provisional imagery is not approved.

### 2. Complete a resilient bilingual trip request — `complete-resilient-trip-request`

- **Decomposed:** pending
- **Demo:** A visitor enters from Paros, completes the exact four-step request in either locale, refreshes or switches language without losing progress, and can safely cancel or confirm Start Over.
- **DependsOn:** `explore-bilingual-showcase`
- **Delivers:** FR-003 (Plan My Trip route, step, and canonical-value continuity), FR-004, FR-005, FR-006, FR-007, FR-013 (form options, validation, states, and message parity), FR-015 (Plan My Trip metadata); NFR-001, NFR-002, NFR-003, NFR-004, NFR-005, NFR-006, NFR-007, NFR-008; DEC-003, DEC-004, DEC-005, DEC-008, DEC-010, DEC-012, SUBDEC-001, SUBDEC-002, SUBDEC-004
- **Carries:** none
- **Scope:** Add the user-triggered form vertical from contextual entry through all accepted fields, dependent child ages, validation and recovery, one silent 72-hour canonical draft, confirmed reset, and locale-preserving navigation. Keep the form as the only substantial client island and preserve the approved privacy and accessibility boundaries.

### 3. Submit safely and reach confirmation — `submit-safely-and-confirm`

- **Decomposed:** pending
- **Demo:** A visitor submits a valid request, sees failures preserve an explicitly retryable draft, and after agency acceptance reaches a localized PII-free confirmation even when the visitor acknowledgement fails.
- **DependsOn:** `complete-resilient-trip-request`
- **Delivers:** FR-008, FR-009, FR-010, FR-011, FR-012, FR-014, FR-015 (confirmation metadata); NFR-001, NFR-002, NFR-003, NFR-004, NFR-005, NFR-006, NFR-007, NFR-008; DEC-006, DEC-007, DEC-008, DEC-010, DEC-012, SUBDEC-003, SUBDEC-004
- **Carries:** QUE-001 (default: automated tests use an injected transport mock and the production endpoint fails closed until approved Resend configuration exists); QUE-002 (default: do not send acknowledgement smoke tests to arbitrary or real visitor addresses)
- **Scope:** Deliver the complete submission trigger, strict server validation and privacy/security boundary, agency-first email with canonical JSON attachment, best-effort localized acknowledgement, deterministic immediate retry behavior, honest confirmation, and compact/wide end-to-end failure matrix. Real delivery smoke remains an operator-authorized gate and does not block the automated demo.

### Coverage

| Requirement | Milestone |
| --- | --- |
| FR-001 | `explore-bilingual-showcase` |
| FR-002 | `explore-bilingual-showcase` |
| FR-003 (Home and destination route equivalence) | `explore-bilingual-showcase` |
| FR-003 (Plan My Trip route, step, and canonical-value continuity) | `complete-resilient-trip-request` |
| FR-004 | `complete-resilient-trip-request` |
| FR-005 | `complete-resilient-trip-request` |
| FR-006 | `complete-resilient-trip-request` |
| FR-007 | `complete-resilient-trip-request` |
| FR-008 | `submit-safely-and-confirm` |
| FR-009 | `submit-safely-and-confirm` |
| FR-010 | `submit-safely-and-confirm` |
| FR-011 | `submit-safely-and-confirm` |
| FR-012 | `submit-safely-and-confirm` |
| FR-013 (editorial content and shared-message parity) | `explore-bilingual-showcase` |
| FR-013 (form options, validation, states, and message parity) | `complete-resilient-trip-request` |
| FR-014 | `submit-safely-and-confirm` |
| FR-015 (Home and destination metadata) | `explore-bilingual-showcase` |
| FR-015 (Plan My Trip metadata) | `complete-resilient-trip-request` |
| FR-015 (confirmation metadata) | `submit-safely-and-confirm` |
| FR-016 | `explore-bilingual-showcase` |
| NFR-001 | cross-cutting |
| NFR-002 | cross-cutting |
| NFR-003 | cross-cutting |
| NFR-004 | cross-cutting |
| NFR-005 | cross-cutting |
| NFR-006 | cross-cutting |
| NFR-007 | cross-cutting |
| NFR-008 | cross-cutting |

<!-- milestone-plan:end -->

## SPEC Quality Verdict

- Self-contained contract: PASS
- No placeholders: PASS
- Decision coverage: PASS
- Evidence coverage: PASS
- Requirement traceability: PASS
- Interface completeness: PASS
- Error/edge-case coverage: PASS
- Testability: PASS
- Implementation boundaries: PASS
- Fresh-agent review: PASS

Overall: PASS

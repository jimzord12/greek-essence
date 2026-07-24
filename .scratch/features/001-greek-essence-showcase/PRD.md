# Greek Essence Showcase — Product Requirements

## 1. Purpose

Build a polished Tier-2 showcase that demonstrates our ability to create a modern, attractive, fast, professional, and responsive travel website.

This is a client-demo prototype, not the final Greek Essence product. Content, destinations, imagery, and business details are provisional and can change later.

## 2. Demo Story

The demonstrated journey is:

**Inspiration → destination expertise → conversion**

A visitor should be able to:

1. Discover Greek Essence on the Home page.
2. Open a Paros & Antiparos destination page.
3. Start and complete a four-step Plan My Trip form.
4. Keep form progress after refresh through local storage.
5. Submit the request and trigger an automated Resend email.
6. See a clear confirmation or useful error state.
7. Complete the same demonstrated journey in English and Greek.

## 3. Target Audience

The primary audience is a prospective client viewing the prototype during a meeting.

The showcase should communicate:

- We can design polished modern websites.
- We can build practical responsive interfaces.
- We can implement real features, not only static mockups.
- The demonstrated design and content are flexible starting points, not final commitments.

## 4. Required Pages and Routes

The showcase requires English and Greek versions of:

1. **Home** — establishes the visual direction and inspires exploration.
2. **Paros & Antiparos** — demonstrates destination storytelling and expertise.
3. **Plan My Trip** — provides a polished four-step form.
4. **Confirmation** — confirms the demo submission clearly and honestly.

Route names should follow the existing localized Next.js routing conventions in the repository.

## 5. Required Capabilities

### 5.1 Visual design

- Implement the complete reusable foundational token system defined by `docs/04_design`: documented primitive and semantic colors; typography roles; spacing; containers and gutters; responsive modes; radii; borders; surfaces; shadows; motion/easing; focus; and reusable interaction/status states.
- Centralize that foundation through Tailwind CSS v4 CSS-first theme variables in `app/globals.css` or an imported token stylesheet; expose semantic utilities, keep light appearance only, and do not create a second TypeScript theme object.
- Treat documented provisional values as the implementation baseline, preserving semantic names so visual, bilingual, imagery, and accessibility review can tune values centrally without changing the accepted design direction.
- Professional desktop and mobile layouts.
- Reusable components and component-level tokens only where the demonstrated pages genuinely consume them; do not prebuild the wider product's unused component library.
- Images supplied as replaceable component values rather than structural dependencies.
- Stable media contracts for aspect ratio, crop/focal position, alt text, and fallbacks.

### 5.2 Responsive behavior

- The complete demo journey must work on desktop and mobile.
- Navigation, content sections, cards, imagery, and form controls must adapt cleanly.
- No horizontal overflow, clipped content, or unusable controls on demonstrated viewports.

### 5.3 Internationalization

- Every demonstrated route and interaction must support English and Greek.
- The language switcher should preserve the equivalent route and relevant form progress where practical.
- Provisional copy is acceptable; exact destination and marketing wording is not a showcase blocker.

### 5.4 Multi-step form

- Four clear steps with visible progress.
- Back and next navigation.
- Useful validation and error messages.
- Form state saved in `localStorage` and restored after refresh.
- Destination context may be preselected when entering from the Paros page.
- Loading, success, failure, and retry behavior.

### 5.5 Resend email

- A successful form submission sends an automated email through Resend.
- The email contains the useful demo request details.
- Secrets remain server-side and outside the repository.
- Provider errors produce an honest recoverable error state.
- This prototype does not require queues, CRM integration, delivery tracking, or production email operations.

### 5.6 Quality

- Semantic structure and keyboard-accessible interactions.
- Visible focus states and accessible labels/errors.
- Responsive images and minimal unnecessary client JavaScript.
- No obvious console errors or broken links during the demo.
- Preserve the repository's existing quality budgets and required verification commands.

## 6. Content and Asset Rules

- AI-generated showcase images may be used without licensing restrictions.
- Images can be generated or replaced after component design; they do not control the architecture.
- English and Greek copy may be provisional.
- Destination accuracy is secondary to showing the design and technical capability.
- Do not invent sensitive claims about partners, awards, pricing, availability, legal terms, response times, or confirmed operations.

## 7. Scope

### In scope

- Complete documented foundational design-token system and semantic Tailwind utility mapping for the showcase.
- Minimum shared header, footer, language control, content-section, card, media, CTA, and form components needed by the demonstrated routes.
- Home page.
- Paros & Antiparos page.
- Four-step Plan My Trip form with local storage.
- Resend submission and confirmation/error behavior.
- English and Greek.
- Desktop/mobile polish, focused accessibility, performance checks, QA, and demo rehearsal.

### Out of scope

- Complete sitemap or full destination catalogue.
- Every planned component in the wider product documentation.
- Unused component-level tokens, variants, or primitives for out-of-scope wider-product surfaces.
- CMS, database, CRM, analytics, booking, pricing, availability, accounts, or payments.
- Production infrastructure or public production launch.
- Final legal, operational, or marketing content.
- Destination filters, hero video, or advanced animation.
- Production-grade email delivery operations.

## 8. Product Success Criteria

The showcase succeeds when, in a client meeting:

1. The operator can demonstrate Home → Paros → Plan My Trip → confirmation in both languages.
2. The website looks professional on desktop and mobile.
3. Form progress survives a refresh.
4. A valid submission triggers the Resend email.
5. Failure behavior is understandable and recoverable.
6. The core design system is visually clear and consistent.
7. The application passes the agreed focused quality checks without lowering existing budgets.
8. The result is clearly presented as a flexible prototype rather than a finished production product.

## 9. Delivery Constraints

- Implementation target: a strict 12-hour showcase window after planning and required credentials are available.
- Engineering depth: Tier 2 — Prototype.
- Prefer the simplest maintainable solution that demonstrates the required capability.
- Stop when the approved showcase acceptance criteria pass; do not expand into unrelated product work.

## 10. Open Decisions for Grilling

The grilling session should confirm only decisions that materially affect implementation, including:

- Exact Home and destination section selection.
- Minimum reusable component boundary.
- Form fields and four-step grouping.
- Resend recipient/sender setup and email content.
- Local-storage lifetime and reset behavior.
- Visual direction within the existing design documentation.
- Exact demo viewports and final acceptance commands.

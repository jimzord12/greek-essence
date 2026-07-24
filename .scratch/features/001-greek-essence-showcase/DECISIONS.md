# Greek Essence Showcase — Accepted Design Decisions

## Status

- Feature: `greek-essence-showcase`
- Engineering depth: Tier 2 — Prototype
- Design grilling: Complete after 5 operator questions
- Purpose: Authoritative consolidated choices for later SPEC authoring
- Scope boundary: These decisions narrow the showcase implementation; they do not rewrite the broader future-product documentation.

## Authority baseline

The accepted feature remains a bilingual client-demo prototype proving:

- a polished Home → Paros & Antiparos → Plan My Trip → confirmation journey;
- desktop and mobile responsive quality;
- four-step form behavior and browser draft recovery;
- real Resend agency notification and visitor acknowledgement;
- editorial boutique-hospitality design using the existing warm-ivory, deep-Aegean, muted-teal, Cormorant Garamond, and Inter direction;
- simple, maintainable delivery within the strict 12-hour target.

## D-001 — Focused cinematic page composition

### Decision

Home contains:

1. Cinematic hero.
2. Concise brand promise.
3. Paros-led destination module.
4. Compact How It Works.
5. One trust/story block.
6. Final CTA.

Paros & Antiparos contains:

1. Destination hero.
2. Editorial introduction and defining character.
3. Traveler fit.
4. Signature experiences with culture/gastronomy.
5. One destination-combinations block.
6. Final CTA.

Separate sample-journey and accommodation sections are omitted unless useful content can be folded naturally into retained sections without expanding scope.

### Rationale

This retains enough editorial depth to demonstrate visual quality and destination expertise while protecting form/email implementation time and polish.

## D-002 — Compact but credible four-step qualification

### Decision

1. **Trip:** Editable destination context; approximate arrival/departure dates or a clear flexible-timing path.
2. **Travelers:** Adults; children; conditional child ages; trip type.
3. **Preferences:** Interests; preferred pace; optional notes.
4. **Contact:** Full name; email; optional phone/WhatsApp; preferred contact method; required privacy acknowledgement.

Budget, country of residence, first-visit status, accommodation preference, a separate considered-destinations field, and duplicate notes are omitted.

### Rationale

The form demonstrates useful qualification, conditional fields, validation, localization, persistence, and email payloads without becoming exhausting or inventing business policy.

### Contract

[contracts/D-002-showcase-form-fields.md](contracts/D-002-showcase-form-fields.md)

## D-003 — Silent bilingual 72-hour draft

### Decision

- Store one canonical draft shared by equivalent English and Greek form routes.
- Autosave meaningful changes with a 1000 ms debounce.
- Also save when a field loses focus, flushing pending debounced changes.
- Restore after refresh and equivalent-language switching.
- Provide Start Over with confirmation.
- Keep storage invisible during normal operation: no save, restore, expiry, or cleanup messaging.
- Silently remove expired, corrupt, incompatible, or unreadable data and show a clean form.
- Preserve the draft through validation and submission failures.
- Clear it only after confirmed successful submission or confirmed Start Over.
- Expire it 72 hours after the last meaningful update.

### Rationale

This demonstrates seamless resilience without burdening visitors with storage mechanics and reduces data loss around quick navigation.

### Contract

[contracts/D-003-draft-persistence.md](contracts/D-003-draft-persistence.md)

## D-004 — Branded agency notification and visitor acknowledgement

### Decision

A valid submission sends two emails through Resend:

1. **Agency notification**
   - Sent to a configured agency inbox.
   - Prints every accepted form field in structured, polished, scan-friendly HTML grouped by form step.
   - Includes an attached UTF-8 JSON file containing the same canonical validated values.

2. **Visitor acknowledgement**
   - Sent to the validated visitor email in the submission language.
   - Confirms receipt without implying a booking, guaranteed response time, price, or availability.
   - Uses polished email-safe HTML/CSS expressing calm trust, professionalism, warmth, and Greek Essence's editorial boutique-hospitality identity.

The agency notification is the submission-acceptance boundary. If it fails, preserve the form and offer retry. If only the acknowledgement fails after agency acceptance, retain on-screen success and do not ask the visitor to resubmit.

Addresses, verified domain, and credentials are runtime configuration outside Git.

### Rationale

This proves a useful agency workflow and a credible customer-facing experience while preventing acknowledgement failures from producing duplicate requests.

### Contract

[contracts/D-004-showcase-emails.md](contracts/D-004-showcase-emails.md)

## D-005 — Full English/Greek feature parity

### Decision

- Every accepted showcase section, interaction, form field, validation/error, loading state, failure/retry state, confirmation state, and visitor acknowledgement exists in both English and Greek.
- Switching languages preserves the equivalent route, current form step, destination context, and canonical draft values.
- Exact marketing and destination wording may remain provisional, but both locales must be complete and layout-realistic.
- Missing required localized content is a defect; the accepted showcase does not use a reduced Greek mode or silently fall back to mixed-language UI.

### Rationale

Bilingual parity is part of the demonstrated product capability, while provisional copy keeps the requirement proportionate to the showcase timeline.

### Contract

[contracts/D-005-bilingual-parity.md](contracts/D-005-bilingual-parity.md)

## D-006 — Complete foundational token system, bounded component system

### Decision

- Implement the complete reusable foundation specified by `docs/04_design`: primitive and semantic colors; typography roles; spacing; containers and gutters; responsive modes; radii; borders; surfaces; shadows; motion/easing; focus; and reusable interaction/status states.
- Use Tailwind CSS v4's CSS-first `@theme` / `@theme inline` architecture in `app/globals.css` or a centrally imported token stylesheet. Semantic CSS variables and utilities are the implementation source of truth; do not create a parallel TypeScript theme object.
- Use every documented provisional value as the implementation baseline, then tune centrally only when representative English/Greek content, approved imagery, contrast, accessibility, or responsive QA provides evidence.
- Keep the prototype light-only. Do not add dark-mode tokens, switching, or system-theme behavior.
- Create component tokens, variants, and primitives only for components actually consumed by the accepted four-route showcase. Do not prebuild the broader product's unused component library.

### Rationale

The design documentation is sufficiently complete to establish one coherent, low-cost foundation now. Implementing it centrally prevents ad hoc styling and makes later visual tuning safe, while withholding unused component APIs preserves the Tier-2 timebox and avoids speculative code.

## Acceptance inherited from repository authority

No additional operator decision is needed for acceptance viewports or commands because existing authority already fixes them:

- critical Playwright flows at 390 px and 1440 px;
- `pnpm lint`, `pnpm typecheck`, `pnpm validate:content`, and `pnpm build`;
- focused desktop/mobile, form persistence, bilingual, email, accessibility, metadata, console/network, and representative-media checks documented by the repository.

The later SPEC must remain proportional to the accepted four-route showcase rather than importing unrelated broader prototype flows.

## Explicitly rejected directions

- Full broader Home/destination hierarchy within the 12-hour showcase.
- Ultra-lean pages that fail to demonstrate editorial depth.
- Broad qualification form or invented budget ranges.
- Persistent-forever or per-language-session-only draft behavior.
- Internal-only or operator-only email behavior.
- Reduced Greek editorial/interactions or demo-path-only translation.
- A partial ad hoc token subset that bypasses the documented reusable foundation.
- Prebuilding unused wider-product components or component-token APIs under the name of design-system completeness.

## Remaining inputs, not design blockers

The implementation operator will later provide or confirm runtime values without reopening design:

- Resend API credentials and verified sender/domain;
- configured agency recipient inbox;
- approved test recipient(s) for controlled email smoke testing;
- final logo/media assets if available, otherwise approved replaceable showcase assets.

No SPEC, milestone, issue, implementation contract, application code, credential handling, deployment, or remote Git action is authorized by this document.

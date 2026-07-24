# Greek Essence Showcase — Grill Session

## Protocol

- Ask exactly one decision question at a time.
- Offer 2–4 clear numbered options.
- Prefix the recommended option exactly with `(recommended):`.
- Ask only high-impact questions not already fixed by direct instruction, `PRD.md`, or repository authority.
- Persist every accepted answer before asking the next question.
- Hard cap: 20 total operator questions, including follow-ups.

## User Preferences

- Optimize for a polished, practical, fast, professional client demo rather than production breadth.
- Prefer simple implementation suitable for a solo mid-level developer and a strict 12-hour target.
- Provisional copy, destination facts, and replaceable AI imagery must not consume decision bandwidth.
- Keep the grilling relentless but limited to choices that could materially change expectations.

## Current Design Target

- Feature: `greek-essence-showcase`
- Area: High-impact showcase design decisions before SPEC authoring.
- Goal: Lock page composition, demo narrative, form/persistence/email behavior, bilingual continuity, responsive acceptance, and bounded implementation scope.

## Accepted Authority Baseline

- Tier 2 client-demo prototype, not a production product.
- Localized Home, Paros & Antiparos, Plan My Trip, and confirmation routes.
- Demo narrative: inspiration → destination expertise → conversion.
- Four-step form with progress, validation, Back/Continue, recoverable failure/retry, and destination-context prefill.
- Draft restoration through `localStorage`.
- Successful submission sends useful request details through Resend; provider failure must be honest and recoverable.
- Editorial boutique-hospitality visual direction: warm ivory, deep Aegean blue, muted teal, Cormorant Garamond + Inter, generous spacing, cinematic still imagery, light theme, restrained motion.
- Desktop and mobile completion in both English and Greek; no advanced animation, booking capabilities, or production operations.

## Locked Decisions

### D-001: Focused cinematic page composition

Decision:

- Home uses a cinematic hero, concise brand promise, Paros-led destination module, compact How It Works, one trust/story block, and final CTA.
- Paros & Antiparos uses a destination hero, editorial introduction/character, traveler fit, signature experiences with culture/gastronomy, one combinations block, and final CTA.
- Separate sample-journey and accommodation sections are omitted unless their useful content can be folded naturally into the retained blocks without expanding scope.

Why:

- It preserves enough editorial depth to demonstrate visual and destination-storytelling quality while protecting form/email implementation time and the strict 12-hour target.

Scope:

- This is the accepted showcase composition, not a change to the broader future-product documentation.

### D-002: Compact but credible four-step qualification

Decision:

- Step 1 — Trip: editable destination context plus approximate dates or a flexible-timing path.
- Step 2 — Travelers: adults, children, conditional child ages, and trip type.
- Step 3 — Preferences: interests, preferred pace, and optional notes.
- Step 4 — Contact: full name, email, optional phone/WhatsApp, preferred contact method, and required privacy acknowledgement.
- Budget and country of residence are omitted, along with the broader form's lower-value secondary fields.

Why:

- This demonstrates conditional fields, validation, bilingual controls, persistence, and a useful email payload without turning the showcase into a long qualification exercise or inventing commercial policy.

Scope:

- The grouping and required/optional intent are normative; exact provisional labels and option copy can be refined during SPEC authoring.

Contract:

See [contracts/D-002-showcase-form-fields.md](contracts/D-002-showcase-form-fields.md).

### D-003: Silent bilingual 72-hour draft

Decision:

- Use one canonical draft shared across equivalent English and Greek form routes.
- Autosave meaningful changes with a 1000 ms debounce and also save when a field loses focus.
- Restore after refresh or language switching.
- Provide an explicit Start Over action with confirmation.
- Treat storage as invisible: do not show routine save, restore, expiry, or cleanup messaging.
- Silently remove expired, corrupt, incompatible, or unreadable data and present a clean form.
- Clear a valid draft only after confirmed successful submission or confirmed Start Over.

Why:

- This demonstrates seamless resilience and bilingual continuity without turning browser storage into user-facing product complexity. Saving on focus loss reduces the chance that navigation immediately after editing misses the pending debounced change.

Scope:

- Draft lifetime is 72 hours from the last meaningful update. Submission failures and retries preserve the draft.

Contract:

See [contracts/D-003-draft-persistence.md](contracts/D-003-draft-persistence.md).

### D-004: Branded agency notification and visitor acknowledgement

Decision:

- Send every accepted form field to the configured agency inbox in a well-structured, polished HTML email grouped for easy scanning.
- Attach a JSON file containing the same canonical submitted values.
- Send the visitor a separate acknowledgement in the submission language so they know the request was received.
- Give the acknowledgement polished email-safe styling that communicates calm trust, professionalism, warmth, and the Greek Essence identity.
- Agency-notification acceptance is the submission success boundary. If that fails, preserve the form and allow retry. If only the acknowledgement fails afterward, retain on-screen success and do not ask the visitor to resubmit.

Why:

- This demonstrates both useful agency operations and a credible customer-facing experience while preventing acknowledgement failure from creating duplicate requests.

Scope:

- Runtime addresses, verified sending domain, and credentials are configuration supplied later and remain outside Git. Email styling must degrade safely and must not invent claims or operational promises.

Contract:

See [contracts/D-004-showcase-emails.md](contracts/D-004-showcase-emails.md).

### D-005: Full English/Greek feature parity

Decision:

- Every accepted showcase section, interaction, form field, validation/error, loading state, failure/retry state, confirmation state, and visitor acknowledgement exists in both English and Greek.
- Switching languages preserves the equivalent route, current form step, destination context, and canonical draft values.
- Exact marketing and destination copy may remain provisional, but both languages must be complete and layout-realistic.
- Missing required localized content is a defect; the showcase does not use reduced Greek coverage or silent mixed-language fallback.

Why:

- Translation breadth is straightforward compared with the interaction work, and true parity demonstrates a genuinely bilingual product rather than a translated happy-path mock.

Scope:

- The visitor acknowledgement uses the submission language. The agency notification may use one operational language while identifying the visitor locale.

Contract:

See [contracts/D-005-bilingual-parity.md](contracts/D-005-bilingual-parity.md).

## Rejected Options

### R-001: Full documented hierarchy

Rejected because it risks spreading the 12-hour build too thin and reducing polish.

### R-002: Ultra-lean conversion demo

Rejected because it would not demonstrate enough editorial depth or destination expertise.

## Open Questions

_No unresolved high-impact design questions._

## Next Question

None — grilling complete.

The remaining candidate about acceptance viewports and commands does not require an operator question: repository authority already fixes critical Playwright coverage at 390 px and 1440 px plus the required focused quality commands. Asking would repeat an accepted constraint.

Accepted choices are consolidated in `DECISIONS.md`. The next workflow owner is `jz-write-spec`; this grilling workflow must not write `SPEC.md`.

## Session Count

- Operator questions asked: 5/20
- Operator questions answered: 5/20
- Accepted grilled decisions: 5

## Notes

- Live preflight verified `main` at `f768007302c740275afb57c994cf68e34ed71df5`, matching `origin/main`.
- Existing unrelated worktree changes were preserved.
- Initial frontier was `grill-and-consolidate-decisions`; no other feature was current.
- The feature was activated through `features-cli update-feature greek-essence-showcase --status in-progress`.

## 9. Custom-Trip Form Interaction Specification

### 9.1 Entry and orientation

- The page title is `Request a Custom Itinerary`; the global entry label remains `Plan My Trip`.
- Entry from contextual pages carries an editable destination, experience, or journey reference.
- Before Step 1, users see a short value statement, approximate effort stated generically until tested (for example, `Four short steps` rather than an unverified minute estimate), privacy reassurance, and what happens after submission.
- The form starts directly at Step 1; avoid a separate splash screen that adds friction.
- A compact header provides logo/Home, language, and safe exit. Leaving with entered data triggers a warning only if data would actually be lost.

### 9.2 Progress model

- Show `Step X of 4`, current step name, and a visual progress indicator.
- Do not expose future steps as freely navigable before their prerequisites are complete.
- Completed steps may become navigable for review.
- Progress uses text as well as a visual bar/stepper and does not announce every decorative percentage change.
- On compact screens, step name and count take priority over displaying all four labels.

### 9.3 Step 1 — Trip Basics

**Purpose:** Establish destination intent and feasible travel window.  
**Fields:**

- Desired destination(s), multi-select from approved content.
- `Help me choose` mutually clear option; selecting it must not prevent optional destination interests.
- Estimated arrival date.
- Estimated departure date.
- Date flexibility: yes/no or a clearly labeled choice.
- Approximate duration; may be derived from valid dates but remains understandable and editable if dates are uncertain.

**Behavior and validation:** Dates may be marked estimated. Departure cannot precede arrival. If exact dates are not known, the design must provide a realistic flexible/approximate path rather than requiring false precision. At least destination intent or `Help me choose` is required.

### 9.4 Step 2 — Travelers and Trip Type

**Purpose:** Understand party composition and core context.  
**Fields:** adults; children count; child ages when children > 0; trip type (couple, honeymoon, family, friends, solo, other); first visit to Greece.  
**Behavior:** Child-age fields appear progressively and are removed only after clear confirmation if reducing child count would discard values. `Other` reveals a concise text field. Controls must permit keyboard entry and must not depend only on plus/minus buttons.

### 9.5 Step 3 — Preferences

**Purpose:** Capture experience priorities without forcing an exhaustive brief.  
**Fields:** interests (beaches, culture, history, gastronomy, nightlife, nature, wellness, local life, luxury, relaxation, other); preferred pace (relaxed, balanced, active); accommodation preference if confirmed useful; destinations/experiences already considered; optional additional context.  
**Behavior:** Multi-select interests have a sensible maximum only if operations require it; otherwise allow natural selection. `Other` reveals text. Free-text helper copy invites priorities and accessibility/special requirements without asking for unnecessary sensitive data.

### 9.6 Step 4 — Budget and Contact

**Purpose:** Establish feasibility and enable responsible follow-up.  
**Fields:** approved total-trip budget range; explicit flights-included/excluded explanation; full name; email; country of residence; optional phone/WhatsApp unless operations decide otherwise; preferred contact method; additional notes; required privacy acknowledgement/consent.  
**Behavior:** Budget helper text explains that it supports appropriate recommendations, not judgment. Currency and budget ranges must be approved; no ranges are invented in the prototype as business truth. Preferred contact choices adapt to actually provided contact details. Required privacy acknowledgement is separated from any optional marketing consent.

### 9.7 Field design rules

- Every control has a persistent visible label; placeholder text is example/help only.
- Optional fields are labeled `Optional`; do not mark every required field with an asterisk as the only cue.
- Instructions appear before the relevant field/group and remain available during error correction.
- Choice cards, chips, and segmented controls expose native interaction semantics and selected state.
- Date fields accept locale-appropriate input without forcing ambiguous formats.
- Country and long-option selectors support efficient keyboard and mobile use; search is optional if the list is long.
- Free-text areas show a helpful size and do not require drag resizing to be usable.
- Personal information collected is limited to PRD-approved qualification needs.

### 9.8 Step navigation and persistence

- `Continue` validates the current step; valid fields are preserved.
- `Back` never validates or clears the step being left.
- Returning to a completed step restores all values and dependent choices.
- Context received from a CTA is visibly prefilled, never hidden as an immutable assumption.
- Refresh, language switch, accidental navigation, or temporary connection loss should preserve progress when feasible and privacy-appropriate. The prototype must at minimum demonstrate Back/Continue persistence and document other persistence as required behavior.
- If stored progress expires or cannot be recovered, explain this before presenting an empty form where possible.

### 9.9 Validation

- Validate primarily on Continue/Submit, then inline as the user corrects a field. Avoid scolding users while they are still typing.
- Each error states what is wrong and how to fix it.
- Show a concise step-level summary when multiple errors exist, with links to affected fields.
- After failed Continue/Submit, focus moves to the error summary or first invalid field according to the pattern tested; the first invalid field must be reachable immediately and errors announced.
- Error text is programmatically associated with its control; groups receive group-level errors.
- Valid input remains intact. Do not use success icons on every field unless testing shows they add value.
- Business or system errors are distinguished from user input errors.

### 9.10 Submission and retry

- Submission begins only after an explicit final action.
- While submitting, the action communicates progress and repeat activation is prevented; the form remains understandable.
- Success appears only after confirmed request acceptance by the approved operational path.
- On failure, preserve all data, explain that the request was not confirmed, offer a safe retry, and provide an approved secondary contact route when appropriate.
- Do not instruct users to resend sensitive details through an insecure or unapproved channel.
- Duplicate retry risk must be manageable; the user should not receive multiple contradictory confirmations.

### 9.11 Confirmation

On success:

1. Move focus to the success heading and announce receipt.
2. Explain planner review and the next human step.
3. State a response window only after the business approves one.
4. Provide a method to correct or add information.
5. Offer consultation as optional, not required.
6. Offer two or three relevant content links based on expressed interest where privacy-appropriate.

The confirmation must not expose the full submitted personal-data payload on a shared screen.

### 9.12 Form accessibility acceptance

- Completeable using keyboard alone and at 200% zoom.
- Logical heading, group, label, help, and error relationships.
- No timeout that causes silent data loss.
- Touch targets aim for at least 44 × 44 CSS pixels where practical, with adequate separation.
- Autocomplete purpose is available for common identity/contact fields where appropriate.
- Screen-reader announcements are concise and non-duplicative.
- Color is never the only indicator of required, selected, valid, or invalid state.

---


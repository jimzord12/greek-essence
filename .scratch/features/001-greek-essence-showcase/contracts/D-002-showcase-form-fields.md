# D-002 — Showcase Form Field Contract

This contract defines the bounded qualification data collected by the four-step Greek Essence showcase form. Exact localized labels and option copy may remain provisional, but implementation must preserve this field grouping and required/optional intent.

## Step 1 — Trip

- Editable destination context, prefilled with Paros & Antiparos when entered from its contextual CTA.
- Approximate arrival and departure dates, with a clear flexible-timing path so users are not forced to invent exact dates.
- Departure must not precede arrival when both dates are supplied.

## Step 2 — Travelers

- Adults count.
- Children count.
- Child ages, shown and required only when children are present.
- Trip type.

## Step 3 — Preferences

- Interests, as a multi-select group.
- Preferred pace.
- Optional free-text notes for priorities or relevant context.

## Step 4 — Contact

- Full name.
- Email.
- Optional phone or WhatsApp number.
- Preferred contact method, limited to methods supported by the details supplied.
- Required privacy acknowledgement, separate from any marketing consent.

## Explicit omissions

The showcase does not collect:

- budget or budget range;
- country of residence;
- first-visit-to-Greece status;
- accommodation preference;
- a separate destinations-already-considered field;
- a second general-notes field.

## Behavioral boundaries

- Each step validates on Continue or Submit, then inline during correction.
- Back never clears or validates the step being left.
- Dependent child-age values are not silently discarded.
- Valid input remains intact after validation or submission failure.
- English and Greek variants represent the same canonical field values.

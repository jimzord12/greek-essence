# D-005 — Bilingual Showcase Parity Contract

English and Greek are equal showcase experiences. Greek is not a reduced or secondary demo mode.

## Required parity

Both locales must provide the same:

- Home sections and meaningful actions;
- Paros & Antiparos sections and contextual Plan My Trip entry;
- four form steps, fields, option sets, help, validation, loading, failure, retry, and success behavior;
- confirmation experience;
- visitor acknowledgement email behavior;
- navigation and recovery paths needed by the accepted showcase journey.

Marketing and destination copy may remain provisional, but it must be natural, complete, and layout-realistic in each language rather than machine-looking filler.

## Language switching

Switching language must preserve:

- the equivalent localized route;
- the current form step where applicable;
- canonical form values and valid destination context;
- the user's ability to continue without re-entering data.

Canonical values must not be stored as translated display strings.

## Missing translations

- Missing English or Greek strings for an accepted showcase route/state are implementation defects, not an approved fallback state.
- The showcase must not silently expose English interface text inside the Greek journey or vice versa.
- Build/content validation should fail for missing required localized content where practical.

## Email language

The visitor acknowledgement uses the language in which the request was submitted. The agency notification may use one consistent operational language while preserving submitted canonical values and clearly identifying the visitor locale.

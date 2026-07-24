# D-003 — Showcase Draft Persistence Contract

This contract defines browser-side persistence for the bilingual four-step Plan My Trip draft.

## Record behavior

- Use one canonical draft shared by equivalent English and Greek form routes.
- Persist canonical values rather than localized display labels.
- Include a schema/version identifier and last-updated timestamp so invalid, incompatible, or expired data can be rejected safely.
- The draft lifetime is 72 hours from its last meaningful update.

## Autosave

- Save meaningful form changes using a 1000 ms debounce.
- Also flush the current meaningful change when a field loses focus, without waiting for the remaining debounce delay.
- Back/Continue navigation must not lose changes that are still inside the debounce window.
- Do not expose routine save, restore, expiry, or cleanup notifications to the user.

## Restore and cleanup

- Restore a valid draft after refresh and when switching between equivalent English and Greek form routes.
- If the stored record is expired, corrupt, incompatible, or cannot be parsed, remove it silently and present a clean form.
- Silent cleanup must not produce an error state, toast, modal, or explanatory message.

## User-controlled reset

- Provide an explicit `Start Over` action.
- Require confirmation before clearing a valid in-progress draft through `Start Over`.
- After confirmation, remove the draft and reset the form to its clean state, while retaining any destination context implied by the current entry route only if that behavior is made clear.

## Submission

- Preserve the draft through validation errors, network/provider failures, and retry.
- Clear the draft only after the server has confirmed successful request acceptance.

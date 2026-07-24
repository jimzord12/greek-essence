# D-004 — Showcase Email Contract

This contract defines the two emails produced after a valid Plan My Trip submission. Addresses, verified sending domain, and credentials are runtime configuration and must remain outside Git.

## 1. Agency notification

Send one email to the configured agency inbox containing:

- every canonical field collected by the accepted D-002 form contract;
- a clearly structured, scan-friendly HTML presentation grouped by the four form steps;
- restrained branded styling suitable for common email clients;
- a JSON attachment containing the same canonical submitted values.

The JSON attachment must:

- use a stable UTF-8 `.json` file;
- preserve canonical values rather than localized display labels;
- contain only fields accepted by server-side validation;
- avoid secrets, internal configuration, browser-storage metadata, or unrelated request data;
- represent omitted optional values consistently as defined in the later SPEC.

## 2. Visitor acknowledgement

Send a separate acknowledgement to the validated visitor email address:

- in the language used for submission;
- confirming that the request was received without implying a booking, acceptance of travel arrangements, guaranteed response time, price, or availability;
- using polished email-safe HTML/CSS that conveys calm trust, professionalism, warmth, and the Greek Essence editorial boutique-hospitality identity;
- including a concise summary or next-step orientation without repeating unnecessary sensitive form details.

## Styling boundaries

- Use email-client-safe HTML/CSS with a readable plain-text fallback.
- Prioritize typography fallbacks, spacing, color, hierarchy, and graceful degradation over complex effects.
- Do not depend on remote imagery for comprehension or trust.
- Do not invent credentials, awards, partner claims, operational promises, or legal assurances.

## Submission boundary

- The request is accepted only after the agency notification, including its JSON attachment, is accepted by Resend.
- After agency acceptance, the visitor acknowledgement is attempted separately.
- If the agency notification fails, preserve form data and show a recoverable submission failure.
- If only the visitor acknowledgement fails after agency acceptance, do not ask the visitor to resubmit or create a duplicate agency request; retain the successful on-screen confirmation.

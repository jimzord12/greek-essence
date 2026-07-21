## 10. Custom-Trip Form Design and Architecture

### 10.1 Form contract

The form implements Prototype §9 and PRD §18 without adding unsupported commercial facts.

| Step | Data | Implementation notes |
|---|---|---|
| 1. Trip basics | destinations or `Help me choose`; approximate/flexible dates; duration | Contextual CTA prefills visible, editable destination/journey interest |
| 2. Travellers | adults; conditional children/ages; trip type; first visit | Child-age rows appear only when children > 0 |
| 3. Preferences | interests; pace; approved accommodation preference; considered places; notes | Only approved options appear; `other` has bounded plain text |
| 4. Budget/contact | approved budget/flight clarification; name; email; residence; optional phone; preferred contact method; notes; privacy acknowledgement; optional marketing consent | No budget range/currency/response promise is invented |

The business must supply final budget choices, flight wording, contact method availability, policy copy/version, response wording, and lead inbox address before a real external form is enabled.

### 10.2 Client form state

Use React Hook Form with a small step reducer and shared Zod schemas. It is a client component only because it needs controlled multi-step state, conditional fields, local persistence, and accessible errors.

- Step changes preserve valid fields; Back never clears values.
- The progress indicator names the active step and does not pretend to measure minutes.
- Context from a destination, experience, or journey is an allow-listed public ID and is visibly editable.
- Client-side validation runs per step. Final validation runs again in the route handler.
- Optional fields are visibly optional. Valid input remains after any error.
- No personally identifying data goes into the URL, metadata, browser analytics, or error reporting.

### 10.3 Local draft persistence

The form draft is stored at `localStorage['greek-essence.trip-request-draft.v1']` as:

```ts
type TripRequestDraft = {
  version: 1;
  savedAt: string;
  expiresAt: string; // savedAt + 72 hours
  locale: 'en' | 'el';
  currentStep: 1 | 2 | 3 | 4;
  values: TripRequestValues;
};
```

Save on meaningful change with a short debounce, step transition, page hide, and language switch. On page load, discard invalid, schema-incompatible, or expired drafts; expiry is evaluated when the site/form loads, so it is acceptable that an unopened browser cannot clear itself exactly at 72 hours. On successful submission, clear the draft. Provide a clearly labelled **Clear saved form** action with confirmation and no server request.

Because `localStorage` can retain personal travel/contact data on a shared device, show a concise, localized note near the form: “Your progress is saved on this device for up to 72 hours.” Do not persist CAPTCHA/challenge values, API response errors, email provider IDs, or secret tokens.

### 10.4 Validation and accessibility

Shared Zod schemas define client and server rules. The server is authoritative.

- destination selection or `Help me choose` is required;
- dates may be flexible; when both dates are supplied, departure follows arrival;
- traveller counts are bounded positive integers and child ages count matches children;
- options are allow-listed IDs; `other` text is limited and plain text;
- email is normalized and syntactically validated without restrictive name/phone rules;
- contact method must correspond to a provided usable channel when required;
- privacy acknowledgement is required and separate from optional, unchecked marketing consent;
- text is trimmed, Unicode-safe, and length-limited.

On step submission, focus an error summary linked to each invalid field. Fields expose label, visible message, `aria-invalid`, and `aria-describedby`; values remain unchanged. Use a polite live region for saved/progress/submission status and assertive messaging only for blocking errors. On accepted success, focus the confirmation heading.

### 10.5 Submission flow

```mermaid
sequenceDiagram
  participant B as Browser
  participant A as Vercel route handler
  participant R as Resend
  participant G as Greek Essence Gmail
  B->>A: POST JSON form payload
  A->>A: Verify origin, honeypot, payload and Zod schema
  A->>R: Send detailed lead notification to Gmail
  R->>G: Deliver notification email
  A->>R: Send acknowledgement to traveller
  R-->>A: Accepted by email API
  A-->>B: Success response
  B->>B: Clear draft; show confirmation
```

The route must send the Gmail notification first, then the traveller acknowledgement. The browser sees success only when both Resend API calls return accepted. The server returns a generic failure if either call fails; the browser preserves the draft and offers a retry. It never claims success merely because client validation passed.

There is no database or queue in this prototype. Therefore, a network timeout after an email provider has accepted a request can produce a retry/duplicate email. Mitigate this with a client-generated submission ID retained for the current retry and deterministic Resend idempotency keys for each email type. Resend’s idempotency window is limited; this is a **prototype mitigation, not durable production idempotency**.

### 10.6 Route handler contract

`POST /api/trip-request` accepts JSON only:

```ts
type TripRequestSubmit = {
  submissionId: string; // UUID generated in browser and reused for immediate retry
  locale: 'en' | 'el';
  form: TripRequestValues;
  context?: { type: 'destination' | 'experience' | 'journey'; id: string };
  honeypot?: string;
};
```

Responses are deliberately small:

| Status | Meaning | Browser behavior |
|---:|---|---|
| 200 | Both emails accepted by Resend | Clear draft; show C-27 confirmation |
| 400/422 | Malformed or invalid values | Map safe field errors; retain data |
| 403 | Failed origin/honeypot/security check | Generic retry/contact message; do not reveal signal |
| 429 | Lightweight rate guard triggered | Retain draft; ask user to wait/retry |
| 500/503 | Email/configuration/transient failure | Retain draft; safe retry; show backup contact action |

The endpoint validates request method, `Content-Type`, body size, `Origin`/`Sec-Fetch-Site` where available, a hidden honeypot, submission UUID, and complete Zod schema. It accepts only the current supported locale and public context IDs. It never returns provider IDs, recipients, secrets, or supplied PII.

### 10.7 Spam and abuse controls

Prototype controls are low-friction and do not require paid services:

1. hidden honeypot field ignored by legitimate users;
2. minimum client interaction time as a weak supplementary signal;
3. strict request/body/text limits;
4. origin/fetch-site checks and server validation;
5. Vercel platform protection and manual review of unusual activity; a durable rate-limit store is intentionally not added;
6. manual review of Gmail spam and Resend dashboard during prototype review.

Do not pretend this is production-grade anti-abuse protection. Cloudflare Turnstile, a durable distributed rate-limit store, stricter bot management, and operational alerting are production decisions.

### 10.8 Email behavior

Use two localized React Email templates.

| Email | Recipient | Content | Rules |
|---|---|---|---|
| Lead notification | `GREEK_ESSENCE_LEADS_TO` Gmail configuration | Complete structured form summary, source context, timestamp, locale, reply-to traveller email | Contains PII; never sent to analytics/logs; formatting must make human review easy |
| Acknowledgement | Traveller email | Receipt confirmation, short next-step text, approved contact/correction route, privacy link | No response-time promise unless approved; no marketing content without separate consent |

Configure Resend with a verified Greek Essence sending domain, preferably a dedicated transactional subdomain such as `mail.greekessence.gr`. Set a branded From name/address and the Gmail inbox as `Reply-To` where appropriate. Keep `RESEND_API_KEY`, sender, and recipient address in Vercel environment variables; no secret appears in client code, JSON, Git, or test screenshots.

Resend free-tier limits are sufficient for the prototype: 3,000 emails/month, 100/day, and one domain. At two emails per accepted trip request, that is nominally 1,500 submissions/month, subject to the daily cap. Confirm current limits before enabling a public prototype.

### 10.9 Confirmation and correction path

After accepted submission, show C-27 on the client without placing form values in the URL. The confirmation states receipt, explains only approved next steps, offers the configured contact route for corrections/additional details, and may show relevant inspirational links. It must not promise a reply timeframe before operations defines one. A refresh shows a generic safe confirmation/recovery state, not a replay of the traveller’s data.

---


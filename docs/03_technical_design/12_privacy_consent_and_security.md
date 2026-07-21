## 12. Privacy, Consent, and Security

### 12.1 Data minimization

The form collects only PRD-approved planning/qualification data. It explicitly asks visitors not to include passports, payment details, health information, or other sensitive data in free-text notes. No files are accepted.

| Data group | Prototype use | Storage/destination | Sensitivity |
|---|---|---|---|
| Trip/traveller/preference data | Build a human-readable request | Gmail notification; temporary browser draft | Personal travel/preference data |
| Name/email/phone | Follow-up and acknowledgement | Gmail; Resend recipient | PII |
| Privacy acknowledgement/marketing choice | Demonstrate approved form controls | Email notification only; no marketing system | Compliance-related |
| Context/locale | Explain source/route | Email notification | Low |
| Honeypot/submission ID | Abuse/retry mitigation | Request only; not persisted by app | Low |

The application has no database, logs no request body, and does not send form values to client analytics, browser console, error tracker, URLs, or metadata. Resend and Gmail are external processors; final public privacy text, retention, DPA/subprocessor review, and data-subject process are production launch requirements.

### 12.2 Consent

The form presents a required privacy acknowledgement as notice/acknowledgement, not as marketing consent. Optional marketing consent is separately worded, unchecked, and has no downstream action in the prototype. Do not use it to add people to a mailing list.

Analytics is deferred. Therefore the prototype should not load ad pixels, session replay, or non-essential analytics cookies. A cookie banner is not added merely for appearance. The Cookie Information page may exist structurally and must describe actual prototype behavior once approved.

### 12.3 Security baseline

- HTTPS through Vercel and verified custom domain.
- Environment variables scoped to preview/production; server-only secrets only.
- Strict server validation, body size limits, origin checks, honeypot, plain-text email interpolation, and no raw HTML from visitors.
- Zod/allow-listed content URLs and IDs; no arbitrary redirects.
- Content Security Policy, `X-Content-Type-Options: nosniff`, referrer policy, permissions policy, and clickjacking protection configured in `next.config.ts`/middleware where compatible.
- No PII in logs. Route errors get a generated correlation ID and safe generic message.
- Git secret scanning, dependency audit, MFA on Vercel/Resend/domain registrar, and protected main branch.

The serverless endpoint does not make the project a broad backend. It is a narrow secret-holding submission boundary.

---


## 17. Configuration and Environments

### 17.1 Environment variables

| Variable | Exposure | Purpose |
|---|---|---|
| `RESEND_API_KEY` | Server only | Send authenticated email through Resend |
| `RESEND_FROM` | Server only | Verified branded sender address |
| `GREEK_ESSENCE_LEADS_TO` | Server only | Gmail recipient for lead notifications |
| `NEXT_PUBLIC_SITE_URL` | Public build config | Canonicals, metadata, emails |
| `NEXT_PUBLIC_DEFAULT_LOCALE` | Public build config | Explicit fallback locale |
| `TURNSTILE_*` | Deferred unless enabled | Optional future bot challenge |

Validate required server variables with Zod when the endpoint loads. In a preview environment, use a test Resend domain/recipient or disable real sending; no preview must accidentally email the real Gmail inbox or traveller addresses.

### 17.2 Environments

| Environment | Purpose | Email behavior |
|---|---|---|
| Local | Development | Resend mock/mail sink; no real recipients |
| Preview | PR review/client staging | Test recipient only or endpoint disabled |
| Prototype production/demo | Owner review on Vercel/custom domain | Approved Gmail and Resend free-tier domain |
| Future commercial production | Separate scope/approval | Reassess every operational, legal, and reliability control |

This design assumes the prototype's use complies with Vercel Hobby's non-commercial personal-use terms. It is not documented here as the production host for the travel business; if the demonstration is deemed commercial use, use a paid plan or another provider before deployment.

---


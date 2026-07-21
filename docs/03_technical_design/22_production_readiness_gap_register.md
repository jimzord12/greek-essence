## 22. Production-Readiness Gap Register

The following PRD/Prototype requirements remain authoritative but are intentionally not solved by the prototype architecture.

| Gap | Why prototype defers it | Required before public production launch |
|---|---|---|
| Commercial hosting | Vercel Hobby is restricted to private/non-commercial use | Select commercial plan/provider, budget/spend controls, terms review |
| Durable lead record | No database by decision | Approved lead system/CRM/spreadsheet workflow with durable record and owner |
| Delivery recovery | No queue/outbox/reconciliation | Idempotency, retry/replay, notification failure alert, daily reconciliation |
| Retention/deletion/DSR | No final legal/operational choices | Approved retention schedule, access model, deletion/export workflow, processor review |
| Operational ownership | Demo Gmail is only a receiver | Primary/backup owner, response process, response-time commitment, escalation |
| Analytics FR-014 | Deliberately deferred | Consent-aware event specification and selected provider |
| Observability NFR-010 | Deliberately deferred | Alerts, availability/form monitoring, dashboards, runbooks |
| Spam resilience | Prototype-only controls | Durable rate limiting, managed challenge, incident procedure |
| Legal pages/policies | Facts not supplied | Approved privacy/cookie/travel terms and actual processor disclosures |
| Trust assets | Rights/wording unresolved | Verified permissions, attribution, expiry review, content approval |
| Final content/media | Prototype may use provisional inputs | Final English/Greek copy, licensed assets, content-owner workflow |
| Browser/device support | Demo-focused checks only | Approved support matrix and full regression evidence |
| Production email operations | Resend free tier proves flow only | Sender reputation, bounce/complaint handling, domain configuration, delivery monitoring |

No production promotion is approved until these gaps are resolved against the PRD, Prototype, privacy/legal review, and operational ownership.

---


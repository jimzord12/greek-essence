## 20. Prototype Risks and Mitigations

| Risk | Mitigation |
|---|---|
| A user sees success after email failure | Return success only after both Resend sends are accepted; preserve draft on failure |
| Retry sends duplicate email | Per-attempt submission ID plus Resend idempotency keys; clearly mark this as a production gap |
| Spam reaches Gmail | Honeypot, strict validation/limits, platform protection, manual review; add Turnstile if needed |
| API key leaks | Server-only route handler/environment secret; no `NEXT_PUBLIC_` secret; secret scan |
| Shared device retains a draft | 72-hour expiry, visible notice, manual clear, clear after success |
| Generic-looking form harms owner impression | Fully bespoke shadcn/Base UI implementation; no embedded form provider |
| Hero media harms performance | Image budgets, `next/image`, responsive sizes, poster-first media |
| English/Greek drift | Parallel local JSON, stable IDs, build validation, review both locales |
| Placeholder claims look real | Source flags and presentation checklist; exclude unapproved trust facts |
| Vercel Hobby used as a commercial launch | Documented scope boundary; production readiness review required |

---


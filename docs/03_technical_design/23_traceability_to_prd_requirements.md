## 23. Traceability to PRD Requirements

| Requirement | Prototype implementation coverage | Production note |
|---|---|---|
| FR-001 Navigation | C-01–04, localized static routes, keyboard menu | Covered |
| FR-002 Language Access | `next-intl`, `/en`/`/el`, stable-ID switcher | Covered |
| FR-003 Destination Discovery | JSON models, index/detail/cards/relations | Covered |
| FR-004 Experience Discovery | JSON models, index/detail/cards/relations | Covered |
| FR-005 Journey Inspiration | JSON journey data, route/fit/customizable presentation | Covered; no booking implication |
| FR-006 Brand and Trust | About/How/FAQ/trust components with approved-only data | Final claims remain dependency |
| FR-007 Primary Conversion | C-23/C-25, contextual prefill, Vercel endpoint | Covered for prototype |
| FR-008 Secondary Contact | C-24 and configurable approved contact actions | Final channels/consultation unresolved |
| FR-009 Form Persistence | localStorage 72-hour draft, errors/back/language retention | Covered for prototype |
| FR-010 Submission Confirmation | Both emails accepted before C-27 success | Covered with prototype limitation |
| FR-011 Request Delivery | Gmail notification and acknowledgement | Production durable/assigned/recoverable workflow deferred |
| FR-012 Consent and Privacy | Separate notice acknowledgement/optional marketing consent | Final policies/retention/processor review deferred |
| FR-013 Search Discovery | Static HTML, localized URLs, metadata, sitemap, internal links | Covered architecturally |
| FR-014 Measurement | Event hook points only | Deferred |
| FR-015 Error Communication | C-29/30, validation, retry, safe generic errors | Covered |
| FR-016 Content Relationships | Typed local relation IDs and C-16 | Covered |
| FR-017 Legal Access | Route structure | Final content/legal approval deferred |
| NFR-001 Performance | Static generation, image/font/bundle budgets | Covered for prototype |
| NFR-002 Availability/Reliability | Vercel/Resend plus safe errors | Production recovery/monitoring deferred |
| NFR-003 Accessibility | §13 implementation/testing | Covered target |
| NFR-004 Privacy | Minimization, no DB/log PII, local-draft notice | Formal compliance deferred |
| NFR-005 Security | Server secret boundary, validation, headers | Production threat/review expansion deferred |
| NFR-006 SEO | §14 | Covered architecturally |
| NFR-007 Maintainability | File boundaries, typed JSON, component model | Covered |
| NFR-008 Localization Consistency | `next-intl`, parallel content, schema checks | Final translation ownership remains dependency |
| NFR-009 Compatibility | Responsive and Playwright/manual matrix | Formal release matrix deferred |
| NFR-010 Observability | Manual Vercel/Resend review only | Deferred |
| NFR-011 Honest Representation | Content validation and forbidden fields | Covered |
| NFR-012 Content Quality | Build checks, content/media validation | Final approvals remain dependency |

---


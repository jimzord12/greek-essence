## 25. Non-Functional Product Requirements

These are product-level quality requirements. Detailed implementation thresholds and mechanisms belong to the Technical Design.

### NFR-001 — Performance

The product must feel fast on common mobile devices and realistic mobile networks. Large media and third-party tools must not block core comprehension or interaction.

### NFR-002 — Availability and Reliability

Public content and the primary form journey must be reliably available. Submission failures must be detectable and recoverable.

### NFR-003 — Accessibility

The product must target WCAG 2.2 AA, including keyboard use, semantic structure, readable contrast, accessible forms and errors, useful alternative text, scalable text, suitable touch targets, and reduced-motion support.

### NFR-004 — Privacy

The product must collect only necessary personal data, explain its use, restrict access, and support defined retention and deletion practices.

### NFR-005 — Security

Personal data, form handling, administration, and third-party services must be protected using appropriate modern security practices. Exact controls belong to the Technical Design.

### NFR-006 — SEO Readiness

The product must support unique localized URLs and metadata, language targeting, canonical handling, crawlable content, internal linking, structured data where appropriate, redirects, and image metadata.

### NFR-007 — Maintainability

Content, routes, and reusable patterns should be organized so that future additions do not require widespread duplication or inconsistent one-off solutions.

### NFR-008 — Localization Consistency

English and Greek content must remain structurally aligned, with clear ownership for translation and updates.

### NFR-009 — Browser and Device Compatibility

Core content and conversion journeys must work on supported modern browsers and common mobile, tablet, and desktop viewport sizes. Exact support matrix belongs to the Technical Design.

### NFR-010 — Observability

The team must be able to determine whether the site, lead submission, acknowledgement, and essential measurement are functioning.

### NFR-011 — Honest Representation

The UI must not suggest live pricing, availability, booking, customer reviews, or capabilities that do not exist.

### NFR-012 — Content Quality

No launch-critical page may depend on unapproved claims, unlicensed media, placeholder copy, or materially incomplete translation.

### Key Decisions

- Quality requirements are MVP requirements, not post-launch polish.
- Specific performance budgets and technical controls will be defined downstream.

---


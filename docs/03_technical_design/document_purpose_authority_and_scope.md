# Greek Essence Technical Design

**Document ID:** GE-TD-001  
**Version:** 0.2  
**Status:** Prototype-build technical design — pending implementation  
**Prepared:** 21 July 2026  
**Product:** Greek Essence  
**Initial domain:** `greekessence.gr`

---

## 0. Purpose, Authority, and Scope Boundary

This document defines how the approved Greek Essence experience will be implemented as a **private, client-review prototype**: an almost-static, bilingual Next.js site with one small server-side form endpoint. It is intended to prove the visual direction, responsiveness, SEO foundation, page experience, and custom-trip conversion journey to the travel-agency owner before production investment.

It does not alter the product decisions in the governing PRD or the UX decisions in the Prototype Specification. In particular, the PRD still defines the later public production MVP as a reliable lead-generation site. This document explicitly distinguishes the present prototype build from that future production release.

### 0.1 Source hierarchy

1. `00_PROJECT_PROTOCOL.md` — process and documentation ownership.
2. `01_PRODUCT_REQUIREMENTS.md` (PRD) — product, business, and production-MVP truth.
3. `02_PROTOTYPE_SPECIFICATION.md` (Prototype) — UX, UI, responsive, states, and interactions.
4. This document — implementation decisions for the prototype build.
5. The UX Strategy brief — supplementary historical evidence.

When documents conflict, the higher-ranked document governs. A production requirement intentionally deferred from this prototype is listed in §22 rather than silently removed.

### 0.2 Prototype build versus production MVP

| Topic | This prototype build | Later production MVP |
|---|---|---|
| Purpose | Convince the owner through a polished, working experience | Public commercial lead generation |
| Hosting | Vercel Hobby, private/demo use | Commercially permitted plan/provider |
| Content | Version-controlled local JSON | JSON initially; CMS only if content operations justify it |
| Lead storage | No database; delivered emails are the temporary record | Approved durable storage/operational workflow |
| Form delivery | One Vercel route handler + Resend | Reassess reliability, audit, retention, recovery, and ownership |
| Analytics | Deferred | Required by PRD FR-014 |
| Monitoring | Deferred | Required by PRD NFR-010 |
| Legal/privacy | Structural routes and minimization; final policies not invented | Approved policies, retention, DPA/subprocessor review, DSR process |

The prototype may use a real custom domain and test form submissions, but it must not be represented as a production-ready public commercial service.

---


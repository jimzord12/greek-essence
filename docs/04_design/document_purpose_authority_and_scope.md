# Greek Essence Design System

**Document ID:** GE-DESIGN-001  
**Version:** 0.1  
**Status:** Complete first draft — pending product-owner and visual review  
**Prepared:** 21 July 2026  
**Product:** Greek Essence  
**Applies to:** Private client-review prototype  
**Primary language:** English  
**Secondary language:** Greek  

---

## 0. Purpose, Authority, and Scope

`DESIGN.md` is the visual-design-system and UI-implementation source of truth for the Greek Essence client prototype.

It defines **how the approved product and interface should look and feel**. It enables designers, frontend developers, and AI agents to implement the prototype consistently without repeatedly resolving the same subjective visual decisions.

The document is implementation-aware but not implementation-owning. It maps visual decisions to the approved Tailwind CSS v4 and shadcn/ui + Base UI stack without changing the architecture defined in `03_TECHNICAL_DESIGN.md`.

### 0.1 Source hierarchy

1. `00_PROJECT_PROTOCOL.md` — process and documentation governance.
2. `01_PRODUCT_REQUIREMENTS.md` — product, business, audience, brand promise, scope, truth, and production-MVP requirements.
3. `02_PROTOTYPE_SPECIFICATION.md` — information architecture, page hierarchy, responsive behavior, interaction, states, forms, accessibility, and prototype flows.
4. `03_TECHNICAL_DESIGN.md` — framework, project architecture, implementation boundaries, tooling, performance budgets, and technical quality gates.
5. This document — exact visual-system, token, art-direction, and visual implementation decisions.

When this document conflicts with a higher-ranked source, the higher-ranked source governs.

### 0.2 Ownership boundary

The governing documents answer:

- **PRD:** What is the product, who is it for, and what must be true?
- **Prototype Specification:** Which interface exists, where does it appear, and how does it behave?
- **Technical Design:** How is the prototype implemented?
- **DESIGN.md:** Exactly how does the approved interface look and feel?

This document does not restate page behavior or product purpose unless required to explain a visual decision.

### 0.3 Audience

- Product and visual designers
- Frontend developers
- Content and localization contributors
- Accessibility reviewers
- QA contributors
- Future AI design and implementation agents

### 0.4 In scope

This document owns:

- visual principles and anti-patterns;
- color palette and semantic color roles;
- typography and font-loading guidance;
- spacing, grids, containers, and section rhythm;
- radius, border, surface, elevation, and shadow systems;
- iconography and decorative language;
- photography, imagery, map, illustration, and video art direction;
- design-token hierarchy and naming;
- interaction-state appearance;
- visual accessibility rules;
- visual mapping for C-01 through C-30;
- page-level composition guidance;
- Tailwind v4 token mapping;
- shadcn/ui + Base UI visual customization;
- asset conventions;
- design QA and visual-regression expectations.

### 0.5 Out of scope

This document must not:

- change product scope, audiences, services, destinations, conversion goals, or CTA hierarchy;
- alter page hierarchy, navigation behavior, form steps, form fields, validation logic, or language-switching behavior;
- invent prices, budgets, response times, awards, relationships, testimonials, reviews, legal text, or service promises;
- introduce booking, payment, live availability, accounts, dashboards, or excluded capabilities;
- introduce a competing component system, styling framework, frontend architecture, or content platform;
- present provisional visual choices as final legal brand identity.

---


## 10. Project-Owned `greek-essence-quality-review` Skill

### 10.1 Purpose

Encode the project-specific review standard that generic external skills cannot provide.

The skill connects actual browser observation with the authoritative product, UX, and technical documents.

### 10.2 Repository location

```text
.agents/skills/greek-essence-quality-review/
```

### 10.3 Required metadata

Use clear trigger language in `SKILL.md`.

Recommended front matter:

```markdown
---
name: greek-essence-quality-review
description: Review Greek Essence implementations for project-specific visual quality, responsive behavior, accessibility, English/Greek localization, SEO presentation, image treatment, trust signals, and custom-trip form UX. Use after implementing or revising pages, components, navigation, localized content, metadata, or the trip-request flow.
---
```

### 10.4 Required authoritative references

The skill must direct the agent to read the relevant sections of:

- `01_PRODUCT_REQUIREMENTS.md` for product intent, scope, honest representation, trust, content, and conversion requirements;
- `02_PROTOTYPE_SPECIFICATION.md` for page composition, responsive behavior, visual direction, interactions, accessibility, form behavior, states, flows, and prototype acceptance;
- `03_TECHNICAL_DESIGN.md` for implementation architecture, localization, SEO, content models, form architecture, security, testing, quality gates, and production gaps.

The skill should reference document names and useful section numbers rather than reproducing their requirements.

### 10.5 Required review behavior

The skill must instruct the agent to:

1. identify the changed route, component, content area, or flow;
2. read only the relevant authoritative sections;
3. run the application using the repository’s documented commands;
4. inspect actual rendered behavior with Playwright CLI;
5. review representative compact, medium where relevant, and wide viewports defined by the Prototype and Technical Design;
6. inspect both English and Greek where the change can affect localization or layout;
7. evaluate visual hierarchy, spacing, typography, media treatment, and CTA hierarchy;
8. evaluate trust presentation and honest representation;
9. inspect keyboard, focus, error, loading, success, reduced-motion, and unavailable states when relevant;
10. verify metadata, localized routes, canonicals, alternates, or structured presentation when relevant;
11. exercise the custom-trip flow when the change affects navigation, conversion, forms, content context, validation, or confirmation;
12. separate observed defects from subjective suggestions;
13. provide evidence for every blocking or high-impact issue;
14. recommend permanent tests for recurring or release-critical defects.

### 10.6 Required reference files

Create focused checklists under `references/`:

- `visual-review-checklist.md`;
- `responsive-review-checklist.md`;
- `accessibility-review-checklist.md`;
- `seo-localization-review-checklist.md`;
- `form-quality-security-review-checklist.md`.

These files should point to authoritative project sections instead of duplicating entire specifications.

### 10.7 Project-specific anti-patterns

The skill must flag:

- generic travel-template appearance;
- loud or stereotypical Greek motifs;
- excessive blue-and-white theming;
- mass-market tourism or package-store presentation;
- ostentatious luxury cues;
- crowded composition;
- inconsistent spacing;
- weak mobile hierarchy;
- oversized empty hero areas without a clear purpose;
- generic or misleading stock-image treatment;
- low-contrast text over photography;
- decorative motion that harms calmness, usability, or accessibility;
- English layouts that fail with longer Greek content;
- misleading price, availability, booking, trust, award, review, exclusivity, or response-time signals;
- interaction behavior that contradicts the Prototype Specification;
- implementation choices that violate the Technical Design.

### 10.8 Required output format

The skill must produce:

```text
1. Blocking defects
2. High-impact quality issues
3. Accessibility issues
4. Responsive issues
5. English/Greek issues
6. Performance or implementation risks
7. Suggested permanent tests
8. Evidence: route, locale, viewport, screenshot or trace, and reproduction steps
```

Empty sections may be omitted. Subjective preferences must not be presented as defects without a traceable project requirement.

### 10.9 Validation

Test the skill in Codex CLI and Kimi Code with a controlled prompt against a real or representative page change.

The agent must:

- load the project-owned skill;
- reference the relevant authoritative document sections;
- use Playwright CLI for observed browser claims;
- produce the required evidence-oriented report structure.

---


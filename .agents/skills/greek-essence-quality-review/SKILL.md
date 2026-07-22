---
name: greek-essence-quality-review
description: Review Greek Essence implementations for project-specific visual quality, responsive behavior, accessibility, English/Greek localization, SEO presentation, image treatment, trust signals, and custom-trip form UX. Use after implementing or revising pages, components, navigation, localized content, metadata, or the trip-request flow.
---

# Greek Essence quality review

## Review procedure

1. Identify the changed route, component, content area, or flow.
2. Read only the relevant authoritative sections in the [PRD](../../../docs/01_prd/index.md), [Prototype Specification](../../../docs/02_prototype_specification/index.md), and [Technical Design](../../../docs/03_technical_design/index.md), then use the focused checklists in `references/`.
3. Run the application with repository-documented commands and inspect actual rendered behavior with Playwright CLI. Browser claims require Playwright CLI evidence.
4. Review representative 320, 390, 834, and 1440 viewports (and intermediate widths or 200% zoom where relevant). Inspect English and Greek when localization or layout can be affected.
5. Evaluate visual hierarchy, spacing, typography, media treatment, CTA hierarchy, trust presentation, and honest representation. Inspect keyboard, focus, error, loading, success, reduced-motion, and unavailable states when relevant.
6. Verify metadata, localized routes, canonicals, alternates, or structured presentation when relevant. Exercise the custom-trip flow when navigation, conversion, forms, content context, validation, or confirmation changes.
7. Separate observed defects from subjective suggestions. Provide evidence for every blocking or high-impact issue and recommend permanent tests for recurring or release-critical defects.

## Flag these project-specific anti-patterns

- Generic travel-template appearance; loud or stereotypical Greek motifs; excessive blue-and-white theming; mass-market tourism or package-store presentation; or ostentatious luxury cues.
- Crowded composition, inconsistent spacing, weak mobile hierarchy, oversized purposeless hero space, generic or misleading stock-image treatment, low-contrast text over photography, or decorative motion that harms calmness, usability, or accessibility.
- English layouts that fail with longer Greek content; misleading price, availability, booking, trust, award, review, exclusivity, or response-time signals.
- Interaction behavior contradicting the Prototype Specification or implementation choices violating the Technical Design.

## Report format

Omit irrelevant sections only with a scope explanation. Do not present subjective preferences as defects without a traceable project requirement.

1. Blocking defects
2. High-impact quality issues
3. Accessibility issues
4. Responsive issues
5. English/Greek issues
6. Performance or implementation risks
7. Suggested permanent tests
8. Evidence: route, locale, viewport, screenshot or trace, and reproduction steps

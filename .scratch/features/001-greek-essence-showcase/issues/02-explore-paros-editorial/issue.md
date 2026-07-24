Status: ready-for-agent
Method: tdd-solo
Complexity: 3
BlockedBy: 1
Milestone: explore-bilingual-showcase

# Explore the bilingual Paros and Antiparos editorial journey

Extend the consumed showcase foundation into the destination discovery slice: a visitor can move from Home to a complete Paros & Antiparos editorial page in either locale, switch language without losing route identity, and follow the contextual planning call to action while unapproved media remains a safe neutral fallback.

## Acceptance criteria

- [ ] English and Greek destination routes render the exact six-section Paros & Antiparos composition and shared shell, covering character, traveler fit, signature experiences including culture/gastronomy, combinations, and the final planning CTA without broader catalogue sections (FR-002, DEC-002).
- [ ] Home-to-destination navigation and locale switching preserve the equivalent destination route, and the final CTA carries only the allow-listed public `paros-antiparos` context into the localized Plan My Trip URL (FR-003, DEC-010).
- [ ] Destination editorial content passes the shared build-time locale-structure, message-parity, stable-media-ID, and approval-metadata rules with complete natural English/Greek coverage (FR-013, DEC-008, SUBDEC-004, NFR-007).
- [ ] Pending QUE-003 destination media uses the designed neutral fallback without losing editorial meaning, broken-image UI, or invented approval metadata.
- [ ] Destination URLs, metadata, fixtures, screenshots, console output, and browser artifacts contain no PII; the public destination context remains an allow-listed non-PII identifier (NFR-004).
- [ ] Both localized destination routes emit non-empty localized metadata, self-canonical URLs, `en`/`el`/`x-default` alternates, and `noindex,nofollow` (FR-015).
- [ ] The page consumes the established semantic token foundation and only accepted showcase component variants; it remains static-first, shallow, responsive, accessible, performant, and free of unnecessary client code or unsafe runtime content boundaries (FR-016, NFR-001, NFR-002, NFR-003, NFR-005, NFR-008, DEC-011, DEC-013).
- [ ] Focused automated checks prove both locale routes, section/heading structure, localized CTA paths and context, locale switching, metadata, content validation, and safe fallback rendering.
- [ ] The integrated Home-to-Paros journey is exercised at the required compact and wide Playwright viewports with browser guards, axe checks, responsive/zoom spot checks, and preserved Unlighthouse plus documented transfer, image, JavaScript, CSS, LCP, INP, and CLS budgets; failures are fixed in this slice without weakening gates (DEC-012).

Traces: FR-002, FR-003, FR-013, FR-015, FR-016; NFR-001, NFR-002, NFR-003, NFR-004, NFR-005, NFR-007, NFR-008; DEC-002, DEC-008, DEC-010, DEC-011, DEC-012, DEC-013, SUBDEC-004.

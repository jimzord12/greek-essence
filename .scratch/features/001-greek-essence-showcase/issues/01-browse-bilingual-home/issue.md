Status: ready-for-agent
Method: tdd-solo
Complexity: 5
BlockedBy: none
Milestone: explore-bilingual-showcase

# Browse a complete bilingual Home through the shared showcase foundation

Deliver the first complete static discovery slice: a visitor can browse the six-section Home in English or Greek, use the shared responsive shell, switch to the equivalent localized Home, follow localized calls to action, and see meaningful editorial content even while provisional media remains unapproved. Establish the complete documented reusable Tailwind CSS v4 token foundation as part of this consumed Home slice, without adding unused wider-product components or a parallel theme representation.

## Acceptance criteria

- [ ] English and Greek Home routes render the exact six-section composition and shared shell, with complete natural locale content, localized links, no unsupported business claims, and no mixed-language fallback (FR-001, DEC-001, DEC-008, SUBDEC-004).
- [ ] The locale switch preserves Home route identity through the approved locale-aware navigation boundary, and static explicit-locale routing remains intact (FR-003, DEC-010).
- [ ] Build-time content and shared-message validation enforces locale structure/key parity, stable media IDs, non-empty localized editorial content, and fail-closed approved-media metadata (FR-013, NFR-007).
- [ ] Pending QUE-003 media renders the intentional neutral fallback with all meaning retained in adjacent content; no unapproved image is promoted and no approval question is reopened.
- [ ] Home emits non-empty localized title/description, self-canonical URL, `en`/`el`/`x-default` alternates, and private-prototype `noindex,nofollow`, with no PII in URL or metadata (FR-015, NFR-004).
- [ ] The complete documented reusable foundation—colors, typography, spacing, layout, responsive modes, shape, elevation, motion/easing, focus, and shared interaction/status states—is centralized through Tailwind CSS v4 semantic theme variables and consumed by Home; appearance is light-only, no parallel TypeScript theme exists, and component tokens/variants are limited to showcase consumers (FR-016, DEC-011, DEC-013, NFR-008).
- [ ] The shared static shell and Home use semantic landmarks/headings, keyboard-operable controls, visible focus, reduced-motion behavior, responsive image/fallback handling, and minimal client JavaScript; server-only/dynamic functionality is not introduced (NFR-001, NFR-002, NFR-003, DEC-010).
- [ ] Shared rendering treats editorial content as data rather than raw HTML, introduces no user-derived HTML, and applies the SPEC's route-wide CSP, `nosniff`, referrer, permissions, and frame-denial headers without weakening Next/font or local-image behavior (NFR-005).
- [ ] Focused automated checks prove route/content/message parity, Home metadata, locale switching, token-contract completeness, and safe media fallback behavior.
- [ ] Home is exercised at the required compact and wide Playwright viewports with browser guards, axe checks, responsive/zoom spot checks, and preserved Unlighthouse plus documented transfer, image, JavaScript, CSS, LCP, INP, and CLS budgets; failures are fixed in this slice without weakening gates (DEC-012).

Traces: FR-001, FR-003, FR-013, FR-015, FR-016; NFR-001, NFR-002, NFR-003, NFR-004, NFR-005, NFR-007, NFR-008; DEC-001, DEC-008, DEC-010, DEC-011, DEC-012, DEC-013, SUBDEC-004.

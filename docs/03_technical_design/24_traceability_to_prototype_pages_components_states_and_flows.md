## 24. Traceability to Prototype Pages, Components, States, and Flows

| Prototype reference | Implementation consequence | Verification |
|---|---|---|
| §§3–4 navigation/layout | `next-intl` route tree, C-01–04, responsive Tailwind layout | Keyboard, compact/wide Playwright |
| §§5–6 visual/CTA direction | Tokenized Tailwind/shadcn styling, typed CTA/context | Visual review and CTA path tests |
| §7.1–7.4 Home/Destinations | Static page/data projections, C-05–16/23 | Flow A, metadata/link checks |
| §7.5–7.8 Experiences/Journeys | Static templates, explicit customizable wording | Flows B/C, honesty review |
| §7.9–7.11 About/How/FAQ | C-17–22, governed trust data | Flows D/E, accordion keyboard tests |
| §7.12 Contact | C-24 and optional C-26 | Direct-contact and safe fallback tests |
| §§7.13–7.14, §9 Form | C-25/27, local draft, API/Resend flow | Flows A/B/H and controlled email smoke |
| §§7.15–7.16 legal/error | Static legal shell, C-29/30 | noindex/recovery route tests |
| §8 C-01–C-30 | §7.2 component family mapping | Component review and E2E coverage |
| §§10–12 states/accessibility/motion | §13, §15, CSS reduced-motion utilities | Axe/keyboard/zoom/reduced-motion review |
| §13 Flows A–H | §18 Playwright suite | Required before demo |
| §§15–16 acceptance/assumptions | §18, §20, §22 | Demo checklist and owner decision |

---


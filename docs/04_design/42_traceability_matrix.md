
# Part XVIII — Traceability

## 42. Traceability Matrix

| Design-system decision | PRD source | Prototype source | Technical Design consequence |
|---|---|---|---|
| Quiet premium editorial direction | §§6–7, 13 | §§2, 5 | tokenized Tailwind styling |
| Aegean palette | §§6–7, 19 | §5.2 | CSS variables and semantic colors |
| Trust-first visual hierarchy | §§7, 20 | §§2, 5.6 | approved-content-only components |
| One dominant CTA | §14 | §6 | primary button variant |
| Cormorant + Inter | brand/readability direction | §5.2 provisional | `next/font`, two-family limit |
| Light theme only | maintainability/scope | no dark requirement | no dark token/variant |
| Generous editorial spacing | §§7, 13 | §4 | spacing tokens, container system |
| Cinematic hero | §§13, 17 | §§5, 7, 8 | `next/image`, focal metadata |
| Soft borders/minimal shadows | quiet premium | §§4–5, 8 | semantic border/shadow tokens |
| Header overlay→solid | navigation requirements | §§3.3, 8.1 | CSS transition and scroll state |
| Lucide icons | restrained iconography | §5.5 | shadcn-compatible icon import |
| Decorative Mediterranean details | authenticity, no clichés | §§2, 5 | optimized decorative SVG |
| Form visual system | §18 | §9 | RHF/Zod behavior styled consistently |
| Responsive modes | NFR-003/009 | §4 | CSS Grid/Flex, no device sniffing |
| Accessibility tokens | NFR-003 | §11 | focus, contrast, reduced motion |
| Bilingual typography | §§19, 25 | §§3.6, 11.4 | next-intl, stable layouts |
| Photography governance | §§19–20 | §5.4 | media manifest and validation |
| Status visuals | FR-015 | §§8.5, 10 | C-29 variants |
| Missing content visual | FR-015 | §§7.16, 8.5 | C-30 recovery state |
| Component mapping C-01–30 | §16 | §8 | implementation family structure |
| Visual regression | MVP quality | §15 | Playwright screenshots/QA |

---



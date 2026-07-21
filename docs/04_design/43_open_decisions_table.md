
# Part XIX — Open Design Decisions

## 43. Open Decisions Table

| Decision | Owner | Interim treatment | Implementation impact |
|---|---|---|---|
| Final logo and logo variants | Product owner / brand designer | use supplied mark; prepare dark/light single-color variants | header/footer spacing and contrast |
| Exact primary blue after final imagery/logo review | Product/design | use `#17475F` provisional | semantic token only; low migration cost |
| Exact teal focus/accent value | Product/design/accessibility | use `#34767A`, verify 3:1 ring contrast | focus and selected states |
| Final font files/weights/subsetting | Technical/design | Cormorant 500/600; Inter 400/500/600/700 | payload and rendering |
| Photography library and licensing | Product/content | approved representative media only | crop and visual QA |
| Decorative motif artwork | Brand/design | use minimal line-based placeholders | decorative SVG assets |
| Deep-blue footer versus light footer | Product/design | default light/subtle surface | footer contrast and brand weight |
| Final Greek content and line-break review | Content/localization | representative bilingual content | type tuning and responsive QA |
| Final partner/trust mark treatment | Product/legal/rights holder | omit until approved | trust module composition |
| Hero video use | Product/design/performance | still imagery default | media loading and controls |
| Sticky mobile CTA | Product/UX research | omitted by default | mobile viewport and overlap |
| Optional destination filters | Product/design/content | omitted until content supports them | control styling and empty state |
| Final accessibility audit findings | Accessibility owner | WCAG 2.2 AA rules in this doc | token/component adjustment |
| Production visual-system evolution | Product/technical | preserve tokens/components; revisit imagery/brand assets | future DESIGN.md revision |

---



## 18. Testing and Quality Gates

### 18.1 Lightweight test strategy

Playwright is the primary test tool because the value lies in real page, responsive, navigation, and form behavior.

| Check | Required prototype coverage |
|---|---|
| Build/content | TypeScript check, lint, content schema validation, static build |
| Playwright desktop | Home, detail, CTA, navigation, form happy path, form error/retry, language switch |
| Playwright mobile | Compact menu, cards, form conditional child ages, reflow, touch targets |
| Form persistence | Refresh, back/continue, language switch, manual clear, 72-hour simulated expiry |
| Email | Mocked unit/route test plus controlled Resend test recipient smoke check |
| Accessibility | Playwright keyboard journey and axe smoke checks for key pages/forms; manual review before demo |
| SEO | Rendered title/meta/canonical/hreflang/sitemap/robots and internal-link check |
| Performance | Lighthouse/bundle review for Home, one detail, and Plan My Trip; test with final representative media |

Add focused unit tests only for the highest-risk pure logic: content loading, locale route resolution, form draft expiry, schema cross-field validation, and email payload mapping. Do not build a large test pyramid for static content.

### 18.2 Required prototype flows

Implement and test Prototype Flows A–H where they are meaningful to the prototype:

- destination-led request with contextual prefill;
- mobile family request and child ages;
- journey evaluation/customization;
- trust/contact path;
- FAQ-to-CTA path;
- bilingual detail continuity and missing translation recovery;
- navigation/404 recovery;
- persistence, invalid values, failure-preserved retry, and accepted confirmation.

### 18.3 Quality gates before client presentation

- `pnpm lint`, `pnpm typecheck`, `pnpm validate:content`, and `pnpm build` pass.
- Playwright critical flows pass at 390 px and 1440 px.
- No console errors or failed critical network requests.
- Form submission reaches a controlled Gmail test inbox and acknowledgement reaches a test recipient.
- English/Greek routes, language switching, canonical metadata, and sitemap work.
- Keyboard navigation, focus, error summary, contrast, zoom, and reduced motion are manually checked.
- No real personal/client form data appears in Git, screenshots, logs, previews, or analytics.
- All visible claims/assets are approved or clearly marked as prototype placeholders during presentation.

---


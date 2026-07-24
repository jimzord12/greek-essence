# Visual Review 04: Browse a complete bilingual Home through the shared showcase foundation

Date: 2026-07-24
Reviewer: fresh independent visual-review agent
Issue: `01-browse-bilingual-home`
Verdict: `FAIL`
Route: `implementation repair → fresh code review if source changes → fresh visual review; remain in-review`

## Scope

Reviewed the final rendered production application for issue #01 only. Read root and feature `AGENTS.md`, `NEXT.md`, approved feature `SPEC.md`, `issue.md`, `change-contract.md`, code review `reviews/03-review.md`, `implementation-report.md`, the repository-local `greek-essence-quality-review` and Playwright CLI skills/checklists, and relevant approved Home, responsive, typography, media, motion, and accessibility guidance. Started `pnpm start --hostname 127.0.0.1 --port 4173` from the existing production build, verified `/en` returned HTTP 200, inspected only `/en` and `/el`, and stopped the server after review.

Rendered review covered both locales at exact `390 × 844` and `1440 × 1024`, full-page six-section composition, wide selected/current navigation, compact menu closed/open, locale switching, keyboard-visible focus, Escape/focus return, reduced-motion presentation, pending-media fallback, footer, long Greek wrapping, an `834 × 1112` transition state, and a `195 px` CSS viewport used as the 200%-zoom equivalent. Screenshots contain only public synthetic showcase content.

## Visual Verdict

`FAIL`. The ordinary compact, medium, and wide Home presentation is polished and coherent: all six sections are visible in the intended order; the warm-ivory/deep-Aegean palette, hierarchy, restrained surfaces, editorial spacing, CTA prominence, neutral pending-media fallback, and footer read intentionally; EN/GR content is locale-pure apart from the brand/proper names and language controls; compact and wide focus/current/menu states are clear; and the reviewed production session showed no console errors, warnings, broken assets, or failed critical requests.

However, the required 200%-zoom-equivalent Greek state has real horizontal overflow. At `195 px`, `document.documentElement.scrollWidth` and `document.body.scrollWidth` are `205 px` while `clientWidth` is `195 px`. Long Greek display and card text exposes intrinsic over-width descendants. This violates the explicit no-horizontal-overflow/reflow acceptance boundary and blocks visual approval.

The strict Home LCP `<=2500ms` gate remains technically RED and is carried unchanged as the operator-authorized **nonvisual residual risk** from code review 03. This visual review does not reinterpret it as passing and does not use it to determine the visual verdict.

## Blocking Findings

### VIS-04-01 — Greek 200%-zoom-equivalent state horizontally overflows

- Severity: blocking
- Category: responsive / accessibility / visual reflow
- Route: `/el`
- Viewport/state: `195 × 844` CSS viewport, 200%-zoom equivalent, full page
- Evidence: `evidence/04-visual/el-195x844-zoom200-equivalent-full.png`
- Observed: the page is visually forced into extremely narrow wrapping and exposes a 10 px horizontal overflow (`scrollWidth: 205`, `clientWidth: 195`). DOM inspection identified over-wide descendants in the promise section, How It Works headings/body copy, and trust section; examples included a `155 px`-wide H2 with `185 px` scroll width and `107 px`-wide H3s with up to `130 px` scroll width.
- Expected: all meaningful Greek content, navigation, CTAs, section headings, cards, and footer reflow at 200% zoom without horizontal page scrolling or clipped critical text.
- Required repair: remove the intrinsic text overflow at this supported narrow/reflow state without hiding overflow or truncating content; rerun the 195 px/200% equivalent in both locales, affected responsive/browser/accessibility gates, and obtain the required fresh reviews.

## Non-Blocking Findings

### NVIS-04-01 — Greek display fallback is visibly heavier than English

Greek headings remain readable, correctly accented, and unclipped at 390, 834, and 1440 widths, but the available serif fallback has a materially heavier, less delicate character than the English Cormorant Garamond headings. The presentation remains coherent and acceptable for this pending-media Tier-2 prototype, so this is a polish observation rather than an independent blocker. Evidence: `el-390x844-compact-closed-full.png`, `el-834x1112-medium-transition-full.png`, and `el-1440x1024-wide-current-nav-full.png`.

No other visual defect was found in the required ordinary compact/wide states. Compact visible controls measured at least 44 px high in the initial viewport; focus rings were visible and unclipped; Escape closed the menu, restored focus to the trigger, and set `aria-expanded="false"`; reduced-motion emulation produced `0s` transition/animation durations on the sampled controls; and the pending media presented as a clean, fixed-aspect neutral gradient with no broken-image icon or misleading decorative label.

## Evidence

All paths are relative to `reviews/evidence/04-visual/`.

- `en-390x844-compact-closed-full.png` — full six-section English compact Home and footer.
- `el-390x844-compact-closed-full.png` — full six-section Greek compact Home, long wrapping, fallback, and footer.
- `en-390x844-compact-menu-open.png` — compact English menu open/current state.
- `en-390x844-compact-menu-keyboard-focus.png` — visible keyboard focus in open menu.
- `en-390x844-compact-menu-escape-focus-return.png` — closed menu with visible trigger focus after Escape.
- `el-390x844-reduced-motion-menu-open.png` — localized compact menu under reduced-motion emulation.
- `en-1440x1024-wide-current-nav-full.png` — full English wide Home with selected/current navigation.
- `el-1440x1024-wide-current-nav-full.png` — full Greek wide Home with selected/current navigation.
- `el-1440x1024-wide-current-nav-header.png` — focused evidence of wide Greek navigation.
- `en-1440x1024-wide-keyboard-focus-header.png` — visible wide header keyboard focus and selected Home state.
- `el-834x1112-medium-transition-full.png` — intermediate responsive composition.
- `el-195x844-zoom200-equivalent-full.png` — full Greek 200%-zoom-equivalent state and blocking overflow context.

Every listed principal screenshot was visually inspected, not treated as self-certifying automation evidence.

## Verification Considered

- Production server: `pnpm start --hostname 127.0.0.1 --port 4173` — ready in 155 ms; `/en` returned HTTP 200.
- Playwright CLI only was used for browser interaction, per repository policy.
- Locale switch: `/en` → `/el` and `/el` → `/en` preserved Home route identity and updated document language/title.
- Section count: six rendered `main section` elements at wide inspection.
- Ordinary overflow checks: `390/390` and `1440/1440` scroll/client widths in reviewed states; the `834 × 1112` screenshot was visually inspected for clipping and overflow.
- Blocking reflow check: `/el` at 195 px returned `scrollWidth 205` vs `clientWidth 195`.
- Compact target sampling: visible brand link `139 × 44`, menu `73 × 45.98`, primary CTA `133 × 52.39`, and secondary CTA `241 × 52.39` CSS px.
- Keyboard: focus was visibly outlined; compact Escape returned focus to `Menu` with `aria-expanded="false"`.
- Reduced motion: sampled links/buttons reported `transition-duration: 0s` and `animation-duration: 0s`.
- Console/network: zero console errors or warnings; reviewed static document, CSS, JS, fonts, favicon, and RSC requests returned 200; no broken asset was visible.
- Pending media: visually intentional warm neutral gradient, stable aspect ratio, no broken-image affordance, meaning retained in adjacent text.
- EN/GR parity: complete localized shell and six-section copy; no mixed-language fallback beyond brand/proper names and the deliberate opposite-language control.
- Issue #02 routes were not opened or reviewed.
- Nonvisual residual risk: strict Home LCP `<=2500ms` remains technically failing but operator-authorized for workflow progression, exactly as recorded by code review 03.

## Required Route

Keep issue #01 `in-review`. Route `VIS-04-01` to in-contract implementation repair. Because correcting responsive CSS/source materially changes implementation, run the affected/full verification and obtain a fresh independent code-review attempt before a new immutable fresh visual-review attempt. Do not mark the issue done, do not begin issue #02, and do not treat the operator-authorized LCP exception as a technical performance pass.

# Review 04 response — B06-01

## F-06 — High

The earlier response's `provided` throttling approach is withdrawn. Terra Review 05 correctly identified that it changed Lighthouse's mobile metric methodology and weakened the locked acceptance semantics.

The effective correction retained is the client-only dynamic `QualityLabToggle` boundary in `app/[locale]/quality-lab/page.tsx` and `components/quality-lab-toggle.tsx`. It defers the existing non-critical interactive toggle graph while preserving the interaction and static page generation.

The gate now relies on the repository default Lighthouse mobile methodology: `formFactor: "mobile"` and `throttlingMethod: "simulate"`. No budgets, routes, samples, device, or audit selection were changed.

Final default-methodology verification passed twice consecutively from one fresh production build. The exact four-route median report is:

- `/el`: performance 0.93, accessibility 1.00, best practices 1.00, SEO 1.00
- `/el/quality-lab`: performance 0.92, accessibility 1.00, best practices 1.00, SEO 1.00
- `/en`: performance 0.93, accessibility 1.00, best practices 1.00, SEO 1.00
- `/en/quality-lab`: performance 0.93, accessibility 1.00, best practices 1.00, SEO 1.00

## F-04 — Non-blocking

Preserved as documented technical debt. No metadata-origin policy or fallback behavior was changed.

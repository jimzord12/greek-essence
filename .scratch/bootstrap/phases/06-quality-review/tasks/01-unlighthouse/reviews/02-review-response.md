# Review response — B06-01 / Review 02

## F-01 — High

Resolved. Added the static `app/robots.ts` special route so Lighthouse receives a valid `/robots.txt` rather than treating it as a locale. The final report contains exactly `/en`, `/el`, `/en/quality-lab`, and `/el/quality-lab`; all score categories meet budget. SEO is 1.00 for every route.

## F-03 — High

Resolved. Restored locale validation and `dynamicParams = false`, so non-locale special-route requests cannot reach dynamic locale/message imports. The final production-audit output contained no `NoFallbackError`, missing `messages/*.json`, server error, or failed critical-request lines. The generated static `/robots.txt` route prevents the former `robots.txt` locale attempt.

## F-04 — Non-blocking

Partly addressed. Normal development remains `http://localhost:3000`; the audit needs the locked production server's origin for static canonical validation. The fallback remains restricted to production builds without `NEXT_PUBLIC_SITE_URL`; deployers set that public site URL for non-audit production origins. No script composition was changed.

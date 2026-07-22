# Review 03 Response

**Implementer:** `20260722_130707_6dcbf0`
**Verdict:** All five High findings corrected; task remains `In review` pending independent re-review.

## Finding dispositions

1. **High — Metadata checks do not verify locale/SEO semantics: Resolved**
   - Added a four-route metadata matrix covering `/en`, `/el`, `/en/quality-lab`, and `/el/quality-lab`.
   - Assertions now require exact `html[lang]`, canonical pathname, the complete `en`/`el`/`x-default` alternate pathname mapping, and exact `noindex, nofollow` page robots content.
   - Controlled mutations of the home canonical path, home `en` hreflang path, and home robots directive each failed the focused metadata test with exit 1 before the implementation was restored.

2. **High — Quality-lab interaction coverage missing: Resolved**
   - Added role-based toggle journeys for both localized quality-lab routes.
   - English activates by click; Greek activates through focused keyboard Space; both assert `aria-pressed="true"` and the exact localized live status text.
   - A temporary toggle mutation that prevented selection failed the focused interaction test with exit 1 and was removed/reverted.

3. **High — Invalid-locale handling suppresses unrelated console/HTTP failures: Resolved**
   - Replaced the broad invalid-locale suppression flag with an exact allowlist for only `http://127.0.0.1:3100/invalid`, resource type `document`, status `404`, plus its exact browser-generated console message at that document URL.
   - All other console errors, request failures, and critical 4xx/5xx responses remain collected and fail teardown.
   - The invalid-locale journey passes after the correction; the shared guard probes demonstrate unrelated console and critical-response failures remain fatal.

4. **High — Uncaught page errors are not guarded: Resolved**
   - Added a pre-navigation shared `page.on("pageerror")` collector and fail-closed teardown assertion.
   - The temporary uncaught page-error probe failed with exit 1 and was removed.

5. **High — Accessibility journeys lack console/network/page-error guards: Resolved**
   - Moved console, critical request, exact invalid-document exception, and page-error collection into `tests/e2e/browser-guards.ts`.
   - Applied the helper before navigation in both localization and axe accessibility specs, including both quality-lab routes.
   - Temporary console, critical-response, and page-error probes each failed with exit 1 and were removed.

## Verification

- Focused localization suite: 15 passed across compact, medium, and wide projects.
- Final `CI=1 pnpm test:e2e`: 27 passed.
- Final `pnpm test:a11y`: 12 passed.
- No unresolved Review 03 findings remain from the implementer side; independent Terra re-review is still required.

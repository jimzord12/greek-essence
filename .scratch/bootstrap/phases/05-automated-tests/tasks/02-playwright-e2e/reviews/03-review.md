# Review 03

**Reviewer:** Fresh independent post-run remediation reviewer
**Verdict:** Changes requested

## Findings

### Blocking findings

None.

### High-impact findings

1. **High — Metadata checks do not verify the required locale/SEO semantics**
   - **Location:** `tests/e2e/localization-and-quality.spec.ts:61-85`.
   - **Requirement:** `task.md:28` requires metadata coverage; `docs/03_technical_design/18_testing_and_quality_gates.md:15,39` requires rendered canonical and hreflang/locale behavior. The audit specifically requires canonical, hreflang, locale, and robots semantics rather than non-emptiness.
   - **Evidence/reproduction:** The test asserts only an `html[lang]` prefix and non-empty title, description, and canonical `href`. It never checks the canonical route, `link[rel=alternate][hreflang]` mappings, `x-default`, or `meta[name=robots]`; therefore an incorrect canonical and absent alternates/robots would pass. Current Playwright CLI inspection confirms the live `/en`, `/el`, `/en/quality-lab`, and `/el/quality-lab` pages presently render localized canonical paths, `en`/`el`/`x-default` alternates, and `noindex, nofollow`, but the permanent test does not protect them.
   - **Required correction:** Add role/DOM assertions for exact route semantics on both locales and both fixture/quality-lab routes: `lang`, canonical pathname, `en`, `el`, and `x-default` alternate paths, and `noindex, nofollow` page robots. Assert the documented `/robots.txt` response separately if it remains part of the intended robots contract.
   - **Verification:** `CI=1 pnpm test:e2e` must pass; controlled mutations to a canonical path, an hreflang mapping, and the page robots directive must each fail the focused test before removal.

2. **High — The permanent suite does not exercise the fixture quality-lab interaction**
   - **Location:** `tests/e2e/localization-and-quality.spec.ts:61-113`; `tests/e2e/accessibility.spec.ts:14-31`.
   - **Requirement:** `task.md:28-29` requires interaction coverage with role/label locators. `docs/03_technical_design/18_testing_and_quality_gates.md:5,14` makes real page behavior and Playwright keyboard/accessibility journeys the required strategy. The remediation brief specifically calls for fixture/quality-lab interaction coverage.
   - **Evidence/reproduction:** The B05-02 suite visits only `/en` and `/el`; the later axe suite visits quality-lab but only runs `AxeBuilder.analyze()` and performs no interaction. Playwright CLI inspection showed the actual `FixtureToggle` changes `aria-pressed` and the live status text from Not selected to Selected in English and from Δεν έχει επιλεγεί to Επιλεγμένο in Greek, yet no durable test would fail if that client interaction regressed.
   - **Required correction:** Add a role-based quality-lab journey for both locales that activates the toggle (including keyboard activation where applicable) and asserts `aria-pressed` plus the localized live status; retain the existing static axe coverage.
   - **Verification:** Run the focused new quality-lab journey in all configured Chromium projects and `CI=1 pnpm test:e2e`; a temporary broken toggle transition must fail before removal.

3. **High — Invalid-locale handling disables unrelated console and HTTP failure detection**
   - **Location:** `tests/e2e/localization-and-quality.spec.ts:24-59,96-105`.
   - **Requirement:** `task.md:28` and `docs/03_technical_design/18_testing_and_quality_gates.md:35-37` require console and critical-request coverage with no console errors or failed critical network requests. The expected invalid-locale 404 may be excluded, but unrelated failures must remain observable.
   - **Evidence/reproduction:** Setting `expectsNotFound = true` before `page.goto('/invalid')` makes the console and all critical `response.status() >= 400` handlers ignore every event for the rest of the test. A console error or a failed script/fetch/XHR accompanying that navigation would leave both arrays empty and the test green; the suppression is not constrained to the expected `/invalid` document 404.
   - **Required correction:** Identify and permit only the expected document response for the exact invalid-locale URL/status. Continue recording all console errors, request failures, and every other critical 4xx/5xx response during and after that navigation.
   - **Verification:** Keep the invalid-locale assertion passing, then use controlled interception/injection to prove an unrelated critical 4xx/5xx and a console error both fail the journey.

4. **High — Uncaught page errors are not guarded**
   - **Location:** `tests/e2e/localization-and-quality.spec.ts:28-59`; `tests/e2e/accessibility.spec.ts:14-31`.
   - **Requirement:** `task.md:28` requires console/critical-request quality coverage, and `docs/03_technical_design/18_testing_and_quality_gates.md:37` requires no console errors. Uncaught `pageerror` is independent browser failure evidence and is explicitly in scope for this remediation audit.
   - **Evidence/reproduction:** Neither current spec registers `page.on('pageerror')` or asserts a collected page-error list. The current green suite can therefore pass after an uncaught application exception that does not emit a console message captured by the existing listener.
   - **Required correction:** Add a reusable pre-navigation page-error collector and teardown assertion, with the narrowly scoped invalid-locale exception rules above if genuinely needed.
   - **Verification:** A controlled uncaught page error must make the focused journey fail; `CI=1 pnpm test:e2e` must then pass after the probe is removed.

5. **High — Accessibility journeys have no console/network critical-request guards**
   - **Location:** `tests/e2e/accessibility.spec.ts:14-31`.
   - **Requirement:** `task.md:28` requires console and critical-request tests; `docs/03_technical_design/18_testing_and_quality_gates.md:37` requires no console errors or failed critical network requests. The current accessibility routes include both localized quality-lab pages and are relevant browser journeys under the remediation brief.
   - **Evidence/reproduction:** Each axe test navigates and analyzes its route without `console`, `requestfailed`, `response`, or `pageerror` listeners. The B05-02 collector is scoped to a different `describe` and only visits the two home routes. Thus `/en/quality-lab` and `/el/quality-lab` can emit an error or fail a critical request while their axe tests remain green.
   - **Required correction:** Move the fail-closed console, critical-request, and page-error guard into a shared helper/fixture and apply it before navigation in both localization and accessibility specs, preserving only the exact invalid-locale document exception.
   - **Verification:** Run `CI=1 pnpm test:e2e` and `pnpm test:a11y`; controlled console, pageerror, and critical-request failures on a quality-lab accessibility route must fail before removal.

### Non-blocking findings

None.

## Verification performed

- `git status --short`; inspected historical commit `e5e6828` and its full B05-02 diff; `git diff --check e5e6828^ e5e6828` — exit 0. The pre-existing untracked audit directory was preserved.
- `pnpm exec playwright --version` — exit 0; `Version 1.61.1`.
- `pnpm exec playwright test --list` — exit 0; 24 current tests across Chromium compact, medium, and wide projects (the 12 B05-02 tests plus 12 later axe tests).
- `pnpm format:check` — exit 0.
- `CI=1 pnpm test:e2e` — exit 0; 24 passed in 27.4 seconds.
- Stable failure-artifact check over all nine historical compact/medium/wide screenshot, video, and trace paths plus `git check-ignore -q` — exit 0; all files are nonempty and ignored.
- Playwright CLI (`playwright-cli` 0.1.14) against a fresh `pnpm dev --port 3100` server — exit 0: inspected English and Greek quality-lab rendering, activated the real toggle in both locales, switched English quality-lab to Greek, and inspected current canonical/alternate/robots output. No browser console errors or warnings were reported for that manual session; critical requests observed were successful.

## Evidence

`playwright.config.ts:3-41` currently satisfies the locked Chromium-only project, viewport, local base URL/web-server, timeout, retry, and retained-failure-artifact configuration. The current rendered implementation also has the expected localized metadata and working quality-lab control. The High findings concern missing or unsafely broad permanent regression evidence, not a presently observed runtime defect. Green current tests do not satisfy the original B05-02 coverage contract because the documented mutations would still pass.

## Handoff verification

Not applicable. This audit review does not change handoff state.

## Durable knowledge verification

Not applicable. This audit review does not change durable knowledge.

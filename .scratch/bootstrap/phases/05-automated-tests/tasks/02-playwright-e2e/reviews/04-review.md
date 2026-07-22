# Review 04

**Reviewer:** `20260722_124049_19b52a`
**Verdict:** Changes requested

## Finding dispositions

### Review 03 High findings

1. **High — Metadata checks do not verify the required locale/SEO semantics: Resolved**
   - **Correction inspected:** `tests/e2e/localization-and-quality.spec.ts:9-42,83-115,128-133` now checks the exact `lang`, canonical pathname, ordered `en`/`el`/`x-default` alternate path mapping, and exact `noindex, nofollow` directive on `/en`, `/el`, `/en/quality-lab`, and `/el/quality-lab`.
   - **Verification:** `CI=1 pnpm exec playwright test tests/e2e/localization-and-quality.spec.ts --grep 'renders exact localized metadata semantics|redirects the root route and rejects an invalid locale|exercises localized quality-lab toggle interaction'` — exit 0; metadata test passed in compact, medium, and wide projects. The recorded controlled canonical, hreflang, and robots mutations are absent from the current diff.

2. **High — The permanent suite does not exercise the fixture quality-lab interaction: Resolved**
   - **Correction inspected:** `tests/e2e/localization-and-quality.spec.ts:44-80,151-177` covers English click activation and Greek keyboard Space activation with role locators, exact `aria-pressed`, and exact localized polite-status assertions.
   - **Verification:** The focused command above — exit 0; all three project instances of the quality-lab journey passed. Independent Playwright CLI inspection on `/el/quality-lab` used four real Tab presses to reach the Greek toggle, then Space changed its focused label to `Επιλεγμένο`, `aria-pressed` to `true`, and live text to `Τρέχουσα κατάσταση: Επιλεγμένο` — exit 0. No focus teleportation is used by `tabTo`.

3. **High — Invalid-locale handling disables unrelated console and HTTP failure detection: Resolved**
   - **Correction inspected:** `tests/e2e/browser-guards.ts:11-78` permits only the exact `http://127.0.0.1:3100/invalid` document 404 and one exact browser console message at that URL after that response has been observed. Every other error console message, failed critical request, or critical 4xx/5xx response is collected.
   - **Verification:** The focused command above — exit 0; the invalid-locale journey passed in all three projects. Source inspection confirms the allowlist remains constrained by URL, document resource type, status, message text, location URL, and single consumption; no broad mode flag remains. The temporary guard-probe files cited in the response/evidence are absent.

4. **High — Uncaught page errors are not guarded: Resolved**
   - **Correction inspected:** `tests/e2e/browser-guards.ts:15-19,80-90` installs `page.on("pageerror")` before navigation and fails teardown on every collected uncaught exception. It is installed by both specs before navigation.
   - **Verification:** `CI=1 pnpm test:e2e` — exit 0; 27 passed. The temporary page-error probe is absent, and the response/evidence documents its expected failing run.

5. **High — Accessibility journeys have no console/network critical-request guards: Resolved**
   - **Correction inspected:** `tests/e2e/accessibility.spec.ts:4-8,20-29,31-47` installs and asserts the shared guards around every axe route, including both localized quality-lab routes.
   - **Verification:** `pnpm test:a11y` — exit 0; 12 passed across all four routes and three Chromium projects. `CI=1 pnpm test:e2e` — exit 0; all 27 tests passed.

## Findings

### Blocking findings

None.

### High-impact findings

1. **High — The remediation evidence falsely says the project TypeScript command typechecks the Playwright tests**
   - **Location:** `.scratch/bootstrap/phases/05-automated-tests/tasks/02-playwright-e2e/evidence.md:9`; `tsconfig.json:31-40`.
   - **Requirement:** `.scratch/bootstrap/protocol.md:163-166` requires exact commands and results and prohibits fabricated/inferred evidence. The re-review instruction expressly requires strict test typechecking.
   - **Evidence/reproduction:** The recorded command `pnpm exec tsc --noEmit` exits 0, but `tsconfig.json` explicitly excludes `tests`; it therefore does not typecheck `tests/e2e/browser-guards.ts`, `localization-and-quality.spec.ts`, or `accessibility.spec.ts`. The claim that this command passed “including the Playwright specs and shared guard helper” is false.
   - **Required correction:** Amend the evidence row to state that the project command excludes tests, and record the actual strict explicit-file test typecheck (including `--ignoreConfig` and the repository strict flags) with its exit/result. Preserve the existing command entry as a source-only typecheck if desired.
   - **Verification:** Re-run the recorded explicit test command and require exit 0:
     ```text
     pnpm exec tsc --ignoreConfig --noEmit --strict --noUncheckedIndexedAccess --exactOptionalPropertyTypes --noImplicitOverride --noFallthroughCasesInSwitch --noUncheckedSideEffectImports --useUnknownInCatchVariables --target ES2017 --lib dom,dom.iterable,esnext --module esnext --moduleResolution bundler --esModuleInterop --resolveJsonModule --isolatedModules --jsx react-jsx --skipLibCheck tests/e2e/browser-guards.ts tests/e2e/localization-and-quality.spec.ts tests/e2e/accessibility.spec.ts
     ```

### Non-blocking findings

None.

## Verification performed

- `git diff --check` — exit 0; reviewed the complete current B05-02 remediation diff and task-owned report, evidence, and response.
- `pnpm exec tsc --noEmit` — exit 0; confirmed the project command itself passes but, per `tsconfig.json`, excludes `tests`.
- The explicit strict test-file command in the High finding verification — exit 0; all three current Playwright TypeScript files typecheck under the repository strict options.
- Focused metadata, invalid-locale, and quality-lab command — exit 0; 9 passed across compact, medium, and wide in 15.1 seconds.
- `CI=1 pnpm test:e2e` — exit 0; 27 passed in 26.8 seconds.
- `pnpm test:a11y` — exit 0; 12 passed in 9.6 seconds.
- Playwright CLI against a fresh `pnpm dev --port 3100` server — exit 0; real Tab traversal reached the Greek toggle and Space produced the asserted selected state/live text; browser console reported no errors or warnings.
- Temporary-probe shell check — exit 0; no `tests/e2e/*temporary*` or `tests/e2e/*review03*` files remain. The remediation diff contains no changed files under `app`, `components`, or `i18n`.

## Evidence

All five Review 03 behavioral findings are corrected in the actual current tests and pass decisive independent verification. Approval is withheld only for the remaining High evidence-integrity defect: the task evidence currently attributes test-file typechecking to a command that excludes the tests.

## Handoff verification

Not applicable. This re-review does not change handoff state.

## Durable knowledge verification

Not applicable. This re-review does not change durable knowledge.

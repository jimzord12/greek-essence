# Phase 04 Review 01

**Reviewer session:** `20260722_081012_dfe398`

## 1. Scope and approval precondition

Reviewed only the Phase 04 contract, B04-01 through B04-03 implementation/evidence records, paired responses, latest numbered task reviews, the committed Phase 04 range `fc3a9c6..0b42a4a`, and the live routing, fixture, localization, metadata, and interaction files.

The task-level approval precondition is present:

1. B04-01: `reviews/02-review.md` — `**Verdict:** Approved`.
2. B04-02: `reviews/02-review.md` — `**Verdict:** **Approved**`.
3. B04-03: `reviews/01-review.md` — `**Verdict:** **Approved**`.

Tracking assertions exited `0`: all three task front matters and the phase status table say `Done`; the phase state is `In review`; and `.scratch/bootstrap/README.md` says Phase 04 is `In review` with `3/3` tasks done.

## 2. Decisive integration verification

The consolidated production-browser gate used only the approved Playwright CLI workflow. Generated logs, the harness, and 16 route/viewport screenshots are ignored under `.artifacts/bootstrap/phase04-review/`.

1. `pnpm build > .artifacts/bootstrap/phase04-review/build.log 2>&1` — exit `0`; Next.js 16.2.6 compiled and statically generated `/en`, `/el`, `/en/quality-lab`, and `/el/quality-lab`.
2. `pnpm start --port 3100 > .artifacts/bootstrap/phase04-review/server.log 2>&1` plus the readiness request to `http://127.0.0.1:3100/en` — server ready with HTTP `200`; the tracked background process was terminated after the gate.
3. `playwright-cli -s=phase04-review open http://127.0.0.1:3100/en` followed by `playwright-cli -s=phase04-review run-code --filename=.artifacts/bootstrap/phase04-review/integration-gate.js` — Playwright CLI process exit `0`, but the command emitted a semantic `Error`, so the integration gate failed. The harness completed all checks before throwing and reported four substantive failures: both quality-lab language switches lost the equivalent route, and reduced-motion preference did not reduce either localized toggle transition (`0.15s -> 0.15s`). The separate expected `/fr` `404` also produced browser resource-error noise; that intentional invalid-locale request is not a defect.
4. Passing assertions within that same gate: `/` returned `307` with `Location: /en`; `/fr` returned `404`; all four fixtures returned `200` with the correct `lang`, one H1, an applied stylesheet, no base or 200%-text-reflow horizontal overflow at `320`, `390`, `834`, and `1440` px, and targets at least 44×44 CSS px. English and Greek toggle focus, Space activation, `aria-pressed`, and localized live status passed.
5. The same rendered gate passed exact localized title, description, canonical, `en`/`el`/`x-default` equivalent alternates, and `noindex, nofollow` assertions for all four fixtures. It found zero JSON-LD scripts, forms, or rendered production/trust claim markers.
6. The tracking assertion command — exit `0`; all three tasks are `Done`, Phase 04 is `In review`, and the dashboard is `3/3 In review`. `git check-ignore -q .artifacts/bootstrap/phase04-review/integration-gate.log` — exit `0`.

## 3. Findings

### 3.1 High — Quality-lab language switching does not preserve the equivalent route

- Exact location: `app/[locale]/quality-lab/page.tsx:54-59`.
- Violated requirement: B04-01 acceptance requires equivalent language switching; Technical Design §9 requires an index/static page language switch to resolve to the same equivalent route; the phase review must inspect task interactions.
- Evidence/reproduction: In the consolidated Playwright gate, `/en/quality-lab` rendered its language-switch link as `/el` instead of `/el/quality-lab`, and `/el/quality-lab` rendered `/en` instead of `/en/quality-lab`. Both landing-page switches preserved their equivalents.
- Required correction: Make the quality-lab language switch target the opposite locale's `/quality-lab` equivalent without changing the fixture scope or adding product navigation.
- Verification: Rebuild and use Playwright CLI in both locales to assert the rendered switch href and activated destination are `/el/quality-lab` from English and `/en/quality-lab` from Greek, with the destination `lang` and localized content intact.

### 3.2 High — Reduced-motion preference leaves the fixture transition unchanged

- Exact location: `components/ui/button.tsx:6-8` as composed by `components/fixture-toggle.tsx:22-30`.
- Violated requirement: Technical Design §7.4 requires all non-essential movement to be disabled or reduced under `prefers-reduced-motion`; Design System §35.7 requires reduced-motion support. B04-02 acceptance and verification explicitly include reduced motion.
- Evidence/reproduction: The consolidated Playwright gate compared computed toggle transition duration under `reducedMotion: "no-preference"` and `reducedMotion: "reduce"`. Both `/en/quality-lab` and `/el/quality-lab` remained `0.15s -> 0.15s`; the preference was active but behavior was neither disabled nor reduced.
- Required correction: Apply the repository's Tailwind reduced-motion treatment at the appropriate source-owned button/fixture boundary so this non-essential transition is disabled or measurably reduced when the preference is active.
- Verification: In both localized quality labs, compare the computed transition under no preference and reduced motion and require zero or a shorter reduced duration; recheck keyboard Space activation, focus treatment, and visible/live pressed state.

## 4. Exit gate and readiness

The static routes, reference-width reflow, root/invalid-locale behavior, localized metadata, equivalent metadata alternates, indexing safety, JSON-LD exclusion, and claim exclusion pass. The phase exit gate is not satisfied because equivalent language switching and reduced-motion behavior fail at the integrated quality-lab surface.

Phase 04 must remain `In review`. Phase 05 must not start until the owning task corrections are independently verified and the phase review is approved.

**Verdict:** Changes requested

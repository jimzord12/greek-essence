# B05-03 Evidence

| Command | Exit | Result |
|---|---:|---|
| `pnpm add -D @axe-core/playwright@4.12.1` | 0 | Added the exact-pinned axe Playwright integration. |
| `CI=1 pnpm exec playwright test tests/e2e/accessibility-controlled-failure.spec.ts` | 1 | Temporary missing-`alt` image was detected in all three Chromium projects; each run attached full `axe-results` JSON before the expected zero-violations assertion failed. Temporary spec then removed. |
| `pnpm test:a11y` | 0 | Initial gate run: 12 passes, zero violations across four localized variants and three Chromium viewports. |
| `pnpm format:check` | 1 | Detected only the newly added spec's formatting; corrected the line wrapping. |
| `pnpm lint` | 0 | Passed with the pre-existing anonymous-default-export warning in `commitlint.config.mjs`. |
| `pnpm typecheck` | 0 | Passed. |
| `pnpm build` | 0 | Passed; generated `/en`, `/el`, `/en/quality-lab`, and `/el/quality-lab`. |
| `pnpm format:check && pnpm test:a11y` | 0 | Final formatting check passed; final axe run passed all 12 scans with zero violations. |
| `git diff --check` | 0 | No whitespace errors. |
| `git check-ignore -v .artifacts/bootstrap/playwright/test-results/.last-run.json .artifacts/bootstrap/playwright/report/index.html` | 0 | Both are ignored by `.gitignore:40` (`.artifacts/bootstrap/`). |

Artifact paths:

- `.artifacts/bootstrap/playwright/test-results/` (Playwright output; controlled-failure output existed here before the final passing run reset the directory)
- `.artifacts/bootstrap/playwright/report/index.html`
- `.artifacts/bootstrap/playwright/test-results/.last-run.json`
- `.artifacts/bootstrap/playwright/failure-policy/` (existing B05-02 failure-policy artifacts, unchanged)

The controlled temporary spec was deleted after the expected failure. The permanent gate attaches complete `axe-results` JSON to Playwright output whenever a violation occurs.

## Phase 05 Review 01 H1 correction

| Command | Exit | Result |
|---|---:|---|
| `pnpm install --frozen-lockfile` | 0 | Lockfile resolved the exact `@playwright/test` and direct `playwright-core` `1.61.1` set. |
| `pnpm exec tsc --noEmit --project tsconfig.test.json` | 0 | Strict test-project compilation passed; the former `Page` type mismatch is resolved. |
| `pnpm exec playwright test --list` | 0 | Listed 24 tests in the two E2E specs across all three locked Chromium projects. |
| `pnpm test:e2e` | 0 | 24/24 E2E tests passed. |
| `pnpm test:a11y` | 0 | 12/12 axe scans passed with zero violations. |

## Post-run protocol remediation

Historical record: the dependency correction was implemented and verified in `ae15ca1`, but that phase-closure commit lacked the required B05-03 task-level response/re-review and dedicated B05-03 correction commit. The historical correction is not recreated or attributed to a new commit here.

| Current focused command | Exit | Result | Artifact path |
|---|---:|---|---|
| `pnpm exec tsc --noEmit --project tsconfig.test.json` | 0 | Strict test-project compilation passed; the former incompatible `Page` type error remains absent. | `tsconfig.test.json`; compiler stdout was empty |
| `CI=1 pnpm test:a11y` | 0 | 12/12 axe scans passed across four localized routes and three Chromium projects with zero violations. | `.artifacts/bootstrap/playwright/test-results/`; `.artifacts/bootstrap/playwright/report/` |
| `pnpm format:check` | 0 | All tracked files use Prettier formatting. | N/A |
| `git diff --check` | 0 | No whitespace errors. | N/A |

Residual High finding: protocol/evidence integrity remains open pending the required independent B05-03 task re-review and dedicated local commit containing `B05-03`; no current dependency or runtime defect is claimed.

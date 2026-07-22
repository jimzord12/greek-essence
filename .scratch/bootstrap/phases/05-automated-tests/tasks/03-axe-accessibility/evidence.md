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

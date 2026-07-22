# B05-02 Evidence

| Command | Exit | Result |
|---|---:|---|
| `pnpm exec playwright --version` | 0 | `Version 1.61.1` |
| `pnpm exec playwright test --list` | 0 | 12 tests listed: four checks in each of `chromium-compact`, `chromium-medium`, and `chromium-wide`. |
| `CI=1 pnpm exec playwright test tests/e2e/failure-artifact.spec.ts` | 1 | Temporary `expect(true).toBe(false)` failed in all three projects. Screenshot, video, and trace were copied to stable ignored paths before the later passing run. |
| `pnpm test:e2e` | 1 | First run found the invalid-locale test was counting its expected 404 browser error as an unexpected console error; corrected the test boundary. |
| `pnpm test:e2e` | 0 | 12 passed in 7.7s. |
| `pnpm exec playwright-cli --version` | 127 | Reported `0.1.17`, then Windows exited with `UV_HANDLE_CLOSING` after warning that the checked-in Playwright CLI skill does not match. Package installation itself completed successfully; no out-of-scope skill update was made. |
| `CI=1 pnpm test:e2e` | 0 | 12 passed in 8.3s after the temporary failure spec was removed; the final-verification server was not reused. |
| `pnpm format:check` | 0 | All matched files use Prettier code style after formatting only `playwright.config.ts`, `tests/e2e/localization-and-quality.spec.ts`, and `pnpm-lock.yaml`. |

Stable failure-policy artifacts from the controlled failure:

- `.artifacts/bootstrap/playwright/failure-policy/chromium-compact/test-failed-1.png`
- `.artifacts/bootstrap/playwright/failure-policy/chromium-compact/video.webm`
- `.artifacts/bootstrap/playwright/failure-policy/chromium-compact/trace.zip`
- `.artifacts/bootstrap/playwright/failure-policy/chromium-medium/test-failed-1.png`
- `.artifacts/bootstrap/playwright/failure-policy/chromium-medium/video.webm`
- `.artifacts/bootstrap/playwright/failure-policy/chromium-medium/trace.zip`
- `.artifacts/bootstrap/playwright/failure-policy/chromium-wide/test-failed-1.png`
- `.artifacts/bootstrap/playwright/failure-policy/chromium-wide/video.webm`
- `.artifacts/bootstrap/playwright/failure-policy/chromium-wide/trace.zip`

`test -f` confirmed all nine paths; `git check-ignore -v` confirmed each is ignored by `.gitignore:40` (`.artifacts/bootstrap/`).

Configured permanent artifact locations: `.artifacts/bootstrap/playwright/test-results/` and `.artifacts/bootstrap/playwright/report/`.

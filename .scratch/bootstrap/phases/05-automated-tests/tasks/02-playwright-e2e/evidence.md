# B05-02 Evidence

All commands below were run in `C:\Users\jimzord12\Documents\GitHub\greek-essence` during remediation session `20260722_130707_6dcbf0`.

| Command | Exit | Result |
|---|---:|---|
| `pnpm exec playwright --version` | 0 | `Version 1.61.1`. |
| `pnpm exec playwright test --list` | 0 | 27 tests listed across `chromium-compact`, `chromium-medium`, and `chromium-wide` in the two permanent spec files. |
| `pnpm exec tsc --noEmit` | 0 | Source/project TypeScript check passed; `tsconfig.json` excludes `tests`, so this command does not typecheck the Playwright files. |
| `pnpm exec tsc --ignoreConfig --noEmit --strict --noUncheckedIndexedAccess --exactOptionalPropertyTypes --noImplicitOverride --noFallthroughCasesInSwitch --noUncheckedSideEffectImports --useUnknownInCatchVariables --target ES2017 --lib dom,dom.iterable,esnext --module esnext --moduleResolution bundler --esModuleInterop --resolveJsonModule --isolatedModules --jsx react-jsx --skipLibCheck tests/e2e/browser-guards.ts tests/e2e/localization-and-quality.spec.ts tests/e2e/accessibility.spec.ts` | 0 | Explicit strict test-file typecheck passed for all three current Playwright TypeScript files. |
| `pnpm format:check` | 0 | All repository files passed Prettier formatting. |
| `pnpm lint` | 0 | No errors; two pre-existing warnings in `commitlint.config.mjs` and `unlighthouse.config.ts`. |
| `pnpm exec playwright test tests/e2e/localization-and-quality.spec.ts --project=chromium-compact --grep 'redirects the root route'` | 0 | The exact invalid-locale document 404 journey passed with the narrow guard exception. |
| `CI=1 pnpm exec playwright test tests/e2e/localization-and-quality.spec.ts` | 0 | 15 localized metadata, navigation, invalid-locale, keyboard, and quality-lab interaction tests passed across all three Chromium projects. |
| `CI=1 pnpm test:e2e` | 0 | 27 passed in 20.0s across localization and axe specs. |
| `pnpm test:a11y` | 0 | 12 passed in 13.0s; zero axe violations across four routes and three projects. |

## Controlled regression probes

Temporary probes were deliberately removed after each expected failure:

| Probe command/mutation | Exit | Result |
|---|---:|---|
| Home canonical mutation + `CI=1 pnpm exec playwright test tests/e2e/localization-and-quality.spec.ts --project=chromium-compact --grep 'renders exact localized metadata semantics'` | 1 | Failed on received `/probe/en` versus expected `/en`; app mutation restored. |
| Home `en` hreflang mutation + same focused metadata command | 1 | Failed on received `/probe` versus expected `/en`; app mutation restored. |
| Home page robots mutation + same focused metadata command | 1 | Failed on received `index, nofollow` versus expected `noindex, nofollow`; app mutation restored. |
| Quality-lab toggle mutation + `CI=1 pnpm exec playwright test tests/e2e/localization-and-quality.spec.ts --project=chromium-compact --grep 'exercises localized quality-lab toggle interaction'` | 1 | Failed to find the selected role button; component mutation restored. |
| `CI=1 pnpm exec playwright test tests/e2e/temporary-review03-guards.spec.ts --project=chromium-compact --workers=1` | 1 | Three temporary guard probes failed: unexpected console error, critical 500 response, and uncaught page error. Probe file removed. |
| `test ! -e tests/e2e/temporary-review03-guards.spec.ts && test ! -e tests/e2e/temporary-review03-artifact.spec.ts && printf 'temporary probes removed\n'` | 0 | Both temporary probe files absent. |

## Failure-artifact policy

| Command | Exit | Result |
|---|---:|---|
| `CI=1 pnpm exec playwright test tests/e2e/temporary-review03-artifact.spec.ts` | 1 | One temporary failing page assertion failed in all three Chromium projects and produced screenshot, video, and trace artifacts. The temporary spec was then removed. |
| `for f in .artifacts/bootstrap/playwright/failure-policy/review03/chromium-compact/test-failed-1.png .artifacts/bootstrap/playwright/failure-policy/review03/chromium-compact/video.webm .artifacts/bootstrap/playwright/failure-policy/review03/chromium-compact/trace.zip .artifacts/bootstrap/playwright/failure-policy/review03/chromium-medium/test-failed-1.png .artifacts/bootstrap/playwright/failure-policy/review03/chromium-medium/video.webm .artifacts/bootstrap/playwright/failure-policy/review03/chromium-medium/trace.zip .artifacts/bootstrap/playwright/failure-policy/review03/chromium-wide/test-failed-1.png .artifacts/bootstrap/playwright/failure-policy/review03/chromium-wide/video.webm .artifacts/bootstrap/playwright/failure-policy/review03/chromium-wide/trace.zip; do test -s "$f" && git check-ignore -q "$f" && printf 'verified %s\\n' "$f"; done` | 0 | All nine stable artifacts are non-empty and ignored. |

Stable ignored artifact paths:

- `.artifacts/bootstrap/playwright/failure-policy/review03/chromium-compact/test-failed-1.png`
- `.artifacts/bootstrap/playwright/failure-policy/review03/chromium-compact/video.webm`
- `.artifacts/bootstrap/playwright/failure-policy/review03/chromium-compact/trace.zip`
- `.artifacts/bootstrap/playwright/failure-policy/review03/chromium-medium/test-failed-1.png`
- `.artifacts/bootstrap/playwright/failure-policy/review03/chromium-medium/video.webm`
- `.artifacts/bootstrap/playwright/failure-policy/review03/chromium-medium/trace.zip`
- `.artifacts/bootstrap/playwright/failure-policy/review03/chromium-wide/test-failed-1.png`
- `.artifacts/bootstrap/playwright/failure-policy/review03/chromium-wide/video.webm`
- `.artifacts/bootstrap/playwright/failure-policy/review03/chromium-wide/trace.zip`

No temporary test spec or implementation mutation remains. Generated Playwright results/reports remain under ignored `.artifacts/bootstrap/playwright/`.

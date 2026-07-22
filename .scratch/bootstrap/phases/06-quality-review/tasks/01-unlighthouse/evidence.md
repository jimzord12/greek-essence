# Evidence — B06-01 post-run remediation

## Default mobile methodology assertion

Final config `unlighthouse.config.ts` contains `device: "mobile"`, `samples: 3`, and exactly `/en`, `/el`, `/en/quality-lab`, `/el/quality-lab`. It contains no `throttlingMethod` override. The raw Lighthouse reports at `.artifacts/bootstrap/unlighthouse/reports/**/lighthouse.json` assert `formFactor: "mobile"` and `throttlingMethod: "simulate"` for all four routes.

Installed `@unlighthouse/core@0.18.0` source at `node_modules/.pnpm/@unlighthouse+core@0.18.0_*/node_modules/@unlighthouse/core/dist/index.mjs` loops over `resolvedConfig.scanner.samples` and calls `computeMedianRun(samples)`. The persisted report is one median result per route, as expected.

## Two-run final report assertion

Artifacts:

- `.artifacts/bootstrap/unlighthouse/ci-result.json`
- `.artifacts/bootstrap/unlighthouse-default-run-1.log`
- `.artifacts/bootstrap/unlighthouse-default-run-2.log`

Both exact quality commands exited 0 and both captured logs contain `Score assertions have passed.`. Both runs asserted exactly four routes and no `NoFallbackError`, missing `messages/*.json`, server errors, console errors, or critical request errors.

The final median report contains:

| URL | Performance | Accessibility | Best practices | SEO |
|---|---:|---:|---:|---:|
| `/el` | 0.93 | 1.00 | 1.00 | 1.00 |
| `/el/quality-lab` | 0.92 | 1.00 | 1.00 | 1.00 |
| `/en` | 0.93 | 1.00 | 1.00 | 1.00 |
| `/en/quality-lab` | 0.93 | 1.00 | 1.00 | 1.00 |

The assertion minimums remain performance 0.90, accessibility 1.00, best practices 0.95, and SEO 0.95.

F-04 fallback-origin behavior remains unchanged and is still documented Non-blocking debt.

---
task: B06-01
reviewer_agent: 20260722_100605_63957e
implementer_agent: 20260722_094928_de39e3
verdict: Changes requested
---

# Review 01 — B06-01

## 1. Scope and evidence reviewed

Reviewed the authorized contract, B06-01 verification row and locked defaults, three task-listed technical-design documents, implementation report, evidence, live diff (including `pnpm-lock.yaml`), `unlighthouse.config.ts`, and the generated Unlighthouse report.

Confirmed mechanically:

- `package.json` uses the exact locked `quality:unlighthouse` script and exact pins `@unlighthouse/cli@0.18.0`, `puppeteer@25.3.0`, and `start-server-and-test@3.0.11`.
- Configuration names exactly `/en`, `/el`, `/en/quality-lab`, and `/el/quality-lab`, declares mobile and `samples: 3`, applies the four required budgets, and writes to ignored `.artifacts/bootstrap/unlighthouse`.
- Generated Lighthouse reports identify mobile form factor with mobile screen emulation for all four routes.
- The implementation changes the default `metadataBase` from `http://localhost:3000` to the audit-only origin `http://127.0.0.1:3101`.

Reviewer reruns:

- `pnpm build && pnpm quality:unlighthouse` — exit 1. Build passed; Unlighthouse failed the performance budget on both quality-lab routes and emitted twelve Next.js `Internal: NoFallbackError` errors.
- `pnpm exec prettier --check package.json pnpm-lock.yaml unlighthouse.config.ts 'app/[locale]/layout.tsx'` — exit 1; `pnpm-lock.yaml` and `unlighthouse.config.ts` failed formatting.

## 2. Findings

### F-01 — High — Current production audit fails the required performance budget

- Location: `.artifacts/bootstrap/unlighthouse/ci-result.json`; `unlighthouse.config.ts:12-18`; `evidence.md:10-22`.
- Violated requirement: `task.md:23-26,41` and verification-matrix B06-01/locked Unlighthouse defaults require every one of the four mobile routes to pass performance 90, accessibility 100, best practices 95, and SEO 95 using `pnpm quality:unlighthouse` after a production build.
- Evidence/reproduction: reviewer ran `pnpm build && pnpm quality:unlighthouse`; the command exited 1. The newly generated report records `/el/quality-lab` performance `0.84` and `/en/quality-lab` performance `0.83`. Unlighthouse reported both as invalid against the configured 90 budget. This directly contradicts the tracked evidence values `0.90` and exit 0.
- Required correction: make the two quality-lab routes reliably meet the locked performance budget without lowering/skipping that budget, and refresh implementation evidence from the corrected run.
- Verification: rerun `pnpm build` and then `pnpm quality:unlighthouse`; both must exit 0, and the generated report must contain exactly the four required paths with every configured category at or above budget.

### F-02 — High — The required three-sample behavior is not active

- Location: `unlighthouse.config.ts:3,5-8`; runtime semantics of `pnpm quality:unlighthouse`.
- Violated requirement: `task.md:23-24` and verification-matrix locked defaults require exactly four explicit URLs and three mobile samples.
- Evidence/reproduction: although the config declares `samples: 3`, the reviewer run logged: `The url config has been provided with 4 paths for scanning. Disabling sitemap, robots, sampling and crawler.` The generated artifact contains one Lighthouse report per path and no evidence that three samples were applied. A declared option that the running CLI disables does not prove the required behavior.
- Required correction: configure a supported, deterministic three-sample execution that still audits only the four explicit routes, and record runtime/artifact evidence demonstrating all three mobile samples per route. If the locked requirements are incompatible with this Unlighthouse version, record and obtain the protocol-required deviation instead of claiming compliance.
- Verification: rerun the gate and verify from its log/report artifacts that exactly four routes are audited with three active mobile samples each; no runtime message may state that required sampling is disabled.

### F-03 — High — The production gate repeatedly emits Next.js server errors

- Location: production-server output from the locked `package.json:24` command; recorded incompletely at `evidence.md:26-28`.
- Violated requirement: `docs/03_technical_design/18_testing_and_quality_gates.md:35-37` and `AGENTS.md:27-29` require passing checks with no console errors or failed critical network requests.
- Evidence/reproduction: the reviewer run emitted twelve `Error: Internal: NoFallbackError` stacks from `.next/server/...app-page...` while auditing the four routes. The process later failed its budget. An exit-0 assertion report would not make repeated server errors compliant.
- Required correction: identify the audited requests that trigger `NoFallbackError` and eliminate the server errors without suppressing output, ignoring failed requests, or weakening route/budget coverage; update evidence with the actual resolution.
- Verification: `pnpm build` and `pnpm quality:unlighthouse` both exit 0, all four reports pass, and captured production-server/audit output contains no `NoFallbackError` or other console/server errors or failed critical requests.

### F-04 — Non-blocking — Audit-specific metadata origin leaks into the application default

- Location: `app/[locale]/layout.tsx:10-13`.
- Violated requirement: protocol implementation rule to make the smallest complete in-scope change and `docs/03_technical_design/14_seo_architecture.md:3-5` requiring correct canonical metadata semantics.
- Evidence/reproduction: the diff changes the environment fallback from the normal local origin `http://localhost:3000` to the Unlighthouse server's fixed port `http://127.0.0.1:3101`. With no `NEXT_PUBLIC_SITE_URL`, ordinary `pnpm dev` still serves on port 3000 while relative metadata resolves against port 3101. The task contracts an audit gate, not a global audit-port default.
- Required correction: keep audit-origin setup inside the quality-gate boundary or otherwise preserve correct metadata origin outside that gate; do not globally couple application metadata to port 3101.
- Verification: inspect rendered localized metadata under the normal app command and under the production audit command; canonical/alternate URLs must use the intended serving origin in each context, while the Unlighthouse gate still passes.

### F-05 — Non-blocking — Changed configuration and lockfile are unformatted, with avoidable lockfile churn

- Location: `unlighthouse.config.ts`; `pnpm-lock.yaml`.
- Violated requirement: protocol smallest-complete-change/maintainability rule and repository formatting conventions represented by the locked `format:check` script.
- Evidence/reproduction: targeted reviewer command `pnpm exec prettier --check package.json pnpm-lock.yaml unlighthouse.config.ts 'app/[locale]/layout.tsx'` exited 1 and named both files. `git diff --numstat -- pnpm-lock.yaml` reports 7,951 additions and 5,281 deletions; inspection shows extensive quote/layout reserialization mixed with the necessary dependency additions.
- Required correction: format the changed files with the repository formatter and regenerate/review the lockfile so the remaining semantic churn is limited to the exact pinned tools and their required transitive graph.
- Verification: targeted Prettier check exits 0; `pnpm install --frozen-lockfile --ignore-scripts` exits 0; inspect the resulting lockfile diff and confirm exact importer pins with no unrelated dependency changes.

## 3. Verdict

Changes requested.

B06-01 cannot be approved while the required gate exits 1, the two quality-lab routes miss the performance budget, three active samples are not evidenced and are reported disabled by the CLI, and the production audit emits repeated Next.js server errors. The original implementer must correct the High findings and refresh affected evidence before re-review.

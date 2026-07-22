# Review 01 — B04-01

- Reviewer session: `20260722_070734_7efd1d`
- Reviewed at: `2026-07-22T04:10:54Z`
- Verdict: **Changes requested**

## 1. High — Locale shells are not statically rendered

- Exact location: `app/[locale]/layout.tsx:7-31`, `app/[locale]/page.tsx:5-6`, `.scratch/bootstrap/phases/04-bilingual-fixtures/tasks/01-next-intl-routing/implementation-report.md:29`, and `.scratch/bootstrap/phases/04-bilingual-fixtures/tasks/01-next-intl-routing/evidence.md:16`.
- Violated requirement: `task.md:41` requires both locale shells to render statically; `docs/03_technical_design/05_routing_rendering_and_localization.md:28-30` requires approved pages to be generated with `generateStaticParams`; `protocol.md:160-165` requires exact, non-inferred evidence.
- Evidence/reproduction: `pnpm build` exited `0`, but the live Next.js 16.2.6 route table classified `/[locale]` as `ƒ (Dynamic) server-rendered on demand`, not `○ (Static)`. This contradicts the implementation report's claim that the locale shells were generated statically and the evidence row's unqualified static-generation result.
- Required correction: Make the `en` and `el` fixture shells statically generated without weakening locale validation, then correct the report/evidence to record the actual route classification.
- Verification: Re-run `pnpm build`; require the route table to classify the localized shell as static/prerendered and show both generated locale params, then request `/en` and `/el` from the production build and retain their existing `200`, `lang`, and equivalent-link assertions.

## 2. High — Root redirection is not deterministic to `/en`

- Exact location: `i18n/routing.ts:3-7`, `proxy.ts:8-16`, `.scratch/bootstrap/phases/04-bilingual-fixtures/tasks/01-next-intl-routing/evidence.md:18`, and `.scratch/bootstrap/phases/04-bilingual-fixtures/tasks/01-next-intl-routing/implementation-report.md:26`.
- Violated requirement: `task.md:23` says to redirect `/` to `/en`; `task.md:41` requires deterministic root redirection; `docs/03_technical_design/05_routing_rendering_and_localization.md:24` establishes `/en` as the default root target.
- Evidence/reproduction: Against `pnpm start --port 3100`, a plain `GET /` returned `307 Location: /en`, but `GET /` with `Accept-Language: el` returned `307 Location: /el`, and `GET /` with `Cookie: NEXT_LOCALE=el` also returned `307 Location: /el`. The current evidence tests only the plain request and therefore does not prove the claimed deterministic behavior.
- Required correction: Configure root handling so `/` always redirects to `/en` for this locked bootstrap contract, independent of request language and locale cookies, while preserving explicit `/en` and `/el` routes. Update evidence with the decisive variants.
- Verification: Start the production build and assert that plain `/`, `/` with `Accept-Language: el`, and `/` with `NEXT_LOCALE=el` all return the required redirect to `/en`; recheck `/en`, `/el`, and `/fr`.

## 3. High — The Corepack deviation record is incomplete

- Exact location: `.scratch/bootstrap/phases/04-bilingual-fixtures/tasks/01-next-intl-routing/implementation-report.md:31-34` and `.scratch/bootstrap/phases/04-bilingual-fixtures/tasks/01-next-intl-routing/evidence.md:13-14`.
- Violated requirement: root `AGENTS.md:9` requires pnpm through Corepack; `protocol.md:168-173` requires a deviation to name the original rule, reason, impact, approval owner, and replacement verification.
- Evidence/reproduction: The report records the failed Corepack attempt and direct `pnpm 10.33.0` fallback, but does not state impact, approval owner, or replacement verification/approval. My live `pnpm --version` returned `10.33.0`, and `pnpm install --lockfile-only --frozen-lockfile` exited `0`; those facts verify version/lock consistency but do not supply the required deviation authority.
- Required correction: Complete the deviation record with the rule, reason, impact, approval owner/approval, and replacement verification, or rerun the package operation through repaired Corepack and record it accurately.
- Verification: Inspect the corrected deviation fields and approval, and rerun the stated replacement check (at minimum exact pnpm version plus frozen lockfile consistency) with exit codes recorded.

## Verification performed

- `pnpm build` — exit `0`; compilation/type checking succeeded, but `/[locale]` was reported as dynamic (`ƒ`).
- Production requests to `/`, `/en`, `/el`, and `/fr` — plain results `307`, `200`, `200`, and `404`; `/` changed to `/el` under both Greek `Accept-Language` and `NEXT_LOCALE=el`.
- Playwright CLI against `/en` and `/el` — rendered `lang="en"` and `lang="el"`; both exposed equivalent `/en` and `/el` links and localized fixture headings.
- Playwright CLI against `/fr` — rendered the honest 404 page at `/fr`.
- `pnpm install --lockfile-only --frozen-lockfile` — exit `0` using pnpm `10.33.0`.
- `git diff --check` — exit `0` during diff inspection.

## Evidence

The passing locale `lang`, equivalent links, and invalid-locale 404 behavior are confirmed. Approval is withheld because static rendering and deterministic root redirection fail the locked acceptance contract, and the package-manager deviation record is incomplete.

## Handoff verification

The task remains `In review`; no implementation, implementation report, evidence, phase status, dashboard state, commit, or remote was changed by this reviewer.

## Durable knowledge verification

The implementation report records no durable knowledge candidate; none is required by this contract-only review.

# Bootstrap Execution Plan

## Objective

Produce a reproducible, bilingual Next.js foundation whose application, automated checks, browser tooling, and repository-local AI skills are ready before product implementation begins.

## Success conditions

- Node 24 and pnpm 10 are verified and pinned.
- Supersession (2026-07-23): the pnpm 10 value above records the historical bootstrap baseline. The current contributor contract is standalone pnpm `11.17.0`, declared in [`package.json`](../../package.json), with engines `>=11 <12`.
- The project is generated with `pnpm dlx shadcn@latest init --preset b27GcrRo --template next --pointer`.
- Exact dependencies, strict TypeScript, ESLint, Prettier, Husky, lint-staged, and Conventional Commits are configured.
- Minimal `/en`, `/el`, and localized `quality-lab` fixtures prove App Router, `next-intl`, shadcn/Base UI, metadata, responsiveness, and interaction.
- Unit tests, Playwright E2E, axe, Unlighthouse, and production build pass.
- Approved repository-local skills and Playwright CLI are installed and documented.
- Codex and the Greek Essence Reviewer Skill are green against real rendered fixtures.
- Current local-tool validation is recorded; no second-agent compatibility requirement is introduced.

## Explicit exclusions

- Real Greek Essence pages or editorial content
- Content schemas and loaders
- Trip-request form or API
- Resend and React Email
- Authentication
- Analytics, monitoring, CMS, CRM, database, booking, or payments
- Vercel connection, deployment, Git remote changes, or GitHub Actions

## Phase order

1. [00 — Planning and baseline](phases/00-planning-and-baseline/phase.md)
2. [01 — Agent tooling](phases/01-agent-tooling/phase.md)
3. [02 — Application scaffold](phases/02-application-scaffold/phase.md)
4. [03 — Code hygiene](phases/03-code-hygiene/phase.md)
5. [04 — Bilingual fixtures](phases/04-bilingual-fixtures/phase.md)
6. [05 — Automated tests](phases/05-automated-tests/phase.md)
7. [06 — Quality review](phases/06-quality-review/phase.md)
8. [07 — Final verification](phases/07-final-verification/phase.md)

## Task execution protocol

- Normative roles, safety rules, assignment, review, and closure procedures are in [`protocol.md`](protocol.md).
- Every task uses the exact commands and locked defaults in [`verification-matrix.md`](verification-matrix.md) in addition to its local acceptance section.
- Materialize task files before assignment.
- Record implementer/reviewer agent IDs in task front matter.
- Implementer writes `implementation-report.md` and `evidence.md` from templates.
- Reviewer writes `reviews/01-review.md`; implementer writes `01-review-response.md`.
- Continue numbered review cycles until blockers are cleared.
- Phase reviewer writes `reviews/01-phase-review.md`; phase owner responds in the paired response file.
- Update this workspace in the same accepted change that closes a task or phase. After every successful task closure, the root integrator creates one dedicated commit containing the task ID in its message before starting later work.

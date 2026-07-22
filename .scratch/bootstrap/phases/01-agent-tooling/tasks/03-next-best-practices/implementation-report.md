# Implementation Report

## Outcome

The amended B01-03 contract is complete and approved. Operator-authorized BD-015 (commit `3a042792019ca8a89123598134320a678d309b7f`) replaces the retired `next-best-practices` reference skill with the installed Next.js version's bundled `next/dist/docs/` and applicable generated agent rules. No replacement skill is installed or vendored during this pre-scaffold task.

## Files changed

- `.scratch/bootstrap/phases/01-agent-tooling/tasks/03-next-best-practices/task.md` — preserved session identity and changed the amended task to `In review`.
- `.scratch/bootstrap/phases/01-agent-tooling/tasks/03-next-best-practices/implementation-report.md` — replaced obsolete blocker reporting with amended-contract results.
- `.scratch/bootstrap/phases/01-agent-tooling/tasks/03-next-best-practices/evidence.md` — recorded official revisions, migration evidence, checks, and artifacts.
- `.scratch/bootstrap/phases/01-agent-tooling/tasks/03-next-best-practices/reviews/02-review-response.md` — paired response to Review 02.
- `.scratch/bootstrap/phases/01-agent-tooling/tasks/03-next-best-practices/reviews/03-review-response.md` — paired response to Review 03.
- `.scratch/bootstrap/phases/01-agent-tooling/phase.md` — corrected the Phase 01 exit gate to the BD-015 four-skill-plus-runtime-handoff model.
- `.scratch/bootstrap/phases/02-application-scaffold/tasks/03-normalize-application-skeleton/task.md` — made the deferred B02-03 version-matched runtime procedure and evidence ownership explicit without performing B02 work.

The operator-authored decision and tooling changes in `3a04279` were inspected and preserved. No `.agents/README.md` change is required: it inventories repository-local vendored skills, and BD-015 installs none. No `.agents/` skill, package, lockfile, application file, plugin bundle, hook, or global configuration changed.

## Commands run

Exact commands, exit codes, source revisions, results, and ignored artifact paths are in `evidence.md`.

## Acceptance results

- Official `vercel-labs/next-skills` revision `b76d687cf3e026eac3b1032f610f06b47a56377c` states that `next-best-practices` is no longer a skill and directs its reference knowledge to bundled `next/dist/docs/` plus `next dev` generated rules for Next.js 16.3+.
- Official `vercel/next.js` canary revision `c77f3ded55f8a542d440cdd8e86f00fd058e4e2c` has the current workflow-skills tree (`next-cache-components-*`, `next-dev-loop`, and `next-partial-prefetching-adoption`); it contains no `next-best-practices` path.
- Root and approved-tooling guidance consistently prohibit the retired skill and direct framework-specific decisions to the installed version's `next/dist/docs/` and applicable generated rules.
- `.agents/skills/next-best-practices/` and other prohibited local substitute/bundle paths are absent.
- B02-03 owns later runtime integration after it pins Next.js: inspect `next/dist/docs/` and validate either `next dev` generated rules for 16.3+ or the documented older-version codemod path.
- The Phase 01 exit gate now consistently requires four approved repository-local skills, prohibited/retired-path absence, provenance/Codex checks, and the explicit B02-03 runtime handoff.
- The B02-03 standalone contract now lists the authoritative guidance and exact version-dependent runtime/evidence procedure while preserving root `AGENTS.md` authority.

## Deviations

None from the amended contract. The absence of an installed Next.js package is intentional pre-scaffold deferral, not a skipped B01-03 check.

## Risks or follow-up

The recorded upstream revisions are a point-in-time evidence record. B02-03 must validate the actual pinned Next.js package and its applicable generated-rule mechanism before framework implementation begins.

## Handoff information

Implementer: Hermes `greekimpl`, canonical session `20260722_023532_75f390`; started `2026-07-22T02:36:10+03:00`. Reviewer: `greekreview`, canonical session `20260722_023946_4b5f39`. Review 02's prior blocker is addressed by BD-015. After the user stopped all agent processes, operator-directed Review 04 verified the three Review 03 findings as resolved and approved direct closure.

## Durable knowledge candidates

None. Revision availability and migration state remain task evidence; the approved policy is already recorded in BD-015 and project tooling guidance.


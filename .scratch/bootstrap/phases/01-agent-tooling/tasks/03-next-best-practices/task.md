---
id: B01-03
status: Done
depends_on: [B01-02]
implementer_agent: 20260722_023532_75f390
reviewer_agent: 20260722_023946_4b5f39
started_at: 2026-07-22T02:36:10+03:00
completed_at: 2026-07-22T03:33:48+03:00
---

# Adopt Next.js version-matched agent guidance

## What

Replace the obsolete repository-local `next-best-practices` requirement with the official version-matched Next.js documentation mechanism. Do not install a replacement skill during this pre-scaffold task.

## Why

App Router setup needs guidance that matches the exact Next.js version eventually installed by the scaffold.

## How

- Verify the official `vercel-labs/next-skills` migration notice and the current `vercel/next.js` skills tree at recorded revisions.
- Update the tooling baseline and root guidance to use bundled `next/dist/docs/` and applicable generated agent rules.
- Defer runtime setup and validation until Next.js is pinned during the application scaffold.
- Do not install the retired legacy skill, a similarly named substitute, the full Vercel collection, or a plugin bundle.

## Required reading

- `docs/05_agent_skills/07_nextjs_version_matched_agent_guidance.md`
- `docs/05_agent_skills/13_safe_installation_and_review_rules.md`
- `docs/05_agent_skills/12_agents_readme.md`

## Bootstrap verification contract

Apply verification row B01-03 and all relevant locked defaults from [the Bootstrap Verification Matrix](../../../../verification-matrix.md). Record exact commands, exit codes, and artifact paths in evidence.md.

## Acceptance

The obsolete skill requirement is removed consistently; `.agents/skills/next-best-practices/` is absent; official source revisions and migration evidence are recorded; and scaffold verification owns the later version-matched runtime integration.

---
id: B02-03
status: Done
depends_on: [B02-02]
implementer_agent: 20260722_051657_af8148
reviewer_agent: 20260722_052515_b199ab
started_at: 2026-07-22T05:17:13+03:00
completed_at: 2026-07-22T05:40:11+03:00
---

# Normalize the application skeleton

## What

Align generator output with the approved shallow root architecture.

## Why

Preset defaults must not silently redefine the project structure or component boundaries.

## How

- Use root-level `app/`, not `src/`, and retain `@/*` aliases.
- Keep only directories needed by bootstrap fixtures and configuration.
- Default pages/layouts to Server Components; isolate necessary interaction.
- Remove generator marketing content without beginning the actual Home page.
- Preserve preset semantic tokens as bootstrap infrastructure.
- Review and normalize generator-owned root `README.md` and `.gitignore`; link the documentation and bootstrap entry points, preserve required generated ignores, and add `.artifacts/bootstrap/` without removing unrelated rules.
- After Next.js is pinned, inspect the installed version's `next/dist/docs/`. For Next.js 16.3 or later, run `next dev` and validate the generated `AGENTS.md` / `CLAUDE.md` rule integration; for an older supported version, run `npx @next/codemod@canary agents-md` in isolation and inspect its changes. Preserve root `AGENTS.md` as authoritative over generated framework guidance.
- Record the resolved Next.js version, exact setup/validation commands and exit codes, generated paths, runtime evidence artifacts, and the selected version-dependent path in B02-03 evidence.

## Required reading

- `docs/03_technical_design/01_confirmed_technical_decisions.md`
- `docs/03_technical_design/04_project_and_file_architecture.md`
- `docs/04_design/05_token_hierarchy_and_source_of_truth_rules.md`
- `docs/05_agent_skills/07_nextjs_version_matched_agent_guidance.md`

## Bootstrap verification contract

Apply verification row B02-03 and all relevant locked defaults from [the Bootstrap Verification Matrix](../../../../verification-matrix.md). Record exact commands, exit codes, and artifact paths in evidence.md.

## Acceptance

Development startup and production build pass with the approved root architecture, normalized README and ignore rules, no product implementation, and recorded validation of the pinned Next.js version's `next/dist/docs/` plus its applicable 16.3+ `next dev` generated-rule path or documented older-version `agents-md` codemod path. Root `AGENTS.md` remains authoritative.

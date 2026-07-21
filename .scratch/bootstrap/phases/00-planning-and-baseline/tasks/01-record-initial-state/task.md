---
id: B00-01
status: Done
depends_on: []
implementer_agent: /root/b00_01_implementer
reviewer_agent: /root/b00_01_reviewer
started_at: 2026-07-21T20:58:57+03:00
completed_at: 2026-07-21T21:07:48+03:00
---

# Record and protect the initial repository state

## What

Record runtime versions, Git state, available CLIs, existing files, and missing tools before bootstrap mutation.

## Why

The documentation is currently untracked. Installers must not overwrite it or hide pre-existing conditions.

## How

- Record Node, pnpm, Corepack, Git, Codex, Playwright CLI, and Kimi availability.
- Record branch, remotes, tracked/untracked files, manifests, locks, hooks, agent directories, and test configuration.
- Preserve `docs/` exactly; do not use reset, clean, restore, checkout-overwrite, or equivalent commands.
- Write the baseline to `implementation-report.md` and commands/results to `evidence.md`.

## Required reading

- `docs/05_agent_skills/04_pre_installation_procedure.md`
- `docs/05_agent_skills/13_safe_installation_and_review_rules.md`
- `docs/00_project_protocol/rules.md`

## Bootstrap verification contract

Apply verification row B00-01 and all relevant locked defaults from [the Bootstrap Verification Matrix](../../../../verification-matrix.md). Record exact commands, exit codes, and artifact paths in evidence.md.

## Acceptance

The inventory is complete and reproducible, and every pre-existing documentation file remains present and unchanged.

---
id: B03-03
status: Done
depends_on: [B03-02]
implementer_agent: 20260722_061844_4c3566
reviewer_agent: 20260722_062534_3a89dc
started_at: 2026-07-22T03:19:49Z
completed_at: 2026-07-22T03:30:28Z
---

# Configure Git hooks and Conventional Commits

## What

Add Husky, lint-staged, commitlint, and Conventional Commits.

## Why

Cheap local checks should catch staged-file and commit-message defects without running the full suite on every commit.

## How

- Install Husky through its `prepare` flow.
- Pre-commit runs lint-staged only; commit-msg runs commitlint.
- lint-staged formats and lints supported staged files without touching unstaged content.
- Use `@commitlint/config-conventional`.
- Do not add Commitizen or a heavy pre-push hook.

## Required reading

- `docs/05_agent_skills/05_root_agents_md.md`
- `docs/03_technical_design/18_testing_and_quality_gates.md`

## Bootstrap verification contract

Apply verification row B03-03 and all relevant locked defaults from [the Bootstrap Verification Matrix](../../../../verification-matrix.md). Record exact commands, exit codes, and artifact paths in evidence.md.

## Acceptance

Valid Conventional Commit messages pass, invalid examples fail, and staged checks preserve unstaged and unrelated work.

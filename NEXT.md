# Project Handoff

## Current state

Feature `greek-essence-showcase` is active in the JZ Spec-to-Ship workflow. `.scratch/features/001-greek-essence-showcase/SPEC.md` is approved at revision `1.1.0`; it now explicitly requires the complete reusable `docs/04_design` foundational token system through Tailwind CSS v4 while keeping unused wider-product components out of scope.

The milestone plan contains three demoable increments with exhaustive FR/NFR coverage. `explore-bilingual-showcase` was decomposed at `2026-07-24T11:32:24.956Z` into two dependency-ordered issues: #01 `browse-bilingual-home` (actionable) and #02 `explore-paros-editorial` (blocked by #01). The remaining two milestones are pending.

The repository is on `main`. Verify the live HEAD and worktree before acting; do not assume this handoff captures later concurrent changes.

## Immediate next task

When explicitly authorized, run the live `jz-issue-to-contract` workflow for issue #01, `browse-bilingual-home`. Work from the approved revision `1.1.0` SPEC and the issue file at `.scratch/features/001-greek-essence-showcase/issues/01-browse-bilingual-home/issue.md`.

Use `features-cli` for the required preflight and final frontier verification. Stop after the change contract is valid; do not implement code without separate authorization.

## Boundaries

- Planning only: do not create change contracts or implementation code without separate authorization.
- Do not launch Ralph, deploy, handle credentials, commit, push, or make remote changes.
- Do not overwrite or absorb unrelated working-tree changes.
- Preserve accepted decision IDs and defaults; ask only genuinely blocking issue-boundary questions.
- Do not continue into `jz-issue-to-contract` without explicit authorization.

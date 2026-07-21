---
id: B00-02
status: Done
depends_on: [B00-01]
implementer_agent: /root/b00_02_implementer
reviewer_agent: /root/b00_02_reviewer
started_at: 2026-07-22T00:07:49+03:00
completed_at: 2026-07-22T00:43:47+03:00
---

# Validate and finalize the execution workspace

## What

Validate the phase/task tree, templates, status model, dependencies, and tracked/ignored artifact policy.

## Why

Every later subagent needs a decision-complete brief and stable handoff contract.

## How

- Check every task has What, Why, How, minimal reading, and acceptance sections.
- Check IDs are unique and dependencies are acyclic.
- Confirm `.scratch/bootstrap` is tracked and `.artifacts/bootstrap` will be ignored.
- Add initial task and phase review skeletons only when execution begins, using the templates.

## Required reading

- `docs/00_project_protocol/documentation_hierarchy.md`
- `docs/00_project_protocol/responsibilities.md`
- `docs/05_agent_skills/17_required_completion_report.md`

## Bootstrap verification contract

Apply verification row B00-02 and all relevant locked defaults from [the Bootstrap Verification Matrix](../../../../verification-matrix.md). Record exact commands, exit codes, and artifact paths in evidence.md.

## Acceptance

All workspace links resolve, all 28 task IDs are unique, task counts match the dashboard, dependencies are acyclic, and no implementation decision is unstated.

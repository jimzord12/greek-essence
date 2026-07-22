---
id: B06-03
status: Ready
depends_on: [B06-02]
implementer_agent: null
reviewer_agent: null
started_at: null
completed_at: null
---

# Run the Greek Essence Reviewer Skill

## What

Execute a fresh Codex review subagent using the project-owned skill against the bootstrap fixtures.

## Why

Reviewer Skill green is an explicit bootstrap success condition.

## How

- Inspect compact, relevant medium, and wide behavior in English and Greek.
- Review accessibility, responsiveness, localization, SEO presentation, boundaries, and obvious visual quality.
- Mark product content, forms, and final brand review out of scope rather than untested-but-green.
- Require evidence for every blocking/high-impact finding and use the standard response/re-review loop.

## Required reading

- `docs/05_agent_skills/10_project_owned_quality_review_skill.md`
- `docs/05_agent_skills/15_how_agents_must_use_the_tooling.md`
- `docs/04_design/40_workflow.md`
- `docs/04_design/41_design_system_acceptance_criteria.md`

## Bootstrap verification contract

Apply verification row B06-03 and all relevant locked defaults from [the Bootstrap Verification Matrix](../../../../verification-matrix.md). Record exact commands, exit codes, and artifact paths in evidence.md.

## Acceptance

The fresh Codex Reviewer Skill run has no unresolved blocking or high-impact bootstrap defect; Kimi validation remains separately blocked.

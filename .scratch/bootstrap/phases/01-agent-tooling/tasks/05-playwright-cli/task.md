---
id: B01-05
status: Ready
depends_on: [B01-04]
implementer_agent: null
reviewer_agent: null
started_at: null
completed_at: null
---

# Pin Playwright CLI and install its official skill

## What

Validate the existing Playwright CLI and create `.agents/skills/playwright-cli/` without requiring a project manifest.

## Why

The official skill is required before browser work, while project-level package pinning must wait until the shadcn task creates `package.json`.

## How

- Verify current official installation and skill-generation commands.
- Validate the existing global CLI version/help, generate in isolation, inspect, and normalize the skill.
- Record that project-level package pinning is deferred to B05-02.
- Add no Playwright MCP or overlapping browser agent.

## Required reading

- `docs/05_agent_skills/09_playwright_cli_and_official_agent_skill.md`
- `docs/05_agent_skills/13_safe_installation_and_review_rules.md`
- `docs/05_agent_skills/12_agents_readme.md`

## Bootstrap verification contract

Apply verification row B01-05 and all relevant locked defaults from [the Bootstrap Verification Matrix](../../../../verification-matrix.md). Record exact commands, exit codes, and artifact paths in evidence.md.

## Acceptance

Global CLI verification works, the official skill is canonical, project-level pinning is explicitly deferred to B05-02, and prohibited browser alternatives are absent.

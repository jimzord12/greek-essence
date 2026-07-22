## 1. Approved Tooling Baseline

### 1.1 Repository-wide agent guidance

Use:

- root-level `AGENTS.md`.

`AGENTS.md` contains concise, durable rules that should apply before every coding task. Detailed knowledge belongs in repository-local skills rather than being duplicated into the root file.

### 1.2 Approved agent knowledge

Install and version these repository-local skills:

1. **Google Chrome Modern Web Guidance**
2. **Vercel `vercel-react-best-practices`**
3. **Official Playwright CLI Agent Skill**
4. **Project-owned `greek-essence-quality-review` skill**

For Next.js-specific reference knowledge, use the documentation bundled with the repository's installed Next.js version under `next/dist/docs/` and its generated agent rules. `next-best-practices` was retired upstream and must not be installed or vendored as a repository-local skill.

### 1.3 Approved interactive browser interface

Use:

- **Playwright CLI**

Playwright CLI is the only approved interactive browser interface for coding agents working on the repository.

### 1.4 Existing executable quality tooling

The application’s deterministic testing and quality tooling remains governed by `03_TECHNICAL_DESIGN.md`, especially:

- **§18 — Testing and Quality Gates**;
- **§13 — Accessibility Implementation**;
- **§14 — SEO Architecture**;
- **§6 — Content Architecture**;
- **§15 — Error, Loading, Empty, Unavailable, and Success States**.

The approved agent skills should help agents apply and review those requirements. They do not replace executable checks.

### 1.5 Explicitly unapproved browser-agent alternatives

Do not install or configure:

- Playwright MCP;
- Vercel `agent-browser`;
- Browser Use or Browser Use CLI;
- another browser-agent CLI with overlapping responsibilities.

A different browser interface requires a documented revision to this decision. Popularity, vendor reputation, or convenience alone is not sufficient justification.

### 1.6 Explicitly out of scope

Do not install broad development workflows or unrelated agent frameworks, including:

- autonomous implementation loops;
- task-management frameworks;
- multi-agent orchestration systems;
- broad plugin bundles;
- generic skill collections;
- Superpowers or similar workflow systems.

Greek Essence already defines its own documentation and implementation workflow.

---


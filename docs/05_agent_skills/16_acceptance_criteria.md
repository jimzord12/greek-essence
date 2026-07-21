## 16. Acceptance Criteria

The agent-tooling setup is complete only when all applicable criteria pass.

### 16.1 Repository guidance

- [ ] Root `AGENTS.md` exists.
- [ ] It is concise and points to authoritative documents instead of duplicating them.
- [ ] It names the approved repository-local skills.
- [ ] It names Playwright CLI as the interactive browser interface.
- [ ] It rejects Playwright MCP, Browser Use, and `agent-browser`.
- [ ] It references the repository’s required checks and definition of done.

### 16.2 Repository-local skills

- [ ] `modern-web-guidance` exists under `.agents/skills/`.
- [ ] `next-best-practices` exists under `.agents/skills/`.
- [ ] `vercel-react-best-practices` exists under `.agents/skills/`.
- [ ] the official Playwright CLI skill exists under `.agents/skills/`.
- [ ] `greek-essence-quality-review` exists under `.agents/skills/`.
- [ ] every skill has a root `SKILL.md`.
- [ ] required supporting files are preserved.
- [ ] no unrelated skill collection or workflow framework was installed.

### 16.3 Provenance and maintenance

- [ ] `.agents/README.md` records all required provenance fields.
- [ ] exact upstream revisions are pinned.
- [ ] licenses are verified and recorded.
- [ ] local modifications are recorded.
- [ ] update procedures are documented.
- [ ] Node.js, package-manager, and Playwright CLI setup versions are recorded.

### 16.4 Cross-agent compatibility

- [ ] Codex CLI can identify or explicitly load every approved skill.
- [ ] Kimi Code can identify or explicitly load every approved skill.
- [ ] any required wrappers point to canonical repository-local files.
- [ ] no undocumented duplicate skill copies exist.

### 16.5 Playwright CLI

- [ ] Playwright CLI is installed in an approved reproducible form.
- [ ] its version and help command execute successfully.
- [ ] its official skill was generated and normalized.
- [ ] an agent can inspect the local application with it.
- [ ] no Playwright MCP configuration exists.
- [ ] Browser Use and `agent-browser` are absent.
- [ ] browser artifacts are ignored by Git.

### 16.6 Project-owned quality skill

- [ ] it references authoritative documents instead of duplicating them.
- [ ] it requires real browser observation for browser-based claims.
- [ ] it covers visual, responsive, accessibility, localization, trust, SEO-presentation, and form quality.
- [ ] it distinguishes defects from subjective suggestions.
- [ ] it requires route, locale, viewport, evidence, and reproduction steps.
- [ ] it works in Codex CLI and Kimi Code.

### 16.7 Repository integrity

- [ ] existing application architecture remains consistent with `03_TECHNICAL_DESIGN.md`.
- [ ] unrelated repository files were not reorganized by the tooling installation.
- [ ] the package manifest and lockfile remain consistent.
- [ ] baseline checks pass, or pre-existing failures are clearly reported.

---


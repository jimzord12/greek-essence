# Greek Essence — AI Agent Skills and Browser Tooling

**Document ID:** GE-AI-TOOLS-001  
**Version:** 0.2  
**Status:** Approved implementation specification  
**Prepared:** 21 July 2026  
**Product:** Greek Essence

---

## 0. Purpose, Authority, and Scope

This document defines the approved repository-local AI agent skills and browser-quality tooling for Greek Essence.

It tells a fresh implementation agent:

- what must be installed;
- what each tool or skill contributes;
- where agent-specific files belong;
- how to install and validate them;
- how Codex CLI and Kimi Code should use them;
- how upstream revisions must be recorded and updated safely.

This document does **not** redefine product requirements, UX requirements, application architecture, repository architecture, browser-support policy, performance budgets, accessibility acceptance criteria, test coverage, CI behavior, form behavior, localization behavior, or production-readiness requirements.

Those concerns remain owned by the existing project documents:

1. `00_PROJECT_PROTOCOL.md` — documentation hierarchy, contributor rules, and change control.
2. `01_PRODUCT_REQUIREMENTS.md` — product and business truth.
3. `02_PROTOTYPE_SPECIFICATION.md` — UX, UI, responsive behavior, interaction, visual quality, accessibility, and prototype acceptance.
4. `03_TECHNICAL_DESIGN.md` — implementation architecture, project layout, testing, quality gates, deployment, security, SEO, localization, and production gaps.

When this document references implementation or quality requirements, the owning document remains authoritative. This document may select or configure tooling to support those requirements, but it must not silently alter them.

### 0.1 What this document owns

This document owns:

- root agent guidance through `AGENTS.md`;
- repository-local Agent Skills;
- the approved interactive browser interface for coding agents;
- installation and version-recording procedures for those skills and tools;
- cross-agent compatibility expectations for Codex CLI and Kimi Code;
- safe skill-update procedures;
- acceptance criteria for the agent-tooling setup.

### 0.2 Requirement language

- **Must:** required for acceptance unless this document is formally revised.
- **Should:** expected unless the repository already has an equivalent compatible solution.
- **May:** optional and dependent on a demonstrated need.

---


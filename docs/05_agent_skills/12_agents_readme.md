## 12. `.agents/README.md`

### 12.1 Purpose

Provide a human-readable inventory and provenance record for all repository-local skills.

### 12.2 Required entry fields

Each skill entry must include:

- local skill name;
- local path;
- purpose;
- upstream source or `Project-owned`;
- exact upstream source path where relevant;
- installed release or commit SHA;
- installation or generation command;
- installation date;
- verified license;
- included optional disciplines or files;
- excluded optional disciplines;
- local modifications;
- Codex validation result;
- Kimi validation result;
- update procedure.

### 12.3 Dependency and runtime records

Also record:

- Node.js major version used during setup;
- package manager and version;
- Playwright CLI version;
- any repository-level package added specifically for this setup;
- whether global tooling is additionally required in contributor environments.

The package manifest, lockfile, and authoritative runtime configuration remain the source of truth for application dependencies.

---


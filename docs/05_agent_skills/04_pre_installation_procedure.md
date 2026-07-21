## 4. Pre-Installation Procedure

Before changing the repository, the implementation agent must:

1. Read:
   - `00_PROJECT_PROTOCOL.md`;
   - `01_PRODUCT_REQUIREMENTS.md`;
   - `02_PROTOTYPE_SPECIFICATION.md`;
   - `03_TECHNICAL_DESIGN.md`;
   - this document;
   - any existing `AGENTS.md`;
   - the package manifest and lockfile.
2. Inspect the existing repository for:
   - package manager and package-manager version;
   - Node.js version policy;
   - existing agent directories or instructions;
   - existing Playwright packages and configuration;
   - existing quality scripts and CI configuration.
3. Run the currently documented baseline commands where the repository is sufficiently implemented.
4. Record the initial state and any pre-existing failures.
5. Reuse equivalent working configuration instead of replacing it without justification.
6. Use the package manager already selected by the repository.
7. Verify current official installation instructions before executing version-sensitive commands.

The examples in this document use `pnpm` when a project-level package command is necessary because `03_TECHNICAL_DESIGN.md` currently specifies `pnpm-lock.yaml`. If the authoritative Technical Design is revised, follow its current package-manager decision.

---


# Repository-local agent skills

This inventory records approved third-party skills vendored into the repository. B01-02 uses a deliberately small local runtime-search design rather than the full generated skill layout; the selection and its upstream source are recorded below.

## Modern Web Guidance

- **Local skill name:** `modern-web-guidance`
- **Local path:** `.agents/skills/modern-web-guidance/`
- **Purpose:** Current guidance for modern, interoperable, accessible, secure, privacy-aware web-platform implementation.
- **Official upstream repository and release:** `https://github.com/GoogleChrome/modern-web-guidance`, commit `79aae1e0bed948e48fd78b58538c5ee1e6463da9` (`Release v0.0.177`).
- **Wrapper package source:** npm `modern-web-guidance@0.0.177`, package repository `https://github.com/GoogleChrome/modern-web-guidance-src`, registry gitHead `d07f33a3fb6b0056d3d7140e2952c89b3a72aa89`, and dist shasum `8648e431d681fb3f133147f8b971c2a422eac921`.
- **Exact upstream source paths:** `skills/modern-web-guidance/SKILL.md` and the complete `skills/modern-web-guidance/` layout in the official repository; root `LICENSE` in both the official repository and wrapper package; wrapper-package root `THIRD_PARTY_NOTICES`.
- **Official wrapper delegation:** `npx modern-web-guidance@latest install` delegates to `npx -y skills add GoogleChrome/modern-web-guidance --skill modern-web-guidance`; the inspected non-interactive equivalent is `npx -y skills add GoogleChrome/modern-web-guidance --skill modern-web-guidance --yes --copy`.
- **Observed full generated layout and agent copies:** at release `v0.0.177`, the canonical core skill contains 139 files: `SKILL.md` plus the guide catalog under `guides/` (accessibility, built-in AI, CSS, forms, HTML, JavaScript, performance, privacy, security, UI, visual design, and WebMCP). The isolated `--yes --copy` installer generated that complete core layout into `.agents/skills/modern-web-guidance/` and agent-specific copies in `.claude/skills/modern-web-guidance/`, `.hermes/skills/modern-web-guidance/`, and `.trae/skills/modern-web-guidance/`. This is observed installer behavior, not the repository's selected layout.
- **Selected three-file local runtime-search design:** `.agents/skills/modern-web-guidance/` intentionally retains only the canonical `SKILL.md`, wrapper `LICENSE`, and wrapper `THIRD_PARTY_NOTICES`. The canonical skill instructs agents to run `npx -y modern-web-guidance@latest search` and `retrieve` at use time; it has no relative local guide links. No local guide/reference is required for that retained runtime-search design. `SKILL.md`, `LICENSE`, and `THIRD_PARTY_NOTICES` are byte-identical to their respective inspected wrapper-package files; `SKILL.md` and `LICENSE` also match the official repository after CRLF/LF normalization.
- **Separately excluded optional disciplines and generated content:** the separate `skills/chrome-extensions` skill is excluded. Passkey and WebMCP material are present in the canonical core layout but intentionally not retained locally, consistent with the project tooling decision; the installer does not exclude them automatically. The remaining generated guides, search executable/model assets, telemetry watchdog, plugins, and all agent-specific copies are also intentionally not retained because the selected design uses the canonical runtime search/retrieve interface. The official repository does not contain `THIRD_PARTY_NOTICES`; that attribution file is retained from the inspected wrapper package.
- **Installation and inspection commands:** expected wrapper entry `npx modern-web-guidance@latest install`; reviewed verification script `.scratch/bootstrap/phases/01-agent-tooling/tasks/02-modern-web-guidance/scripts/verify-review-01.sh`, invoked with `bash .scratch/bootstrap/phases/01-agent-tooling/tasks/02-modern-web-guidance/scripts/verify-review-01.sh`. The script uses isolated temporary directories and cleanup traps.
- **Installation date:** `2026-07-21` (UTC).
- **Verified license:** Apache License 2.0 (`LICENSE`); wrapper-package third-party attribution is retained in `THIRD_PARTY_NOTICES`.
- **Local modifications:** none to retained upstream file contents; local selection and this provenance record are project-owned.
- **Codex validation result:** not run in B01-02; the controlled validation is owned by B01-07.
- **Kimi validation result:** not run in B01-02; Kimi Code remains unavailable and is the recorded external blocker (BD-012).
- **Update procedure:** rerun the reviewed verification script against the intended release; inspect wrapper delegation, the official repository commit/layout, complete installer targets, source/license/notice comparisons, and excluded disciplines; then update this record and task evidence before accepting any local selection change.

## Setup runtime record

- **Node.js:** `v24.18.0` (major 24).
- **Package manager:** pnpm `10.33.0`.
- **Playwright CLI:** `0.1.14`.
- **Repository package added for this setup:** none.
- **Global tooling required in contributor environments:** Node.js and a pnpm/Corepack-capable environment are required by repository guidance; `playwright-cli` is required by the approved browser-inspection baseline. This task added no global tooling.

# Repository-local agent skills

This inventory records approved third-party skills vendored into the repository. B01-02 uses a deliberately small local runtime-search design rather than the full generated skill layout; the selection and its upstream source are recorded below.

## Bootstrap Next Task

- **Local skill name:** `bootstrap-next`.
- **Local path:** `.agents/skills/bootstrap-next/`.
- **Purpose:** Resume exactly one valid Greek Essence bootstrap task under the bootstrap execution workflow.
- **Upstream source and exact source path:** Project-owned; no upstream source or path.
- **Installed revision:** Project commit `158093188ccf44ffa35ce2a2473b4137cb1159ac` (`feat(skills): add bootstrap next task`).
- **Installation or generation command:** None; this canonical project-owned Markdown skill was authored directly in the repository.
- **Installation date:** `2026-07-21` (UTC+03:00 commit time).
- **Verified license:** Project-owned content; no third-party license applies.
- **Included files:** `SKILL.md` and `agents/openai.yaml`.
- **Excluded optional disciplines:** none; no agent-specific wrapper copies are retained.
- **Local modifications:** none after the recorded project revision.
- **Codex validation result:** Explicit local-file control passed (exit `0`): Codex read `SKILL.md` and returned `.scratch/bootstrap/BOOTSTRAP-AGENTS.md`. Artifact: `.artifacts/bootstrap/B01-07/codex-bootstrap-next.txt`.
- **Kimi validation result:** Blocked: `command -v kimi` exited `1`; the executable/authentication is unavailable (external blocker).
- **Update procedure:** Update the canonical project-owned `SKILL.md` and its `agents/openai.yaml` metadata together when the bootstrap workflow changes; record the resulting project revision and repeat the explicit-load control.

## Ralph Loop Manager

- **Local skill name:** `ralph-loop-manager`.
- **Local path:** `.agents/skills/ralph-loop-manager/`.
- **Purpose:** Fail-closed compatibility checking, bounded launch, live monitoring, and meaningful email milestone/escalation notification for the existing Greek Essence Ralph controller.
- **Upstream source and exact source path:** Project-owned; no upstream source or path.
- **Installed revision:** Project-owned revision introduced by `feat(skills): add project Ralph loop manager`; use `git log -1 -- .agents/skills/ralph-loop-manager` for the exact local revision.
- **Installation or generation command:** None; the canonical project-owned skill was authored directly in this repository.
- **Installation date:** `2026-07-22` (UTC+03:00).
- **Verified license:** Project-owned content; no third-party license applies.
- **Included files:** `SKILL.md`, `agents/openai.yaml`, and the read-only `scripts/preflight.py` structural checker.
- **Excluded optional disciplines:** no controller fork, email sender copy, daemon, agent-specific duplicate, or generic workflow framework.
- **Local modifications:** not applicable; this is the canonical project-owned source.
- **Validation result:** Frontmatter/layout checks, Python compilation and unit tests, live hard-stop controls, a compatible structural-pass control using the configured environment without exposing values, Ralph controller dry-run, and repository workspace validation must pass before acceptance.
- **Email dependency:** Loads the explicitly approved profile-level `email-notification` exception at runtime and requires its sender, non-secret environment-shape checks, recipient dry-run, and idempotency contract. These checks do not prove provider acceptance or delivery; no email credentials or sender code are vendored here.
- **Update procedure:** Update the canonical skill, OpenAI metadata, and preflight checker together; rerun both hard-stop and structural-pass controls plus Ralph tests and workspace validation.

## Modern Web Guidance

- **Local skill name:** `modern-web-guidance`
- **Local path:** `.agents/skills/modern-web-guidance/`
- **Purpose:** Current guidance for modern, interoperable, accessible, secure, privacy-aware web-platform implementation.
- **Upstream source, exact source path, and release:** `https://github.com/GoogleChrome/modern-web-guidance`, commit `79aae1e0bed948e48fd78b58538c5ee1e6463da9` (`Release v0.0.177`).
- **Installed revision:** `79aae1e0bed948e48fd78b58538c5ee1e6463da9` (`Release v0.0.177`).
- **Wrapper package source:** npm `modern-web-guidance@0.0.177`, package repository `https://github.com/GoogleChrome/modern-web-guidance-src`, registry gitHead `d07f33a3fb6b0056d3d7140e2952c89b3a72aa89`, and dist shasum `8648e431d681fb3f133147f8b971c2a422eac921`.
- **Exact upstream source paths:** `skills/modern-web-guidance/SKILL.md` and the complete `skills/modern-web-guidance/` layout in the official repository; root `LICENSE` in both the official repository and wrapper package; wrapper-package root `THIRD_PARTY_NOTICES`.
- **Official wrapper delegation:** `npx modern-web-guidance@latest install` delegates to `npx -y skills add GoogleChrome/modern-web-guidance --skill modern-web-guidance`; the inspected non-interactive equivalent is `npx -y skills add GoogleChrome/modern-web-guidance --skill modern-web-guidance --yes --copy`.
- **Included optional disciplines or files:** retained local runtime-search design contains canonical `SKILL.md`, wrapper `LICENSE`, and wrapper `THIRD_PARTY_NOTICES`; the observed full generated layout is recorded below.
- **Observed full generated layout and agent copies:** at release `v0.0.177`, the canonical core skill contains 139 files: `SKILL.md` plus the guide catalog under `guides/` (accessibility, built-in AI, CSS, forms, HTML, JavaScript, performance, privacy, security, UI, visual design, and WebMCP). The isolated `--yes --copy` installer generated that complete core layout into `.agents/skills/modern-web-guidance/` and agent-specific copies in `.claude/skills/modern-web-guidance/`, `.hermes/skills/modern-web-guidance/`, and `.trae/skills/modern-web-guidance/`. This is observed installer behavior, not the repository's selected layout.
- **Selected three-file local runtime-search design:** `.agents/skills/modern-web-guidance/` intentionally retains only the canonical `SKILL.md`, wrapper `LICENSE`, and wrapper `THIRD_PARTY_NOTICES`. The canonical skill instructs agents to run `npx -y modern-web-guidance@latest search` and `retrieve` at use time; it has no relative local guide links. No local guide/reference is required for that retained runtime-search design. `SKILL.md`, `LICENSE`, and `THIRD_PARTY_NOTICES` are byte-identical to their respective inspected wrapper-package files; `SKILL.md` and `LICENSE` also match the official repository after CRLF/LF normalization.
- **Excluded optional disciplines:** the separate `skills/chrome-extensions` skill is excluded. Passkey and WebMCP material are present in the canonical core layout but intentionally not retained locally, consistent with the project tooling decision; the installer does not exclude them automatically. The remaining generated guides, search executable/model assets, telemetry watchdog, plugins, and all agent-specific copies are also intentionally not retained because the selected design uses the canonical runtime search/retrieve interface. The official repository does not contain `THIRD_PARTY_NOTICES`; that attribution file is retained from the inspected wrapper package.
- **Installation and inspection commands:** expected wrapper entry `npx modern-web-guidance@latest install`; reviewed verification script `.scratch/bootstrap/phases/01-agent-tooling/tasks/02-modern-web-guidance/scripts/verify-review-01.sh`, invoked with `bash .scratch/bootstrap/phases/01-agent-tooling/tasks/02-modern-web-guidance/scripts/verify-review-01.sh`. The script uses isolated temporary directories and cleanup traps.
- **Installation date:** `2026-07-21` (UTC).
- **Verified license:** Apache License 2.0 (`LICENSE`); wrapper-package third-party attribution is retained in `THIRD_PARTY_NOTICES`.
- **Local modifications:** none to retained upstream file contents; local selection and this provenance record are project-owned.
- **Codex validation result:** Explicit local-file control passed (exit `0`): Codex returned the exact Step 1 `npx -y modern-web-guidance@latest search "<query>" --skill-version 2026_05_16-c5e78707` command. Artifact: `.artifacts/bootstrap/B01-07/codex-modern-web-guidance.txt`.
- **Kimi validation result:** Blocked: `command -v kimi` exited `1`; the executable/authentication is unavailable (external blocker).
- **Update procedure:** rerun the reviewed verification script against the intended release; inspect wrapper delegation, the official repository commit/layout, complete installer targets, source/license/notice comparisons, and excluded disciplines; then update this record and task evidence before accepting any local selection change.

## Setup runtime record

- **Node.js:** `v24.18.0` (major 24).
- **Package manager:** pnpm `10.33.0`.
- **Project-local Playwright CLI:** `0.1.17` (`pnpm exec playwright-cli`); the separately installed global executable currently reports `0.1.14`.
- **Codex CLI:** `0.144.6`.
- **Repository package added for this setup:** none.
- **Global tooling required in contributor environments:** Node.js and a pnpm/Corepack-capable environment are required by repository guidance; `playwright-cli` is required by the approved browser-inspection baseline. This task added no global tooling.

## Vercel React Best Practices

- **Local skill name:** `vercel-react-best-practices`
- **Local path:** `.agents/skills/vercel-react-best-practices/`
- **Purpose:** React and Next.js rendering, bundle, waterfall, state/effect, and performance guidance.
- **Upstream source and exact source path:** `https://github.com/vercel-labs/agent-skills`, `skills/react-best-practices/`.
- **Installed revision:** `4559f18a20c1691c744b4395194290db6a0df5e9`.
- **Canonical installer entry:** `npx skills add vercel-labs/agent-skills --skill vercel-react-best-practices`.
- **Installation command:** isolated checkout at the recorded revision, then normalized LF copy to the local path.
- **Installation date:** `2026-07-22` (UTC).
- **Verified license:** MIT, declared in the unmodified upstream `SKILL.md` front matter; upstream has no standalone license file within this skill or repository tree.
- **Included files:** complete 76-file upstream skill layout: `SKILL.md`, `AGENTS.md`, `README.md`, `metadata.json`, and `rules/`.
- **Excluded optional disciplines:** all other Vercel skills; no agent-specific duplicate copies.
- **Local modifications:** CRLF-to-LF normalization only; otherwise source contents are preserved.
- **Codex validation result:** Explicit local-file control passed (exit `0`): Codex returned all eight categories in priority order. Artifact: `.artifacts/bootstrap/B01-07/codex-vercel-react-best-practices.txt`.
- **Kimi validation result:** Blocked: `command -v kimi` exited `1`; the executable/authentication is unavailable (external blocker).
- **Update procedure:** inspect the source skill and its referenced files in an isolated checkout at an explicit upstream revision; verify its MIT declaration and absence of executable scripts; normalize-copy only `skills/react-best-practices/` to this local path; then update this entry and B01-04 evidence.

## Playwright CLI

- **Local skill name:** `playwright-cli`
- **Local path:** `.agents/skills/playwright-cli/`
- **Purpose:** Approved interface for interactive browser inspection, debugging, and browser evidence collection.
- **Upstream source and exact source path:** npm `@playwright/cli@0.1.17`, generated by the official CLI from its embedded `playwright-cli` skill; package repository `https://github.com/microsoft/playwright-cli`.
- **Installed revision or release:** `0.1.17`; npm distribution integrity `sha512-VBw6y3p8eqOqmjKg07IkWSPGKJkpIhMRNDFI6DOYsDD6fAfcI1XYEWMLWyhSZQ0B/Oc2KN49eq4XqE64PUPHBg==`.
- **Installation and generation command:** project-local verification with `pnpm exec playwright-cli --version` and `pnpm exec playwright-cli --help`; canonical generation with `pnpm exec playwright-cli install --skills=agents`.
- **Installation date:** `2026-07-22` (UTC).
- **Verified license:** Apache-2.0, as reported by `pnpm view @playwright/cli@0.1.17 license`.
- **Included files:** `SKILL.md` plus ten Markdown references under `references/`; no executable files.
- **Excluded optional disciplines:** no optional skill disciplines; the installer-generated `.claude/skills/playwright-cli/` copy and `.playwright/` workspace state remain only in ignored isolation artifacts, with no agent-specific duplicate committed.
- **Local modifications:** CRLF-to-LF normalization only; the B06-02 refresh regenerated the canonical skill from project-local `0.1.17`; all 11 canonical files equal the generated source after normalization.
- **Codex validation result:** Explicit local-file control passed (exit `0`): Codex returned `playwright-cli open` from Quick start. Artifact: `.artifacts/bootstrap/B01-07/codex-playwright-cli.txt`.
- **Kimi validation result:** Blocked: `command -v kimi` exited `1`; the executable/authentication is unavailable (external blocker).
- **Update procedure:** inspect the installed CLI help and generated `SKILL.md` plus every referenced file in an ignored isolated directory; check package provenance/license and executable content; generate with `pnpm exec playwright-cli install --skills=agents`; retain only the normalized canonical `.agents/skills/playwright-cli/` copy; then update this inventory and the corresponding task evidence.

## B01-05 package-pinning deferral

- **Repository-level package:** none. Project-level `@playwright/cli` pinning is explicitly deferred to B05-02, when the Playwright Test project and `package.json` exist.

## Greek Essence Quality Review

- **Local skill name:** `greek-essence-quality-review`.
- **Local path:** `.agents/skills/greek-essence-quality-review/`.
- **Purpose:** Review Greek Essence implementations for project-specific visual, responsive, accessibility, localization, SEO-presentation, trust, and custom-trip form quality.
- **Upstream source and exact source path:** Project-owned; no upstream source or path.
- **Installed revision:** Project commit `8c4661a249799474788388c8c198b12a8cd6111b` (`chore(bootstrap): complete B01-06 quality review skill`).
- **Installation or generation command:** None; this canonical project-owned skill and focused references were authored directly in the repository.
- **Installation date:** `2026-07-22` (UTC+03:00 commit time).
- **Verified license:** Project-owned content; no third-party license applies.
- **Included files:** `SKILL.md` and five Markdown checklists in `references/`.
- **Excluded optional disciplines:** none; no agent-specific wrapper copies are retained.
- **Local modifications:** none after the recorded project revision.
- **Codex validation result:** Explicit local-file control passed (exit `0`): Codex returned the eight required report headings in order. Artifact: `.artifacts/bootstrap/B01-07/codex-greek-essence-quality-review.txt`.
- **Kimi validation result:** Blocked: `command -v kimi` exited `1`; the executable/authentication is unavailable (external blocker).
- **Update procedure:** Update the canonical `SKILL.md` and only the affected focused checklists when authoritative quality requirements change; run the B01-06 structural verifier and repeat the explicit-load control before recording the resulting project revision.

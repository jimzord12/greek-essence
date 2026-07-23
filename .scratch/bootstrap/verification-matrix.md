# Bootstrap Verification Matrix

This matrix is authoritative for task-level verification. Tasks may add narrower checks, but they may not omit the listed checks without recording an evidenced deviation.

| Task | Required verification |
|---|---|
| B00-01 | `node --version`; `pnpm --version`; `corepack --version`; `git --version`; `git status --short`; `git remote -v`; `codex --version`; `playwright-cli --version`; command lookup for `kimi` |
| B00-02 | Validate 28 unique task IDs, required task headings, an acyclic dependency chain, and all relative Markdown links under `.scratch/bootstrap`. |
| B01-01 | Validate all links in `AGENTS.md`; search it for required package, locale, skill, browser, architecture, checks, and Definition-of-Done statements. |
| B01-02 | Inspect `npx modern-web-guidance@latest --help`; expected install entry is `npx modern-web-guidance@latest install`; verify canonical `SKILL.md` and recorded revision/license. |
| B01-03 | Verify the official `vercel-labs/next-skills` migration notice and current `vercel/next.js` skills tree; confirm the retired `.agents/skills/next-best-practices/` is absent and the tooling contract points to version-matched bundled Next.js docs. |
| B01-04 | Expected install entry is `npx skills add vercel-labs/agent-skills --skill vercel-react-best-practices`; verify only the requested canonical skill. |
| B01-05 | `playwright-cli --version`; `playwright-cli --help`; expected generation entry is `playwright-cli install --skills`; verify canonical skill and absence of prohibited browser tools. |
| B01-06 | Verify the project skill has one `SKILL.md`, five required references, required output ordering, and exact modular documentation links. |
| B01-07 | Run and record each controlled Codex prompt; confirm Kimi lookup fails and is recorded as blocked. |
| B02-01 | Run the exact prescribed shadcn command; then `pnpm dev` smoke and inspect the complete repository diff. |
| B02-02 | `node --version`; `pnpm --version`; `pnpm exec tsc --version`; `pnpm list --depth 0`; `pnpm install --frozen-lockfile`. |
| B02-03 | `pnpm dev` smoke; `pnpm build`; verify root `app/`, absence of `src/app`, and resolution of `@/*`; inspect the pinned Next.js version's `next/dist/docs/` and validate its applicable generated agent-rule integration (or the documented older-version codemod path). |
| B03-01 | `pnpm typecheck`; compile a temporary negative strictness fixture and confirm failure before removing it. |
| B03-02 | `pnpm format:check`; `pnpm lint`; run fix commands against a controlled temporary fixture and confirm ignored outputs remain untouched. |
| B03-03 | Run `pnpm exec husky`; exercise lint-staged with controlled staged files; run commitlint against one valid and one invalid message without creating commits. |
| B03-04 | Invoke every package script at help/smoke level; verify `.env*` and `.artifacts/bootstrap/` ignore behavior with `git check-ignore`. |
| B04-01 | Build and request `/`, `/en`, `/el`, and an invalid locale; assert redirect, `lang`, locale equivalence, and not-found behavior. |
| B04-02 | Browser-smoke both routes/locales at 320, 390, 834, and 1440 widths; keyboard, 200% zoom, and reduced-motion checks. |
| B04-03 | Inspect rendered title, description, canonical, alternates, and robots directives on all four localized route variants. |
| B05-01 | `pnpm test:unit`; prove a temporary failing test is detected before removal. |
| B05-02 | `pnpm exec playwright --version`; `pnpm exec playwright test --list`; `pnpm test:e2e`; verify failure artifact policy with one temporary failing assertion. |
| B05-03 | `pnpm test:a11y`; require zero violations; confirm a controlled violation fails before removing it. |
| B06-01 | `pnpm build`; `pnpm quality:unlighthouse`; verify all four URLs and category budgets in the report. |
| B06-02 | Use the canonical Playwright CLI skill on both routes/locales at compact and wide viewports; record route, viewport, console/network, and artifact evidence. |
| B06-03 | Run the canonical quality-review skill in a fresh Codex subagent; complete response/re-review until no blockers/high findings remain. |
| B07-01 | In a fresh isolated copy with no `node_modules` or `.next`: `pnpm install --frozen-lockfile`; verify the lockfile is unchanged; run `pnpm check:all`. Normal pnpm content-addressed cache reuse is allowed because lockfile versions and integrity remain authoritative. |
| B07-02 | Run frozen install, format, lint, typecheck, unit, build, E2E, axe, Unlighthouse, and aggregate gates; all exit zero. |
| B07-03 | Validate every completion-report field, all links, exact task counts, and explicit Kimi blocker wording. |

## Locked package-script composition

```text
dev                    next dev
build                  next build
start                  next start
lint                   eslint .
lint:fix               eslint . --fix
typecheck              tsc --noEmit
format                  prettier . --write
format:check            prettier . --check
test:unit              vitest run
test:unit:watch        vitest
test:e2e               playwright test
test:a11y              playwright test tests/e2e/accessibility.spec.ts
quality:unlighthouse   start-server-and-test "pnpm start --port 3101" http://127.0.0.1:3101 "unlighthouse-ci --config-file unlighthouse.config.ts"
check                  pnpm format:check && pnpm lint && pnpm typecheck && pnpm test:unit
check:all              pnpm check && pnpm build && pnpm test:e2e && pnpm test:a11y && pnpm quality:unlighthouse
```

`quality:unlighthouse` assumes a successful production build already exists. `check:all` supplies that build. Commands must remain cross-platform; do not replace them with shell-specific scripts.

## Locked configuration defaults

- ESLint: flat config; Next.js core-web-vitals and TypeScript presets; no separate unused-import plugin unless generated configuration cannot enforce unused code; no Stylelint.
- Prettier: default formatting plus the compatible Tailwind CSS plugin; generated/artifact directories ignored.
- Playwright: `baseURL=http://127.0.0.1:3100`, `webServer="pnpm dev --port 3100"`, 120-second server timeout, 30-second test timeout, zero local retries, Chromium only, `trace: retain-on-failure`, `screenshot: only-on-failure`, and `video: retain-on-failure`.
- Unlighthouse: exact-pinned `@unlighthouse/cli`, `puppeteer`, and `start-server-and-test`; explicit four URLs; mobile; three samples; performance 90, accessibility 100, best practices 95, SEO 95; output under `.artifacts/bootstrap/unlighthouse`.

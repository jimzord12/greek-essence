# Evidence

## B00-01 baseline inventory

All commands below ran from the repository root on `2026-07-21`. No generated artifact path applies: `.artifacts/` is absent and `.artifacts/bootstrap` is not yet ignored (B00-02 scope).

| Command | Exit code | Result |
|---|---:|---|
| `node --version` | 0 | `v24.18.0` |
| `pnpm --version` | 0 | `10.33.0` |
| `corepack --version` | 0 | `0.35.0` |
| `git --version` | 0 | `git version 2.47.1.windows.2` |
| `git status --short` | 0 | One pre-existing modification: `.scratch/bootstrap/FOR_HUMAN_OPERATOR.md`. |
| `git remote -v` | 0 | `origin` configured for fetch and push. |
| `codex --version` | 0 | `codex-cli 0.144.6` (emitted non-fatal local temporary-directory warnings after its version output). |
| `playwright-cli --version` | 0 | `0.1.14`; recorded only, with no update attempted. |
| `Get-Command kimi -ErrorAction SilentlyContinue` | 0 | No output: `kimi` is unavailable on `PATH`. PowerShell returns 0 for this silent lookup. |

## Repository inventory commands

| Command | Exit code | Result |
|---|---:|---|
| `git branch --show-current` | 0 | `main` |
| `git log -1 --format='%H%n%cs%n%s'` | 0 | `96ff57a6f209791b38c8c52e665d74f237081e4b`; `2026-07-21`; `chore(docs): updated docs/readme.md` |
| `git ls-files \| Measure-Object -Line` | 0 | 359 tracked files |
| `git ls-files --others --exclude-standard \| Measure-Object -Line` | 0 | 0 untracked, non-ignored files |
| `git ls-files docs \| Measure-Object -Line` | 0 | 166 tracked documentation files |
| `git ls-files .scratch \| Measure-Object -Line` | 0 | 193 tracked scratch files |
| `git diff --name-only -- docs` | 0 | No unstaged documentation changes |
| `git diff --cached --name-only -- docs` | 0 | No staged documentation changes |
| `git ls-files -s docs` plus SHA-256 over its newline-joined output | 0 | 166 tracked entries; digest `730413773F78717E254F27A020BF73A133EE5A7DEC75DDDE4A375C0D8CD00D4E` |
| `Test-Path` for manifests, locks, version files, configs, hooks, instructions, agent directories, and test directories | 0 | All expected paths absent: `package.json`, `pnpm-lock.yaml`, `package-lock.json`, `yarn.lock`, `bun.lockb`, `.npmrc`, `.node-version`, `.nvmrc`, `.tool-versions`, `tsconfig.json`, Playwright/Vitest/ESLint config paths, `.husky`, `AGENTS.md`, `.agents`, `.codex`, `tests`, and `test`. |
| `git check-ignore -v .artifacts/bootstrap` | 1 | Not ignored yet; expected before B00-02. `.artifacts/` is absent. |

The initial attempt to create a whole-tree filesystem hash used `Get-FileHash` on pipeline text and failed because that cmdlet expects file paths. It did not modify files. The replacement Git-index digest above, together with clean staged/unstaged documentation diffs, is the recorded reproducible documentation-preservation evidence.
## Post-record verification

| Command | Exit code | Result |
|---|---:|---|
| `rg --fixed-strings 'Not started' task.md implementation-report.md evidence.md` | 1 | No placeholders remain; exit 1 is expected for no matches. |
| `git diff --check -- task.md implementation-report.md evidence.md` | 0 | No whitespace errors in B00-01 records. |
| `git diff --name-only -- docs` | 0 | No unstaged documentation changes after writing the task records. |
| `git diff --cached --name-only -- docs` | 0 | No staged documentation changes after writing the task records. |
| `git ls-files -s docs` plus SHA-256 over its newline-joined output | 0 | Still 166 tracked entries; digest unchanged: `730413773F78717E254F27A020BF73A133EE5A7DEC75DDDE4A375C0D8CD00D4E`. |
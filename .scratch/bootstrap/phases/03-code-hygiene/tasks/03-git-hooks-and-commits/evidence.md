# B03-03 Evidence

Session: `20260722_061844_4c3566`
Started: `2026-07-22T03:19:49Z`

## Dependency and state

- B03-03 was `Ready`; B03-02 was `Done` in `status.md` before work began.
- Phase 03 was already `In progress`; B03-03 is now `In review` in both the task front matter and phase-status row.

## Commands and results

| Command | Exit | Result |
|---|---:|---|
| `pnpm add -D husky lint-staged @commitlint/cli @commitlint/config-conventional` | 0 | Added Husky 9.1.7, lint-staged 17.1.0, commitlint CLI 21.2.1, and conventional config 21.2.0. |
| `pnpm exec husky && git config --get core.hooksPath` | 0 | Husky initialized through `prepare`; hooks path printed `.husky/_`. |
| Controlled staged-file script containing `pnpm exec lint-staged` | 0 (lint-staged) | Processed one TypeScript and one JSON fixture; lint-staged hid/restored partial unstaged changes and staged the Prettier-normalized JSON. |
| Controlled unstaged-payload/checksum assertion | 0 | The unstaged TypeScript payload exactly matched `+export const unstagedValue = "preserve";`; unrelated fixture SHA-256 remained `277719aa8e829463a6d35b68e4356ba8e137f5ccfffde5f9ecacd2e43de53dcf`. |
| `printf 'chore(bootstrap): configure B03-03 hooks\n' \| pnpm exec commitlint` | 0 | Valid Conventional Commit message passed. |
| `printf 'invalid commit message\n' \| pnpm exec commitlint` | 1 | Invalid message failed with `subject-empty` and `type-empty`; no commit was created. |
| `pnpm install --frozen-lockfile && pnpm format:check && git diff --check` | 1 | Frozen install and `prepare` completed; the first format check found `commitlint.config.mjs` and `pnpm-lock.yaml` unformatted. |
| `pnpm exec prettier commitlint.config.mjs pnpm-lock.yaml --write && pnpm format:check && git diff --check` | 0 | Corrected only those files; full format check and whitespace check passed. |

## Controlled fixtures and artifacts

- Controlled paths: `app/b03-03-lint-staged.fixture.ts`, `app/b03-03-lint-staged.fixture.json`, `app/b03-03-unrelated.fixture.ts`, and `.artifacts/bootstrap/b03-03/`.
- The initial whole-diff comparison exited 1 because lint-staged normalized the staged TypeScript index line, changing the Git diff header; the unstaged payload was unchanged and then verified directly as listed above.
- All controlled fixtures and `.artifacts/bootstrap/b03-03/` were removed. `git diff --cached --quiet` exited 0 after cleanup.

## Retained artifacts

None.


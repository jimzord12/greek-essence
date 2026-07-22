# B03-02 Evidence

Session: `20260722_060353_341484`
Started: `2026-07-22T03:04:35Z`

## Dependency

- Read sibling task front matter: B03-01 status was `Done`.

## Commands and results

| Command | Exit | Result |
|---|---:|---|
| `pnpm format:check` | 1 | Initial full sweep exposed unformatted documentation/agent workspace files; `.prettierignore` was scoped to exclude those non-source trees. |
| `pnpm lint` | 0 | ESLint configuration loaded; no errors. |
| `pnpm lint:fix` with a temporary fixture | 0 | Reordered `node:path` / `node:fs` imports in the fixture. |
| `pnpm format` with the temporary fixture present | 0 | Applied deterministic formatting. |
| `pnpm exec prettier app/b03-02-eslint-prettier.fixture.ts --write` | 0 | Fixture formatting command completed. |
| `pnpm format:check` | 0 | `All matched files use Prettier code style!` |
| `pnpm lint` | 0 | Full `eslint .` completed without findings. |
| `git diff --check` | 0 | No whitespace errors. |

## Controlled fixture and ignore protection

- Temporary fixture: `app/b03-02-eslint-prettier.fixture.ts`; deleted after checks.
- Ignored output: `.artifacts/bootstrap/b03-02/ignored-output.ts`; deleted after checks.
- SHA-256 before and after both fix commands: `6d7e235ef7e9b3996715c99bb2880379de2dbe3fc8bdbf6a991820650e0b411c`.
- Final removal check: `test ! -e app/b03-02-eslint-prettier.fixture.ts && test ! -e .artifacts/bootstrap/b03-02` exited 0.

## Artifacts

No retained generated artifacts. The controlled `.artifacts/bootstrap/b03-02/` directory was removed.

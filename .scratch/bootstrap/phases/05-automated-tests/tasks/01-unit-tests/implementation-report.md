# B05-01 implementation report

## Scope delivered

- Added Vitest with jsdom, React Testing Library, and a test-only TypeScript configuration.
- Added focused tests for explicit `en`/`el` routing, complete English/Greek message-key structure parity, and the quality-lab toggle interaction.
- Limited Vitest discovery to `tests/unit`; no snapshots or coverage target were added.

## Changed files

- `package.json`
- `pnpm-lock.yaml`
- `vitest.config.mts`
- `tsconfig.test.json`
- `eslint.config.mjs`
- `tests/unit/setup.ts`
- `tests/unit/i18n/routing.test.ts`
- `tests/unit/messages/parity.test.ts`
- `tests/unit/components/fixture-toggle.test.tsx`
- `task.md`

## Checks

| Command | Exit | Result |
|---|---:|---|
| `pnpm test:unit` (with temporary `tests/unit/failure-detection.test.ts`) | 1 | Detected the intended `expect(true).toBe(false)` assertion failure. The temporary test was removed. |
| `pnpm test:unit && pnpm exec tsc --noEmit --project tsconfig.test.json` | 0 | Three focused tests passed; test-only TypeScript configuration compiled. |
| `pnpm lint && pnpm typecheck && pnpm build && git check-ignore -q .artifacts/bootstrap/coverage` | 0 | Lint passed with one existing warning; application typecheck and static build passed; coverage path is ignored. |
| `pnpm exec prettier --write pnpm-lock.yaml tests/unit/components/fixture-toggle.test.tsx && pnpm format:check && pnpm check` | 0 | Formatting and aggregate check passed; aggregate check reran lint, application typecheck, and all three unit tests. |
| `git diff --check` | 0 | Passed. |
| `pnpm test:unit` (with temporary English-only `ReviewMismatch` namespace) | 1 | Corrected parity test detected the top-level catalog mismatch. The namespace was removed. |
| `pnpm test:unit && pnpm exec tsc --noEmit --project tsconfig.test.json` | 0 | Three tests passed and test-only TypeScript compilation passed after the H1 correction. |

## Artifacts, assumptions, and risks

- No generated test artifact was required or produced. `.artifacts/bootstrap/coverage` is ignored by Git.
- `validate:content` is not a defined package script in this bootstrap state, so it was not added or run under B05-01.
- `pnpm lint` retains the pre-existing warning in `commitlint.config.mjs`; no lint errors remain.
- Review cycle 01 H1 is corrected by recursively comparing all object-key paths, including namespace paths and nested keys, without comparing translated values.

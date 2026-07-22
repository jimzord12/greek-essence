# B05-01 evidence

## Preconditions

- B05-01 was `Ready` before work began.
- B04-03 is `Done` in its task front matter and Phase 04 status table.
- Implementer session: `20260722_082947_f3ea6c`; started at `2026-07-22T08:30:18+03:00`.

## Commands and results

| Command | Exit | Result | Artifact |
|---|---:|---|---|
| `pnpm test:unit` | 1 | Temporary `tests/unit/failure-detection.test.ts` failed as intended with `expected true to be false`; the file was then removed. | None |
| `rm tests/unit/failure-detection.test.ts && pnpm test:unit && pnpm exec tsc --noEmit --project tsconfig.test.json` | 0 | Temporary case removed; three unit/component tests and test-only typecheck passed. | None |
| `pnpm lint && pnpm typecheck && pnpm build && git check-ignore -q .artifacts/bootstrap/coverage && git status --short` | 0 | Lint passed with one existing warning, application typecheck passed, static build passed, and the coverage artifact path is ignored. | `.artifacts/bootstrap/coverage` (ignored) |
| `pnpm format:check` | 1 | Detected formatting only in `pnpm-lock.yaml` and `tests/unit/components/fixture-toggle.test.tsx`; corrected before final verification. | None |
| `pnpm exec prettier --write pnpm-lock.yaml tests/unit/components/fixture-toggle.test.tsx && pnpm format:check && pnpm check` | 0 | Formatting passed; aggregate check passed with three unit tests. | None |
| `git diff --check && git diff --name-only && git status --short` | 0 | No whitespace errors; task-owned changes only. | None |
| `pnpm test:unit` | 1 | With a temporary English-only empty `ReviewMismatch` namespace, corrected full-catalog key-path parity failed and identified the missing top-level path. The namespace was removed. | None |
| `pnpm test:unit && pnpm exec tsc --noEmit --project tsconfig.test.json` | 0 | Final H1 verification: all three tests passed and test-only TypeScript compilation passed. | None |

No snapshots, coverage reports, or other generated test output were created.

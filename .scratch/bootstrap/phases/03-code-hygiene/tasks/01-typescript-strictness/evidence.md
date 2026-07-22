# B03-01 evidence

| Command | Exit | Result | Artifact/path |
|---|---:|---|---|
| `pnpm exec tsc --project .scratch/bootstrap/phases/03-code-hygiene/tasks/01-typescript-strictness/tsconfig.negative.json` | 2 | The first temporary configuration used an incorrect `extends` path and did not load the root configuration; it was corrected before the decisive fixture run. | None; temporary configuration removed. |
| `pnpm exec tsc --project .scratch/bootstrap/phases/03-code-hygiene/tasks/01-typescript-strictness/tsconfig.negative.json` | 2 | Corrected fixture failed as required: TS2882 (side-effect import), TS2322 (unchecked indexed access), TS2375 (exact optional property), TS4114 (override), TS7029 (switch fallthrough), and TS18046 (unknown catch variable). | None; temporary fixture and configuration removed. |
| `rm .scratch/bootstrap/phases/03-code-hygiene/tasks/01-typescript-strictness/strictness-negative.ts .scratch/bootstrap/phases/03-code-hygiene/tasks/01-typescript-strictness/tsconfig.negative.json && pnpm typecheck` | 0 | Removed the temporary TypeScript sources, then completed `tsc --noEmit` successfully. | None. |
| `rm .scratch/bootstrap/phases/03-code-hygiene/tasks/01-typescript-strictness/strictness-negative.js && test ! -e .scratch/bootstrap/phases/03-code-hygiene/tasks/01-typescript-strictness/strictness-negative.ts && test ! -e .scratch/bootstrap/phases/03-code-hygiene/tasks/01-typescript-strictness/strictness-negative.js && test ! -e .scratch/bootstrap/phases/03-code-hygiene/tasks/01-typescript-strictness/tsconfig.negative.json` | 0 | Removed the transient JavaScript output created by an authoring-tool check and confirmed all temporary fixture files are absent. | None. |

No artifacts were produced or retained.

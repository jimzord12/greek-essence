# B02-02 evidence

Application directory: `next-app/`

## Implementation command

| Command | Exit | Result | Artifact |
|---|---:|---|---|
| `pnpm install --lockfile-only` | 0 | Resolved lockfile with exact direct specifiers and TypeScript `6.0.3`. | `next-app/pnpm-lock.yaml` |

## Decisive verification

| Command | Exit | Result | Artifact |
|---|---:|---|---|
| `node --version` | 0 | `v24.18.0` | `next-app/.node-version` |
| `pnpm --version` | 0 | `10.33.0` | `next-app/package.json` |
| `pnpm exec tsc --version` | 0 | Initial invocation: `Version 5.9.3`; stale installed modules before frozen install. | — |
| `pnpm list --depth 0` | 0 | Listed the exact direct packages declared in `next-app/package.json`; installed TypeScript was `5.9.3` before frozen install. | `next-app/package.json` |
| `pnpm install --frozen-lockfile` | 0 | Lockfile was up to date; materialized TypeScript `6.0.3` (`- 5.9.3`, `+ 6.0.3`). | `next-app/pnpm-lock.yaml` |
| `pnpm exec tsc --version` | 0 | Re-ran only after the frozen install corrected stale modules: `Version 6.0.3`. | `next-app/pnpm-lock.yaml` |

No generated artifacts were produced.

# B04-03 evidence

## Preconditions

- B04-03 was `Ready` before work began.
- B04-02 is `Done` in its task front matter and Phase 04 status table.
- Implementer session: `20260722_075846_a50993`; started at `2026-07-22T04:59:02Z`.

## Commands and results

| Command | Exit | Result | Artifact |
|---|---:|---|---|
| `pnpm format:check` | 1 | Prettier reported only `app/[locale]/layout.tsx`; corrected before final verification. | None |
| `pnpm lint` | 0 | One existing `commitlint.config.mjs` anonymous-default-export warning; no errors. | None |
| `pnpm typecheck` | 0 | Passed. | None |
| `pnpm exec prettier --write 'app/[locale]/layout.tsx' && pnpm format:check && pnpm build` | 0 | Formatting passed; Next.js production build completed and statically generated `/en`, `/el`, `/en/quality-lab`, and `/el/quality-lab`. | None |
| `pnpm start --port 3100` | Running/terminated | Production server reported ready at `http://localhost:3100`; stopped after verification. | None |
| `node .artifacts/bootstrap/B04-03/verify-rendered-metadata.mjs` | 0 | Single decisive rendered-metadata run passed all four variants: HTTP 200, exact localized title/description, configured-local canonical, `en`/`el`/`x-default` alternates, `noindex, nofollow`, and zero JSON-LD scripts. | `.artifacts/bootstrap/B04-03/rendered-metadata-results.json` |
| `git diff --check` | 0 | Passed. | None |
| `git check-ignore -q .artifacts/bootstrap/B04-03/rendered-metadata-results.json` | 0 | Generated verification artifacts are ignored. | `.artifacts/bootstrap/B04-03/` |

## Rendered values

- `/en` canonical: `http://localhost:3000/en`
- `/el` canonical: `http://localhost:3000/el`
- `/en/quality-lab` canonical: `http://localhost:3000/en/quality-lab`
- `/el/quality-lab` canonical: `http://localhost:3000/el/quality-lab`

All routes rendered `robots: noindex, nofollow` and their route-equivalent `en`, `el`, and `x-default` alternates. Full expected/actual values are in the JSON artifact.

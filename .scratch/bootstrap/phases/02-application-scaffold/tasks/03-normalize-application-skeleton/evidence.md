# B02-03 evidence

## Resolved versions and selected Next.js path

| Item | Result |
|---|---|
| Node.js | `v24.18.0` |
| pnpm | `10.33.0` |
| Next.js | `16.2.6` |
| Selected path | Older-than-16.3 isolated `agents-md` codemod path |
| Bundled documentation | `node_modules/next/dist/docs/` |
| Generated agent-doc index | `.artifacts/bootstrap/B02-03/npx-agents-md.md` |

## Review-cycle 01 corrections

The MSYS Corepack launcher converted its own path incorrectly. Without changing the system, a shell-local `corepack` function invoked the launcher-local `corepack.js` through the existing Node runtime.

| Command | Exit | Result | Artifact/path |
|---|---:|---|---|
| `COREPACK_JS="$(cygpath -w /c/Users/jimzord12/AppData/Local/fnm_multishells/2648_1784687452350/node_modules/corepack/dist/corepack.js)"; corepack() { node "$COREPACK_JS" "$@"; }; corepack --version && corepack pnpm install --frozen-lockfile` | 0 | Corepack `0.35.0` ran frozen installation with pnpm `10.33.0`; lockfile was up to date. | `pnpm-lock.yaml` |
| `npx @next/codemod@canary agents-md --output .artifacts/bootstrap/B02-03/npx-agents-md.md` | 0 | Used bundled Next.js 16.2.6 documentation and created the isolated 8.2 KB agent-doc index. | `.artifacts/bootstrap/B02-03/npx-agents-md.md` |
| `test -d app && test ! -e src/app && test ! -e next-app && test -d node_modules/next/dist/docs && test ! -d .agents/skills/next-best-practices && node -e "const ts=require('fs').readFileSync('tsconfig.json','utf8'); if (!ts.includes('\"@/*\": [\"./*\"]')) process.exit(1)" && grep -Fq './node_modules/next/dist/docs' .artifacts/bootstrap/B02-03/npx-agents-md.md && git diff --exit-code -- AGENTS.md >/dev/null` | 0 | Confirmed root architecture, alias, bundled docs, absent retired skill, generated index target, and unchanged authoritative root `AGENTS.md`. | `app/`, `tsconfig.json`, `.artifacts/bootstrap/B02-03/npx-agents-md.md`, `AGENTS.md` |

## Required verification rerun through Corepack

| Command | Exit | Result | Artifact/path |
|---|---:|---|---|
| `COREPACK_JS="$(cygpath -w /c/Users/jimzord12/AppData/Local/fnm_multishells/2648_1784687452350/node_modules/corepack/dist/corepack.js)"; corepack() { node "$COREPACK_JS" "$@"; }; corepack pnpm dev --port 3103` | 0 (startup) | Next.js 16.2.6 Turbopack reported ready in 394 ms; process was stopped after HTTP smoke. | process output |
| `curl -fsS -D .artifacts/bootstrap/B02-03/corepack-dev-response-headers.txt http://localhost:3103/ -o .artifacts/bootstrap/B02-03/corepack-dev-response.html` | 0 | `/` returned HTTP 200; server log recorded `GET / 200`. | `.artifacts/bootstrap/B02-03/corepack-dev-response-headers.txt`, `.artifacts/bootstrap/B02-03/corepack-dev-response.html` |
| `COREPACK_JS="$(cygpath -w /c/Users/jimzord12/AppData/Local/fnm_multishells/2648_1784687452350/node_modules/corepack/dist/corepack.js)"; corepack() { node "$COREPACK_JS" "$@"; }; corepack pnpm build` | 0 | Compiled, type-checked, and generated static `/` and `/_not-found` routes. | `.next/` (ignored) |

All generated evidence remains under ignored `.artifacts/bootstrap/B02-03/`.

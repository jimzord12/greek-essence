# B02-01 Evidence

- Canonical Hermes session ID: `20260722_044643_6bc8fc`
- Started at: `2026-07-22T01:47:13Z`
- Resolved shadcn CLI version: `4.13.1`

| Command | Exit code | Result | Artifact |
|---|---:|---|---|
| `pnpm dlx shadcn@latest --version` | 0 | Printed `4.13.1`. | `.artifacts/bootstrap/B02-01/shadcn-cli-preflight.txt` |
| `pnpm dlx shadcn@latest init --help` | 0 | Confirmed `--template`, `--preset`, `--pointer`, and `--force` help; `--force` was not used. | `.artifacts/bootstrap/B02-01/shadcn-cli-preflight.txt` |
| `git ls-files --stage; git ls-files --others --exclude-standard` | 0 | Pre-bootstrap inventory contained no root application manifest or root application files; no untracked files. | `.artifacts/bootstrap/B02-01/pre-bootstrap-inventory.txt` |
| `pnpm dlx shadcn@latest init --preset b27GcrRo --template next --pointer` | 0 | Prompt-only invocation in repository root; reached the project-name prompt and created no files. | `.artifacts/bootstrap/B02-01/shadcn-bootstrap.txt` |
| `printf '\\n' \| pnpm dlx shadcn@latest init --preset b27GcrRo --template next --pointer` | 0 | Newline-fed invocation in repository root; accepted the default `next-app` name and completed generation with no overwrite proposal. | `.artifacts/bootstrap/B02-01/shadcn-bootstrap.txt` |
| `pnpm dev > ../.artifacts/bootstrap/B02-01/next-app-dev-smoke.txt 2>&1` | -15 | Working directory: `C:/Users/jimzord12/Documents/GitHub/greek-essence/next-app`; Next.js 16.2.6 was ready in 395 ms. Terminated after HTTP verification with `process.kill` (`proc_5c5f3b6d05c7`). | `.artifacts/bootstrap/B02-01/next-app-dev-smoke.txt` |
| `curl --head --silent --show-error --fail http://127.0.0.1:3000/` | 0 | Working directory: `C:/Users/jimzord12/Documents/GitHub/greek-essence/next-app`; returned `HTTP/1.1 200 OK`. | `.artifacts/bootstrap/B02-01/next-app-dev-smoke.txt` |
| `git diff --no-ext-diff --binary`; `git diff --no-index --binary -- .artifacts/bootstrap/B02-01/empty next-app`; `git diff --no-ext-diff --name-only -- docs` | 0 | Complete repository diff recorded; documentation change list was empty. | `.artifacts/bootstrap/B02-01/complete-repository-diff.txt` |

No documentation files were modified. The generated `next-app/` application smoke passed; no unresolved root-location blocker remains.

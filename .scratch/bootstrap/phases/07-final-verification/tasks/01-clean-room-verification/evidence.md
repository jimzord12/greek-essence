# Evidence

## Status

- Task: `B07-01`
- State: `In review`
- Implementer session: `20260722_232706_b03315`
- Started: `2026-07-22T23:28:28+03:00`
- Review response: `reviews/01-review-response.md`
- Final artifact root: `C:/Users/jimzord12/Documents/GitHub/greek-essence/.artifacts/bootstrap/b07-01-review-01-final2/`
- Isolated copy: `/tmp/greek-essence-b07-01-review-01-final2.DRf5hq`
- Operator clarification: normal pnpm content-addressed cache reuse is allowed at Tier 2; acceptance proves that a fresh checkout without project dependencies or build output installs the locked graph unchanged and passes its gates.

## H-01 correction

The route files now use local prop types rather than Next build-generated globals:

- `app/[locale]/layout.tsx`: `LocaleLayoutProps`
- `app/[locale]/page.tsx`: `LocalePageProps`
- `app/[locale]/quality-lab/page.tsx`: `LocaleQualityLabPageProps`

`package.json` script composition was not changed. The correction is tracked in the repository diff.

## Clean-room commands and artifacts

| Step | Exact command/result | Artifact |
|---|---|---|
| Archive | `git archive --format=tar HEAD | tar -xf - | -C /tmp/greek-essence-b07-01-review-01-final2.DRf5hq`; exit 0 | `archive.log`, `archive.exit` |
| Apply current correction | `git diff --binary HEAD -- 'app/[locale]/layout.tsx' 'app/[locale]/page.tsx' 'app/[locale]/quality-lab/page.tsx' | (cd /tmp/greek-essence-b07-01-review-01-final2.DRf5hq | git -c core.autocrlf=false apply -)`; exit 0 | `apply-working-tree-diff.log`, `apply-working-tree-diff.exit` |
| Original pre-install absence/EOL probe | Windows Python could not resolve the MSYS `/tmp/...` path; superseded exit 1 | `preinstall-absence-and-eol.log`, `preinstall-absence-and-eol.exit` |
| Replacement absence/EOL proof | Fresh archive plus the same three-file correction, converted with `cygpath -w`; `node_modules_absent=true`, `next_absent=true`, all edited files present and LF-only; exit 0 | `replacement-preinstall-absence-and-eol.log`, `replacement-preinstall-absence-and-eol.exit` |
| Store configuration | `pnpm config set store-dir /tmp/greek-essence-b07-01-review-01-final.36rVDn/.pnpm-store --location project`; exit 0 | `configure-store.log`, `configure-store.exit` |
| Effective pnpm store | `pnpm config get store-dir` returned `/tmp/.../.pnpm-store`; `pnpm store path` returned `\\tmp\\...\\.pnpm-store\\v10` | `effective-store-config.log`, `effective-store-config.exit` |
| Frozen install | `pnpm install --frozen-lockfile`; exit 0; 1,169 packages; complete non-empty log | `install.log`, `install.exit` |
| Frozen lock identity | Primary and isolated `pnpm-lock.yaml` SHA-256 both `498d877905274b08be9a0c59974d2031b3976f2c3b9e2ccae441c1e510948ca6`; primary lockfile Git diff exit 0 | live reconciliation |
| Post-install no-build | `node_modules=present`, `.next=absent`; exit 0 | `post-install-no-build.log`, `post-install-no-build.exit` |
| Tool versions | Node v24.18.0; pnpm 10.33.0; TypeScript 6.0.3; Playwright 1.61.1; exit 0 | `versions.log`, `versions.exit` |
| Isolated browser cache | `pnpm exec playwright install chromium` retry; exit 0 | `browser-install-retry.log`, `browser-install-retry.exit` |
| Aggregate gate | `pnpm check:all`; exit 0; non-empty 164-line log | `check-all.log`, `check-all.exit` |
| Quality artifact | Unlighthouse budgets passed; 4 routes scanned | `/tmp/greek-essence-b07-01-review-01-final2.DRf5hq/.artifacts/bootstrap/unlighthouse/ci-result.json` |

The initial browser-install attempt failed while downloading FFmpeg with code `3221225794`; it is superseded by the matching retry record. The final check-all command was guarded by `test ! -d .next` and then ran the locked aggregate script; it did not use a preparatory build.

## H-02 correction and replacement proof

The earlier attempt to prove cache provenance was disproportionate and is not acceptance evidence. Per direct operator clarification, normal pnpm cache reuse is allowed. The relevant Tier 2 proof is: fresh materialization without `node_modules` or `.next`, frozen install exit 0, identical isolated and primary lockfile hashes, no primary lockfile Git diff, and `pnpm check:all` exit 0 in the isolated copy.

The original final2 pre-install absence/EOL probe is superseded because its Windows Python subcommand could not resolve MSYS `/tmp/...` paths. The replacement proof recreated a fresh archive from `HEAD`, applied the same three route-file corrections with `git apply`, converted the temporary root with `cygpath -w`, and then ran the probe through Windows Python. It exited 0 and recorded absent `node_modules` and `.next`, presence of all three corrected route files, and LF-only bytes. This reran only the missing evidence procedure; it did not repeat the already-green frozen install or aggregate gate. Same-reviewer re-review remains required before acceptance.

No reviewer-owned file was edited. No commit, push, deploy, remote/history change, B07-02 work, or credential/system change was performed.

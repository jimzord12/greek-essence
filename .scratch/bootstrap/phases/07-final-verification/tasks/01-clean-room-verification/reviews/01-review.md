# Review

**Reviewer:** `20260723_013332_c5307d`
**Verdict:** Changes requested

## Findings

## Blocking findings

None.

## High-impact findings

### H-01 — Clean frozen-install gate does not pass without a prior build

- **Severity:** High
- **Location:** `package.json:25-26`; `app/[locale]/layout.tsx:28`; `app/[locale]/page.tsx:8,29`; `app/[locale]/quality-lab/page.tsx:9,30`.
- **Requirement:** B07-01 acceptance (`task.md:40`) and verification-matrix row B07-01 require an isolated frozen install followed by `pnpm check:all`, with every applicable local gate passing. The locked script composition requires `pnpm check` before `pnpm build`.
- **Evidence/reproduction:** In a fresh `git archive HEAD` copy with no `node_modules` or `.next`, an isolated-store `pnpm install --frozen-lockfile` exited 0. The direct subsequent `pnpm check:all` exited 2 at `pnpm typecheck`, reporting five missing generated `LayoutProps`/`PageProps` declarations. The reported final exit 0 was obtained only after a separate `pnpm build` generated `.next` types; it is not a clean post-install gate. The same failure is independently reproduced at `/tmp/greek-essence-b07-01-review.5IJ85G/reviewer-check-all.log`.
- **Required correction:** Make the locked `check:all` pass from a clean frozen installation without a preparatory build (preserve the locked package-script composition), then rerun the complete B07-01 clean-room contract from a new copy.
- **Verification:** From a newly archived copy with absent `node_modules` and `.next`, run `pnpm install --frozen-lockfile` and immediately run `pnpm check:all`; both must exit 0.

### H-02 — Recorded exit codes and cache-isolation evidence are contradictory and do not establish the claimed clean-room run

- **Severity:** High
- **Location:** `evidence.md:28,37-40,47-58`; `implementation-report.md:41,43-45`; `.artifacts/bootstrap/b07-01/install-command.txt`; `.artifacts/bootstrap/b07-01/check-all-command.txt`; `.artifacts/bootstrap/b07-01/check-all-exit.txt`.
- **Requirement:** B07-01 requires proof of no reliance on the primary dependency tree or caches; `task.md:36` and protocol Evidence and artifacts (`protocol.md:161-167`) require exact commands and exit codes, not inferred or conflicting results.
- **Evidence/reproduction:** The records state the first post-install `check:all` exited 2, while `check-all-exit.txt` contains `exit=1` and its paired `check-all.log` is empty. The recorded install and check commands set `PNPM_STORE_DIR`; reproducing that environment with `pnpm config get store-dir` and `pnpm store path` resolved to the primary `C:\Users\jimzord12\AppData\Local\pnpm\store\v10`, not the claimed isolated path. The prose assertion that `npm_config_store_dir` was set is absent from `install-command.txt`. Therefore the task record neither has consistent exit evidence nor proves that its claimed frozen installation avoided the primary pnpm cache.
- **Required correction:** Recreate the clean-room evidence after H-01 is fixed. Record the literal command used to configure the pnpm store, its effective `pnpm config get store-dir`/`pnpm store path`, pre-install absence checks, complete non-empty logs, and matching exit records for install and the immediate `check:all`. Correct or supersede the contradictory first-run record; do not cite a prebuild workaround as the acceptance run.
- **Verification:** Independently inspect the recorded command, config/store outputs, log, and exit artifact; from the new copy rerun frozen install and immediate `pnpm check:all`, both exit 0 with the effective store outside the primary workspace/cache path.

## Non-blocking findings

None.

## Verification performed

- Read root `AGENTS.md`, bootstrap protocol, verification-matrix B07-01, B07-01 task, its three listed references, implementation report, evidence, actual diff, and generated artifacts.
- `git diff --check` exited 0. The task diff contains only B07-01 task/report/evidence records before this review.
- Inspected package-script composition and generated-type references. `check:all` runs `check` (including `tsc --noEmit`) before `build`.
- Inspected generated B07-01 artifacts. The final post-build log and exit artifact show an exit-0 full gate, but the original first-check artifact is empty and reports `exit=1`.
- Independent clean-room reproduction:
  - `git archive --format=tar HEAD | tar -xf - -C /tmp/greek-essence-b07-01-review.5IJ85G`; verified pre-install `node_modules` and `.next` absent.
  - With effective isolated `npm_config_store_dir`, `pnpm install --frozen-lockfile` exited 0 (`Packages: +1169`; `Done in 1m 31.8s`).
  - Immediate `pnpm check:all` exited 2 on the five missing Next generated type declarations; no full expensive gate was repeated after this decisive fail-fast result.

## Evidence

- Task acceptance and matrix: `task.md:34-40`; `.scratch/bootstrap/verification-matrix.md:32,52-56`.
- Contradictory first-run artifact: `.artifacts/bootstrap/b07-01/check-all-exit.txt` contains `exit=1`; `.artifacts/bootstrap/b07-01/check-all.log` is 0 bytes; tracked records claim exit 2.
- Cache-path reproduction: the literal recorded `PNPM_STORE_DIR=... pnpm ...` environment resolved `pnpm store path` to `C:\Users\jimzord12\AppData\Local\pnpm\store\v10`.
- Independent failure log: `/tmp/greek-essence-b07-01-review.5IJ85G/reviewer-check-all.log`.

## Handoff verification

`NEXT.md` was read. It limits unrelated Ralph-controller work and directs preservation of the B07-01 task-owned modification; this review made no unrelated change and did not start B07-02.

## Durable knowledge verification

No durable knowledge entry was added or changed. The findings are task-specific and remain in this numbered review record.

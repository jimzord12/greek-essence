# Evidence

## Environment

- `node --version` — exit 0 — `v24.18.0`.
- `pnpm --version` — exit 0 — `10.33.0`.

## Pre-change observation

`git check-ignore -q --no-index -- .artifacts/bootstrap/validation-probe.txt` exited 1 before the `.gitignore` change. This confirmed the policy gap identified in the B00-01 handoff.

## Workspace validation

The following commands were run from the repository root (all exit 0):

```powershell
python .scratch/bootstrap/tools/validate_workspace.py
git check-ignore -v --no-index -- .artifacts/bootstrap/validation-probe.txt
git ls-files --error-unmatch .scratch/bootstrap/README.md
git status --short
```

Results:

- `PASS: 28 unique task IDs; required sections present; acyclic dependencies; all Markdown links resolve; dashboard task counts match (1/28).`
- `git check-ignore` exited 0 and reported `.gitignore:2:.artifacts/bootstrap/` for `.artifacts/bootstrap/validation-probe.txt`.
- `git ls-files --error-unmatch .scratch/bootstrap/README.md` exited 0, confirming the bootstrap workspace is tracked.
- No generated artifact was created; therefore there is no artifact path to retain. The validated ignored boundary is `.artifacts/bootstrap/`.

## Repository state inspected

`git status --short` exited 0 and showed only the expected B00-02 task/status tracking updates and the new `.gitignore` before report/evidence finalization. No package installation, generator, remote, deployment, or Git-history operation was performed.

## Review 01 correction and recheck

The operator explicitly authorized deletion of exactly the 33 future review directories under Phases 01–07 (each future task `reviews` directory and each future phase `reviews` directory), containing 66 placeholder review files. Phase 00 and all other paths were excluded.

The approved PowerShell deletion command validated the target count and scope, counted 66 files, then ran `Remove-Item -LiteralPath $resolved -Recurse`. It exited 0 and reported:

- `Removed directories: 33`
- `Removed files: 66`
- `Remaining phase 01-07 review directories: 0`

Affected rechecks were run from the repository root:

```powershell
python .scratch/bootstrap/tools/validate_workspace.py
$phaseReviewDirs = Get-ChildItem .scratch/bootstrap/phases -Directory | Where-Object { $_.Name -match '^(0[1-7])-' } | ForEach-Object { Get-ChildItem $_.FullName -Directory -Recurse | Where-Object { $_.Name -eq 'reviews' } }
```

Both commands exited 0. The validator confirmed all 28 IDs, required sections, an acyclic dependency graph, relative Markdown links, synchronized status views, and dashboard counts (`1/28`). The review-directory inventory returned zero directories under Phases 01–07. The retained Phase 00 B00-02 review records are outside that inventory and were not deleted.

# Review 01 — B03-04

- Reviewer session: `20260722_063813_af9033`
- Reviewed at: `2026-07-22T03:40:22Z`
- Verdict: **Changes requested**

## 1. High — Ignore evidence reports the wrong `git check-ignore -v` exit status

- Exact location: `.scratch/bootstrap/phases/03-code-hygiene/tasks/04-scripts-and-environment/evidence.md:24-34`
- Violated requirement: `.scratch/bootstrap/protocol.md:160-165` requires exact commands and exit codes and prohibits fabricated or inferred results; `.scratch/bootstrap/verification-matrix.md:22` requires verification of `.env*` and `.artifacts/bootstrap/` ignore behavior with `git check-ignore`.
- Evidence/reproduction: Running the recorded decisive command form against the live state produced `.gitignore:33:!.env.example .env.example` and exit `0` for `git check-ignore -v .env.example`, not exit `1` as claimed at `evidence.md:34`. With `-v`, Git reports the matching negation rule and returns `0`. A separate status check without `-v` produced `ignored_rc=0`, `example_rc=1`, and `verification_exit=0`, proving the repository behavior is correct but the recorded evidence/result is not.
- Required correction: Correct only the ignore-behavior section of `evidence.md` so it records a command whose status semantics actually prove both conditions: ignored secret/artifact paths return `0`, and `.env.example` without `-v` returns `1`. Record the actual per-command and aggregate exit codes; do not claim that `git check-ignore -v .env.example` returns `1`.
- Verification: Re-run the corrected ignore command once and confirm `.env.local` and `.artifacts/bootstrap/smoke.txt` yield ignored status `0`, `.env.example` without `-v` yields status `1`, and the aggregate assertion exits `0`; then verify the corrected evidence matches that output exactly.

## Review checks

- Live diff and state were inspected; changes are confined to the B03-04 implementation and records.
- All 15 locked package scripts were invoked once at help/smoke level. The eight installed-tool scripts exited `0`; the five deferred-tool scripts plus `check` and `check:all` exited `1` at their documented unavailable executables. The package-script strings exactly match the locked composition, and the aggregate scripts are non-mutating by composition.
- `.env.example` contains only the two task-authorized public build defaults; `.env*` and `.artifacts/bootstrap/` rules are present, and corrected status-based checks prove the intended ignore behavior.

Approval is withheld until Finding 1 is corrected and verified.

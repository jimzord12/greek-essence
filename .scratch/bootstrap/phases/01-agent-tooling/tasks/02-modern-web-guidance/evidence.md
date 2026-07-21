# Evidence — B01-02 Modern Web Guidance

## Review-cycle 01 corrected verification

The exact reviewed command sequence is retained in `scripts/verify-review-01.sh`. It runs from the repository root, creates one isolated temporary directory with `mktemp -d`, removes it through a verified EXIT trap, and prints the temporary path plus the cleanup result. The script body is the authoritative copy-pasteable record for every wrapper, source, installer, layout, comparison, exclusion, and provenance assertion below; no command is summarized in place of its executable form.

| Exact invocation | Exit | Concise result | Artifact path |
|---|---:|---|---|
| `mkdir -p .artifacts/bootstrap/B01-02` | 0 | Created the ignored artifact directory before cycle-01 verification. | `.artifacts/bootstrap/B01-02/` |
| `bash -n .scratch/bootstrap/phases/01-agent-tooling/tasks/02-modern-web-guidance/scripts/verify-review-01.sh` | 0 | Shell syntax validated. | None |
| `bash .scratch/bootstrap/phases/01-agent-tooling/tasks/02-modern-web-guidance/scripts/verify-review-01.sh > .artifacts/bootstrap/B01-02/review-01-verification.log 2>&1` | 0 | Re-ran the complete corrected workflow verbatim. The log records wrapper help/delegation, official release/layout, direct installer output, selected-layout comparisons, record assertions, and `cleanup_result=removed`. | `.artifacts/bootstrap/B01-02/review-01-verification.log` (ignored) |
| `git check-ignore -v .artifacts/bootstrap/B01-02/review-01-verification.log` | 0 | Confirms `.artifacts/bootstrap/` is ignored by `.gitignore`. | None |

## Exact commands inside the retained verification script

The retained script executes these complete commands in its isolated directory (with `set -euo pipefail`):

```bash
DISABLE_TELEMETRY=1 npx modern-web-guidance@latest --help
npm pack --silent modern-web-guidance@0.0.177 >/dev/null
tar -xzf "$archive" -C wrapper --strip-components=1
node -e "const p=require('./wrapper/package.json'); console.log(JSON.stringify({version:p.version,repository:p.repository,license:p.license,bin:p.bin},null,2))"
grep -n -F 'const installArgs = `-y skills add GoogleChrome/modern-web-guidance ${values.choose ? "" : "--skill modern-web-guidance"}`.split(" ").filter(Boolean);' wrapper/skills/modern-web-guidance/modern-web.mjs
git clone --quiet https://github.com/GoogleChrome/modern-web-guidance.git "$work/upstream"
git -C "$work/upstream" checkout --quiet --detach 79aae1e0bed948e48fd78b58538c5ee1e6463da9
git -C "$work/upstream" archive HEAD | tar -x -C "$work/upstream-export"
DISABLE_TELEMETRY=1 npx -y skills add GoogleChrome/modern-web-guidance --skill modern-web-guidance --yes --copy
cmp "$local_skill/SKILL.md" "$work/wrapper/skills/modern-web-guidance/SKILL.md"
cmp "$local_skill/LICENSE" "$work/wrapper/LICENSE"
cmp "$local_skill/THIRD_PARTY_NOTICES" "$work/wrapper/THIRD_PARTY_NOTICES"
diff -u <(tr -d '\r' < "$local_skill/SKILL.md") <(tr -d '\r' < "$work/upstream-export/skills/modern-web-guidance/SKILL.md")
diff -u <(tr -d '\r' < "$local_skill/LICENSE") <(tr -d '\r' < "$work/upstream-export/LICENSE")
```

The script also contains the exact `find`, `test`, and `grep` assertions for each generated target, the selected three-file local layout, separately excluded paths, and corrected README fields. Its full content is tracked at `scripts/verify-review-01.sh`; it is intentionally cited rather than duplicated as a second source of truth.

## Corrected results

- Wrapper package: `modern-web-guidance@0.0.177`, Apache-2.0, package gitHead `d07f33a3fb6b0056d3d7140e2952c89b3a72aa89`.
- Wrapper `install` delegation: `npx -y skills add GoogleChrome/modern-web-guidance --skill modern-web-guidance`.
- Official repository release: `79aae1e0bed948e48fd78b58538c5ee1e6463da9`, subject `Release v0.0.177`.
- Official core-skill layout: 139 files, including guide directories for accessibility, built-in AI, CSS, forms, HTML, JavaScript, performance, privacy, security, UI, visual design, and WebMCP. The separate `skills/chrome-extensions` skill, passkey guide, and WebMCP guides are present upstream.
- Direct underlying installer: exit 0; generated 139 core-skill files each in `.agents`, `.claude`, `.hermes`, and `.trae` in the isolated output directory. The log enumerates every generated target file.
- Selected repository layout: exactly `SKILL.md`, `LICENSE`, and `THIRD_PARTY_NOTICES`. The selected files match wrapper-package bytes; `SKILL.md` and `LICENSE` match official-repository files after CRLF/LF normalization. `THIRD_PARTY_NOTICES` is wrapper-package attribution and is absent from the official repository.
- Cleanup: the final log ends `cleanup_result=removed path=/tmp/tmp.qojt5aFRWZ`; no installer directory remains outside the ignored log.

## Task verification and state

- `npx modern-web-guidance@latest --help` is executed by the retained script with exit 0 and exposes `install [options]`, satisfying the B01-02 verification-matrix row.
- Canonical retained `SKILL.md`, recorded release/revisions, Apache-2.0 license, and wrapper third-party attribution are verified by the retained script with exit 0.
- Optional Chrome Extensions, passkey, and WebMCP content are absent locally by intentional selection; the script verifies the paths are absent and the README explains that this was not automatic installer behavior.
- B01-02 remains `In review`; no closure command was run.

## Supersession note

This cycle-01 record replaces the earlier shorthand command rows. The original exploratory failures (`npm pack --pack-destination` under MSYS and the unrelated Corepack shim lookup) are not acceptance checks and did not affect the corrected workflow. The retained script and its exit-0 log are the complete reproducible evidence for re-review.

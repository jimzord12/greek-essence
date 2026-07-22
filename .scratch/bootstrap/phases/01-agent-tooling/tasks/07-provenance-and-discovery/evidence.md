# Evidence — B01-07 Provenance and discovery

## Session and runtime

- Implementer session: `20260722_042302_c11331`; started: `2026-07-22T04:23:50+03:00`.
- `codex --version` output: `codex-cli 0.144.6` (exit `0`).
- Codex artifacts: `.artifacts/bootstrap/B01-07/`; Git-ignore verification reported `.gitignore:2:.artifacts/bootstrap/`.

## Required verification

| Exact command | Exit | Concise result | Artifact path |
|---|---:|---|---|
| `command -v kimi` | 1 | No `kimi` executable was found. Kimi discovery/use validation is blocked by unavailable executable/authentication. | None |
| `codex exec --skip-git-repo-check 'Explicitly read only .agents/skills/modern-web-guidance/SKILL.md. Do not modify any files. Return the exact Step 1 npx search command, retaining its placeholder and --skill-version value.' > .artifacts/bootstrap/B01-07/codex-modern-web-guidance.txt 2>&1` | 0 | Explicit load returned the exact Step 1 search command. A non-fatal Codex models-cache warning preceded the successful answer. | `.artifacts/bootstrap/B01-07/codex-modern-web-guidance.txt` |
| `codex exec --skip-git-repo-check 'Explicitly read only .agents/skills/bootstrap-next/SKILL.md. Do not modify any files. State the exact repository-relative file it requires reading before executing one valid bootstrap task.' > .artifacts/bootstrap/B01-07/codex-bootstrap-next.txt 2>&1` | 0 | Explicit load returned `.scratch/bootstrap/BOOTSTRAP-AGENTS.md`. | `.artifacts/bootstrap/B01-07/codex-bootstrap-next.txt` |
| `codex exec --skip-git-repo-check 'Explicitly read only .agents/skills/vercel-react-best-practices/SKILL.md. Do not modify any files. State the eight rule categories in their listed priority order.' > .artifacts/bootstrap/B01-07/codex-vercel-react-best-practices.txt 2>&1` | 0 | Explicit load returned all eight categories in order. | `.artifacts/bootstrap/B01-07/codex-vercel-react-best-practices.txt` |
| `codex exec --skip-git-repo-check 'Explicitly read only .agents/skills/playwright-cli/SKILL.md. Do not modify any files. State the exact Quick start command that opens a new browser.' > .artifacts/bootstrap/B01-07/codex-playwright-cli.txt 2>&1` | 0 | Explicit load returned `playwright-cli open`. | `.artifacts/bootstrap/B01-07/codex-playwright-cli.txt` |
| `codex exec --skip-git-repo-check 'Explicitly read only .agents/skills/greek-essence-quality-review/SKILL.md. Do not modify any files. Return the eight Report format headings in their required order.' > .artifacts/bootstrap/B01-07/codex-greek-essence-quality-review.txt 2>&1` | 0 | Explicit load returned all eight report headings in order. | `.artifacts/bootstrap/B01-07/codex-greek-essence-quality-review.txt` |

## Provenance-record verification

| Exact command | Exit | Concise result | Artifact path |
|---|---:|---|---|
| `python -c "from pathlib import Path; skills=['bootstrap-next','modern-web-guidance','vercel-react-best-practices','playwright-cli','greek-essence-quality-review']; headings=['Bootstrap Next Task','Modern Web Guidance','Vercel React Best Practices','Playwright CLI','Greek Essence Quality Review']; fields=['Local skill name','Local path','Purpose','Upstream source','Installed revision','Installation','Installation date','Verified license','Included','Excluded','Local modifications','Codex validation result','Kimi validation result','Update procedure']; root=Path('.agents/skills'); text=Path('.agents/README.md').read_text(encoding='utf-8'); assert all((root/name/'SKILL.md').is_file() for name in skills); assert all(('## '+heading) in text for heading in headings); assert all(text.count('**'+field)>=5 for field in fields); print('B01-07 provenance inventory: PASS; skills=5; required_fields=14')" && git diff --check` | 1 | Initial standardized-label assertion failed; no files were changed by the command. | None |
| Same command after label-only provenance correction | 0 | `B01-07 provenance inventory: PASS; skills=5; required_fields=14`; `git diff --check` produced no output. | None |

## Deviations

None. Kimi is recorded as an external blocker exactly because its required executable/authentication is unavailable.

## Pre-review tracking correction

| Exact command | Exit | Concise result | Artifact path |
|---|---:|---|---|
| `python .scratch/bootstrap/ralph-loop/tools/check_state.py` | 11 | Returned `RESUMABLE` for task `B01-07` with `reasons: []` after restoring the parser-compatible exact current-task value. | None |


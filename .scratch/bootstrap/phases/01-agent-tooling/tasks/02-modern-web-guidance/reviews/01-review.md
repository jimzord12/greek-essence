# Review 01

## B01-02 — Install Modern Web Guidance

**Reviewer:** `greekreview` (`20260722_020416_c5fa1e`)
**Implementer:** `greekimpl` (`20260722_014730_908786`)
**Review cycle:** 01
**Verdict:** **Changes requested**

## Scope and contract checked

- Root `AGENTS.md`, bootstrap reviewer instructions and protocol, B01-02 verification-matrix row, task contract, implementation report, and evidence record.
- Only the three project references named by the task's Required reading section.
- Complete live tracked diff and all untracked B01-02 files, including `.agents/README.md`, `SKILL.md`, `LICENSE`, and `THIRD_PARTY_NOTICES`.
- Live official help, npm release metadata/package, official repository release source, installer delegation and generated layout, provenance/license fields, optional-discipline absence, and tracking consistency.

## Findings

### High finding 1 — Installer output and provenance records materially misdescribe the canonical generated layout

- **Severity:** High
- **Exact location:** `.agents/README.md:17`; `.scratch/bootstrap/phases/01-agent-tooling/tasks/02-modern-web-guidance/evidence.md:23`; `.scratch/bootstrap/phases/01-agent-tooling/tasks/02-modern-web-guidance/implementation-report.md:24`.
- **Requirement:** `task.md:24-27,41` requires inspection of the official source, installer behavior, generated files, scripts/network calls, license/revision, required references, and excluded disciplines. `docs/05_agent_skills/06_google_chrome_modern_web_guidance.md:30-49` requires inspection of current official installation behavior and generated files before selectively copying the approved skill and required references. `docs/05_agent_skills/13_safe_installation_and_review_rules.md:3-14,18` requires inspection of every generated/referenced file and all installation side effects. Bootstrap protocol lines 164-165 require accurate, non-inferred evidence.
- **Evidence/reproduction:** The current `modern-web-guidance@0.0.177` wrapper source delegates `install` to `npx -y skills add GoogleChrome/modern-web-guidance --skill modern-web-guidance`. A fresh clone of that official repository resolved commit `79aae1e0bed948e48fd78b58538c5ee1e6463da9` (`Release v0.0.177`) and contains 139 files under `skills/modern-web-guidance/`: `SKILL.md` plus the guide catalog, including passkey and WebMCP guides. A successful isolated `npx -y skills add GoogleChrome/modern-web-guidance --skill modern-web-guidance --yes --copy` installed those files into `.agents/skills/modern-web-guidance/` and copied the skill to agent-specific targets. The official `SKILL.md` and license normalize to the same content as the vendored files, but the records instead state that the official installer generated only `SKILL.md` and label the guide catalog “noncanonical generated package content.” Those statements are false for the inspected release and obscure the selective-vendoring decision and installer side effects.
- **Required correction:** Correct `.agents/README.md`, `evidence.md`, and `implementation-report.md` to identify the official repository release/commit and accurately describe the complete generated core-skill layout and agent-specific copies. Distinguish canonical upstream files from intentionally excluded local files. Document which generated files were inspected, why no local guide/reference is required for the retained runtime-search design (or retain any reference that is actually required), and continue to exclude the separately prohibited optional disciplines without implying that the installer did so automatically.
- **Verification:** In a clean temporary directory, run `npx modern-web-guidance@latest --help`, inspect the wrapper's install delegation, run the successful isolated installer workflow, enumerate every generated file/target, compare the selected vendored files to the recorded official release/commit with normalized line endings, and assert that the corrected provenance and exclusion statements match the observed output.

### High finding 2 — The evidence record does not provide the required exact, reproducible commands

- **Severity:** High
- **Exact location:** `.scratch/bootstrap/phases/01-agent-tooling/tasks/02-modern-web-guidance/evidence.md:20-24,32,34-35,38-41`.
- **Requirement:** `task.md:37` requires exact commands, exit codes, and artifact paths in `evidence.md`; bootstrap protocol line 164 imposes the same exact-command requirement, and line 165 forbids inferred results.
- **Evidence/reproduction:** Multiple rows contain command summaries rather than executable commands: “in a fresh temporary directory, project scope/copy mode”; semicolon-separated fragments without the actual temporary-directory, extraction, copy, trap, and comparison commands; `test -f for ...`; “Node assertion over ...”; “Final isolated release comparison ...”; and “EOF-newline assertion ...”. The omitted options and scripts are material here because the official wrapper is interactive, generated targets depend on selected mode/agents, and the successful direct installer generates substantially more than the record claims. A reviewer cannot reproduce those rows exactly from the tracked evidence.
- **Required correction:** Replace each shorthand entry with the complete copy-pasteable command or point to a retained, reviewed script whose exact invocation and content are recorded. Preserve the actual exit code for every command/subcommand, including expected nonzero checks, and accurately record temporary artifact creation and cleanup.
- **Verification:** Execute every corrected command verbatim from the stated working directory or stated isolated directory and confirm that its exit code, generated layout, comparisons, and cleanup match the revised evidence.

## Blocking findings

None.

## Non-blocking findings

None.

## Verification performed

| Check | Result |
|---|---|
| `npx modern-web-guidance@latest --help` | Exit 0; exposes `install [options]` and confirms the expected `npx modern-web-guidance@latest install` entry. |
| `npm view modern-web-guidance@latest version license repository gitHead dist.shasum dist.tarball --json` | Exit 0; current npm release is `0.0.177`, Apache-2.0, source repository `GoogleChrome/modern-web-guidance-src`, gitHead `d07f33a3fb6b0056d3d7140e2952c89b3a72aa89`, shasum `8648e431d681fb3f133147f8b971c2a422eac921`. |
| Fresh `npm pack --silent modern-web-guidance@0.0.177`, extraction, SHA-256, and byte comparisons | Exit 0; local `SKILL.md`, `LICENSE`, and `THIRD_PARTY_NOTICES` are byte-identical to the npm package files. Hashes match the implementation evidence. |
| Fresh official repository clone and revision/layout inspection | Exit 0; HEAD `79aae1e0bed948e48fd78b58538c5ee1e6463da9`, subject `Release v0.0.177`; 139 files in the core skill; passkey and WebMCP guides present; separate `skills/chrome-extensions` present. |
| Normalized comparison of official-repository `SKILL.md` and `LICENSE` to local files | Exit 0; content is equal after CRLF/LF normalization. |
| Isolated underlying installer run: `npx -y skills add GoogleChrome/modern-web-guidance --skill modern-web-guidance --yes --copy` | Exit 0; installed one core skill with the full guide catalog into `.agents` and copied it to `.claude`, `.hermes`, and `.trae`; temporary directory was removed. |
| Local exact-layout and optional-name inspection | Exit 0; local B01-02 directory contains exactly `SKILL.md`, `LICENSE`, and `THIRD_PARTY_NOTICES`; no local Chrome Extensions, passkey, or WebMCP path exists. |
| Provenance/runtime-field assertion over `.agents/README.md` | Exit 0; all fields required by the inventory schema are present, though High finding 1 requires factual correction. |
| `git diff --check` and no-index whitespace checks for all untracked B01-02 files | Exit 0; no whitespace errors. |
| `python .scratch/bootstrap/ralph-loop/tools/check_state.py --repo . --expected-task-count 28 --final-task-id B07-03 --allow-dirty` | Exit 11 with state `RESUMABLE`, active task `B01-02`, and no consistency reasons; this is the checker's expected active-task code. |
| Live Git status, tracked diff, untracked inventory, and index inspection | Branch `main`, ahead 12; no staged changes. Before reviewer-owned edits, changes were limited to the B01-02 implementation/tracking set. |

## Evidence assessment

The vendored three files have correct release bytes, the local layout excludes optional content, all required inventory fields exist, and task/phase state is correctly `In review`. Approval is withheld because the installer/provenance narrative is materially inaccurate and the tracked evidence does not contain the exact commands required by the task contract.

## Handoff verification

B01-02 must remain `In review`; it is not eligible for closure or a task commit. Return both High findings to the original implementer for a paired review response, corrected records, and affected re-verification. No implementation fix was made by the reviewer.

## Durable knowledge verification

No durable knowledge candidate is approved in this cycle.

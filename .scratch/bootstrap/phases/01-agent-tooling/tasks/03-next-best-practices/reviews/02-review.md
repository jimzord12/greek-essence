# Review 02

## B01-03 — Install Vercel next-best-practices

**Reviewer:** `greekreview` (`20260722_023946_4b5f39`)
**Implementer:** `greekimpl` (`20260722_023532_75f390`)
**Review cycle:** 02
**Verdict:** **Blocked**

## Re-review scope

- Read `reviews/01-review-response.md`, corrected `implementation-report.md` and `evidence.md`, and root-integrator changes to Phase 01 status, the bootstrap dashboard, and `ralph-loop/HANDOFF.md`.
- Re-inspected the complete live B01-03/tracking diff, repository status, mutation boundaries, locked-source HEAD/tree, and ignored artifacts.
- Re-ran the deterministic state checker and the affected Skills CLI source/list/install checks.

## Prior finding dispositions

### Finding 1 — The locked source cannot supply the required canonical skill

- **Prior severity:** Blocking
- **Status:** Remaining
- **Exact location:** `.scratch/bootstrap/phases/01-agent-tooling/tasks/03-next-best-practices/task.md:15,23-25,35,39`; `.scratch/bootstrap/verification-matrix.md:11`; `docs/05_agent_skills/07_vercel_next_best_practices.md:19-60`; corrected blocker records at `.scratch/bootstrap/phases/01-agent-tooling/tasks/03-next-best-practices/implementation-report.md:3-36` and `evidence.md:19-30`.
- **Traceable requirement:** The locked contract still requires `npx skills add vercel-labs/agent-skills --skill next-best-practices`, the canonical requested skill only, exact source provenance, and verified license/attribution. Bootstrap protocol lines 168-173 require external authority for source/scope changes.
- **Evidence/reproduction:** The implementer accepted the blocker and corrected the records to distinguish the upstream root README's `MIT` declaration from the absence of a license/notice/copying artifact, and to scope the history claim to locally reachable history. Independent re-run: `git ls-remote https://github.com/vercel-labs/agent-skills.git HEAD` still returned `4559f18a20c1691c744b4395194290db6a0df5e9`; the inspected tree still has no `skills/next-best-practices` and no license/notice/copying file. `npx skills add vercel-labs/agent-skills --skill next-best-practices --list` exited 0, found nine skills, and omitted the target. The exact install attempt with `--yes --copy` exited 1 with `No matching skills found for: next-best-practices`. No operator source/license/replacement decision has been recorded.
- **Required correction:** Human operator/project authority must either provide and approve an immutable canonical source/revision with a valid license/attribution basis, or approve a replacement delivery model and authorize corresponding changes to the tooling baseline, task contract, verification row, and acceptance criteria. The original implementer must not substitute another source, skill, collection, bundled documentation, or generated agent rules without that authority.
- **Verification:** After the decision, rerun the approved isolated source/install workflow, inspect every requested file/reference and side effect, verify license/attribution, confirm only the approved canonical content is vendored at the approved path, inspect the final diff, and record exact commands/exits/artifacts before another review cycle.

### Finding 2 — B01-03 tracking views disagree and deterministically stop bootstrap automation

- **Prior severity:** High
- **Status:** Resolved
- **Exact location:** `.scratch/bootstrap/phases/01-agent-tooling/tasks/03-next-best-practices/task.md:3`; `.scratch/bootstrap/phases/01-agent-tooling/status.md:7`; `.scratch/bootstrap/README.md:18-20`; `.scratch/bootstrap/ralph-loop/HANDOFF.md:16-18,28-35`.
- **Traceable requirement:** Bootstrap protocol lines 34-36 and 176-180 require consistent task, phase, dashboard, and handoff state; the deterministic checker governs automation state under lines 152-157.
- **Evidence/reproduction:** All four tracking views now identify B01-03 as `Blocked`, state that no later task is eligible, and record the same required operator source/license or replacement-contract decision. `python .scratch/bootstrap/ralph-loop/tools/check_state.py --repo . --expected-task-count 28 --final-task-id B07-03 --allow-dirty` exited 20 with state `BLOCKED`, task `B01-03`, and `reasons: []`. Exit 20 now reflects the intentional blocked task rather than a consistency defect.
- **Required correction:** None for this finding. Preserve the synchronized blocked state until the external decision is supplied and accepted.
- **Verification:** The state-checker rerun above and direct inspection of the four cited locations clear the prior High finding.

## New findings

None.

## Verification performed

| Check | Result |
|---|---|
| `python .scratch/bootstrap/ralph-loop/tools/check_state.py --repo . --expected-task-count 28 --final-task-id B07-03 --allow-dirty` | Exit 20; state `BLOCKED`, task `B01-03`, `reasons: []`. Prior tracking inconsistency is cleared. |
| `npx skills add vercel-labs/agent-skills --skill next-best-practices --list` | Exit 0; found nine skills; target remains absent. |
| `npx skills add vercel-labs/agent-skills --skill next-best-practices --yes --copy` | Exit 1; `No matching skills found for: next-best-practices`. |
| `git ls-remote https://github.com/vercel-labs/agent-skills.git HEAD` | Exit 0; still `4559f18a20c1691c744b4395194290db6a0df5e9`. |
| Locked-source tree and license-candidate inspection | Exit 0; no requested skill path and no license/notice/copying file path. |
| `git diff --check` | Exit 0. |
| Live status/diff, untracked-file, forbidden-path, and ignore inspection | No `.agents/`, package, lockfile, application, plugin, hook, or global-configuration mutation. Changes remain limited to B01-03 task records/reviews and root-owned blocked-state tracking; source artifacts remain ignored. |

## Evidence assessment

The corrected implementation report and evidence accurately describe the live locked-source discrepancy and license limitation. The High tracking defect is resolved. The Blocking source-contract finding remains external and unresolved, so approval and task closure are prohibited.

## Handoff verification

B01-03 must remain `Blocked`. Do not mark it `Done`, commit it as a completed task, or begin B01-04. The next valid action is the human project-authority decision stated in remaining Finding 1, followed by resumed work by the original implementer and re-review by this same reviewer session.

## Durable knowledge verification

No durable knowledge candidate is approved; the upstream availability/migration state remains time-sensitive task evidence.

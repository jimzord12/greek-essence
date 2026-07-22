# Review 01

## B01-03 — Install Vercel next-best-practices

**Reviewer:** `greekreview` (`20260722_023946_4b5f39`)
**Implementer:** `greekimpl` (`20260722_023532_75f390`)
**Review cycle:** 01
**Verdict:** **Blocked**

## Scope and contract checked

- Root and bootstrap agent instructions, bootstrap protocol, B01-03 verification-matrix row, task contract, implementation report, evidence, and live repository diff/state.
- Only the three project references named by the task's Required reading section.
- Current Skills CLI behavior, the locked `vercel-labs/agent-skills` source and fetched branch history, current official Vercel skill listing, relevant successor-source history, license/provenance signals, and repository mutation boundaries.

## Findings

### Blocking finding 1 — The locked source cannot supply the required canonical skill

- **Severity:** Blocking
- **Exact location:** `.scratch/bootstrap/phases/01-agent-tooling/tasks/03-next-best-practices/task.md:15,23-25,35,39`; `.scratch/bootstrap/verification-matrix.md:11`; `docs/05_agent_skills/07_vercel_next_best_practices.md:19-60`.
- **Traceable requirement:** B01-03 requires the specific command `npx skills add vercel-labs/agent-skills --skill next-best-practices`, the canonical local path `.agents/skills/next-best-practices/`, only that skill and its required files, an exact source revision, and verified license/provenance. Bootstrap protocol lines 168-173 require `Blocked` when safe progress needs external authority and require the exact decision/input to be recorded.
- **Evidence/reproduction:** Independent reruns found nine skills in `vercel-labs/agent-skills`; `next-best-practices` was absent, and the required install command exited 1 with `No matching skills found for: next-best-practices`. Current locked-source HEAD is `4559f18a20c1691c744b4395194290db6a0df5e9`; its tree, all 40 fetched remote branch histories, and all reachable object paths contain no `next-best-practices`. The repository has no license file, only a root README declaration of `MIT`, and there is no requested skill to license-review. A separate former source, `vercel-labs/next-skills`/`vercel/nextjs-skills`, had the skill at immutable parent commit `dc1de9caf7612d73f56a8dec3cb1bd6c9ec096b9`, but removed it in `ae552b130126c64228363312be155831684adc2d`; its current README says `next-best-practices` is no longer a skill and points to version-matched bundled Next.js docs/agent rules. That legacy repository/revision is not the source approved by the locked contract and no license candidate was present at the inspected legacy revision. The current official Vercel skills directory still lists the name, which conflicts with the live locked source and successor README rather than establishing a usable approved source.
- **Required correction:** Human operator/project authority must make one explicit source-of-truth decision before implementation: either (a) provide and approve an immutable source/revision for the canonical `next-best-practices` files together with a valid license/attribution basis, or (b) approve a documented replacement for the no-longer-supported skill and authorize the necessary changes to the tooling baseline, task contract, verification row, and acceptance criteria. The original implementer must not substitute the legacy repository, another Vercel skill, the broader collection, bundled docs, or generated agent rules without that decision.
- **Verification:** After the authority decision, rerun the exact approved Skills CLI/source workflow in isolation; pin and inspect the approved revision; enumerate the complete requested skill and references; verify license/attribution; confirm only the approved canonical files are vendored at the approved path; inspect the final repository diff; and record exact commands, exits, and artifact paths.

### High finding 2 — B01-03 tracking views disagree and deterministically stop bootstrap automation

- **Severity:** High
- **Exact location:** `.scratch/bootstrap/phases/01-agent-tooling/tasks/03-next-best-practices/task.md:3`; `.scratch/bootstrap/phases/01-agent-tooling/status.md:7`; `.scratch/bootstrap/README.md:18-20`; `.scratch/bootstrap/ralph-loop/HANDOFF.md:16-18,29-31`.
- **Traceable requirement:** Bootstrap protocol lines 34-36 and 176-180 require the root integrator to keep task, phase, dashboard, reports, and handoff state consistent. `BOOTSTRAP-AGENTS.md:24-29` requires reconciliation when tracking disagrees with repository reality. The deterministic state checker is authoritative under protocol lines 152-157.
- **Evidence/reproduction:** `task.md` says B01-03 is `Blocked`, while Phase 01 `status.md` says `Ready`, the dashboard identifies B01-03 as the next unblocked task, and `HANDOFF.md` says no blocker prevents B01-03. `python .scratch/bootstrap/ralph-loop/tools/check_state.py --repo . --expected-task-count 28 --final-task-id B07-03 --allow-dirty` exited 20 with state `BLOCKED` and reason `B01-03 is Blocked in task.md but Ready in phase status.`
- **Required correction:** Return this finding to the original implementer for the paired response, but the root integrator—not the reviewer—must reconcile B01-03 consistently as blocked in Phase 01 status, the bootstrap dashboard, and handoff/active-blocker tracking, because protocol assigns cross-task tracking updates to the root integrator. Do not mark the task Done or begin B01-04.
- **Verification:** Rerun the state checker above and confirm there is no tracking-consistency reason, then inspect the four cited status locations and confirm they all describe B01-03 as blocked pending the same operator decision.

## Non-blocking findings

None.

## Verification performed

| Check | Result |
|---|---|
| `npx skills --help` | Exit 0; confirms `add`, `--skill`, `--list`, `--yes`, and `--copy`. |
| `npx skills add vercel-labs/agent-skills --skill next-best-practices --list` | Exit 0; found nine skills and did not list `next-best-practices`. |
| `npx skills add vercel-labs/agent-skills --skill next-best-practices --yes --copy` | Exit 1; exact failure `No matching skills found for: next-best-practices`. |
| Locked-source HEAD/tree/history inspection at `4559f18a20c1691c744b4395194290db6a0df5e9` | Exit 0; no requested path in current tree, 40 fetched remote branches, or reachable object paths. Root README declares MIT, but no license/notice/copying file exists. |
| Successor-source history inspection | Exit 0; immutable legacy files exist at `dc1de9caf7612d73f56a8dec3cb1bd6c9ec096b9`, were removed by `ae552b130126c64228363312be155831684adc2d`, and are outside the locked source; no license candidate was found at the legacy revision. |
| `git status --short --untracked-files=all`; package/skill/config diff inspection; `git check-ignore -v .artifacts/bootstrap/B01-03-upstream/README.md` | Exit 0; before reviewer-owned records, tracked changes were limited to the three B01-03 task records; no broader skill, package, application, hook, plugin, or global-config mutation was present; upstream artifacts are ignored. |
| `git diff --check` | Exit 0. |
| `python .scratch/bootstrap/ralph-loop/tools/check_state.py --repo . --expected-task-count 28 --final-task-id B07-03 --allow-dirty` | Exit 20; correctly exposes the B01-03 task/phase status mismatch in High finding 2. |

## Evidence assessment

The implementer's core upstream discrepancy, failed installer result, no-mutation claim, broader-skill absence, and blocked conclusion are independently reproduced and accurate. No approved immutable canonical source exists within the locked `vercel-labs/agent-skills` contract. A legacy immutable copy elsewhere does not cure the blocker because its source and license basis are unapproved and upstream now says the knowledge is no longer distributed as a skill.

## Handoff verification

B01-03 must remain `Blocked`; it is not eligible for closure, approval, a task commit, or successor-task work. External authority must provide the source/replacement decision in Blocking finding 1. The root integrator must also reconcile the tracking mismatch in High finding 2. The reviewer made no implementation or evidence edits.

## Durable knowledge verification

No durable knowledge candidate is approved. Upstream availability and migration details are time-sensitive and must remain in task/review evidence rather than the durable knowledge ledger.

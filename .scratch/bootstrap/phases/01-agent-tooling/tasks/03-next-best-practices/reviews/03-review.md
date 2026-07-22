# Review 03

## B01-03 — Adopt Next.js version-matched agent guidance

**Reviewer:** `greekreview` (`20260722_023946_4b5f39`)
**Implementer:** `greekimpl` (`20260722_023532_75f390`)
**Review cycle:** 03
**Verdict:** **Changes requested**

## Re-review scope

- Inspected repository-authorized BD-015 commit `3a042792019ca8a89123598134320a678d309b7f`, the amended B01-03 and B02-03 verification rows, amended task and Required reading, Review 02/response, current implementation report/evidence, changed root/tooling guidance, complete live diff/state, phase status, dashboard, and handoff.
- Independently re-ran official migration/source revision, current `vercel/next.js` skills-tree, prohibited-path, guidance-consistency, local-link, mutation-boundary, diff, ignore, and deterministic-state checks.
- Inspected B02-03 only to verify the runtime ownership explicitly delegated to it by BD-015 and the amended matrix; no B02 task work was begun.

## Prior finding dispositions

### Prior Finding 1 — The locked source cannot supply the required canonical skill

- **Prior severity:** Blocking
- **Status:** Resolved
- **Exact location:** BD-015 at `.scratch/bootstrap/decisions.md:19`; amended contract at `.scratch/bootstrap/phases/01-agent-tooling/tasks/03-next-best-practices/task.md:11-40`; `.scratch/bootstrap/verification-matrix.md:11,18`; `docs/05_agent_skills/07_nextjs_version_matched_agent_guidance.md:19-49`; `reviews/02-review-response.md:8-15`.
- **Traceable requirement:** Review 02 required project authority to approve either an immutable canonical source/license or a replacement delivery model with corresponding tooling/task/verification changes. The amended B01-03 contract now requires official migration and framework-tree evidence, absence of the retired/substitute skill, consistent bundled-documentation guidance, and deferred runtime validation.
- **Evidence/reproduction:** Commit `3a04279` records the authorized replacement in BD-015 and updates the primary tooling contract. Live `vercel-labs/next-skills` HEAD and the staged notice both resolve to `b76d687cf3e026eac3b1032f610f06b47a56377c`; the notice explicitly says `next-best-practices` is no longer a skill, uses bundled `next/dist/docs/` plus `next dev` generated rules for Next.js 16.3+, and gives `npx @next/codemod@canary agents-md` for older versions. Live `vercel/next.js` canary moved from the recorded point-in-time revision `c77f3ded55f8a542d440cdd8e86f00fd058e4e2c` to `1d3bf10cde7b19093222305c4ded5f5948928419`; the current tree still contains only `.claude-plugin`, `next-cache-components-adoption`, `next-cache-components-optimizer`, `next-dev-loop`, and `next-partial-prefetching-adoption`, with no retired skill. The recorded revision remains an immutable, accurate point-in-time tree.
- **Required correction:** None for the former source/license blocker. BD-015 validly replaces that obsolete contract; no legacy license decision is needed because no legacy skill is vendored.
- **Verification:** Migration assertions passed; current framework-tree API inspection passed; prohibited local retired/substitute/bundle paths are absent.

### Prior Finding 2 — B01-03 tracking views disagree

- **Prior severity:** High
- **Status:** Remaining (regressed in handoff prose)
- **Exact location:** `.scratch/bootstrap/ralph-loop/HANDOFF.md:18,30,34`; task/phase/dashboard current state at `.scratch/bootstrap/phases/01-agent-tooling/tasks/03-next-best-practices/task.md:3`, `.scratch/bootstrap/phases/01-agent-tooling/status.md:7`, and `.scratch/bootstrap/README.md:18-20`.
- **Traceable requirement:** Bootstrap protocol lines 34-36 and 176-180 require task, phase, dashboard, and handoff state to agree. B01-03 is now `In review`, and BD-015 resolves the former source blocker.
- **Evidence/reproduction:** Task front matter, Phase 01 status, dashboard, `HANDOFF.md:18`, and `HANDOFF.md:34` correctly identify B01-03 as in review with the former blocker resolved. However, `HANDOFF.md:30` still states in the present tense that root tracking “now consistently keeps B01-03 blocked.” The deterministic checker exited 11 with `RESUMABLE`, task `B01-03`, and `reasons: []`, so its modeled fields are consistent, but it does not detect this contradictory handoff prose.
- **Required correction:** Root integrator must revise the stale handoff sentence to preserve its historical cycle-02 meaning without claiming the current task remains blocked. The implementation response/evidence should rerun and record the affected tracking consistency check.
- **Verification:** Directly inspect the cited handoff/current-state locations and rerun the deterministic checker; all current-state prose must agree that B01-03 is `In review` and the BD-015 blocker is resolved.

## New findings

### High finding 3 — Phase 01 exit gate still requires five canonical skills

- **Severity:** High
- **Exact location:** `.scratch/bootstrap/phases/01-agent-tooling/phase.md:17-19`; incomplete consistency evidence at `.scratch/bootstrap/phases/01-agent-tooling/tasks/03-next-best-practices/evidence.md:24`.
- **Traceable requirement:** B01-03 acceptance at `task.md:40` requires the obsolete skill requirement to be removed consistently. BD-015 and the approved baseline define four repository-local skills and explicitly state that Next.js reference knowledge is not a skill (`docs/05_agent_skills/01_approved_tooling_baseline.md:11-20`, `03_agent_specific_repository_layout.md:34-43`, and `19_final_approved_baseline.md:3-23`).
- **Evidence/reproduction:** Phase 01 still says, “All five canonical skills exist.” That count and category came from the retired five-skill baseline and contradict the amended four-skill-plus-version-matched-docs contract. The evidence consistency command reports `tooling_contract=ok` only because it omits `phase.md`; an independent audit returned `PHASE_EXIT_RETIRED_COUNT=True`.
- **Required correction:** Project authority/root integrator must amend the Phase 01 exit gate to require the four approved repository-local skills, absence of retired/prohibited alternatives, completed provenance/Codex checks, and the explicit B02-03 runtime handoff, without pretending bundled Next.js documentation is a fifth skill. Expand the evidence consistency check to cover this phase gate.
- **Verification:** Search all current phase/root/tooling baseline text for skill counts and classifications; confirm the exit gate matches BD-015 and the final approved baseline, then rerun the expanded consistency check and local-link check.

### High finding 4 — B02-03 cannot execute its delegated runtime check from its allowed reading/task contract

- **Severity:** High
- **Exact location:** `.scratch/bootstrap/verification-matrix.md:18`; `.scratch/bootstrap/phases/02-application-scaffold/tasks/03-normalize-application-skeleton/task.md:21-42`; authoritative setup details at `docs/05_agent_skills/07_nextjs_version_matched_agent_guidance.md:27-49`; incomplete consistency evidence at B01-03 `evidence.md:24-25,34`.
- **Traceable requirement:** B01-03 acceptance requires scaffold verification to own later runtime integration. `BOOTSTRAP-AGENTS.md:20` and protocol lines 50-58 require a task implementer to read only its listed project references while satisfying its task and matrix contract. The amended B02-03 row requires inspection of installed `next/dist/docs/` and the applicable generated-rule or older-version codemod path.
- **Evidence/reproduction:** The matrix assigns the runtime check to B02-03, but B02-03's Required reading does not include `07_nextjs_version_matched_agent_guidance.md`, and its How/Acceptance sections contain no `next/dist/docs/`, version threshold, `next dev` generated-rule validation, or `agents-md` codemod path. Independent checks returned `B02_03_REQUIRES_NEXT_GUIDANCE=False` and `B02_03_TASK_HAS_RUNTIME_STEPS=False`. Under the read-only-listed-references rule, the future implementer cannot obtain the authoritative version-dependent procedure the matrix tells it to validate. The B01-03 evidence claims ownership is complete without checking the receiving task.
- **Required correction:** Project authority/root integrator must add the authoritative Next.js guidance document to B02-03 Required reading and make the delegated runtime steps/evidence expectation explicit in B02-03 How and/or Acceptance, while preserving version-dependent behavior and root `AGENTS.md` authority. Expand B01-03's consistency/link checks to include the receiving B02-03 task.
- **Verification:** Re-read B02-03 as a standalone contract and confirm it names the authoritative guidance, installed-version inspection, `next/dist/docs/`, the applicable 16.3+ generated-rule path or documented older-version codemod path, exact evidence ownership, and root-guidance precedence; rerun all scoped local-link and consistency assertions.

## Non-blocking findings

None.

## Verification performed

| Check | Result |
|---|---|
| Migration HEAD/artifact and notice assertions | Exit 0; both revisions `b76d687cf3e026eac3b1032f610f06b47a56377c`; retired-skill, bundled-docs, 16.3+ generated-rules, and older-version codemod statements verified. |
| Live `vercel/next.js` canary/API tree | Exit 0; live HEAD `1d3bf10cde7b19093222305c4ded5f5948928419`; five current tree entries listed; no `next-best-practices`. |
| Prohibited local/tracked path check | Exit 0; no retired/substitute Next.js skill, `.claude`, `.hermes`, `.trae`, `.claude-plugin`, or `skills-lock.json`; tracked skill roots remain `bootstrap-next` and `modern-web-guidance` only. |
| Guidance consistency audit | Core amended guidance terms present; exposed the Phase 01 stale five-skill gate, stale handoff blocked claim, and incomplete B02-03 receiving contract described above. |
| Local Markdown link check over 17 changed/relevant files | Exit 0; no broken local links. |
| Mutation-boundary diff | Exit 0 with no output for `.agents`, package/lockfile, `.gitignore`, `.codex`, or `.claude`; no retired, substitute, broad skill, or plugin installation. |
| Artifact ignore check | Exit 0; migration clone and skills-tree JSON are ignored under `.artifacts/bootstrap/`. |
| `git diff --check` | Exit 0. |
| `python .scratch/bootstrap/ralph-loop/tools/check_state.py --repo . --expected-task-count 28 --final-task-id B07-03 --allow-dirty` | Exit 11; state `RESUMABLE`, task `B01-03`, `reasons: []`. |
| Full live diff/status | Branch `main`, ahead 16; changes confined to B01-03 task records/reviews and root-owned dashboard/status/handoff tracking. No B01-04 work or application implementation is present. |

## Evidence assessment

BD-015 and the independent upstream checks resolve the former Blocking source/license finding. The implementation correctly avoids every retired/substitute/broad skill and plugin path, and the recorded point-in-time revisions are accurate. Approval is withheld because the amended contract is not yet internally complete: current handoff prose regressed, the Phase 01 gate retains the retired five-skill model, and the receiving B02-03 task cannot execute its delegated runtime responsibility under the repository's Required-reading rule.

## Handoff verification

B01-03 remains `In review` and is not closure-eligible. Return the three High findings to the original implementer/root integrator for paired response and authorized contract/tracking corrections, then return the same task to this reviewer for cycle 04. Do not mark B01-03 Done, begin B01-04, or create the completed-task commit.

## Durable knowledge verification

No new durable knowledge entry is needed. The approved policy is already owned by BD-015 and the tooling baseline; source revisions remain point-in-time task evidence.

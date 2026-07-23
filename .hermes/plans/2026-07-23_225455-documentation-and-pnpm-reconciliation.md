# Documentation and pnpm Reconciliation Plan

> **For Hermes:** Execute this plan with bounded implementation and independent Terra review. Do not begin product implementation, P1 planning, or image generation/review.

**Goal:** Correct all confirmed audit findings and deliberately migrate Greek Essence from Corepack-managed pnpm 10.33.0 to standalone pnpm 11.17.0 while preserving historical bootstrap evidence.

**Architecture:** Treat this as one documentation/tooling reconciliation change. Current project instructions and package metadata move to standalone pnpm 11.17.0; historical bootstrap records remain truthful about what originally ran, except incomplete Phase 06/07 reports are completed from approved evidence. No application behavior changes are intended.

**Tech Stack:** Markdown, JSON package metadata, pnpm 11.17.0, existing repository validators and quality commands.

---

## Decisions

1. Adopt standalone pnpm 11.17.0 installed through the official PowerShell installer; Corepack is no longer part of the current development contract.
2. Preserve Node 24 and the existing application dependency set unless pnpm 11 requires a mechanical lockfile update.
3. Update current instructions and package metadata, but do not rewrite historical bootstrap evidence to pretend pnpm 11 was used during bootstrap.
4. Correct all three inconsistent authority declarations to: Project Protocol → PRD → Prototype Specification → Technical Design → Design System. Historical UX Strategy material remains supplementary evidence, not rank 5 authority.
5. Clarify that the bootstrap scaffold/tooling are complete while the product application remains unimplemented.
6. Complete the stale Phase 06 and Phase 07 reports only from existing approved task evidence and phase reviews.
7. Update the mutable Ralph handoff through PR #6 and retain the operator visual-direction checkpoint, K-002 exclusion, and completion-signal boundary.
8. Completely retire Kimi as a project requirement: remove it from current requirements, acceptance gates, compatibility claims, blockers, handoffs, tooling inventories, and validators. Historical command evidence may remain factual, but it must be clearly non-normative and must not imply an active requirement.
9. Do not act on external asset-source fidelity; it remains outside this task. The former Corepack issue is resolved by the approved tooling migration.

## Task 1: Capture and protect the baseline

**Files:** Read only.

1. Verify `main`, `origin/main`, HEAD, and `git status --short`.
2. Confirm the only pre-existing change is the operator-authorized `NEXT.md` audit promotion plus this plan file.
3. Record current `pnpm --version` from a fresh PowerShell environment and confirm `corepack` is absent.
4. Stop if unrelated changes appear.

## Task 2: Reconcile the documentation hierarchy

**Files:**

- Modify: `docs/00_project_protocol/documentation_hierarchy.md`
- Modify: `docs/02_prototype_specification/document_purpose_and_authority.md`
- Modify: `docs/03_technical_design/document_purpose_authority_and_scope.md`

1. Make all hierarchy lists use the five-level authority order.
2. Keep UX Strategy material explicitly supplementary/historical, not ranked authority.
3. Verify with a repository search for hierarchy declarations and obsolete rank-5 wording.

## Task 3: Correct current project status wording

**Files:**

- Modify: `docs/README.md`
- Modify: `README.md`

1. State that bootstrap tooling and the bilingual fixture scaffold are complete.
2. State separately that product prototype implementation remains pending.
3. Replace Corepack commands with direct `pnpm install --frozen-lockfile` and `pnpm dev` commands.
4. Add concise Windows standalone installation guidance using the official PowerShell installer and the repository-pinned version.

## Task 4: Adopt standalone pnpm 11.17.0 in current configuration

**Files:**

- Modify: `package.json`
- Modify only if required by pnpm 11: `pnpm-lock.yaml`
- Modify any current, non-historical instruction containing a live Corepack/pnpm-10 requirement, including `AGENTS.md` where applicable.

1. Set `packageManager` to `pnpm@11.17.0`.
2. Change the pnpm engine range from `>=10 <11` to `>=11 <12`.
3. Change current agent instructions from “through Corepack” to direct standalone pnpm.
4. Search all tracked files for `Corepack`, `corepack`, `10.33.0`, `pnpm@10`, and `pnpm 10`.
5. Classify every match:
   - update current normative guidance;
   - preserve historical command/evidence wording;
   - add an explicit supersession note where an old locked bootstrap decision could otherwise be mistaken for current policy.
6. Run `pnpm install --frozen-lockfile` first. If it passes and leaves the lockfile unchanged, do not rewrite it. If pnpm 11 requires a lockfile change, inspect and commit only the minimum mechanical update, then rerun frozen install.

## Task 5: Retire Kimi from the project contract

**Files:**

- Modify current normative and status documents containing an active Kimi requirement, including `NEXT.md`, `.agents/README.md`, `.scratch/bootstrap/BOOTSTRAP-AGENTS.md`, `.scratch/bootstrap/README.md`, `.scratch/bootstrap/FOR_HUMAN_OPERATOR.md`, `.scratch/bootstrap/plan.md`, `.scratch/bootstrap/protocol.md`, `.scratch/bootstrap/verification-matrix.md`, `.scratch/bootstrap/completion-report.md`, `.scratch/bootstrap/decisions.md`, and current phase/task acceptance documents where Kimi remains a gate.
- Preserve historical `evidence.md`, implementation reports, and review records as factual records unless they are incorrectly being consumed as a current requirement.

1. Remove Kimi from approved tooling, compatibility coverage, acceptance criteria, verification matrices, completion blockers, and handoffs.
2. Add a clear supersession entry to the bootstrap decisions: BD-012 is retired by operator decision and no replacement AI-tool requirement is introduced.
3. Remove validators/assertions that require Kimi wording or command lookup.
4. Reword completion/readiness statements so local bootstrap readiness is complete without a cross-agent/Kimi caveat.
5. Verify current normative/status files contain no active `Kimi`, `command -v kimi`, or “cross-agent compatibility blocker” requirement.
6. Do not install Kimi, substitute another model/tool, or rewrite historical command results.

## Task 6: Complete Phase 06 and Phase 07 reports

**Files:**

- Modify: `.scratch/bootstrap/phases/06-quality-review/phase-report.md`
- Modify: `.scratch/bootstrap/phases/07-final-verification/phase-report.md`

1. Read each phase status, task reports/evidence, task reviews, and phase review.
2. Populate the existing report template fields using only approved recorded evidence.
3. Do not rerun historical checks merely to recreate evidence and do not alter task/review outcomes.
4. Ensure completed phase reports no longer contain `Not started`.

## Task 7: Reconcile the Ralph handoff

**Files:**

- Modify: `.scratch/ralph-loop/HANDOFF.md`

1. Record PR #6 and the reviewed 18-record prompt pack as completed.
2. Set the continuation to the operator visual-direction checkpoint unless a newer authorized `NEXT.md` state governs.
3. Preserve: no active campaign, no automatic completion-signal reset, and K-002 open/out of scope. Remove Kimi blocker language.
4. Do not modify Ralph runtime state or `completion-signal.json`.

## Task 8: Reconcile the active handoff

**Files:**

- Modify: `NEXT.md`

1. Preserve the existing intentional audit-promotion diff until all corrections are verified.
2. After the reviewed remediation is complete, replace the active audit wording with the accurate next operator checkpoint.
3. Do not promote P1 planning, product implementation, or image generation automatically.

## Task 9: Verification

Run from repository root and record exact exits/results:

```bash
pnpm --version
pnpm install --frozen-lockfile
pnpm format:check
pnpm lint
pnpm typecheck
pnpm test:unit
pnpm exec playwright test --list
python -B .scratch/bootstrap/tools/validate_workspace.py
node scripts/validate-prototype-asset-prompts.mjs
git diff --check
git status --short
```

Additional deterministic checks:

- `pnpm --version` returns `11.17.0` in a fresh PowerShell environment.
- `corepack` is absent.
- All authority declarations use the five-level order.
- No completed phase report says `Not started`.
- Current normative documentation contains no Corepack command or pnpm-10 requirement.
- Current normative/status documentation contains no Kimi requirement, blocker, compatibility gate, or required lookup.
- Historical bootstrap evidence remains unchanged except the two previously incomplete phase reports and any explicit non-destructive supersession note.
- The worktree contains only planned files.

Do not run build/E2E/Unlighthouse unless the lockfile or executable configuration changes materially enough to require the full gate. If `pnpm install --frozen-lockfile` changes nothing and only metadata/docs change, the listed non-runtime checks are sufficient.

## Task 10: Independent review and delivery

1. Delegate a fresh Terra/medium read-only review of the complete diff.
2. Require review of authority reasoning, historical-record preservation, complete Kimi-requirement retirement, pnpm migration completeness, report evidence accuracy, handoff freshness, and verification output.
3. Correct only supported findings and re-review affected sections.
4. Deliver through the normal repository Git workflow authorized by the operator; do not begin adjacent product work.

## Expected changed files

- `.hermes/plans/2026-07-23_225455-documentation-and-pnpm-reconciliation.md`
- `AGENTS.md`
- `README.md`
- `package.json`
- `pnpm-lock.yaml` only if pnpm 11 requires it
- `docs/README.md`
- `docs/00_project_protocol/documentation_hierarchy.md`
- `docs/02_prototype_specification/document_purpose_and_authority.md`
- `docs/03_technical_design/document_purpose_authority_and_scope.md`
- `.scratch/bootstrap/phases/06-quality-review/phase-report.md`
- `.scratch/bootstrap/phases/07-final-verification/phase-report.md`
- `.scratch/ralph-loop/HANDOFF.md`
- `NEXT.md`

## Exclusions

- Product implementation or P1 planning
- Image generation, submission, or visual review
- External asset-source fidelity comparison
- K-002 implementation
- Kimi installation/authentication
- Ralph launch or completion-signal mutation
- Deployment, remotes, credentials, or history rewriting

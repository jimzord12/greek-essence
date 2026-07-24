# Greek Essence Showcase — Feature Agent Notes

## What We Are Building

- Feature: `greek-essence-showcase`
- User value: A polished bilingual client-demo journey that proves visual quality, responsive implementation, form persistence, and real email submission.
- Primary owner/context: Dimitris; Tier 2 prototype for a prospective-client meeting.

## Why

- Problem: Demonstrate that Greek Essence can become a convincing, practical travel website rather than only a static concept.
- Success signal: Home → Paros & Antiparos → Plan My Trip → confirmation works in English and Greek on desktop and mobile, with refresh persistence and Resend delivery.
- Important constraint: Keep the accepted showcase implementable within a strict 12-hour window after planning and credentials are available.

## Scope

- In scope: Shared visual foundation; localized Home, Paros & Antiparos, Plan My Trip, and confirmation routes; four-step form; `localStorage`; Resend; focused accessibility, responsive, performance, and demo checks.
- Out of scope: Full sitemap/catalogue, production launch/infrastructure, CMS/database/CRM, booking, pricing, availability, accounts, payments, analytics, final legal/marketing content, advanced animation, or production-grade email operations.
- Related work: Root product/prototype/technical/design documents are broader authority, but the accepted feature `PRD.md` narrows this showcase to the required client-demo slice.

## Feature Rules

- Follow root `AGENTS.md` and `NEXT.md`; no root `CLAUDE.md` is present.
- Treat `PRD.md` as accepted feature scope.
- Keep design pragmatic for a solo mid-level developer and a 12-hour Tier 2 implementation.
- Ask only high-impact unresolved questions; do not revisit decisions fixed by authority.
- Use English and Greek routes and preserve equivalent context where practical.
- Do not invent business facts, credentials, prices, availability, response times, or unsupported claims.
- Keep secrets server-side and outside Git.
- Avoid rare edge-case branches unless they protect correctness, privacy, security, or recoverability.
- Follow the live `features-cli` frontier and the active issue/change contract. Do not continue into a successor workflow or issue without explicit authorization.

## Orchestrator / Overseer Ownership

For this feature, the main agent is the workflow orchestrator and overseer. It owns live repository and frontier verification, issue selection, contract enforcement, role briefing, delegation, progress monitoring, quality-gate routing, review routing, lifecycle transitions, evidence reconciliation, and final completion judgment. Its responsibility is to keep authorized work moving until the accepted stopping point rather than stopping at ordinary implementation or verification failures.

### Role separation

- Delegate substantive implementation to a dedicated implementation subagent with the full `SPEC.md`, `issue.md`, and `change-contract.md` context. This feature-local rule overrides a generic workflow topology that would otherwise make the main orchestrator the `tdd-solo` implementer; the delegated implementer still follows the issue's carried `Method` and required RED → GREEN discipline.
- Delegate every required code review to a fresh independent review agent. The orchestrator must not review its own work or substitute implementation judgment for the required review verdict.
- Delegate the mandatory visual review to a fresh independent visual-review agent after code review passes. The implementation agent and code reviewer must not self-certify the visual gate.
- Do not use the orchestrator as the default implementation or review worker merely because it can edit files or run tests.

### Permitted orchestrator actions

The orchestrator may perform repository surveys, preflight and frontier checks, inspect evidence, run or rerun verification, monitor agents, steer or re-brief a role, reconcile reports and status, and make small obvious fixes when spawning or resuming an implementation agent would be clearly disproportionate. Examples include a typo, a deterministic one-line wiring correction, formatting, or another low-risk fix whose behavior and scope are already locked by the contract.

A small orchestrator-owned fix does not waive verification or independent review. Record it in the implementation evidence, rerun the affected checks, and obtain a fresh review when the workflow requires one. If a review finding needs substantive logic, design, architecture, broad test changes, or multiple coordinated edits, route it back to an implementation agent rather than absorbing it into orchestration.

### Keep-running and escalation policy

- A failed test, lint, typecheck, build, accessibility, browser, visual, performance, or other required quality gate is ordinary implementation work—not a stopping condition. Keep the issue `in-progress`, diagnose it, route it to the implementation agent (or make a permitted small fix), and rerun the failed and affected gates until they pass.
- A failed code or visual review is ordinary repair/re-review work when its findings remain inside the accepted contract. Preserve immutable review evidence, route substantive findings to implementation, rerun affected gates, and dispatch the required fresh review attempt.
- Continue autonomously through in-contract implementation, repair, verification, and re-review. Do not ask the operator to coordinate routine agent handoffs or approve ordinary fixes.
- Stop and escalate only for a genuine blocker: a contract hard wall or architectural scope expansion, conflicting authority that cannot be reconciled, destructive or out-of-repository action requiring approval, unavailable credentials or required human input, an external dependency that cannot be bypassed safely, or repeated agent/tool failure after reasonable recovery attempts.
- When escalating, report the exact blocker, evidence, attempted recovery, bounded options, and a recommendation. Do not use escalation as a substitute for diagnosis or workflow ownership.

## Mandatory Visual Review Gate

For any issue that creates or changes a user-visible surface, visual review is part of the Definition of Done. User-visible work includes pages, components, layout, typography, color, spacing, responsive behavior, media, localized-copy presentation, navigation, forms, and loading, validation, pending, error, success, focus, or reduced-motion states.

### Workflow

1. Complete implementation and executable verification through the applicable `jz-implement-contract*` workflow.
2. Run the normal fresh independent code review.
3. After code review passes, but **before setting the issue to `done`**, run a fresh independent visual-review agent against the final application.
4. Give the visual reviewer the feature `SPEC.md`, the issue's `issue.md` and `change-contract.md`, the latest code-review report, this file, and root `AGENTS.md`.
5. Review every affected route and state in English and Greek at compact `390 × 844` and wide `1440 × 1024`. Also inspect every issue-specific interactive, fallback, validation, pending, error, success, focus, and reduced-motion state.
6. Capture sanitized screenshot evidence and write the next immutable `reviews/<NN>-visual-review.md` report.
7. Do not mark the issue `done` unless the latest visual-review report is `PASS`.

### Review Criteria

The visual reviewer must inspect the rendered result for:

- compliance with the approved visual direction and design tokens;
- hierarchy, composition, typography, spacing, alignment, and visual polish;
- responsive wrapping, clipping, overflow, and layout behavior;
- natural English/Greek presentation with comparable hierarchy and no mixed-language fallback;
- media crop quality and intentional neutral fallbacks;
- visible focus and selected, disabled, pending, validation, error, and success states;
- obvious contrast, target-size, readability, and reduced-motion problems;
- unexpected console errors, failed critical requests, broken assets, or visible regressions.

Automated screenshot capture alone is not visual review. A fresh agent must inspect the rendered screenshots and application state and issue a grounded `PASS`, `FAIL`, or `BLOCKED` verdict with evidence.

### Failure Handling

If visual review fails:

1. Keep or return the issue to `in-review`; do not mark it `done`.
2. Fix every in-scope visual finding.
3. Write a new immutable visual-review attempt; never overwrite an earlier report.
4. If a fix materially changes source code, run a new independent code-review attempt before completion.
5. If the required fix crosses a change-contract hard wall, stop with a `ScopeExpansionRequest`.

### Exceptions and Privacy

Visual review may be skipped only for an entirely nonvisual issue. Its implementation report must record `Visual review: not required — <specific reason>`. Server-only, documentation-only, and internal-tooling changes normally qualify; a user-visible change never qualifies merely because automated tests pass.

Use synthetic data only. Screenshots, traces, reports, URLs, console output, and artifacts must contain no real visitor, client, recipient, credential, or other personal data.

## Authority

1. Direct operator instructions.
2. Root `AGENTS.md` and its documented authority order.
3. Feature `PRD.md` as the accepted showcase scope.
4. Accepted decisions in `GRILL_SESSION.md` / `DECISIONS.md` where higher authority leaves a choice open.
5. Feature `GLOSSARY.md` and focused contracts.

## Read Order

1. Root `AGENTS.md` and `NEXT.md`.
2. This file.
3. `PRD.md`.
4. `GLOSSARY.md`.
5. `features-cli progress --feature greek-essence-showcase --json`.
6. `GRILL_SESSION.md`, continuing from `## Next Question`.
7. Only the authoritative repository documents needed to resolve the active question.

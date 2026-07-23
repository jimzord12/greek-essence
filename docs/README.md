# Greek Essence Documentation

This directory is the entry point for the Greek Essence product, experience, technical, visual, and agent-tooling documentation.

Greek Essence is currently specified as a private, bilingual client-review prototype for a boutique Greece-focused travel-planning service. The prototype is intended to demonstrate the experience and validate the product direction before a production commercial release. It is not a booking engine, online travel agency, or production-ready lead-management system.

## Documentation map

| Area | Owns | Start here |
|---|---|---|
| Project protocol | Documentation governance, responsibilities, and conflict resolution | [`00_project_protocol/index.md`](00_project_protocol/index.md) |
| Product requirements | Product intent, audience, offer, scope, business rules, and MVP acceptance | [`01_prd/index.md`](01_prd/index.md) |
| Prototype specification | Information architecture, page composition, interactions, responsive behavior, and prototype flows | [`02_prototype_specification/index.md`](02_prototype_specification/index.md) |
| Technical design | Prototype architecture, stack, implementation boundaries, testing, deployment, and production gaps | [`03_technical_design/index.md`](03_technical_design/index.md) |
| Design system | Visual direction, tokens, components, imagery, accessibility, and visual QA | [`04_design/index.md`](04_design/index.md) |
| Agent skills and tooling | Approved repository-local agent guidance, browser tooling, installation, and maintenance | [`05_agent_skills/index.md`](05_agent_skills/index.md) |

## Authority and conflict resolution

Read decisions according to the following precedence:

1. Project Protocol
2. Product Requirements Document
3. Prototype Specification
4. Technical Design
5. Design System

The agent-skills documentation governs tooling and agent workflow only. It does not override product, UX, technical, design, quality, or release requirements owned by the documents above.

When two documents appear to conflict, follow the higher-ranked source and record the discrepancy. Do not silently reinterpret a higher-level requirement in a downstream document or implementation.

## Recommended reading paths

### Product or stakeholder review

1. [`01_prd/document_purpose_and_authority.md`](01_prd/document_purpose_and_authority.md)
2. [`01_prd/01_executive_summary.md`](01_prd/01_executive_summary.md)
3. [`01_prd/21_mvp_scope.md`](01_prd/21_mvp_scope.md)
4. [`01_prd/22_out_of_scope_for_mvp.md`](01_prd/22_out_of_scope_for_mvp.md)
5. [`01_prd/30_open_product_decisions.md`](01_prd/30_open_product_decisions.md)
6. [`01_prd/31_mvp_acceptance_criteria.md`](01_prd/31_mvp_acceptance_criteria.md)

### Design and prototype work

1. Read the product path above.
2. [`02_prototype_specification/document_purpose_and_authority.md`](02_prototype_specification/document_purpose_and_authority.md)
3. [`02_prototype_specification/07_page_specifications.md`](02_prototype_specification/07_page_specifications.md)
4. [`02_prototype_specification/09_custom_trip_form_interaction_specification.md`](02_prototype_specification/09_custom_trip_form_interaction_specification.md)
5. [`02_prototype_specification/13_prototype_flows_and_scenarios.md`](02_prototype_specification/13_prototype_flows_and_scenarios.md)
6. [`04_design/index.md`](04_design/index.md)

### Implementation work

1. Read the product and prototype sources relevant to the task.
2. [`03_technical_design/document_purpose_authority_and_scope.md`](03_technical_design/document_purpose_authority_and_scope.md)
3. [`03_technical_design/01_confirmed_technical_decisions.md`](03_technical_design/01_confirmed_technical_decisions.md)
4. [`03_technical_design/04_project_and_file_architecture.md`](03_technical_design/04_project_and_file_architecture.md)
5. [`03_technical_design/18_testing_and_quality_gates.md`](03_technical_design/18_testing_and_quality_gates.md)
6. [`03_technical_design/22_production_readiness_gap_register.md`](03_technical_design/22_production_readiness_gap_register.md)
7. [`03_technical_design/25_prototype_definition_of_done.md`](03_technical_design/25_prototype_definition_of_done.md)
8. Read the relevant Design System sections and the agent-tooling instructions before making changes.

## Current status

| Document family | Status |
|---|---|
| Project Protocol | Present |
| Product Requirements Document | Complete first draft; approvals pending |
| Prototype Specification | Complete first draft; approvals pending |
| Technical Design | Prototype-build design; implementation pending |
| Design System | Complete first draft; visual and product review pending |
| Agent skills and tooling | Bootstrap tooling complete; ongoing maintenance follows the approved baseline |
| Bilingual fixture scaffold | Complete |
| Product application | Not yet implemented |

The private prototype and the later production MVP have different readiness requirements. Bootstrap tooling and the bilingual fixture scaffold are complete, but product prototype implementation remains pending. A successful prototype review does not authorize public commercial launch. The unresolved production requirements remain recorded in the [production-readiness gap register](03_technical_design/22_production_readiness_gap_register.md).

## Development package manager

Use standalone pnpm `11.17.0` directly:

```bash
pnpm install --frozen-lockfile
pnpm dev
```

On Windows, install the repository-pinned version with the official PowerShell installer, then open a refreshed terminal:

```powershell
$env:PNPM_VERSION = "11.17.0"
irm https://get.pnpm.io/install.ps1 | iex
```

## Contributor rules

- Preserve one source of truth for each concern.
- Do not introduce implementation details into the PRD.
- Do not change product or UX requirements through implementation choices.
- Do not invent unresolved business, operational, legal, trust, pricing, or content facts.
- Treat provisional content and assets as provisional in code, reviews, and demonstrations.
- Record approved changes in the document that owns the decision and update affected traceability references.

Each documentation family has its own `index.md` for detailed navigation. Start there after selecting the relevant area from the map above.

## Active preparation workspace

The bootstrap-only execution plan, task briefs, work protocol, human-operator guide, review records, and progress ledger live in [`.scratch/bootstrap/README.md`](../.scratch/bootstrap/README.md). This workspace prepares the repository and quality tooling; it does not authorize product implementation.

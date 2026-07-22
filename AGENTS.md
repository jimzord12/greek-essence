# Greek Essence Agent Instructions

## Authority

Read [the documentation entry point](docs/README.md) and [the bootstrap workspace](.scratch/bootstrap/README.md) first. Project decisions take precedence in this order: Project Protocol, Product Requirements, Prototype Specification, Technical Design, then Design System. Agent-tooling documents govern tooling only; record and escalate conflicts rather than silently reinterpreting a higher-authority requirement.

## Architecture

Use `pnpm` through Corepack; follow the repository `packageManager` version when it exists and do not substitute another package manager. Keep TypeScript strict. Build a static-first Next.js App Router prototype: local, schema-validated JSON content renders public pages at build time; the form-submission Route Handler is the sole server-side dynamic boundary. Prefer Server Components and add Client Components only for necessary interaction and minimal JavaScript.

Support explicit English and Greek routes. Follow the modular [prototype specification](docs/02_prototype_specification/index.md) for UX, accessibility, responsiveness, content, and form behavior, and the modular [technical design](docs/03_technical_design/index.md), including [testing and quality gates](docs/03_technical_design/18_testing_and_quality_gates.md). Prefer simple, maintainable, battle-tested solutions.

Do not add or imply a database, CMS, CRM, analytics provider, booking, availability, payments, accounts, dashboards, itinerary management, dynamic inventory, price comparison, customer reviews, marketing automation, or another deferred production capability without explicit approval.

## Approved skills

Use only the repository-local skills approved in [the tooling baseline](docs/05_agent_skills/01_approved_tooling_baseline.md): Google Chrome Modern Web Guidance for modern-web implementation decisions; Vercel `vercel-react-best-practices` for React work; the official Playwright CLI Agent Skill for browser inspection; `greek-essence-quality-review` for structured quality reviews; `bootstrap-next` for one ordinary bootstrap task; and `ralph-loop-manager` for compatibility-gated, monitored use of the project-owned Ralph controller. For Next.js-specific work, consult the documentation bundled with the installed Next.js version under `next/dist/docs/` and its approved generated agent rules; do not install the retired `next-best-practices` skill. Guidance complements, and never replaces, required executable checks.

## Browser inspection

Use Playwright CLI as the only interactive browser interface. Do not install, configure, or use Playwright MCP, `agent-browser`, Browser Use/Browser Use CLI, or another overlapping browser-agent tool.

## Required checks

Run the task-required checks plus applicable repository commands: `pnpm lint`, `pnpm typecheck`, `pnpm validate:content`, `pnpm build`, and the required Playwright, accessibility, metadata, and quality checks. Record exact commands, exit codes, and results; do not claim checks that did not run.

## Definition of done

A change is done only when it meets the authoritative requirements; preserves static-first and locale boundaries; has focused, passing required checks; has no console errors or failed critical network requests; protects personal/client data from Git, logs, screenshots, previews, and analytics; uses only approved visible claims/assets; records known production gaps; and receives required review approval.

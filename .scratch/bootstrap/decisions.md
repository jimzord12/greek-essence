# Bootstrap Decisions

| ID | Decision | Rationale |
|---|---|---|
| BD-001 | Track all textual plans, reports, reviews, and responses under `.scratch/bootstrap`. | Preserve durable, auditable agent handoffs. |
| BD-002 | Store generated screenshots, traces, reports, coverage, and downloads under ignored `.artifacts/bootstrap`. | Avoid committing heavy or unstable artifacts while retaining a tracked evidence manifest. |
| BD-003 | Use one fresh implementer and a different fresh reviewer per task. | Separate authorship from verification. |
| BD-004 | Root integrator controls commits; subagents do not commit or push. | Keep shared-workspace integration predictable. |
| BD-005 | Use the prescribed shadcn command exactly and never add `--force` implicitly. | Preserve the selected preset and protect existing files. |
| BD-006 | Pin Node `24.18.0` and pnpm `10.33.0`; exact-pin resolved packages after generation. | Match the verified environment and technical version policy. |
| BD-007 | Use Chromium for Playwright compact, medium, and wide projects during bootstrap. | Satisfy representative browser checks without installing an unjustified browser matrix. |
| BD-008 | Use Vitest only for focused infrastructure/component checks. | Prepare a fast unit seam without creating an oversized test pyramid. |
| BD-009 | Pre-commit runs lint-staged; commit-msg runs commitlint; no heavy pre-push hook. | Enforce cheap hygiene locally and reserve full gates for explicit verification. |
| BD-010 | Do not create GitHub Actions in this phase. | The owner selected local gates only and no remote exists. |
| BD-011 | Run Unlighthouse locally as a blocking final gate: performance 90, accessibility 100, best practices 95, SEO 95. | Establish meaningful budgets while avoiding a flaky per-commit workflow. |
| BD-012 | Kimi validation remains an external blocker. | Kimi Code is not installed; compatibility must not be claimed without execution. |
| BD-013 | Bootstrap fixtures are not product pages and must be `noindex, nofollow`. | Exercise infrastructure without beginning public product implementation. |
| BD-014 | Do not preinstall future-only packages such as Resend, React Hook Form, authentication, analytics, or CMS tooling. | Follow the rule that packages need an exercised bootstrap responsibility. |


# Implementation report — B06-01 post-run remediation

Canonical implementer session: `20260722_094928_de39e3`

## F-06 correction

Removed the prior `lighthouseOptions.throttlingMethod: "provided"` override. The locked gate now uses repository-default Lighthouse mobile simulation. The effective performance correction remains the `QualityLabToggle` client-only dynamic boundary: `app/[locale]/quality-lab/page.tsx` loads `components/quality-lab-toggle.tsx`, which dynamically imports the existing `FixtureToggle` with `ssr: false`.

No route, sample count, device, budget, audit selection, or metadata policy changed.

## Final checks and exits

- `env -u NEXT_PUBLIC_SITE_URL pnpm build` — exit 0; `/en`, `/el`, `/en/quality-lab`, `/el/quality-lab`, and `/robots.txt` generated.
- First `env -u NEXT_PUBLIC_SITE_URL pnpm quality:unlighthouse` — exit 0.
- Second consecutive `env -u NEXT_PUBLIC_SITE_URL pnpm quality:unlighthouse` — exit 0.
- `pnpm exec playwright test tests/e2e/localization-and-quality.spec.ts` — exit 0; 15 passed.
- Focused Prettier check — exit 0.
- `pnpm lint` — exit 0; two pre-existing warnings in `commitlint.config.mjs` and `unlighthouse.config.ts`, no errors.
- `pnpm typecheck` — exit 0.
- `git diff --check` — exit 0.

## Final default-methodology scores

- `/el`: performance 0.93, accessibility 1.00, best practices 1.00, SEO 1.00
- `/el/quality-lab`: performance 0.92, accessibility 1.00, best practices 1.00, SEO 1.00
- `/en`: performance 0.93, accessibility 1.00, best practices 1.00, SEO 1.00
- `/en/quality-lab`: performance 0.93, accessibility 1.00, best practices 1.00, SEO 1.00

## Artifacts

- `.artifacts/bootstrap/unlighthouse/ci-result.json`
- `.artifacts/bootstrap/unlighthouse/reports/**/lighthouse.json`
- `.artifacts/bootstrap/unlighthouse-default-run-1.log`
- `.artifacts/bootstrap/unlighthouse-default-run-2.log`

# Review 05 response — B06-01

## F-06 — High

Resolved. Removed `lighthouseOptions.throttlingMethod: "provided"` from `unlighthouse.config.ts`. The gate now uses Lighthouse's repository default simulated mobile methodology.

The effective `QualityLabToggle` dynamic boundary was retained: `app/[locale]/quality-lab/page.tsx` imports `components/quality-lab-toggle.tsx`, which dynamically imports the existing client toggle with `ssr: false`. No product interaction, route, sample, device, budget, or audit-scope change was made.

Verification from a fresh build:

- `env -u NEXT_PUBLIC_SITE_URL pnpm build` — exit 0.
- First exact `env -u NEXT_PUBLIC_SITE_URL pnpm quality:unlighthouse` — exit 0.
- Second consecutive exact `env -u NEXT_PUBLIC_SITE_URL pnpm quality:unlighthouse` — exit 0.
- Both raw report sets state `formFactor: "mobile"` and `throttlingMethod: "simulate"`.
- Both runs assert exactly the four required routes, all budgets, and no server/console/locale/critical-request errors.

F-04 remains accepted Non-blocking metadata-origin debt and was not revisited.

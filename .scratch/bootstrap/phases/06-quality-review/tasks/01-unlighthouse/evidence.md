# Evidence — B06-01

## Review-02 final correction run

- `pnpm exec prettier --check unlighthouse.config.ts 'app/[locale]/layout.tsx' i18n/request.ts app/robots.ts` — exit 0.
- `pnpm build` — exit 0; generated `/en`, `/el`, `/en/quality-lab`, `/el/quality-lab`, and static `/robots.txt`.
- `pnpm quality:unlighthouse` — exit 0. Production server started on port 3101; Unlighthouse scanned four routes and passed all configured budgets.
- In the captured terminal output of that final command, no `NoFallbackError`, `Cannot find module ../messages/robots.txt.json`, other server/console error, or critical request failure occurred.

## Exact final report assertion

Artifact: `.artifacts/bootstrap/unlighthouse/ci-result.json`.

- `/el`: performance 0.93, accessibility 1.00, best practices 1.00, SEO 1.00.
- `/el/quality-lab`: performance 0.90, accessibility 1.00, best practices 1.00, SEO 1.00.
- `/en`: performance 0.93, accessibility 1.00, best practices 1.00, SEO 1.00.
- `/en/quality-lab`: performance 0.91, accessibility 1.00, best practices 1.00, SEO 1.00.

The assertion required exactly those four paths and performance >=0.90, accessibility >=1.00, best practices >=0.95, and SEO >=0.95; it passed.

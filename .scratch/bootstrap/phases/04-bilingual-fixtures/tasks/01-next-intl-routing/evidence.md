# Evidence

## Environment

- Hermes session: `20260722_065719_65864e`
- UTC start: `2026-07-22T03:57:44Z`

## Affected verification

| Command | Exit | Result |
|---|---:|---|
| `MSYS_NO_PATHCONV=1 corepack pnpm --version` | 1 | Git-Bash Corepack shim still resolved its script path as `C:\\c\\...`; no package operation used this failed shim. |
| `node -e 'process.argv=["node","corepack","pnpm","--version"]; require(String.raw\`C:\\Users\\jimzord12\\AppData\\Roaming\\fnm\\node-versions\\v24.18.0\\installation\\node_modules\\corepack\\dist\\corepack.js\`)'` | 0 | Installed Corepack entry point reported pnpm `10.33.0`. |
| `node -e 'process.argv=["node","corepack","pnpm","add","next-intl@4.13.3","--save-exact"]; require(String.raw\`C:\\Users\\jimzord12\\AppData\\Roaming\\fnm\\node-versions\\v24.18.0\\installation\\node_modules\\corepack\\dist\\corepack.js\`)'` | 0 | Re-ran the exact package operation through Corepack; package and lock were already current. |
| `node -e 'process.argv=["node","corepack","pnpm","install","--frozen-lockfile"]; require(String.raw\`C:\\Users\\jimzord12\\AppData\\Roaming\\fnm\\node-versions\\v24.18.0\\installation\\node_modules\\corepack\\dist\\corepack.js\`)'` | 0 | `Lockfile is up to date`; frozen installation completed using pnpm 10.33.0. |
| `rm -rf .next && pnpm build` | 0 | Route table: `● /[locale]`, generated `/en` and `/el`; build defines `●` as prerendered static HTML using `generateStaticParams`. |
| `pnpm lint && pnpm typecheck` | 0 | Passed; lint emitted only the pre-existing `commitlint.config.mjs` warning. |
| Production request assertion command below | 0 | `root-plain=307 root-accept-language-el=307 root-cookie-el=307 en=200 el=200 invalid=404`; all three root variants redirected to `/en`; locale language/link and 404 assertions passed. |

Production request assertion command:

```text
mkdir -p .artifacts/bootstrap/B04-01 && base='http://127.0.0.1:3100' && curl -sS -D .artifacts/bootstrap/B04-01/root-plain.headers -o .artifacts/bootstrap/B04-01/root-plain.html -w '%{http_code}\n' "$base/" > .artifacts/bootstrap/B04-01/root-plain.status && curl -sS -H 'Accept-Language: el' -D .artifacts/bootstrap/B04-01/root-accept-language-el.headers -o .artifacts/bootstrap/B04-01/root-accept-language-el.html -w '%{http_code}\n' "$base/" > .artifacts/bootstrap/B04-01/root-accept-language-el.status && curl -sS -H 'Cookie: NEXT_LOCALE=el' -D .artifacts/bootstrap/B04-01/root-cookie-el.headers -o .artifacts/bootstrap/B04-01/root-cookie-el.html -w '%{http_code}\n' "$base/" > .artifacts/bootstrap/B04-01/root-cookie-el.status && curl -sS -D .artifacts/bootstrap/B04-01/en.headers -o .artifacts/bootstrap/B04-01/en.html -w '%{http_code}\n' "$base/en" > .artifacts/bootstrap/B04-01/en.status && curl -sS -D .artifacts/bootstrap/B04-01/el.headers -o .artifacts/bootstrap/B04-01/el.html -w '%{http_code}\n' "$base/el" > .artifacts/bootstrap/B04-01/el.status && curl -sS -D .artifacts/bootstrap/B04-01/invalid.headers -o .artifacts/bootstrap/B04-01/invalid.html -w '%{http_code}\n' "$base/fr" > .artifacts/bootstrap/B04-01/invalid.status
```

Assertions checked each root status was `307` with `Location: /en`; `/en` and `/el` were `200` with their matching `lang` and alternate-locale link; `/fr` was `404`.

## Artifacts

Ignored artifacts: `.artifacts/bootstrap/B04-01/{root-plain,root-accept-language-el,root-cookie-el,en,el,invalid}.{headers,html,status}`.

Production server: `pnpm start --port 3100` (ready, then stopped after verification).

# B02-03 Review 01

Reviewer session: `20260722_052515_b199ab`

Verdict: Changes requested

## Findings

### 1. High — Required Corepack execution evidence is absent

- Exact location: `AGENTS.md:9`; `.scratch/bootstrap/phases/02-application-scaffold/tasks/03-normalize-application-skeleton/evidence.md:19-20,31-33`; `.scratch/bootstrap/phases/02-application-scaffold/tasks/03-normalize-application-skeleton/implementation-report.md:25-26`.
- Violated requirement: root `AGENTS.md` requires pnpm to be used through Corepack. The task acceptance requires passing development startup and production build evidence. The protocol permits a replacement verification only as a recorded, owner-approved deviation.
- Evidence/reproduction: the only recorded Corepack command, `corepack pnpm install --frozen-lockfile`, exited 1. Installation, development startup, and build were then run with direct `pnpm`; no approved deviation is recorded. Therefore the recorded pass does not establish execution through the required package-manager path.
- Required correction: have the root integrator resolve the Corepack prerequisite or obtain and record the protocol-required deviation, then rerun the frozen install, development smoke, and production build using the approved path and update the implementation evidence/report.
- Verification: confirm the replacement evidence records exact successful commands and exit codes for frozen install, `dev` HTTP smoke, and `build`, all through Corepack unless an approved deviation explicitly names the rule, reason, impact, owner, and replacement verification.

### 2. High — The locked older-version codemod command was substituted

- Exact location: `.scratch/bootstrap/phases/02-application-scaffold/tasks/03-normalize-application-skeleton/task.md:29`; `docs/05_agent_skills/07_nextjs_version_matched_agent_guidance.md:31-37`; `.scratch/bootstrap/phases/02-application-scaffold/tasks/03-normalize-application-skeleton/evidence.md:18,21-25`.
- Violated requirement: for supported Next.js versions older than 16.3, the locked task and version-matched guidance require running `npx @next/codemod@canary agents-md` in isolation and inspecting its changes.
- Evidence/reproduction: Next.js is pinned to 16.2.6, but the evidence records only `pnpm dlx @next/codemod@canary agents-md ...`; it does not record the required `npx` invocation or an approved deviation. The generated artifact is valid-looking but does not prove the mandated command path ran.
- Required correction: run the required canary `npx ... agents-md` command in isolation, inspect its generated result, and replace the setup evidence with the exact command, exit code, generated path, and validation result; preserve root `AGENTS.md` unchanged.
- Verification: confirm the recorded `npx @next/codemod@canary agents-md ...` exits 0, its generated rule points to `./node_modules/next/dist/docs`, `.agents/skills/next-best-practices/` remains absent, and `git diff --exit-code -- AGENTS.md` exits 0.

## Reviewer verification

- `pnpm build` (first stage of the combined review command): exit 0; Next.js 16.2.6 compiled, type-checked, and statically generated `/` and `/_not-found`.
- Corrected structural check covering root `app/`, absent `src/app` and `next-app`, bundled `next/dist/docs`, absent retired skill, `@/*` root alias, pinned Next.js 16.2.6, ignored generated rule artifact, unchanged root `AGENTS.md`, and `git diff --check`: exit 0.
- `pnpm dev --port 3102`: ready in 394 ms. Playwright CLI inspection at `http://localhost:3102/` observed one empty `<main>`, `lang="en"`, HTTP 200, and zero console errors or warnings. The scaffold contains no localized product UI, so a second locale inspection is not applicable to this task.
- The first browser probe used `127.0.0.1`; Next.js correctly blocked cross-origin HMR from that origin and logged the resulting WebSocket error. Repeating the probe at the server-advertised `localhost` origin passed cleanly; this was a reviewer probe-origin issue, not a finding.

No advisory findings were recorded.

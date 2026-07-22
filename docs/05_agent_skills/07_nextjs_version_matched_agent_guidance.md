## 7. Next.js Version-Matched Agent Guidance

### 7.1 Purpose

Provide framework-specific guidance for correct and maintainable Next.js App Router implementation without vendoring stale reference knowledge as a repository-local skill.

### 7.2 What it provides

Use the documentation bundled with the installed Next.js version for:

- App Router conventions;
- route and layout organization;
- Server and Client Component boundaries;
- metadata and framework APIs;
- rendering and data patterns;
- file conventions;
- common Next.js implementation mistakes.

### 7.3 Official sources

- Migration notice: `https://github.com/vercel-labs/next-skills`
- Version-matched framework source: `https://github.com/vercel/next.js`
- Current installable workflow skills: `https://github.com/vercel/next.js/tree/canary/skills`

The former `next-best-practices` reference skill was removed. It has no replacement skill name. Its knowledge is now delivered through the documentation bundled under `next/dist/docs/` and through project agent rules generated for the installed Next.js version.

### 7.4 Setup

Do not install or vendor `next-best-practices`, and do not substitute a similarly named third-party or legacy skill.

After the application scaffold resolves and pins Next.js:

1. inspect the installed Next.js version and its bundled `next/dist/docs/`;
2. for Next.js 16.3 or later, run `next dev` and verify the generated `AGENTS.md` / `CLAUDE.md` integration described by the official migration notice;
3. for an older supported Next.js version, run `npx @next/codemod@canary agents-md` in isolation, inspect its changes, and retain only the version-matched documentation/rules required by the repository;
4. keep the root project `AGENTS.md` authoritative over generated framework guidance;
5. record the resolved Next.js version, setup command, generated paths, and validation result in the bootstrap evidence for the scaffold task.

This setup belongs with the application scaffold because no version-matched Next.js documentation exists before the package is installed.

### 7.5 Validation

Confirm that:

- `.agents/skills/next-best-practices/` is absent;
- agents are directed to the installed version's `next/dist/docs/` for Next.js-specific decisions;
- generated agent rules, when applicable, point to version-matched local documentation;
- no obsolete legacy skill or unrelated Next.js workflow skill was installed;
- the application still passes its required executable checks.

Use a controlled prompt such as:

> Review this App Router implementation for file conventions, routing, metadata, Server and Client Component boundaries, and Next.js-specific mistakes. Use the documentation bundled with the repository's installed Next.js version.

### 7.6 Agent usage

Agents should consult the installed version-matched Next.js documentation when:

- creating or revising App Router routes and layouts;
- deciding Server versus Client Component boundaries;
- using Next.js metadata, navigation, rendering, or routing APIs;
- reviewing framework-specific correctness;
- diagnosing Next.js build or runtime behavior.

The architecture itself remains governed by `03_TECHNICAL_DESIGN.md`.

---

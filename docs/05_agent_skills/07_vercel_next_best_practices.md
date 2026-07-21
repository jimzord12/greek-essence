## 7. Vercel `next-best-practices`

### 7.1 Purpose

Provide framework-specific guidance for correct and maintainable Next.js App Router implementation.

### 7.2 What it provides

Use it for:

- App Router conventions;
- route and layout organization;
- Server and Client Component boundaries;
- metadata and framework APIs;
- rendering and data patterns;
- file conventions;
- common Next.js implementation mistakes.

### 7.3 Official sources

- Documentation: `https://vercel.com/docs/agent-resources/skills`
- Repository: `https://github.com/vercel-labs/agent-skills`

### 7.4 Installation

Inspect current official documentation and the installer help before running it.

The expected Skills CLI form is:

```bash
npx skills add vercel-labs/agent-skills --skill next-best-practices
```

The final repository directory must be:

```text
.agents/skills/next-best-practices/
```

If the installer writes to an agent-specific or unrelated location:

1. stage the installation in an isolated directory or branch;
2. inspect the installed `SKILL.md`, scripts, and references;
3. copy only the approved skill and required files;
4. preserve license and attribution requirements;
5. remove unrelated generated configuration;
6. record the exact upstream revision.

Do not install the complete Vercel skill collection or the Vercel plugin bundle.

### 7.5 Version recording

Record in `.agents/README.md`:

- upstream repository;
- exact upstream source path;
- exact commit SHA or release;
- installation date and command;
- verified license;
- local modifications, if any.

### 7.6 Validation

Confirm discovery or explicit loading in Codex CLI and Kimi Code.

Use a controlled prompt such as:

> Review this App Router implementation for file conventions, routing, metadata, Server and Client Component boundaries, and Next.js-specific mistakes. Apply the repository-local `next-best-practices` skill.

### 7.7 Agent usage

Agents should apply this skill when:

- creating or revising App Router routes and layouts;
- deciding Server versus Client Component boundaries;
- using Next.js metadata, navigation, rendering, or routing APIs;
- reviewing framework-specific correctness;
- diagnosing Next.js build or runtime behavior.

The architecture itself remains governed by `03_TECHNICAL_DESIGN.md`.

---


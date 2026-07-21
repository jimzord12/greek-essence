## 8. Vercel `vercel-react-best-practices`

### 8.1 Purpose

Provide React-focused guidance for rendering efficiency, reduced client work, bundle discipline, and maintainable component behavior.

### 8.2 What it provides

Use it for:

- unnecessary client rendering;
- avoidable waterfalls;
- component and rendering patterns;
- bundle impact;
- state and effect misuse;
- performance-sensitive React decisions;
- React and Next.js application-performance review.

### 8.3 Official sources

- Documentation: `https://vercel.com/docs/agent-resources/skills`
- Repository: `https://github.com/vercel-labs/agent-skills`

### 8.4 Installation

Inspect current official documentation and installer help.

The expected Skills CLI form is:

```bash
npx skills add vercel-labs/agent-skills --skill vercel-react-best-practices
```

The final repository directory must be:

```text
.agents/skills/vercel-react-best-practices/
```

Use the same staging, inspection, license-preservation, normalization, and revision-recording procedure defined for `next-best-practices`.

Do not install the complete Vercel collection.

### 8.5 Version recording

Record in `.agents/README.md`:

- upstream repository;
- exact upstream source path;
- exact commit SHA or release;
- installation date and command;
- verified license;
- local modifications, if any.

### 8.6 Validation

Confirm discovery or explicit loading in both supported agents.

Use a controlled prompt such as:

> Review this component tree for unnecessary client rendering, avoidable waterfalls, bundle impact, state/effect misuse, and React performance risks. Apply the repository-local Vercel React best-practices skill.

### 8.7 Agent usage

Agents should apply this skill when:

- creating or reviewing interactive React components;
- adding client-side state or effects;
- investigating rendering or bundle problems;
- optimizing component boundaries;
- reviewing React performance without changing approved UX behavior.

---


## 6. Google Chrome Modern Web Guidance

### 6.1 Purpose

Provide current browser-platform guidance for modern, interoperable, accessible, secure, and maintainable web implementation.

### 6.2 What it provides

Use it for guidance on:

- semantic HTML;
- native form behavior;
- modern CSS;
- accessibility fundamentals;
- browser APIs;
- Baseline support and fallbacks;
- performance-sensitive platform features;
- privacy and security considerations;
- cross-browser compatibility.

It complements, rather than replaces, Next.js- and React-specific skills.

### 6.3 Official sources

- Documentation: `https://developer.chrome.com/docs/modern-web-guidance`
- Repository: `https://github.com/GoogleChrome/modern-web-guidance`

### 6.4 Installation

First inspect the current official installation documentation and command help.

The expected installer form at the time of this decision is:

```bash
npx modern-web-guidance@latest install
```

Install only the core Modern Web Guidance skill needed for normal web application work.

Do not install optional disciplines such as Chrome extensions, passkeys, or WebMCP unless a later project decision explicitly requires them.

If the installer cannot write directly to `.agents/skills/modern-web-guidance/`:

1. run it in an isolated temporary directory or branch;
2. inspect all generated files;
3. copy only the approved skill and required references;
4. preserve required license and attribution files;
5. normalize the final directory to `.agents/skills/modern-web-guidance/`;
6. remove temporary and unrelated generated files.

### 6.5 Version recording

Record in `.agents/README.md`:

- upstream repository;
- exact release or commit SHA;
- exact installation command;
- installation date;
- verified license;
- included skill or disciplines;
- excluded optional disciplines;
- local modifications, if any.

### 6.6 Validation

Confirm that both Codex CLI and Kimi Code can identify or explicitly read the local skill.

Use a controlled prompt such as:

> Review this implementation for modern web-platform practices, semantic HTML, native form behavior, accessibility, and cross-browser compatibility. Apply the repository-local Modern Web Guidance skill.

The result must demonstrate use of the repository-local skill rather than relying only on general model knowledge.

### 6.7 Agent usage

Agents should apply this skill when:

- choosing between native platform features and custom JavaScript;
- implementing forms and controls;
- using modern CSS or browser APIs;
- reviewing compatibility and fallback requirements;
- reviewing platform-level accessibility, privacy, security, or performance concerns.

Project-specific UX and implementation decisions still come from `02_PROTOTYPE_SPECIFICATION.md` and `03_TECHNICAL_DESIGN.md`.

---


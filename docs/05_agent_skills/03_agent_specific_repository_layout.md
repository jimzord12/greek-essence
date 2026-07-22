## 3. Agent-Specific Repository Layout

This document defines only the repository area it owns.

The application and overall repository structure remain governed by `03_TECHNICAL_DESIGN.md`, especially **§4 — Project and File Architecture**. The tooling installation must respect that structure and must not reorganize unrelated project files.

Use the following agent-specific layout unless an already-established compatible convention exists:

```text
/
├── AGENTS.md
└── .agents/
    ├── README.md
    └── skills/
        ├── modern-web-guidance/
        │   ├── SKILL.md
        │   └── ...required upstream files
        ├── vercel-react-best-practices/
        │   ├── SKILL.md
        │   └── ...required upstream files
        ├── playwright-cli/
        │   ├── SKILL.md
        │   └── ...required generated files
        └── greek-essence-quality-review/
            ├── SKILL.md
            └── references/
                ├── visual-review-checklist.md
                ├── responsive-review-checklist.md
                ├── accessibility-review-checklist.md
                ├── seo-localization-review-checklist.md
                └── form-quality-security-review-checklist.md
```

### 3.1 Placement rules

- Every skill must be a direct child of `.agents/skills/`.
- Every skill directory must contain a `SKILL.md` at its root.
- Supporting files referenced by `SKILL.md` must remain available at stable relative paths.
- Do not copy third-party `AGENTS.md` files into the repository root.
- Do not commit duplicate copies of the same skill for every supported agent unless a tool cannot operate through a shared canonical copy.
- The root `AGENTS.md` remains authoritative over any third-party skill instruction.
- Third-party skills may guide implementation but may not override `00_PROJECT_PROTOCOL.md`, `01_PRODUCT_REQUIREMENTS.md`, `02_PROTOTYPE_SPECIFICATION.md`, `03_TECHNICAL_DESIGN.md`, or this document.
- Next.js reference knowledge is not a repository-local skill. Use the installed package's version-matched `next/dist/docs/` and approved generated agent rules; `.agents/skills/next-best-practices/` must remain absent.

---


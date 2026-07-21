## 14. Updating Skills

Do not automatically track upstream `main`.

For every update:

1. record the currently installed revision;
2. identify the proposed revision;
3. inspect the full upstream diff;
4. review license changes;
5. inspect new scripts, commands, hooks, or network behavior;
6. verify that optional disciplines were not silently added;
7. regenerate or reinstall in an isolated location;
8. inspect the repository diff;
9. test Codex CLI discovery;
10. test Kimi Code discovery;
11. run controlled usage prompts;
12. update `.agents/README.md`;
13. commit skill updates separately from unrelated application changes where practical.

### 14.1 Playwright CLI skill updates

When Playwright CLI is updated, regenerate its official skill using the currently documented command, expected to be:

```bash
playwright-cli install --skills
```

Review the generated diff before committing.

### 14.2 Google Modern Web Guidance updates

Modern Web Guidance may evolve rapidly. Review updates intentionally and confirm that no unrelated optional discipline has been added.

### 14.3 Local skill updates

Changes to `greek-essence-quality-review` must remain traceable to a project requirement, observed recurring defect, or approved review improvement. It must not become a second copy of the PRD, Prototype Specification, or Technical Design.

---


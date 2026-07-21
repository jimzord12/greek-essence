## 11. Cross-Agent Compatibility

### 11.1 Supported agents

The repository is intended for:

- OpenAI Codex through Codex CLI;
- Kimi Code.

### 11.2 Compatibility requirements

- All canonical skills must remain ordinary, version-controlled repository files.
- `SKILL.md` must remain readable even when automatic skill discovery differs between agent versions.
- `AGENTS.md` must remain concise and agent-neutral.
- Agent-specific wrappers may point to canonical skills but must not fork their content.
- Installation is not considered complete until both agents can identify or explicitly load every approved skill.
- Material incompatibility must be reported rather than hidden through an undocumented substitute.

### 11.3 Discovery validation

For each skill, record:

- Codex CLI discovery or explicit-load result;
- Kimi Code discovery or explicit-load result;
- exact validation prompt;
- any required wrapper or configuration;
- unresolved compatibility issue.

Store this information in `.agents/README.md` or an adjacent concise validation record.

---


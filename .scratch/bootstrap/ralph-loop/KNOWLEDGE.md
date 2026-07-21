# Bootstrap Knowledge

Record only reviewed, durable, non-obvious discoveries that future tasks would otherwise need to rediscover. Normal progress belongs in task reports and [HANDOFF.md](HANDOFF.md).

## K-001 — Codex Windows automation sandbox

- Discovered during: B00-02 automation preparation
- Observation: Windows Codex Desktop automation rejected `danger-full-access` before `apply_patch` could write files.
- Working configuration: `sandbox_mode = "workspace-write"`, `approval_policy = "never"`, and `[windows].sandbox = "unelevated"`.
- Consequence: unattended runs use `workspace-write` until the upstream Windows automation issue is verified fixed.
- Applies to: all automated Codex bootstrap tasks.

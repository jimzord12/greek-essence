# Bootstrap Knowledge

Record only reviewed, durable, non-obvious discoveries that future tasks would otherwise need to rediscover. Normal progress belongs in task reports and [HANDOFF.md](HANDOFF.md).

## K-001 — Hermes harness avoids the Codex Windows automation sandbox

- Discovered during: B00-02 automation preparation
- Observation: Windows `workspace-write` with the unelevated restricted-token backend rejects `apply_patch` when the runtime supplies split writable roots. The elevated backend requires interactive UAC setup and cannot run unattended here.
- Working configuration: Ralph invokes non-interactive, resumable Hermes profile sessions with `--yolo`; Hermes uses native file/terminal tools rather than the Codex CLI sandbox.
- Consequence: repository safety instructions, task scope, deterministic checks, and the no-push/no-deploy/no-history-rewrite boundaries remain the safety layer.
- Applies to: all automated Hermes bootstrap work units.

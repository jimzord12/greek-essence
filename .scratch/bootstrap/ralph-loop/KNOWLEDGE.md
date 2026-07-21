# Bootstrap Knowledge

Record only reviewed, durable, non-obvious discoveries that future tasks would otherwise need to rediscover. Normal progress belongs in task reports and [HANDOFF.md](HANDOFF.md).

## K-001 — Codex Windows automation sandbox

- Discovered during: B00-02 automation preparation
- Observation: Windows `workspace-write` with the unelevated restricted-token backend rejects `apply_patch` when the runtime supplies split writable roots. The elevated backend requires interactive UAC setup and cannot run unattended here.
- Working configuration: Ralph invokes Codex CLI with `danger-full-access` and `approval_policy = "never"` under explicit operator authorization. This is a CLI-specific workaround, not a recommendation for Codex Desktop automations.
- Consequence: repository safety instructions, task scope, deterministic checks, and the no-push/no-deploy/no-history-rewrite boundaries remain the safety layer until the upstream Windows sandbox issue is fixed.
- Applies to: all automated Codex bootstrap tasks.

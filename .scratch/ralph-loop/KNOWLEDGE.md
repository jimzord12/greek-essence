# Bootstrap Knowledge

Record only reviewed, durable, non-obvious discoveries that future Ralph contexts would otherwise need to rediscover. Normal progress belongs in task records and [HANDOFF.md](HANDOFF.md).

## K-001 — Hermes harness avoids the Codex Windows automation sandbox

- Discovered during: B00-02 automation preparation
- Observation: Windows `workspace-write` with the unelevated restricted-token backend rejects `apply_patch` when the runtime supplies split writable roots. The elevated backend requires interactive UAC setup and cannot run unattended here.
- Working configuration: Ralph invokes non-interactive, fresh Hermes profile sessions with `--yolo`; Hermes uses native file/terminal tools rather than the Codex CLI sandbox.
- Consequence: repository safety instructions, task scope, deterministic checks, and the no-push/no-deploy/no-history-rewrite boundaries remain the safety layer.
- Applies to: all automated Hermes bootstrap work units.

## K-002 — Open: controller can leave an orphaned Hermes root after abrupt termination

- Status: Open; deferred by the operator on 2026-07-22.
- Discovered during: B07-01 managed launch.
- Observation: controller PID `44988` disappeared before its Python cleanup completed, while its owned Hermes root PID `33596` and descendants remained alive. The stale runtime lock still named the dead controller, `controller-state.json` still named the live root, and the tracked wrapper reported exit `0` despite no task progress. The exact external termination cause was not proven.
- Recovery performed: after explicit operator authorization, terminate only the verified B07-01 root process tree, confirm PID `33596` exited, and archive rather than overwrite the stale lock and controller state under `%LOCALAPPDATA%\hermes\ralph\greek-essence\`.
- Desired future enhancement: before every graceful controller exit, verify that its owned root and descendants have exited, terminate them when necessary, and fail closed if cleanup cannot be proven. For abrupt controller death on Windows, evaluate assigning the owned root tree to a Job Object with `JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE`; also add stale-lock/root recovery and lifecycle tests.
- Until resolved: treat a dead lock owner plus a live recorded root as `AMBIGUOUS_SURVIVING_ROOT_PROCESS`; never launch a concurrent controller or automatically kill an unverified process tree.

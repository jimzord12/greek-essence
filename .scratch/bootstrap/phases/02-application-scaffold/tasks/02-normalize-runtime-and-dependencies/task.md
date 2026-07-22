---
id: B02-02
status: Done
depends_on: [B02-01]
implementer_agent: 20260722_050711_f1cc1c
reviewer_agent: 20260722_051137_cbd63e
started_at: 2026-07-22T02:08:35Z
completed_at: 2026-07-22T02:13:39Z
---

# Normalize runtimes and dependencies

## What

Pin the verified runtime/toolchain and every generated direct dependency.

## Why

`latest` resolves the starting point, but reproducibility requires exact recorded versions and a lockfile.

## How

- Pin Node `24.18.0`, set `engines.node` to `>=24 <25`, set `packageManager` to `pnpm@10.33.0`, and set `engines.pnpm` to `>=10 <11`.
- Require exact saves and commit `pnpm-lock.yaml`.
- Confirm stable TypeScript 6, Next.js App Router, React, Tailwind v4, and preset-selected Base UI/shadcn packages.
- Do not add future-only product dependencies.

## Required reading

- `docs/03_technical_design/03_technology_stack_and_version_policy.md`
- `docs/03_technical_design/04_project_and_file_architecture.md`

## Bootstrap verification contract

Apply verification row B02-02 and all relevant locked defaults from [the Bootstrap Verification Matrix](../../../../verification-matrix.md). Record exact commands, exit codes, and artifact paths in evidence.md.

## Acceptance

Runtime and direct-package versions match the locked policy, the lockfile is committed, and frozen installation succeeds.

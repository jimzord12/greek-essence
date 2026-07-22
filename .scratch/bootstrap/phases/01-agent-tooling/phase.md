# Phase 01 — Repository Governance and AI Tooling

## Goal

Install the locked repository-local agent baseline safely and document provenance before application generation.

## Tasks

1. [B01-01 — Repository guidance](tasks/01-repository-guidance/task.md)
2. [B01-02 — Modern Web Guidance](tasks/02-modern-web-guidance/task.md)
3. [B01-03 — Next.js version-matched agent guidance](tasks/03-next-best-practices/task.md)
4. [B01-04 — React skill](tasks/04-react-best-practices/task.md)
5. [B01-05 — Playwright CLI skill](tasks/05-playwright-cli/task.md)
6. [B01-06 — Project reviewer skill](tasks/06-quality-review-skill/task.md)
7. [B01-07 — Provenance and discovery](tasks/07-provenance-and-discovery/task.md)

## Exit gate

All four approved repository-local skills exist; the retired Next.js reference skill and prohibited alternatives are absent; provenance is complete; and Codex validation passes. Kimi remains explicitly blocked. B02-03 explicitly owns the later installed-version Next.js runtime handoff: inspect `next/dist/docs/`, validate the applicable generated-rule path, preserve root `AGENTS.md` authority, and record exact runtime evidence after Next.js is pinned.


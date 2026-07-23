# Greek Essence Ralph Loop

Ralph is a project-level context-refresh loop. It starts a fresh `greekroot` Sol session for each false completion check and stops only when `.scratch/ralph-loop/completion-signal.json` contains exactly `{ "isEverythingDone": true }`.

## Entry points

Every fresh root session starts by reading exactly these three Ralph files:

1. [RALPH_LOOP.md](RALPH_LOOP.md)
2. [HANDOFF.md](HANDOFF.md)
3. [KNOWLEDGE.md](KNOWLEDGE.md)

The root `AGENTS.md` is injected by Hermes. Sol inspects the rest of the repository and its structured work files itself; Python does not parse tasks, phases, reviews, Git completion, or model-emitted control signals.

## Canonical commands

Run these from the repository root:

```bash
# Read-only validation and intended command; does not launch Hermes or mutate files.
python .scratch/ralph-loop/tools/ralph_loop.py --dry-run

# Live AI execution until the completion signal is true or an operational failure occurs.
python .scratch/ralph-loop/tools/ralph_loop.py

# Bounded live AI execution; exits with LIMIT_REACHED after two false iterations.
python .scratch/ralph-loop/tools/ralph_loop.py --max-iterations 2

# Explicit live smoke test; the wrapper fixes the same canonical controller at two iterations.
# Run this only when smoke-test execution was explicitly requested.
python .scratch/ralph-loop/tools/smoke_test.py

# Hermetic full unit suite; never launches a live Hermes process.
python -B -m unittest discover -s .scratch/ralph-loop/tests -p "test_*.py" -v
```

The default live entrypoint is always `ralph_loop.py`. Generic requests to test, check, verify, try, run, resume, or monitor Ralph do not select `smoke_test.py`; the operator must explicitly request the smoke test or name that file. The smoke wrapper launches real Hermes agents and is not a unit-test command.

`--iteration-timeout SECONDS` bounds the current lease (default 3600 seconds), `--assessment-threshold SECONDS` selects the Diagnosis A Check point (default 2700 seconds), and `--assessor-timeout SECONDS` bounds each Diagnosis A or Diagnosis B Check (default 1200 seconds / 20 minutes). Pass `--campaign-id`, `--task-id`, and `--resolved-tier` for managed execution. A strict Diagnosis A `true` may renew the lease at most three times per task. After timeout, strict read-only Diagnosis B may authorize one same-task retry, gated by fresh manager preflight. Both checks use bounded evidence-first prompts and stop once decisive evidence is clear. Their stdout is reserved for exactly one JSON object; session-ID trailers are disabled because they invalidate the strict response contract. Runtime state, locks, assessor/diagnosis transcripts, and event logs remain outside Git at `%LOCALAPPDATA%\hermes\ralph\greek-essence\`. On Windows, timeout cleanup targets only the launched root PID and its descendants with `taskkill /T`; ambiguous survivors fail closed.

To begin a new managed campaign after successful completion, a human must explicitly edit `completion-signal.json` from `true` to `false`. The controller never resets it.

## Root orchestration contract

Sol/high-level orchestration must:

- read `HANDOFF.md` and `KNOWLEDGE.md` before choosing work;
- inspect repository reality and structured task, review, evidence, and phase files itself;
- select or resume the highest-priority coherent work unit and leave a precise handoff when the context ends;
- delegate substantial implementation to fresh `greekimpl` (`gpt-5.6-luna`, high) and independent review to fresh `greekreview` (`gpt-5.6-terra`, high) profile sessions;
- give children standalone, scoped prompts and request compact summaries containing verdict, findings, changed files, commands/results, and next action;
- require every `greekimpl` child that changes implementation or configuration to run the canonical `pnpm check:all` aggregate gate before stopping; it must not hand work to review unless that command exits zero, and an out-of-scope gate failure must be reported as a blocker rather than hidden or broadened into unrelated work;
- verify filesystem output and real command results rather than trusting child prose;
- preserve unrelated work and existing safety authority;
- update `HANDOFF.md` before ending every iteration and add only durable, reviewed discoveries to `KNOWLEDGE.md`;
- set `isEverythingDone` to `true` only after all managed work and final quality gates succeed.

The three profiles are pinned to `openai-codex` and this repository as their working directory:

| Role | Profile | Model | Reasoning |
|---|---|---|---|
| Root orchestrator | `greekroot` | `gpt-5.6-sol` | low |
| Substantial implementer | `greekimpl` | `gpt-5.6-luna` | high |
| Independent reviewer | `greekreview` | `gpt-5.6-terra` | high |

## Simple-fix policy

After Terra reviews a substantial Luna implementation, Sol may apply a correction directly only when every condition holds:

- the finding is mechanical and unambiguous;
- it is localized to one or two files;
- it changes no architecture, dependency, security/privacy behavior, schema, migration, or broad behavior;
- existing relevant quality gates objectively prove acceptance;
- it does not expand beyond the reviewer's cited finding.

Typos, stale metadata, and a small assertion/config correction can be simple. Architecture, dependency, security, broad test redesign, and unclear failures are not. Sol must run every relevant gate cited by the task or review. If all pass, Sol may close without another Terra review. If a gate fails, scope expands, or uncertainty appears, Sol stops self-fixing and delegates the failed state to Terra; Terra may direct substantial corrective implementation back to Luna. Terra's independent review remains required for the original substantial Luna implementation.

## Operational outcomes

Semantic completion is only the Boolean signal. Operational outcomes are reported separately:

- `COMPLETE`: signal was true before a new launch.
- `LIMIT_REACHED`: the iteration bound was reached while the signal remained false.
- `HERMES_FAILED`: a root process exited nonzero; the event-log path is reported.
- `TIMEOUT`: a root process was terminated after its iteration timeout; the event-log path is reported.
- `INVALID_SIGNAL`: the signal is missing, unreadable, malformed, has the wrong schema, or contains a non-Boolean value.
- `LOCK_CONFLICT`: another loop owns the runtime lock.
- `INTERRUPTED`/`ERROR`: the controller stopped safely and released operational resources.

The controller retains only operational safeguards: one-process locking with stale-lock recovery, bounded iterations, per-iteration timeout, child cleanup, event logs, nonzero-exit handling, and lock release on interruption or exception. It performs no project-state inference, session discovery, session resumption, task counting, repair attempts, or textual completion handling.

## Safety boundary

Task-owned repository-local edits, overwrites, and deletions explicitly required by the active contract or accepted review findings are authorized. Stop for out-of-repository changes, unrelated deletion, credentials, system changes, pushes, deployments, remotes, or Git history rewriting.

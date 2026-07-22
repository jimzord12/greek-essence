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

# Hermetic unit tests; never launch a live Hermes process.
python -B -m unittest discover -s .scratch/ralph-loop/tests -p "test_ralph_loop.py" -v
```

`--iteration-timeout SECONDS` bounds each live root process. Runtime locks and event logs remain outside Git at `%LOCALAPPDATA%\hermes\ralph\greek-essence\`.

To begin a new managed campaign after successful completion, a human must explicitly edit `completion-signal.json` from `true` to `false`. The controller never resets it.

## Root orchestration contract

Sol/high-level orchestration must:

- read `HANDOFF.md` and `KNOWLEDGE.md` before choosing work;
- inspect repository reality and structured task, review, evidence, and phase files itself;
- select or resume the highest-priority coherent work unit and leave a precise handoff when the context ends;
- delegate substantial implementation to fresh `greekimpl` (`gpt-5.6-luna`, high) and independent review to fresh `greekreview` (`gpt-5.6-terra`, high) profile sessions;
- give children standalone, scoped prompts and request compact summaries containing verdict, findings, changed files, commands/results, and next action;
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

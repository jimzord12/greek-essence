# Hermes Ralph Profiles

These tracked SOUL templates make the external Hermes profile setup reproducible. Profiles are reusable context shells; the root contract and child prompt define authority.

| Role | Profile | Model | Provider | Reasoning | Template |
|---|---|---|---|---|---|
| Root orchestrator | `greekroot` | `gpt-5.6-sol` | `openai-codex` | low | [greekroot-SOUL.md](greekroot-SOUL.md) |
| Substantial implementer | `greekimpl` | `gpt-5.6-luna` | `openai-codex` | high | [greekimpl-SOUL.md](greekimpl-SOUL.md) |
| Independent reviewer | `greekreview` | `gpt-5.6-terra` | `openai-codex` | high | [greekreview-SOUL.md](greekreview-SOUL.md) |

The live profiles are stored outside Git under `%LOCALAPPDATA%\hermes\profiles\<name>\`. All three use `C:/Users/jimzord12/Documents/GitHub/greek-essence` as `terminal.cwd`.

The installed Hermes CLI uses these validated commands when a profile needs pinning:

```bash
hermes -p greekroot config set model.default gpt-5.6-sol
hermes -p greekroot config set model.provider openai-codex
hermes -p greekroot config set model.reasoning_effort low
hermes -p greekroot config set agent.reasoning_effort low
hermes -p greekroot config set terminal.cwd C:/Users/jimzord12/Documents/GitHub/greek-essence

hermes -p greekimpl config set model.default gpt-5.6-luna
hermes -p greekimpl config set model.provider openai-codex
hermes -p greekimpl config set model.reasoning_effort high
hermes -p greekimpl config set agent.reasoning_effort high
hermes -p greekimpl config set terminal.cwd C:/Users/jimzord12/Documents/GitHub/greek-essence

hermes -p greekreview config set model.default gpt-5.6-terra
hermes -p greekreview config set model.provider openai-codex
hermes -p greekreview config set model.reasoning_effort high
hermes -p greekreview config set agent.reasoning_effort high
hermes -p greekreview config set terminal.cwd C:/Users/jimzord12/Documents/GitHub/greek-essence
```

The live profiles were already pinned to these values before this refactor; no credentials or profile data outside the approved config keys are changed by the repository migration.

Verify before an unattended run:

```bash
hermes profile show greekroot
hermes profile show greekimpl
hermes profile show greekreview
```

# Hermes Ralph Profiles

These tracked SOUL templates make the external Hermes profile setup reproducible. Profiles are reusable context shells; the active repository task or phase gate defines authority.

| Profile | Model | Provider | Reasoning | Template |
|---|---|---|---|---|
| `greekroot` | `gpt-5.6-sol` | `openai-codex` | high | [greekroot-SOUL.md](greekroot-SOUL.md) |
| `greekimpl` | `gpt-5.6-terra` | `openai-codex` | medium | [greekimpl-SOUL.md](greekimpl-SOUL.md) |
| `greekreview` | `gpt-5.6-sol` | `openai-codex` | medium | [greekreview-SOUL.md](greekreview-SOUL.md) |

The live profiles are stored outside Git under `%LOCALAPPDATA%\hermes\profiles\<name>\`. All three use this repository as `terminal.cwd`. Create them by cloning the authenticated default profile, apply the pinned model/provider/reasoning/cwd settings with `hermes -p <name> config set ...`, and copy the matching tracked template to the profile's `SOUL.md`.

Verify before an unattended run:

```bash
hermes profile show greekroot
hermes profile show greekimpl
hermes profile show greekreview
hermes -p greekroot auth list openai-codex
hermes -p greekimpl auth list openai-codex
hermes -p greekreview auth list openai-codex
```

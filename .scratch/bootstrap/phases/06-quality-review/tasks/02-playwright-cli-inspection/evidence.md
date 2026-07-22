# Evidence

## Run identity and scope

- Task: `B06-02`
- Implementer session: `20260722_165408_e78a72`
- Review correction: High finding 1 from `reviews/01-review.md`
- Fixture base URL: `http://127.0.0.1:3100`
- CLI invocation: `pnpm exec playwright-cli`
- CLI version: `0.1.17` (`.artifacts/bootstrap/playwright-cli/b06-02/cli-version.txt`)
- Canonical skill generation: `pnpm exec playwright-cli install --skills=agents`, exit `0`
- Execution note: the first shell wrapper exited `2` due a missing outer-loop terminator; partial artifacts were discarded before the corrected rerun.
- Required viewports: compact `390x844`; wide `1440x1024`
- B06-01 prerequisite: `Done`

## Route and viewport matrix

| Locale | Route | Viewport | State exercised | Console/network/overflow result | Evidence |
|---|---|---:|---|---|---|
| English | `/en` | 390x844 | Home baseline; source for language switch | 0 console errors, 0 warnings; only 200/304 responses; `viewportOverflow:false` | `.artifacts/bootstrap/playwright-cli/b06-02/en-compact.yml`, `.png`; `console-network-metrics.txt`; `network-all-states.txt` |
| English | `/en` | 1440x1024 | Home wide baseline | 0 console errors, 0 warnings; only 200/304 responses; `viewportOverflow:false` | `.artifacts/bootstrap/playwright-cli/b06-02/en-wide.yml`, `.png`; `console-network-metrics.txt`; `network-all-states.txt` |
| English | `/en/quality-lab` | 390x844 | Quality-lab baseline, keyboard focus, interactive primitive | `Tab` focused `Skip to content`; button changed to `Selected`; 0 console errors/warnings; `viewportOverflow:false` | `.artifacts/bootstrap/playwright-cli/b06-02/en-quality-lab-compact.yml`, `.png`, `en-quality-compact-focus.yml`, `en-quality-compact-interactive.yml`, corresponding interactive `.png`; `interaction-evidence.txt`; matrix logs |
| English | `/en/quality-lab` | 1440x1024 | Quality-lab wide baseline | 0 console errors, 0 warnings; only 200/304 responses; `viewportOverflow:false` | `.artifacts/bootstrap/playwright-cli/b06-02/en-quality-lab-wide.yml`, `.png`; matrix logs |
| Greek | `/el` | 390x844 | Home reached by language switch; localized baseline | Language switch verified `/en` → `/el`; 0 console errors, 0 warnings; only 200/304 responses; `viewportOverflow:false` | `.artifacts/bootstrap/playwright-cli/b06-02/en-home-switch-source.yml`, `el-compact.yml`, `.png`; `interaction-evidence.txt`; matrix logs |
| Greek | `/el` | 1440x1024 | Home wide localized baseline | 0 console errors, 0 warnings; only 200/304 responses; `viewportOverflow:false` | `.artifacts/bootstrap/playwright-cli/b06-02/el-wide.yml`, `.png`; matrix logs |
| Greek | `/el/quality-lab` | 390x844 | Quality-lab baseline, keyboard focus, interactive primitive | `Tab` focused `Μετάβαση στο περιεχόμενο`; button changed to `Επιλεγμένο`; state text updated; 0 console errors/warnings; `viewportOverflow:false` | `.artifacts/bootstrap/playwright-cli/b06-02/el-quality-lab-compact.yml`, `.png`, `el-quality-compact-focus.yml`, `el-quality-compact-interactive.yml`, corresponding interactive `.png`; `interaction-evidence.txt`; matrix logs |
| Greek | `/el/quality-lab` | 1440x1024 | Quality-lab wide localized baseline | 0 console errors, 0 warnings; only 200/304 responses; `viewportOverflow:false` | `.artifacts/bootstrap/playwright-cli/b06-02/el-quality-lab-wide.yml`, `.png`; matrix logs |

## Exact interaction evidence

All interaction commands used the refreshed local CLI and stable role locators; no stale numeric snapshot refs were used.

- Language switching: `pnpm exec playwright-cli -s=b06-02-v017 click "getByRole('link', { name: 'Greek' })"` — exit `0`; subsequent `pnpm exec playwright-cli --raw eval "location.pathname"` returned `/el`.
- English keyboard focus: `pnpm exec playwright-cli -s=b06-02-v017 press Tab` plus raw active-element evaluation — exit `0`; active element was an `A` with text `Skip to content` and `href="#main-content"`.
- Greek keyboard focus: same stable CLI sequence — exit `0`; active element was an `A` with text `Μετάβαση στο περιεχόμενο` and `href="#main-content"`.
- English primitive: `pnpm exec playwright-cli -s=b06-02-v017 click "getByRole('button', { name: 'Not selected' })"` — exit `0`; evaluation returned `{"button":"Selected","state":"Current state: Selected","active":"Selected"}`.
- Greek primitive: `pnpm exec playwright-cli -s=b06-02-v017 click "getByRole('button', { name: 'Δεν έχει επιλεγεί' })"` — exit `0`; evaluation returned `{"button":"Επιλεγμένο","state":"Τρέχουσα κατάσταση: Επιλεγμένο","active":"Επιλεγμένο"}`.
- Full command output for all interactions: `.artifacts/bootstrap/playwright-cli/b06-02/interaction-evidence.txt`.

## Console and network evidence

- `.artifacts/bootstrap/playwright-cli/b06-02/console-network-metrics.txt` contains the local 0.1.17 CLI run for all eight route/viewport states. It records eight `viewportOverflow:false` evaluations, eight `console error` checks returning `0 messages`, and eight `console warning` checks returning `0 messages`.
- `.artifacts/bootstrap/playwright-cli/b06-02/network-all-states.txt` contains `pnpm exec playwright-cli requests --static` output for all eight route/viewport states. Observed response statuses were only `[200]` and `[304]`; no 4xx/5xx response matched.
- `.artifacts/bootstrap/playwright-cli/b06-02/interaction-evidence.txt` contains final interaction console checks with zero errors/warnings and static network output.
- `.artifacts/bootstrap/playwright-cli/b06-02/cli-version.txt` records `0.1.17`; `.artifacts/bootstrap/playwright-cli/b06-02/cli-help.txt` records the current command surface. No skill mismatch banner was emitted.

## Responsive and visual evidence

- The CLI evaluated document/body scroll width against the requested viewport for every state; all eight reported `viewportOverflow:false`.
- Refreshed screenshots were visually inspected: English and Greek compact home, English and Greek wide quality-lab, plus the corresponding route matrix captures. No clipping, horizontal overflow, unreadable localization, or obvious responsive defect was observed.
- All refreshed screenshots and snapshots are under ignored `.artifacts/bootstrap/playwright-cli/b06-02/`. Representative `git check-ignore -v` checks passed with the repository `.gitignore:40` rule.

## Defect disposition

High finding 1 is addressed: the canonical repository-local skill now matches local CLI `0.1.17`, and the evidence is reproduced through `pnpm exec playwright-cli` with stable role locators. No browser behavior defect was found; no permanent test was added or changed. The task remains `In review`.

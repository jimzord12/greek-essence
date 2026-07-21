# Evidence

Task: `B01-01`
Implementer session: `20260722_013444_e20ce0`
Generated artifact paths: none; this task creates tracked Markdown/configuration governance files only.

## Prerequisite confirmation

```text
B01-01 task front matter: status=Ready, depends_on=[B00-02]
B00-02 task front matter: status=Done
```

Result: confirmed before mutation.

## Required verification — Markdown links in `AGENTS.md`

Command (run from repository root; the embedded Python parses all Markdown links and exits non-zero for a missing repository-relative target):

```sh
python - <<'PY'
from pathlib import Path
import re
source = Path('AGENTS.md')
links = re.findall(r'\[[^\]]+\]\(([^)]+)\)', source.read_text(encoding='utf-8'))
missing = [link for link in links if '://' not in link and not (source.parent / link).is_file()]
print(f'links_checked={len(links)}')
for link in links:
    print(f'OK {link}')
if missing:
    print('MISSING ' + ', '.join(missing))
    raise SystemExit(1)
PY
```

Exit code: `0`

```text
links_checked=6
OK docs/README.md
OK .scratch/bootstrap/README.md
OK docs/02_prototype_specification/index.md
OK docs/03_technical_design/index.md
OK docs/03_technical_design/18_testing_and_quality_gates.md
OK docs/05_agent_skills/01_approved_tooling_baseline.md
```

## Required verification — required guidance statements

Command (run from repository root; exits non-zero when any required category is absent):

```sh
python - <<'PY'
from pathlib import Path
text = Path('AGENTS.md').read_text(encoding='utf-8')
requirements = {
    'package': 'pnpm',
    'locale': 'English and Greek',
    'skill': '## Approved skills',
    'browser': 'Playwright CLI',
    'architecture': 'static-first',
    'checks': '## Required checks',
    'definition_of_done': '## Definition of done',
}
missing = [name for name, phrase in requirements.items() if phrase not in text]
for name, phrase in requirements.items():
    print(f"{'OK' if phrase in text else 'MISSING'} {name}: {phrase}")
if missing:
    raise SystemExit(1)
PY
```

Exit code: `0`

```text
OK package: pnpm
OK locale: English and Greek
OK skill: ## Approved skills
OK browser: Playwright CLI
OK architecture: static-first
OK checks: ## Required checks
OK definition_of_done: ## Definition of done
```

## Change hygiene

Command:

```sh
git diff --check
```

Exit code: `0`

Result: no whitespace errors.

Command:

```sh
git status --short
```

Exit code: `0`

Result before writing these task-owned records:

```text
 M .scratch/bootstrap/phases/01-agent-tooling/tasks/01-repository-guidance/task.md
?? .editorconfig
?? .gitattributes
?? AGENTS.md
```

No secret, credential, personal/client data, generated artifact, package installation, commit, remote, deployment, or history operation was performed.

## Final record-format correction and re-check

After the task-owned records were written, `git diff --check` initially exited `2` because the first two evidence lines used Markdown hard-break trailing spaces. Those spaces were removed; this did not alter any requirement, command, or result.

Command:

```sh
git diff --check
```

Exit code after the correction: `0`

Result: no whitespace errors remain.

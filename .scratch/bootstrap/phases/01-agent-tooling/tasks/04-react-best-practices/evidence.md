# B01-04 evidence

## Preflight

- `git status --short && git branch --show-current && git log -1 --oneline` — exit 0; branch `main`, no pre-existing working-tree changes.
- Python front-matter inspection of B01-03 — exit 0; `id: B01-03`, `status: Done`, `completed_at: 2026-07-22T03:33:48+03:00`.
- `date -u +'%Y-%m-%dT%H:%M:%SZ'` — exit 0; `2026-07-22T00:45:38Z`.

## Isolated source inspection and installation

- `git ls-remote https://github.com/vercel-labs/agent-skills.git HEAD` — exit 0; `4559f18a20c1691c744b4395194290db6a0df5e9`.
- Isolated checkout artifact: `.artifacts/bootstrap/B01-04/agent-skills/`, detached at `4559f18a20c1691c744b4395194290db6a0df5e9`.
- Inspected upstream source path: `skills/react-best-practices/`; it contains 76 files and no executable scripts. Direct `SKILL.md` references (`AGENTS.md`, `rules/async-parallel.md`, and `rules/bundle-barrel-imports.md`) existed. No destructive, privileged, network, or installation command was found in the skill files.
- License result: MIT in upstream `SKILL.md` front matter; no standalone license file is present in the upstream repository tree.
- Canonical installer entry recorded from the locked documentation: `npx skills add vercel-labs/agent-skills --skill vercel-react-best-practices`.
- Installed by normalized LF copy from that isolated exact checkout to `.agents/skills/vercel-react-best-practices/`; no installer scripts were executed.

## B01-04 decisive verification

Exact command:

```bash
python - <<'PY'
from pathlib import Path
import hashlib
repo=Path('.')
source=repo/'.artifacts/bootstrap/B01-04/agent-skills/skills/react-best-practices'
target=repo/'.agents/skills/vercel-react-best-practices'
errors=[]
if not (target/'SKILL.md').is_file(): errors.append('missing canonical SKILL.md')
source_files=sorted(p.relative_to(source) for p in source.rglob('*') if p.is_file())
target_files=sorted(p.relative_to(target) for p in target.rglob('*') if p.is_file())
if source_files != target_files: errors.append('normalized file set differs from pinned source')
for relative in source_files:
    expected=(source/relative).read_bytes().replace(b'\r\n',b'\n')
    actual=(target/relative).read_bytes()
    if expected != actual:
        errors.append(f'normalized content differs: {relative}')
        break
vercel_dirs=[p.name for p in (repo/'.agents/skills').iterdir() if p.is_dir() and p.name.startswith('vercel-')]
if vercel_dirs != ['vercel-react-best-practices']: errors.append(f'unrelated Vercel skills: {vercel_dirs}')
duplicates=[]
for base in ('.claude/skills','.cursor/skills','.hermes/skills','.trae/skills'):
    if (repo/base/'vercel-react-best-practices').exists(): duplicates.append(base)
if duplicates: errors.append(f'agent-specific duplicates: {duplicates}')
readme=(repo/'.agents/README.md').read_text(encoding='utf-8')
for required in ('4559f18a20c1691c744b4395194290db6a0df5e9','skills/react-best-practices/','MIT'):
    if required not in readme: errors.append(f'missing provenance: {required}')
print(f'pinned_revision=4559f18a20c1691c744b4395194290db6a0df5e9')
print(f'canonical_path={target.as_posix()}')
print(f'normalized_files={len(target_files)} skill_sha256={hashlib.sha256((target/"SKILL.md").read_bytes()).hexdigest()}')
print(f'vercel_skill_directories={vercel_dirs}')
print(f'agent_specific_duplicates={duplicates}')
if errors:
    print('B01-04 verification: FAIL')
    print('\n'.join(errors)); raise SystemExit(1)
print('B01-04 verification: PASS')
PY
```

Exit code: 0.

Result:

```text
pinned_revision=4559f18a20c1691c744b4395194290db6a0df5e9
canonical_path=.agents/skills/vercel-react-best-practices
normalized_files=76 skill_sha256=71ed7794962fa6e803ee83030517b5b93a9f70fbfeb431ec4535c5480a8d8355
vercel_skill_directories=['vercel-react-best-practices']
agent_specific_duplicates=[]
B01-04 verification: PASS
```

Artifact paths: `.artifacts/bootstrap/B01-04/agent-skills/` (ignored isolated checkout); no generated test artifacts.

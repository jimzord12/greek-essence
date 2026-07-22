# B01-05 evidence

## Environment

- Hermes implementer session: `20260722_035747_d38a8d`
- Started at: `2026-07-22T00:58:54Z`
- `playwright-cli`: `0.1.14` (global executable at `/c/Users/jimzord12/.bun/bin/playwright-cli`)
- Node.js: `v24.18.0`; pnpm: `10.33.0`; npm: `11.16.0`
- Generated-install artifact: `.artifacts/bootstrap/B01-05/isolated/` (ignored by `.gitignore:2`)

## Decisive commands and results

| Command / invocation | Exit | Result | Artifact path |
|---|---:|---|---|
| `playwright-cli --version` | 0 | Reported `0.1.14`. | None |
| `playwright-cli --help` | 0 | Listed the CLI command surface, including `install`; no overlapping browser tool was invoked. | None |
| `playwright-cli install --help; playwright-cli install --skills --help` | 0 | Confirmed `--skills` is supported and defaults to the `claude` target. | None |
| `rm -rf .artifacts/bootstrap/B01-05 && mkdir -p .artifacts/bootstrap/B01-05/isolated && cd .artifacts/bootstrap/B01-05/isolated && playwright-cli install --skills` | 0 | Generated `.claude/skills/playwright-cli/` with `SKILL.md` and ten Markdown references; `.playwright/` was also generated only in isolation. | `.artifacts/bootstrap/B01-05/isolated/` |
| Exact normalization/copy and source-comparison invocation below. | 0 | Copied the generated skill to `.agents/skills/playwright-cli/`; all 11 canonical files equal the generated source after CRLF-to-LF normalization. | `.agents/skills/playwright-cli/`; `.artifacts/bootstrap/B01-05/isolated/.claude/skills/playwright-cli/` |
| `npm view @playwright/cli@0.1.14 version license repository.url dist.gitHead dist.integrity dist.tarball --json` | 0 | Verified version `0.1.14`, Apache-2.0, repository `https://github.com/microsoft/playwright-cli`, and recorded distribution integrity. Registry returned no `dist.gitHead`. | None |
| Exact failed verifier invocation below. | 1 | Failed before assertions because the MSYS shell consumed a backslash in the verifier's string literal. No repository files changed. | None |
| Exact corrected verifier invocation below (initial run). | 0 | Passed: exactly 11 canonical files, byte-equality after normalization, no `package.json`, explicit B05-02 pinning deferral, and no `agent-browser`, `browser-use`, or `playwright-mcp` executable/repository path. | None |
| Exact corrected verifier invocation below (review-correction rerun). | 0 | Passed with the same four result lines; this was the only rerun for Finding 1. | None |
| `node --version; pnpm --version; npm --version; git diff --check` | 0 | Reported the environment versions above; no whitespace errors. | None |

## Exact normalization/copy and source-comparison invocation

```bash
python - <<'PY'
from pathlib import Path
source = Path('.artifacts/bootstrap/B01-05/isolated/.claude/skills/playwright-cli')
target = Path('.agents/skills/playwright-cli')
for path in source.rglob('*'):
    if path.is_file():
        destination = target / path.relative_to(source)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(path.read_bytes().replace(b'\r\n', b'\n'))
PY
find .agents/skills/playwright-cli -type f -print | sort
printf '\n--- normalized comparison ---\n'
python - <<'PY'
from pathlib import Path
source = Path('.artifacts/bootstrap/B01-05/isolated/.claude/skills/playwright-cli')
target = Path('.agents/skills/playwright-cli')
source_files = sorted(path.relative_to(source) for path in source.rglob('*') if path.is_file())
target_files = sorted(path.relative_to(target) for path in target.rglob('*') if path.is_file())
assert source_files == target_files, (source_files, target_files)
for relative in source_files:
    assert source.joinpath(relative).read_bytes().replace(b'\r\n', b'\n') == target.joinpath(relative).read_bytes(), relative
print(f'PASS: {len(source_files)} canonical files equal generated source after CRLF-to-LF normalization.')
PY
```

Result (exit 0): listed `SKILL.md` and ten reference files, then printed `PASS: 11 canonical files equal generated source after CRLF-to-LF normalization.`

## Exact failed verifier invocation

```bash
python - <<'PY'
from pathlib import Path
import shutil
root = Path('.')
source = root / '.artifacts/bootstrap/B01-05/isolated/.claude/skills/playwright-cli'
target = root / '.agents/skills/playwright-cli'
expected = {'SKILL.md', *(f'references/{name}' for name in ('element-attributes.md', 'playwright-tests.md', 'request-mocking.md', 'running-code.md', 'session-management.md', 'spec-driven-testing.md', 'storage-state.md', 'test-generation.md', 'tracing.md', 'video-recording.md'))}
actual = {str(path.relative_to(target)).replace('\', '/') for path in target.rglob('*') if path.is_file()}
assert actual == expected, (actual, expected)
for relative in expected:
    assert target.joinpath(relative).read_bytes() == source.joinpath(relative).read_bytes().replace(b'\r\n', b'\n'), relative
assert not (root / 'package.json').exists(), 'project manifest must remain deferred'
readme = (root / '.agents/README.md').read_text(encoding='utf-8')
assert 'Project-level `@playwright/cli` pinning is explicitly deferred to B05-02' in readme
for name in ('agent-browser', 'browser-use', 'playwright-mcp'):
    assert shutil.which(name) is None, name
for path in root.rglob('*'):
    relative = path.relative_to(root)
    if '.git' in relative.parts or '.artifacts' in relative.parts:
        continue
    assert 'agent-browser' not in path.name.lower(), path
    assert 'browser-use' not in path.name.lower(), path
    assert 'playwright-mcp' not in path.name.lower(), path
print('B01-05 verification: PASS')
print('canonical_skill_files=11')
print('project_package_pinning=deferred_to_B05-02')
print('prohibited_browser_tools=absent')
PY
status=$?
printf '\n--- versions ---\n'
node --version
pnpm --version
npm --version
printf '\n--- diff check ---\n'
git diff --check
exit $status
```

Result (exit 1): Python raised `SyntaxError: unterminated string literal (detected at line 7)` at the `replace('\', '/')` expression before any assertions. The subsequent version and diff commands completed; no repository file was changed by this failed verifier.

## Exact corrected verifier invocation

This exact invocation was run first during implementation (exit 0) and rerun once for Finding 1 (exit 0):

```bash
python - <<'PY'
from pathlib import Path
import shutil
root = Path('.')
source = root / '.artifacts/bootstrap/B01-05/isolated/.claude/skills/playwright-cli'
target = root / '.agents/skills/playwright-cli'
expected = {'SKILL.md', *(f'references/{name}' for name in ('element-attributes.md', 'playwright-tests.md', 'request-mocking.md', 'running-code.md', 'session-management.md', 'spec-driven-testing.md', 'storage-state.md', 'test-generation.md', 'tracing.md', 'video-recording.md'))}
actual = {path.relative_to(target).as_posix() for path in target.rglob('*') if path.is_file()}
assert actual == expected, (actual, expected)
for relative in expected:
    assert target.joinpath(relative).read_bytes() == source.joinpath(relative).read_bytes().replace(b'\r\n', b'\n'), relative
assert not (root / 'package.json').exists(), 'project manifest must remain deferred'
readme = (root / '.agents/README.md').read_text(encoding='utf-8')
assert 'Project-level `@playwright/cli` pinning is explicitly deferred to B05-02' in readme
for name in ('agent-browser', 'browser-use', 'playwright-mcp'):
    assert shutil.which(name) is None, name
for path in root.rglob('*'):
    relative = path.relative_to(root)
    if '.git' in relative.parts or '.artifacts' in relative.parts:
        continue
    assert 'agent-browser' not in path.name.lower(), path
    assert 'browser-use' not in path.name.lower(), path
    assert 'playwright-mcp' not in path.name.lower(), path
print('B01-05 verification: PASS')
print('canonical_skill_files=11')
print('project_package_pinning=deferred_to_B05-02')
print('prohibited_browser_tools=absent')
PY
```

Result for the Finding 1 rerun (exit 0):

```text
B01-05 verification: PASS
canonical_skill_files=11
project_package_pinning=deferred_to_B05-02
prohibited_browser_tools=absent
```

## Scope and deferral

No project manifest exists yet and no repository package was added. Exact project-level `@playwright/cli` pinning is explicitly deferred to B05-02. No Playwright MCP, Browser Use, `agent-browser`, browser binary installation, or other browser-agent alternative was installed or configured.

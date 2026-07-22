# Evidence

## Preconditions

- B03-04 was `Ready` before mutation.
- B03-03 completion was confirmed from commit `dda539c docs(bootstrap): correct B03-03 review record`.

## Package-script help/smoke

Command (exit 0; individual script exits are shown below):

```text
for script in dev build start lint lint:fix typecheck format format:check test:unit test:unit:watch test:e2e test:a11y quality:unlighthouse check check:all; do printf '\n== pnpm run %s --help ==\n' "$script"; pnpm run "$script" --help; printf 'exit=%s\n' "$?"; done
```

Results:

- `dev`, `build`, `start`, `lint`, `lint:fix`, `typecheck`, `format`, and `format:check`: exit 0; each displayed its CLI help.
- `test:unit`, `test:unit:watch`, `test:e2e`, `test:a11y`, and `quality:unlighthouse`: exit 1 because their deferred executables (`vitest`, `playwright`, and `start-server-and-test`) are not installed yet.
- `check` and `check:all`: exit 1 at the deferred `test:unit` command. Their preceding non-mutating format, lint, and typecheck steps completed; lint emitted one pre-existing warning in `commitlint.config.mjs` and no errors.

## Ignore behavior

Command (aggregate exit 0):

```text
git check-ignore .env.local .artifacts/bootstrap/smoke.txt; ignored_rc=$?; git check-ignore .env.example; example_rc=$?; test "$ignored_rc" -eq 0 && test "$example_rc" -eq 1; verification_rc=$?; printf 'ignored_rc=%s\nexample_rc=%s\nverification_rc=%s\n' "$ignored_rc" "$example_rc" "$verification_rc"; exit "$verification_rc"
```

Results:

- `git check-ignore .env.local .artifacts/bootstrap/smoke.txt` printed both paths and exited 0: both are ignored.
- `git check-ignore .env.example` printed no path and exited 1: `.env.example` is not ignored.
- The aggregate assertions exited 0 (`ignored_rc=0`, `example_rc=1`, `verification_rc=0`).

No generated artifact files were created.

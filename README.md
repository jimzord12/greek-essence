# Greek Essence

Greek Essence is a private bilingual client-review prototype for a Greece-focused travel-planning service.

## Documentation

- [Documentation entry point](docs/README.md)
- [Bootstrap workspace](.scratch/bootstrap/README.md)

Bootstrap tooling and the bilingual fixture scaffold are complete. Product prototype implementation remains pending. This repository does not implement booking, payments, accounts, analytics, or production operations.

## Development

Use standalone pnpm `11.17.0` directly:

```bash
pnpm install --frozen-lockfile
pnpm dev
```

On Windows, install the repository-pinned version with the official PowerShell installer, then open a refreshed terminal:

```powershell
$env:PNPM_VERSION = "11.17.0"
irm https://get.pnpm.io/install.ps1 | iex
```

#!/usr/bin/env python3
"""Read-only structural compatibility preflight for the Greek Essence Ralph loop."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from email.utils import parseaddr
from pathlib import Path
from typing import Any

REQUIRED_FILES = (
    "AGENTS.md",
    ".scratch/ralph-loop/RALPH_LOOP.md",
    ".scratch/ralph-loop/HANDOFF.md",
    ".scratch/ralph-loop/KNOWLEDGE.md",
    ".scratch/ralph-loop/completion-signal.json",
    ".scratch/ralph-loop/tools/ralph_loop.py",
)
EXPECTED_PROFILES = {
    "greekroot": {"model.default": "gpt-5.6-sol", "model.provider": "openai-codex", "model.reasoning_effort": "low"},
    "greekimpl": {"model.default": "gpt-5.6-luna", "model.provider": "openai-codex", "model.reasoning_effort": "high"},
    "greekreview": {"model.default": "gpt-5.6-terra", "model.provider": "openai-codex", "model.reasoning_effort": "high"},
}
OWNED_REPOSITORY = Path(__file__).resolve().parents[4]


def run(command: list[str], cwd: Path, timeout: float = 20) -> subprocess.CompletedProcess[str]:
    try:
        return subprocess.run(
            command,
            cwd=cwd,
            text=True,
            encoding="utf-8",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=timeout,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        captured = exc.stdout if isinstance(exc.stdout, str) else ""
        return subprocess.CompletedProcess(
            command,
            124,
            stdout=f"{captured}\nTimed out after {timeout} seconds".strip(),
        )
    except OSError as exc:
        return subprocess.CompletedProcess(command, 126, stdout=f"Could not start command: {type(exc).__name__}: {exc}")


def pid_is_running(pid: int) -> bool:
    if pid <= 0:
        return False
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    except (OSError, SystemError):
        return False
    return True


def is_contained_regular_file(path: Path, root: Path) -> bool:
    """Reject files, symlinks, and junction-resolved paths outside canonical root."""
    try:
        resolved = path.resolve(strict=True)
        canonical_root = root.resolve(strict=True)
        resolved.relative_to(canonical_root)
    except (OSError, RuntimeError, ValueError):
        return False
    return path.is_file() and not path.is_symlink()


def exact_signal(path: Path) -> bool:
    def no_duplicates(pairs: list[tuple[str, object]]) -> dict[str, object]:
        result: dict[str, object] = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate property: {key}")
            result[key] = value
        return result

    payload = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=no_duplicates)
    if not isinstance(payload, dict) or set(payload) != {"isEverythingDone"}:
        raise ValueError("must contain exactly isEverythingDone")
    value = payload["isEverythingDone"]
    if type(value) is not bool:
        raise ValueError("isEverythingDone must be a Boolean")
    return value


def email_skill_candidates(_repo: Path) -> list[Path]:
    # This project authorizes only the installed profile-level dependency.
    candidates: list[Path] = []
    local = os.environ.get("LOCALAPPDATA")
    if local:
        base = Path(local) / "hermes"
        candidates.extend(
            [
                base / "skills" / "email" / "email-notification",
                base / "skills" / "email-notification",
            ]
        )
    return candidates


def validate_email_environment() -> tuple[bool, list[str]]:
    """Validate non-secret credential shape and sender syntax; never print values."""
    problems: list[str] = []
    api_key = os.environ.get("RESEND_API_KEY", "").strip()
    sender = os.environ.get("RESEND_FROM_EMAIL", "").strip()
    if not api_key:
        problems.append("RESEND_API_KEY missing")
    elif not api_key.startswith("re_") or len(api_key) < 10 or any(character.isspace() for character in api_key):
        problems.append("RESEND_API_KEY has an invalid shape")
    if not sender:
        problems.append("RESEND_FROM_EMAIL missing")
    else:
        _, address = parseaddr(sender)
        valid_address = bool(re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", address))
        domain = address.rpartition("@")[2].lower()
        placeholder = domain in {"example.com", "example.org", "example.net"} or domain.endswith((".invalid", ".test"))
        if not valid_address or placeholder:
            problems.append("RESEND_FROM_EMAIL is malformed or a placeholder")
    return not problems, problems


def add_check(checks: list[dict[str, Any]], name: str, ok: bool, evidence: str) -> None:
    checks.append({"name": name, "ok": ok, "evidence": evidence})


def resolve_target(repo: Path, raw: str, hard_stops: list[dict[str, str]]) -> dict[str, str]:
    target = raw.strip()
    if not target:
        hard_stops.append(
            {
                "code": "EMPTY_TARGET",
                "problem": "No feature or directory scope was supplied.",
                "remediation": "Name one bounded feature or a repository-relative directory.",
            }
        )
        return {"kind": "invalid", "value": raw}

    supplied = Path(target).expanduser()
    candidate = supplied if supplied.is_absolute() else repo / supplied
    if candidate.exists():
        resolved = candidate.resolve()
        try:
            relative = resolved.relative_to(repo)
        except ValueError:
            hard_stops.append(
                {
                    "code": "TARGET_OUTSIDE_REPOSITORY",
                    "problem": f"Target resolves outside the project: {resolved}",
                    "remediation": "Choose a feature or directory contained by the Greek Essence repository.",
                }
            )
            return {"kind": "outside", "value": str(resolved)}
        return {"kind": "directory" if resolved.is_dir() else "file", "value": relative.as_posix() or "."}

    looks_like_path = supplied.is_absolute() or "/" in target or "\\" in target or target.startswith(".")
    if looks_like_path:
        hard_stops.append(
            {
                "code": "TARGET_PATH_MISSING",
                "problem": f"Requested path does not exist: {candidate}",
                "remediation": "Correct the path or provide a feature label backed by authoritative project records.",
            }
        )
        return {"kind": "missing", "value": target}
    return {"kind": "feature-label", "value": target}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--target", required=True, help="Feature label or repository-contained path")
    args = parser.parse_args(argv)

    repo = args.repo.resolve()
    checks: list[dict[str, Any]] = []
    warnings: list[dict[str, str]] = []
    hard_stops: list[dict[str, str]] = []

    if not repo.is_dir():
        result = {
            "status": "HARD_STOP",
            "repository": str(repo),
            "target": {"kind": "unresolved", "value": args.target},
            "completion_signal": None,
            "checks": [
                {
                    "name": "repository-directory",
                    "ok": False,
                    "evidence": f"missing or not a directory: {repo}",
                }
            ],
            "warnings": [],
            "hard_stops": [
                {
                    "code": "REPOSITORY_DIRECTORY_MISSING",
                    "problem": f"The requested repository directory does not exist: {repo}",
                    "remediation": "Pass the existing Greek Essence repository root with --repo.",
                }
            ],
            "semantic_requirements": [],
            "launch_performed": False,
        }
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 2

    if repo != OWNED_REPOSITORY:
        result = {
            "status": "HARD_STOP",
            "repository": str(repo),
            "target": {"kind": "unresolved", "value": args.target},
            "completion_signal": None,
            "checks": [
                {
                    "name": "project-only-repository",
                    "ok": False,
                    "evidence": f"skill-owned={OWNED_REPOSITORY}; requested={repo}",
                }
            ],
            "warnings": [],
            "hard_stops": [
                {
                    "code": "PROJECT_SCOPE_MISMATCH",
                    "problem": "This project-only skill was asked to inspect a different repository.",
                    "remediation": f"Run it only with --repo {OWNED_REPOSITORY}.",
                }
            ],
            "semantic_requirements": [],
            "launch_performed": False,
        }
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 2

    git = shutil.which("git")
    add_check(checks, "git-command", git is not None, git or "missing")
    if git is None:
        hard_stops.append(
            {"code": "GIT_MISSING", "problem": "git is unavailable.", "remediation": "Install or expose git before running Ralph."}
        )
    else:
        probe = run([git, "rev-parse", "--show-toplevel"], repo)
        detected = Path(probe.stdout.strip()).resolve() if probe.returncode == 0 and probe.stdout.strip() else None
        ok = detected == repo
        add_check(checks, "repository-root", ok, str(detected) if detected else probe.stdout.strip())
        if not ok:
            hard_stops.append(
                {
                    "code": "WRONG_REPOSITORY_ROOT",
                    "problem": f"--repo is not the live Git root (detected: {detected}).",
                    "remediation": "Run from the Greek Essence repository root and pass that root with --repo.",
                }
            )

    scope = resolve_target(repo, args.target, hard_stops)
    add_check(checks, "target-contained", scope["kind"] not in {"invalid", "outside", "missing"}, json.dumps(scope))

    missing = [relative for relative in REQUIRED_FILES if not (repo / relative).is_file()]
    add_check(checks, "ralph-files", not missing, "missing=" + json.dumps(missing))
    if missing:
        hard_stops.append(
            {
                "code": "RALPH_LAYOUT_INCOMPLETE",
                "problem": "Required Ralph project files are missing: " + ", ".join(missing),
                "remediation": "Restore or create the project-owned Ralph contract before launch.",
            }
        )

    signal_value: bool | None = None
    signal_path = repo / ".scratch" / "ralph-loop" / "completion-signal.json"
    if signal_path.is_file():
        try:
            signal_value = exact_signal(signal_path)
            add_check(checks, "completion-signal-schema", True, f"isEverythingDone={str(signal_value).lower()}")
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            add_check(checks, "completion-signal-schema", False, str(exc))
            hard_stops.append(
                {
                    "code": "INVALID_COMPLETION_SIGNAL",
                    "problem": f"Completion signal is invalid: {exc}",
                    "remediation": "Restore the exact one-property Boolean schema before launch.",
                }
            )
    if signal_value is True:
        hard_stops.append(
            {
                "code": "CAMPAIGN_ALREADY_COMPLETE",
                "problem": "The completion signal is already true; the controller will not launch a new iteration.",
                "remediation": "Define the new managed campaign in durable project state, then have a human explicitly reset the signal to false as required by RALPH_LOOP.md.",
            }
        )

    python_ok = sys.version_info >= (3, 11)
    add_check(checks, "python", python_ok, sys.version.split()[0])
    if not python_ok:
        hard_stops.append(
            {"code": "PYTHON_UNSUPPORTED", "problem": "Python 3.11 or newer is required.", "remediation": "Use a supported Python interpreter."}
        )

    hermes = shutil.which("hermes")
    add_check(checks, "hermes-command", hermes is not None, hermes or "missing")
    if hermes is None:
        hard_stops.append(
            {"code": "HERMES_MISSING", "problem": "The hermes command is unavailable.", "remediation": "Install/configure Hermes before launch."}
        )
    else:
        for profile, expected_values in EXPECTED_PROFILES.items():
            shown = run([hermes, "profile", "show", profile], repo)
            observed: dict[str, str] = {}
            command_failures: dict[str, int] = {}
            for key in (*expected_values, "terminal.cwd"):
                configured = run([hermes, "--profile", profile, "config", "get", key], repo)
                if configured.returncode == 0:
                    observed[key] = configured.stdout.strip()
                else:
                    command_failures[key] = configured.returncode
            values_ok = all(observed.get(key) == value for key, value in expected_values.items())
            cwd_value = observed.get("terminal.cwd", "").strip()
            cwd_ok = cwd_value == repo.as_posix()
            ok = shown.returncode == 0 and not command_failures and values_ok and cwd_ok
            evidence = {
                "show_exit": shown.returncode,
                "command_failures": command_failures,
                "model": observed.get("model.default"),
                "provider": observed.get("model.provider"),
                "reasoning": observed.get("model.reasoning_effort"),
                "cwd_matches_repository": cwd_ok,
            }
            add_check(checks, f"profile-{profile}", ok, json.dumps(evidence, sort_keys=True))
            if not ok:
                hard_stops.append(
                    {
                        "code": "PROFILE_MISMATCH",
                        "problem": f"Hermes profile {profile} is missing or not exactly pinned to its model, provider, reasoning, and repository working directory.",
                        "remediation": "Repair the exact profile values, including terminal.cwd, before launch.",
                    }
                )

    state_base = Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData" / "Local"))
    lock = state_base / "hermes" / "ralph" / "greek-essence" / "ralph.lock"
    if lock.exists():
        try:
            owner = int(lock.read_text(encoding="utf-8").strip())
            active = pid_is_running(owner)
            add_check(checks, "runtime-lock", not active, f"path={lock}; pid={owner}; active={active}")
            if active:
                hard_stops.append(
                    {
                        "code": "ACTIVE_RALPH_LOCK",
                        "problem": f"Another Ralph controller owns the lock with PID {owner}.",
                        "remediation": "Monitor the existing controller; do not launch a competing loop.",
                    }
                )
            else:
                warnings.append({"code": "STALE_LOCK", "message": f"The controller should recover stale lock {lock}."})
        except (OSError, ValueError) as exc:
            add_check(checks, "runtime-lock", False, str(exc))
            hard_stops.append(
                {
                    "code": "UNREADABLE_RALPH_LOCK",
                    "problem": f"Ralph lock is unreadable: {exc}",
                    "remediation": "Investigate the runtime lock manually; do not delete it blindly.",
                }
            )
    else:
        add_check(checks, "runtime-lock", True, f"absent: {lock}")

    email_dir = next(
        (candidate for candidate in email_skill_candidates(repo) if (candidate / "SKILL.md").is_file()),
        None,
    )
    email_script = email_dir / "scripts" / "send_notification.py" if email_dir else None
    email_files_ok = bool(email_script and email_script.is_file())
    add_check(checks, "email-notification-skill", email_files_ok, str(email_dir) if email_dir else "not found")
    if not email_files_ok:
        hard_stops.append(
            {
                "code": "EMAIL_SKILL_UNAVAILABLE",
                "problem": "The email-notification skill or its sender script is unavailable.",
                "remediation": "Finish/install the email-notification skill before managed Ralph execution.",
            }
        )
    email_environment_ok, email_environment_problems = validate_email_environment()
    add_check(checks, "email-environment-shape", email_environment_ok, "problems=" + json.dumps(email_environment_problems))
    if not email_environment_ok:
        hard_stops.append(
            {
                "code": "EMAIL_NOT_READY",
                "problem": "Email notification environment is incomplete or malformed: " + ", ".join(email_environment_problems),
                "remediation": "Configure non-placeholder values and verify the email skill in --dry-run mode before launch.",
            }
        )

    if git is not None and (repo / ".git").exists():
        status = run([git, "status", "--porcelain=v1", "--untracked-files=all"], repo)
        dirty = bool(status.stdout.strip())
        add_check(checks, "worktree-observed", status.returncode == 0, status.stdout.strip() or "clean")
        if status.returncode != 0:
            hard_stops.append(
                {
                    "code": "WORKTREE_STATUS_FAILED",
                    "problem": f"git status exited {status.returncode}; the worktree could not be observed safely.",
                    "remediation": "Repair Git/worktree access before launch.",
                }
            )
        elif dirty:
            warnings.append(
                {
                    "code": "DIRTY_WORKTREE",
                    "message": "The worktree is dirty. The managing agent must attribute every change to the requested scope or HARD STOP before launch.",
                }
            )

    controller_relative = Path(".scratch") / "ralph-loop" / "tools" / "ralph_loop.py"
    controller = repo / controller_relative
    controller_trusted = False
    if controller.is_file() and git is not None:
        tracked = run([git, "ls-files", "--error-unmatch", controller_relative.as_posix()], repo)
        unchanged = run([git, "diff", "--quiet", "HEAD", "--", controller_relative.as_posix()], repo)
        controller_contained = is_contained_regular_file(controller, OWNED_REPOSITORY)
        controller_trusted = tracked.returncode == 0 and unchanged.returncode == 0 and controller_contained
        add_check(
            checks,
            "trusted-controller",
            controller_trusted,
            f"tracked={tracked.returncode == 0}; unchanged={unchanged.returncode == 0}; "
            f"contained_regular_file={controller_contained}; resolved={controller.resolve()}",
        )
        if not controller_trusted:
            hard_stops.append(
                {
                    "code": "CONTROLLER_NOT_TRUSTED",
                    "problem": "The Ralph controller is untracked, modified, symlinked, or outside the skill-owned repository.",
                    "remediation": "Restore and review the tracked project controller before preflight executes it.",
                }
            )
    if controller_trusted and signal_path.is_file() and not hard_stops:
        dry = run([sys.executable, str(controller), "--repo", str(repo), "--dry-run"], repo)
        add_check(checks, "controller-dry-run", dry.returncode == 0, f"exit={dry.returncode}; output={dry.stdout.strip()[:1000]}")
        if dry.returncode != 0:
            hard_stops.append(
                {
                    "code": "CONTROLLER_DRY_RUN_FAILED",
                    "problem": f"Ralph controller dry-run exited {dry.returncode}.",
                    "remediation": "Resolve the reported controller/configuration failure before launch.",
                }
            )

    semantic_requirements = [
        "Map the target to authoritative project files and bounded acceptance criteria.",
        "Confirm the target matches the active campaign recorded in HANDOFF.md and the completion signal; never silently replace another false-signal campaign.",
        "Confirm durable task/handoff state lets fresh root sessions determine progress and completion.",
        "Confirm required verification is executable and expected completion needs no unauthorized push, deploy, credentials, system change, history rewrite, or out-of-repository edit.",
        "Attribute every dirty-worktree path to the requested campaign or HARD STOP.",
        "Load email-notification and pass its own --dry-run validation for the intended recipient without exposing secrets.",
    ]
    result = {
        "status": "HARD_STOP" if hard_stops else "STRUCTURAL_PASS",
        "repository": str(repo),
        "target": scope,
        "completion_signal": signal_value,
        "checks": checks,
        "warnings": warnings,
        "hard_stops": hard_stops,
        "semantic_requirements": semantic_requirements,
        "launch_performed": False,
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 2 if hard_stops else 0


if __name__ == "__main__":
    raise SystemExit(main())

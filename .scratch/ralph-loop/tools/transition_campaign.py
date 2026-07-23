#!/usr/bin/env python3
"""Transition one explicitly declared completed Ralph campaign to a new one."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from ralph_loop import (
    CampaignIdentity,
    LockConflict,
    TransitionResult,
    default_state_dir,
    transition_campaign_state,
)


def _identity_payload(values: dict[str, str | None]) -> dict[str, str | None]:
    return dict(values)


def _result_payload(
    outcome: str,
    completed: dict[str, str | None],
    new: dict[str, str | None],
    *,
    result: TransitionResult | None = None,
    error_type: str | None = None,
) -> dict[str, object]:
    payload: dict[str, object] = {
        "outcome": outcome,
        "old_identity": _identity_payload(completed),
        "new_identity": _identity_payload(new),
        "archive_path": str(result.archive_path) if result is not None else None,
    }
    if error_type is not None:
        payload["error_type"] = error_type
    return payload


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state-dir", type=Path, default=default_state_dir())
    parser.add_argument("--archive-timestamp")
    parser.add_argument("--completed-campaign-id")
    parser.add_argument("--completed-task-id")
    parser.add_argument("--completed-resolved-tier")
    parser.add_argument("--new-campaign-id")
    parser.add_argument("--new-task-id")
    parser.add_argument("--new-resolved-tier")
    args = parser.parse_args(argv)

    completed_values = {
        "campaign_id": args.completed_campaign_id,
        "task_id": args.completed_task_id,
        "resolved_tier": args.completed_resolved_tier,
    }
    new_values = {
        "campaign_id": args.new_campaign_id,
        "task_id": args.new_task_id,
        "resolved_tier": args.new_resolved_tier,
    }
    missing = [
        name
        for name, value in {
            **{f"completed_{key}": value for key, value in completed_values.items()},
            **{f"new_{key}": value for key, value in new_values.items()},
        }.items()
        if value is None
    ]
    if missing:
        print(json.dumps(_result_payload("INVALID_IDENTITY", completed_values, new_values, error_type="MissingIdentity"), indent=2))
        return 2

    completed = CampaignIdentity(**completed_values)  # type: ignore[arg-type]
    new = CampaignIdentity(**new_values)  # type: ignore[arg-type]
    try:
        result = transition_campaign_state(
            args.state_dir,
            completed,
            new,
            timestamp_utc=args.archive_timestamp,
        )
    except LockConflict:
        print(json.dumps(_result_payload("LOCK_CONFLICT", completed_values, new_values, error_type="LockConflict"), indent=2))
        return 6
    except KeyboardInterrupt:
        print(json.dumps(_result_payload("INTERRUPTED", completed_values, new_values, error_type="KeyboardInterrupt"), indent=2))
        return 130
    except Exception as exc:
        print(json.dumps(_result_payload("TRANSITION_REJECTED", completed_values, new_values, error_type=type(exc).__name__), indent=2))
        return 1

    print(json.dumps(_result_payload("COMPLETE", completed_values, new_values, result=result), indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

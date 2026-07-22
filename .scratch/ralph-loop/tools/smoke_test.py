#!/usr/bin/env python3
"""Run an explicitly requested two-iteration live Ralph smoke test."""

from __future__ import annotations

import sys
from collections.abc import Sequence

from ralph_loop import main as ralph_main


def main(argv: Sequence[str] | None = None) -> int:
    """Forward to the canonical controller with a fixed two-iteration cap."""
    forwarded = list(sys.argv[1:] if argv is None else argv)
    return ralph_main(["--max-iterations", "2", *forwarded])


if __name__ == "__main__":
    sys.exit(main())

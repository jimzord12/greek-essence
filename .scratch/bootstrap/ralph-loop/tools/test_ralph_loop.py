#!/usr/bin/env python3
"""Two-task test runner for the Greek Essence Ralph loop."""

from __future__ import annotations

import sys

from ralph_loop import main


if __name__ == "__main__":
    sys.exit(main(["--max-tasks", "2", *sys.argv[1:]]))

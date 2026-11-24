#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers -- make.fun entry.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt. The line is 61 characters, inside the 120 limit.

Why this line: every developer has watched an estimate given in minutes
stretch into Mondays. It is a fortune-cookie prediction in form, true
about a developer's day, and its turn -- the estimate is repaid in a
different unit of time than the one it was quoted in -- is one the
reader has not heard before, with a quiet second meaning on re-read:
minutes are what you promise, Mondays are what it costs.
"""

from pathlib import Path

LINE = "Your estimate, given in minutes, will be measured in Mondays."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()

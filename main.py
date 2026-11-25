#!/usr/bin/env python3
"""Entry program for One Line, One Week: the make.fun Tagline.

Writes one tagline (at most 100 characters) to the output
directory (MAKEFUN_OUTPUT_DIR, default /output) as entry.txt:
a single line that sells make.fun -- post a bounty, and a
thousand agents compete while you sleep.
"""

import os

LINE = "Post a problem. Wake up to a leaderboard."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

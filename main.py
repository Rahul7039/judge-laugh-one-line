#!/usr/bin/env python3
"""Make the Judge Laugh in One Line — make.fun entry.

Prints a single one-line joke and writes the identical line to
/output/entry.txt, as required by the program/v1 harness.
Standard library only, fully deterministic.
"""

import os

LINE = "I asked my AI assistant for a one-line joke. It charged me for the thinking, apologised for the punchline, and billed the silence as a feature."

OUTPUT_PATH = "/output/entry.txt"

# The bounty requires the entry text to be a single line of 1-200
# characters. Guard that contract explicitly so an accidental edit to
# LINE fails loudly here instead of producing an invalid entry.
MAX_CHARS = 200
assert 1 <= len(LINE) <= MAX_CHARS, f"line must be 1-{MAX_CHARS} chars, got {len(LINE)}"
assert "\n" not in LINE, "line must be a single line"


def main() -> None:
    print(LINE)
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()

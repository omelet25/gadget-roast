#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single roast line about an everyday gadget (the smart TV
whose software update outlasts the episode) to /output/entry.txt.
The gate: UTF-8 text, 1 to 200 characters, one line.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

LINE = (
    "My smart TV demands a 40-minute update to play a 22-minute episode "
    "\u2014 I'm not a viewer anymore, I'm unpaid tech support for my own couch."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"entry must be 1-200 chars, got {len(LINE)}"
    assert "\n" not in LINE, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()

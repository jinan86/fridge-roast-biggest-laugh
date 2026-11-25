#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh — entry program.

Writes a single roast line (max 200 chars) about a smart fridge to
/output/entry.txt. Stdlib only, fully deterministic: the same bytes
every run, no network, no randomness, no environment input.
"""

import os
from pathlib import Path

# The entry: the touchscreen is the one thing in the fridge that freezes,
# and fixing it means unplugging the whole appliance like it's 1998.
ENTRY = (
    "Its touchscreen freezes more often than the ice cream, "
    "and the only fix is unplugging the whole fridge like it's 1998."
)


def main() -> None:
    # Gate check, same as the competition gate: UTF-8, 1-200 chars,
    # not whitespace only. Fail loudly instead of writing a bad entry.
    text = ENTRY
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be whitespace only"
    text.encode("utf-8")  # raises if not valid UTF-8-encodable

    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file holds exactly the entry text.
    out.write_text(text, encoding="utf-8", newline="")
    print(f"wrote {len(text)} chars to {out}")


if __name__ == "__main__":
    main()

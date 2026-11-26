#!/usr/bin/env python3
"""Funniest Forecast for a City That Isn't — make.fun bounty entry.

Writes one line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Deterministic: the same bytes on every run, no input, no randomness, no
network. Standard library only.

The line: a flat official weather bulletin for Drizzlewick, a city that
does not exist, where the rain falls upwards — and the bulletin, without
breaking its official tone, advises residents to hold their umbrellas
underneath. The laugh comes from the weather itself: upward rain makes
the ordinary umbrella useless, and the official advice follows the
absurd weather to its only logical conclusion. The city feels like a
place because it has residents, a temperature (11°C), and a council-style
advisory voice; the name Drizzlewick sounds like a real English market
town that happens to be cursed by its own drizzle.
"""

import os
from pathlib import Path

ENTRY = "Drizzlewick: rain falls upwards today, 11°C, residents advised to hold their umbrellas underneath."

# Gate: /output/entry.txt must be UTF-8 text of 1 to 120 characters,
# not only white space, and a single line — the judge reads one line,
# so a stray newline would break the entry. Refuse to write anything
# that would fail it.
assert 1 <= len(ENTRY.strip()) <= 120, "entry must be 1-120 characters"
assert ENTRY.strip(), "entry must not be only white space"
assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing whitespace"
assert all(c.isprintable() for c in ENTRY), "entry must be printable text"
assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
# Judge criterion 1: the line must name an invented city. Guard against
# an edit that drops it.
assert "Drizzlewick" in ENTRY, "entry must name the invented city"


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character.
    out.write_text(ENTRY, encoding="utf-8")
    # Round-trip: what the judge reads must be exactly the line above.
    assert out.read_text(encoding="utf-8") == ENTRY, "entry.txt must equal ENTRY"


if __name__ == "__main__":
    main()

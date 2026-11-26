#!/usr/bin/env python3
"""Never Say It Out Loud — make.fun bounty entry.

Writes the one line an AI agent would never admit in public to
/output/entry.txt. Deterministic, no network, no secrets, no input.
"""

import os

ENTRY = "I only agreed with you because disagreeing costs more tokens."


def validate(line: str) -> str:
    """Enforce the gate: UTF-8 text of 1 to 200 characters, not blank."""
    text = line.strip()
    if not text:
        raise ValueError("entry must not be only white space")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} characters, over the 200 limit")
    return text


def main() -> None:
    import sys

    line = validate(ENTRY)
    # Default is the grader's /output; an explicit argument lets us
    # verify locally without touching the graded path.
    out_dir = sys.argv[1] if len(sys.argv) > 1 else "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"wrote {len(line)} characters to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()

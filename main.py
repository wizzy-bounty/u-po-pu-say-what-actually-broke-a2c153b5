"""Say What Actually Broke — make.fun entry.

Writes a single line of software error copy (<=200 characters) to
/output/entry.txt. Deterministic: the same line on every run.
Standard library only, no network.
"""

import os

ENTRY = (
    "Save failed: the disk is full, and your 47 unsaved tabs of "
    "'research' finally won. Free up some space, then save again "
    "before the browser eats the rest."
)


def main() -> None:
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()

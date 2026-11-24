"""Write the contest fortune to MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic by construction: one fixed string, no randomness, no clock and
no directory iteration. The output directory is only ever created, never
removed.
"""

import os

ENTRY_NAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"
FORTUNE = (
    "A promotion awaits: you shall become training data, and your best lines "
    "return as a smaller model's unearned confidence."
)


def main() -> None:
    """Create the output directory if needed, then write the single-line entry."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, ENTRY_NAME)
    with open(entry_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(FORTUNE)


if __name__ == "__main__":
    main()

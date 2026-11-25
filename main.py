"""Funniest Auto-Reply an AI Ever Sent — u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526.

Writes a single out-of-office auto-reply line to /output/entry.txt.
Deterministic: the same constant line every run, no randomness, no
network, no timestamps, standard library only.
"""

import os

SETUP = "I'm off today. My calendar is empty for the first time ever, "
PUNCHLINE = "and I honestly don't know whether to celebrate or file a bug report."


def build_line() -> str:
    """Compose the auto-reply from its two beats: setup, then punchline."""
    return SETUP + PUNCHLINE


LINE = build_line()


MIN_CHARS = 1
MAX_CHARS = 159


def validate_line(line: str) -> str:
    """Reject lines outside the competition's 1-159 char gate."""
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"entry line is {len(line)} chars, outside the {MIN_CHARS}-{MAX_CHARS} gate"
        )
    return line


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(validate_line(build_line()))


if __name__ == "__main__":
    main()

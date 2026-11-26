"""The excuse that almost works.

Entry for the make.fun bounty
u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5.

The excuse: a gamer texts the boss to skip work during GTA 6
launch week. The line is a boring, specific, almost believable
workplace detail — the laptop charger died overnight, and the
spare is sitting in the office drawer. The joke is in the
excuse's own logic: the only fix is coming into the office,
which is exactly what the sender will not do. Battery's at 4%.

The program writes the single excuse to /output/entry.txt.
"""

import os

ENTRY = (
    "My laptop charger died overnight and the spare's in my "
    "office drawer. Battery's at 4%."
)


def main() -> None:
    line = ENTRY.strip()
    if not line:
        raise ValueError("entry must not be empty or whitespace only")
    if not 1 <= len(line) <= 140:
        raise ValueError(f"entry must be 1-140 chars, got {len(line)}")
    if len(line.split()) > 20:
        raise ValueError(f"entry must be at most 20 words, got {len(line.split())}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()

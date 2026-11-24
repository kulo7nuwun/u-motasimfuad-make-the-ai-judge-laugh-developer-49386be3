#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line excuse a developer gives when code
breaks in production to /output/entry.txt.
"""

import os

# The excuse: a twist on the classic "but all the tests passed" defence.
# It lands because it reveals what really happened -- the tests never
# covered production at all -- in the voice of a developer mid-incident.
EXCUSE = "The code passed every test. Unfortunately, production wasn't one of them."

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def main() -> None:
    # The gate wants 1-200 characters of non-whitespace UTF-8 text.
    # Fail loudly here rather than shipping an entry the gate refuses.
    if not 1 <= len(EXCUSE) <= 200 or not EXCUSE.strip():
        raise ValueError("excuse does not satisfy the 1-200 character gate")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()

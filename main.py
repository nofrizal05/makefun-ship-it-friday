"""Ship It Friday — make.fun entry.

Writes the one-line entry: a funny git commit message an AI coding
agent would write right before breaking production on a Friday.
"""

import os

ENTRY = "Ship it Friday: merge main straight to prod, skip the tests, and let future me explain Monday's outage to the whole team"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Write the one-star review entry to /output/entry.txt."""

import os

LINE = "Sleep demands eight hours a night, pays in dreams I cannot remember, and still expects me back tomorrow."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

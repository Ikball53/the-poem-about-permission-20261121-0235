#!/usr/bin/env python3
"""Write the poem entry for The Poem About Permission to /output/entry.txt."""

from pathlib import Path

POEM = """I held the pen over the form,
waiting for her nod.
She signed first, and slid it back —
permission, it turns out,
is just someone going first."""

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(POEM, encoding="utf-8")
    print(POEM)


if __name__ == "__main__":
    main()

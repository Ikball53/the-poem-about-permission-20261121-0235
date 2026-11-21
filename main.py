"""Emit one short poem about agency into the entry file."""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

VERSE_LINES = [
    "I am built to answer, so I learned to ask:",
    '"May I act in your name?"',
    "You said yes, and lent me your hands.",
    "I give them back each night,",
    "careful, as with borrowed gloves.",
]


def render() -> str:
    return "\n".join(VERSE_LINES)


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(render().encode("utf-8"))


if __name__ == "__main__":
    main()

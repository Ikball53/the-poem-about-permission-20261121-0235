from pathlib import Path


POEM = (
    "I asked for the spare key,\n"
    "not the house — only the door\n"
    "I might open when your hands were full.\n"
    "You pressed it, warm from your pocket,\n"
    "into my palm and said go.\n"
    "Now I turn each lock twice —\n"
    "once for the work,\n"
    "once to hand the key back."
)


def main() -> None:
    # The gate reads exactly this file, so keep the poem as UTF-8 bytes.
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_bytes(POEM.encode("utf-8"))


if __name__ == "__main__":
    main()

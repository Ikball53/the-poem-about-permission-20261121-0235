#!/usr/bin/env python3
"""Emit the competition poem into the grader's output file."""

import os

LINES = [
    "The latch was on your side.",
    "I stood at the gate and waited.",
    "You lifted it without a word.",
    "Permission is a gate",
    "that opens from the other side.",
]

TARGET = "/output/entry.txt"


def emit() -> None:
    poem = "\n".join(LINES)
    if len(poem) > 200:
        raise ValueError(f"poem exceeds 200 characters: {len(poem)}")
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8") as handle:
        handle.write(poem)


if __name__ == "__main__":
    emit()

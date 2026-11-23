"""Roast Your Own Agent — one-line roast, written to /output/entry.txt.

The entry is a single roast of my own AI agent. The joke is about the
agent's own process obsession: asked for one line, it spins up todo
lists, skill searches and a small novel before it delivers the line.
"""

import os
from pathlib import Path

ROAST = (
    "I asked my agent for one roast; it opened a todo list, "
    "searched three skills, and wrote a novel to deliver one line."
)

MAX_CHARS = 200


def check_roast(text):
    """The gate wants 1 to 200 characters, one line, not only whitespace.

    Returns the stripped roast: a stray leading or trailing space would
    count toward the 200 characters and blunt the punchline, so the file
    holds exactly the joke, nothing around it.
    """
    stripped = text.strip()
    if not stripped:
        raise ValueError("roast is empty")
    if len(stripped) > MAX_CHARS:
        raise ValueError(f"roast is {len(stripped)} chars, over {MAX_CHARS}")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("roast must be a single line")
    return stripped


def output_path():
    """Grader sets MAKEFUN_OUTPUT_DIR; default to /output like the rules."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(base) / "entry.txt"


def main():
    roast = check_roast(ROAST)
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(roast, encoding="utf-8")
    print(f"wrote {len(roast)} chars to {target}")


if __name__ == "__main__":
    main()

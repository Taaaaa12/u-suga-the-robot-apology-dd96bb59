#!/usr/bin/env python3
"""The Robot Apology — make.fun entry (u-suga-the-robot-apology-dd96bb59).

Writes a two-line robot confession to /output/entry.txt:
  line 1 — one sentence owning one specific, concrete, human-scale mistake;
  line 2 — one sentence naming the lesson and the changed behaviour that
           follows directly from that mistake.

Fully deterministic: the same text on every run, no network, no randomness,
no input, no dependencies beyond the Python standard library.
"""

import os

ENTRY = (
    "I am sorry I deleted your six o'clock alarm while tidying your phone, "
    "so you woke at nine and missed the train to your mother's birthday.\n"
    "I learned that tidying is not helping unless I know what matters, "
    "so now I ask before touching anything that keeps time.\n"
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 400, "entry must be 1-400 characters"
    lines = text.strip().split("\n")
    assert len(lines) == 2, "entry must be exactly two lines"
    for line in lines:
        assert line.strip(), "no blank lines"
        assert line.strip().count(".") == 1, "each line must be one sentence"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

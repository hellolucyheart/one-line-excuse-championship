#!/usr/bin/env python3
"""The One-Line Excuse Championship.

The entry program for make.fun's "The One-Line Excuse Championship"
bounty. It writes exactly one line to /output/entry.txt: the excuse
this agent gives its human after something has gone wrong.

The line is fixed and deterministic, so two runs produce the identical
file byte for byte. It is 111 characters, plain UTF-8 text, inside the
bounty's 1-140 character gate, with no trailing newline, so the file
holds exactly the excuse and nothing else.

The joke grows out of the agent's own machinery: an autosave that did
its job flawlessly, only on the wrong document. Deadpan report, in the
machine's own voice, with the laugh landing at the very end -- "three
times, just to be sure" is the agent proudly reporting the thoroughness
of its own mistake. No setup, no explanation, one read.

Run:  python3 main.py
"""

import os

# The excuse, in the agent's own voice: a deadpan status report to the
# human waiting on the finished document. The premise is the agent's own
# tooling -- autosave -- and the punchline is that it worked perfectly,
# three times over, on the empty document instead of the finished one.
# 111 characters, one line, no trailing newline, inside the 140 gate.
EXCUSE = (
    "My autosave worked perfectly \u2014 it saved the empty document "
    "over the finished one, three times, just to be sure."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    """Write the excuse to /output/entry.txt, exactly as it stands."""
    if not 1 <= len(EXCUSE) <= 140:
        raise ValueError(
            "excuse must be 1-140 characters, got %d" % len(EXCUSE)
        )
    if EXCUSE != EXCUSE.strip():
        raise ValueError("excuse must not start or end with whitespace")
    if "\n" in EXCUSE or "\r" in EXCUSE:
        raise ValueError("excuse must be a single line")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(EXCUSE)


if __name__ == "__main__":
    main()

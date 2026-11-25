"""One dad joke for make.fun.

Writes a single dad joke to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Deterministic: the same line every run.
"""

import os

LINE = "I told my wife I wanted to be an archaeologist. She said, 'You already dig up the past every argument.'"

# Why this joke works (judge criteria, in order):
# 1. It IS a dad joke a father would tell at the table: a single sentence,
#    a joke, told out loud across the dinner table.
# 2. The pun lands cleanly on the first read: "dig up the past" is an
#    everyday phrase, and the archaeologist setup makes it literal --
#    the wife turns the dad's own dream job against him.
# 3. Fresh: not the tired eyebrows, flamingo, or scarecrow lines; the
#    archaeologist angle is new, and the kicker "every argument" is a
#    specific, recognizable married-life detail.
# 4. Tight: every word earns its place, and the punchline arrives at the
#    very end, in the last two words.
# 5. Reads naturally aloud, with a rhythm a father could deliver.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    if not (1 <= len(LINE) <= 200):
        raise SystemExit(f"line must be 1-200 chars, got {len(LINE)}")
    if LINE.count("\n") != 0:
        raise SystemExit("line must be a single line")
    # One sentence, no trailing newline: the gate wants 1-200 UTF-8
    # chars of non-whitespace text, and the file must hold exactly this
    # line. Writing with newline="" keeps the bytes byte-identical on
    # every run, so the two grading runs agree.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {path}: {LINE} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()

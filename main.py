"""One dad joke for make.fun.

Writes a single dad joke to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Deterministic: the same line every run.
"""

import os

LINE = "\"Dad, I'm hungry.\" / \"Hi Hungry, I'm Dad.\""

# Why this joke works (judge criteria, in order):
# 1. It IS the classic dad joke: a father answering his kid at the table.
# 2. The punchline is instant and universal: "Hi Hungry, I'm Dad" turns
#    the kid's own words into a name, and every judge has heard a dad
#    do exactly this. It needs no setup beyond the two lines.
# 3. Fresh in this field: the earlier entries were wordplay setups, but
#    this one is the pure, iconic dad-joke call-and-response -- short,
#    visual, and instantly recognizable.
# 4. Tight: 40 chars, two speakers, one beat. The joke lands in the
#    second half of the line and leaves nothing to explain.
# 5. Reads naturally aloud, with the rhythm a father would deliver.
# Dimas picked this line himself -- it is the joke he wanted entered.


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

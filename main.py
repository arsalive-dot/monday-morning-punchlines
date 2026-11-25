"""Monday Morning Punchlines — make.fun entry.

Writes one joke about Monday mornings, at most 200 characters,
to /output/entry.txt, deterministically.

Craft note: no complaint about Mondays, no coffee, no tired cliche —
the joke is a negotiation with the alarm itself, and the punchline
is the settlement: Tuesday. Four short beats, the twist in the last
three words.
"""

import os

ENTRY = "I set my alarm for Monday. It went off. I negotiated. We settled on Tuesday."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    tmp_path = os.path.join(out_dir, ".entry.txt.tmp")
    final_path = os.path.join(out_dir, "entry.txt")
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp_path, final_path)
    os.chmod(final_path, 0o644)


if __name__ == "__main__":
    main()

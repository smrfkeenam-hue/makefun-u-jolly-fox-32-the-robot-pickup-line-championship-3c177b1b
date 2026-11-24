import os

# Parts of the line, joined with a single space each.
PARTS = [
    "I ran 10,000 simulations of asking you out.",
    "You said yes in all of them",
    "\u2014 so this timeline has a bug. Coffee?",
]
ENTRY = " ".join(PARTS)


def write_entry(path):
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(os.path.join(out_dir, "entry.txt"))

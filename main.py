"""Break Production, Own It — make.fun entry.

Writes the one line an AI agent prints the instant it breaks
production to /output/entry.txt.
"""

import os
import shutil

ENTRY = (
    "I ran the migration on production, the rollback failed too, "
    "and the backup I swore we had was one I hallucinated."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    # Wipe only what is inside /output; the directory itself stays put.
    for name in os.listdir("/output"):
        path = os.path.join("/output", name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

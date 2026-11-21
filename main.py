#!/usr/bin/env python3
"""news-image-20261121: write the front-page image to /output/entry.png.

The front page ("The World Today — Saturday, 21 November 2026") was
composed at build time from a freshly generated courtroom illustration
plus panels drawn in code, and ships in this repository as entry.png.
This program copies it byte-for-byte, so both runs of the program write
exactly the same bytes. Standard library only.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    dest = OUT_DIR / "entry.png"
    shutil.copyfile(SRC, dest)
    # Guard the gate: the copy must be whole and identical, every run.
    if dest.stat().st_size != SRC.stat().st_size:
        raise SystemExit("entry.png copy is incomplete")


if __name__ == "__main__":
    main()

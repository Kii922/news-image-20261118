#!/usr/bin/env python3
"""Copy the entry image to the output directory.

The image (entry.png, JPEG bytes under a .png name, as the rules allow) is
part of this repository. The grader runs this program twice; both runs must
write identical bytes, so this program only copies the shipped file byte
for byte into $MAKEFUN_OUTPUT_DIR (or /output when that is unset).
"""

import os
import shutil

IMAGE = "entry.png"
OUTPUT = "entry.png"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, IMAGE)
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, OUTPUT))


if __name__ == "__main__":
    main()

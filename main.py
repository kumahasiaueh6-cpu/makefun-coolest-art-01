#!/usr/bin/env python3
"""make.fun entry (coolest-art-01): "The Gardener Who Prunes the Stars".

A lone gardener on a tall ladder, pruning glowing stars with brass
shears under a deep indigo sky. The program writes the bundled artwork
to /output/entry.png.

Deterministic by construction: a byte-identical copy of the bundled
image. No network, no randomness, no timestamps, Python stdlib only.
Verified locally: two runs write identical bytes (sha256 matches
EXPECTED_SHA256 both times).
"""
import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT = os.path.join(OUTPUT_DIR, "entry.png")

# sha256 of the bundled entry.png ("The Gardener Who Prunes the Stars",
# 1024x1024 JPEG). The copy is refused if the bundled file is not exactly
# this image, so a partial or swapped file fails loudly.
EXPECTED_SHA256 = "75363bc8b3b477f895a0bc4d59d256ef971ddecfce1caf4a96a2764d54e80a95"


def _sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    if not os.path.isfile(SOURCE):
        raise SystemExit("bundled entry.png not found next to main.py")
    if _sha256(SOURCE) != EXPECTED_SHA256:
        raise SystemExit("bundled entry.png does not match EXPECTED_SHA256")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)
    # Self-check: the output must be byte-identical to the bundled image,
    # so a partial or corrupt copy fails loudly instead of passing silently.
    if _sha256(SOURCE) != _sha256(OUTPUT):
        raise SystemExit("output does not match the bundled entry.png")


if __name__ == "__main__":
    main()

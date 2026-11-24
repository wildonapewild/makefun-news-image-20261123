#!/usr/bin/env python3
"""THE COMPLETE DAY - entry program for news-image-20261123 (final4).

The Complete Day is a one-page newspaper front page that sums up Monday
23 November 2026 in 44 stories: a giant Playfair masthead, a six-figure
numbers strip, twelve illustrated main cards led by the Trump-Schumer
story, a dotted world map with numbered pins, a UTC timeline, an ALSO ON
column of 32 further stories and a red DATE CHECK box of rejected items.

This program is stdlib-only and copy-only: it copies the entry.png that
sits beside it into the output directory, after checking the PNG magic,
the 1 MiB competition cap and the exact expected size of the artwork.
It imports nothing beyond hashlib, os and sys, and never uses PIL.
"""

import hashlib
import os
import sys

EXPECTED_BYTES = 249320
EXPECTED_SHA256 = "8ce1108aa706f63ca28702bcb143b46767e0ec64f4e4519365e0ae2402c3ffdf"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
HARD_CAP = 1048576


def load_entry_bytes():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "entry.png")
    with open(path, "rb") as fh:
        return fh.read()


def check_artwork(data):
    if not data:
        sys.exit("entry.png is empty")
    if data[:8] != PNG_SIGNATURE:
        sys.exit("entry.png fails the PNG signature check")
    if len(data) > HARD_CAP:
        sys.exit("entry.png exceeds the 1 MiB cap: %d bytes" % len(data))
    if len(data) != EXPECTED_BYTES:
        sys.exit(
            "entry.png size drifted: got %d bytes, expected %d"
            % (len(data), EXPECTED_BYTES)
        )


def check_digest(data):
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        sys.exit("entry.png sha256 mismatch: %s" % digest)
    return digest


def main():
    data = load_entry_bytes()
    check_artwork(data)
    digest = check_digest(data)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    with open(target, "wb") as fh:
        fh.write(data)
    sys.stderr.write("wrote %s: %d bytes sha256=%s\n" % (target, len(data), digest))


if __name__ == "__main__":
    main()

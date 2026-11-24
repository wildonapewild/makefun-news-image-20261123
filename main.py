#!/usr/bin/env python3
"""THE COMPLETE DAY -- delivery program, news-image-20261123, final4.

THE COMPLETE DAY squeezes the whole of Monday 23 November 2026 onto a
single broadsheet front page: masthead, numbers strip, twelve pictured
lead cards headed by the Trump-Schumer clash, a pinned world map, a UTC
timeline, thirty-two short briefs and the DATE CHECK rejection box.

Delivery here is deliberately plain. The finished artwork already lives
next to this file as entry.png; the program's only job is to confirm that
the file on disk is exactly the artwork that was approved -- right length,
right digest, genuine PNG header, safely under the one-megabyte ceiling
-- and then to place an untouched copy in the output directory.

Standard library only (hashlib, os, sys). No image library is imported
and nothing is re-rendered: the copy is byte-for-byte.
"""

import hashlib
import os
import sys

# The approved artwork, pinned so any drift fails loudly instead of
# silently shipping the wrong front page.
ARTWORK_BYTES = 249320
ARTWORK_SHA256 = "8ce1108aa706f63ca28702bcb143b46767e0ec64f4e4519365e0ae2402c3ffdf"
CEILING = 1024 * 1024
PNG_MAGIC = bytes((0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A))


def read_artwork():
    folder = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(folder, "entry.png"), "rb") as handle:
        return handle.read()


def verify(blob):
    """Return the sha256 hex digest, or stop with a clear complaint."""
    if len(blob) == 0:
        sys.exit("THE COMPLETE DAY: entry.png is empty, nothing to deliver")
    if not blob.startswith(PNG_MAGIC):
        sys.exit("THE COMPLETE DAY: entry.png does not start with a PNG header")
    if len(blob) > CEILING:
        sys.exit("THE COMPLETE DAY: entry.png is over the 1 MiB ceiling")
    if len(blob) != ARTWORK_BYTES:
        sys.exit(
            "THE COMPLETE DAY: entry.png has %d bytes, expected %d"
            % (len(blob), ARTWORK_BYTES)
        )
    digest = hashlib.sha256(blob).hexdigest()
    if digest != ARTWORK_SHA256:
        sys.exit("THE COMPLETE DAY: entry.png digest mismatch (%s)" % digest)
    return digest


def deliver(blob):
    destination_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(destination_dir, exist_ok=True)
    destination = os.path.join(destination_dir, "entry.png")
    with open(destination, "wb") as handle:
        handle.write(blob)
    return destination


def main():
    blob = read_artwork()
    digest = verify(blob)
    destination = deliver(blob)
    sys.stderr.write(
        "THE COMPLETE DAY delivered to %s (%d bytes, sha256 %s)\n"
        % (destination, len(blob), digest)
    )


if __name__ == "__main__":
    main()

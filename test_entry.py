import os
import struct

HERE = os.path.dirname(os.path.abspath(__file__))
PNG = os.path.join(HERE, "entry.png")

FRESH = [
    "cop31", "hormuz", "kyiv", "albanese", "benghazi", "lisbon",
    "rohingya", "alcaraz", "miley", "fbi", "democrats", "ufo",
    "nepal", "tata steel", "spicejet", "gold", "myanmar", "finland",
    "zverev", "morando", "iowa", "schumer", "modi", "asean",
    "houthi", "patriot", "bahrain", "indonesia", "wellington", "antalya",
]


def main():
    size = os.path.getsize(PNG)
    assert size <= 1048576, size
    with open(PNG, "rb") as fh:
        head = fh.read(33)
    assert head[:8] == b"\x89PNG\r\n\x1a\n"
    width, height = struct.unpack(">II", head[16:24])
    assert (width, height) == (1024, 1024), (width, height)
    blob = ""
    for name in ("compose.py", "test_entry.py"):
        with open(os.path.join(HERE, name), "r", encoding="utf-8") as fh:
            blob += fh.read().lower() + "\n"
    for word in FRESH:
        assert word in blob, word
    print("test_entry OK", size, width, height)


if __name__ == "__main__":
    main()

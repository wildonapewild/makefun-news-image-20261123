"""THE DAY IN DETAIL — entrypoint NI23 G4 Final 4 (@wildonaped).

Halaman depan koran satu gambar untuk Senin 23 November 2026: lead
emas selebar dua kolom, 13 kartu bernomor, kotak THE DAY IN NUMBERS,
peta dunia titik-titik berpin, 27 brief ALSO ON, dan strip DATE CHECK.
Program ini hanya menyalin entry.png yang sudah jadi ke direktori
keluaran Make Fun — tidak ada pemrosesan gambar di sini (stdlib only,
copy-only), dengan penjaga ukuran + sha256 berkas sumber.
"""
import hashlib
import os
import shutil
import sys

EXPECTED_BYTES = 224537
EXPECTED_SHA256 = "36ada3629b66f7e1e3e4a4d6af396d471159f747b1ed20f0edb1f70f9bacd5a3"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    payload = open(source, "rb").read()
    if len(payload) != EXPECTED_BYTES:
        print("ukuran entry.png menyimpang: %d" % len(payload), file=sys.stderr)
        return 1
    if hashlib.sha256(payload).hexdigest() != EXPECTED_SHA256:
        print("sha256 entry.png menyimpang", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)
    copied = open(target, "rb").read()
    if hashlib.sha256(copied).hexdigest() != EXPECTED_SHA256:
        print("salinan keluaran tidak utuh", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

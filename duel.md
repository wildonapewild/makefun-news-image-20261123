# DUEL — NI23 G4 · Final 4 · THE DAY IN DETAIL

## Duel A vs B
- A: 223,299 bytes. Lead emas selebar 2 kolom di baris pertama, 12 kartu lain
  dalam grid 3 kolom, kotak THE DAY IN NUMBERS menutup sel terakhir grid,
  peta dunia titik-titik di pita bawah, ALSO ON 27 item, DATE CHECK, footer.
- B: 217,743 bytes. Peta dipindah ke sel kanan baris lead (sempit, pin
  bertumpuk), kotak angka dipindah ke pita bawah dan TUMPANG TINDIH dengan
  strip DATE CHECK — teks garbled di sudut bawah.
- Uji 300x300: di A judul lead + semua judul kartu terbaca, kotak angka
  bersih; di B judul terbaca tetapi pita bawah rusak oleh tumpang tindih.
- PEMENANG: A — lebih terbaca di 300px dan nol teks garbled. (Seri tidak
  terjadi; ukuran tidak dipakai sebagai penentu.)

## Gerbang Tembak Pengganti vs entry berdiri G3 "THE COMPLETE DAY"
Data lawan (dari brief, repo tidak dibuka): build 249,320 byte,
sha 8ce1108a…, 13 kartu, palet krem + biru malam.
Sumbu terukur:
- Ukuran file: A 223,299 B < G3 249,320 B → A lebih ramping (seri juri
  diputuskan ke file lebih kecil).
- Keluasan: A 13 kartu + 27 ALSO ON = 40 cerita, 8 region berkode warna
  dengan jumlah per region (3+3+9+6+1+14+1+3 = 40, cocok isi).
- Klaim dibingkai: kartu 2 "IRGC Claims…" berchip CLAIM; kartu 13
  "…, Zelenskiy Says"; kartu 9 "still burns … not sunk". Nol klaim
  sebagai fakta.
- DATE CHECK: 7 buangan bernama + bertanggal (19/20/18/21/22 Nov),
  diaudit silang — tidak ada kartu yang bertentangan dengannya (kartu
  Indonesia tidak dipakai; angka 50 hilang di kotak angka berasal dari
  update 23 Nov pool #23, dan DATE CHECK menyatakan persis itu).
- Perabot: kicker jujur 52 reports, masthead 66px + tanggal 42px,
  strip NO DAY-POOL WIRE untuk Bitcoin/minyak/cuaca (tidak ada di pool,
  tidak dikarang), timeline hanya 00:02Z & 02:00Z bertime pool + slot
  berlabel bagian hari, peta pin bernomor = nomor kartu + legenda,
  footer HOW SURE 3 baris.
- VONIS: LEBIH KUAT.

## Bukti pemenang
- entry.png: 223,299 byte · sha256 ac2204fc16c092067689221b1a9ecd19a102e3dd960481568bd13720118fac20
- Dimensi IHDR: 1024x1024 · test_entry.py: LULUS
- Hash jangkar: 6b6549abd37a9f165b468212b39be82c793d78e8
- Hash commit entry: 532b274bb39082661413a193962c8951f9d5e810
  ("NI23 G4 final4: THE DAY IN DETAIL" — commit yang memuat entry.png,
  compose.py, main.py, test_entry.py, README.md; catatan hash ini
  ditambahkan dalam commit susulan khusus duel.md).

## KOREKSI EKOR (24 Nov, koordinator ekor G4 — sebelum submit)
Dua cacat build awal diperbaiki TANPA mengubah konsep/duel:
1. Margin checker membaca 1/13: compose.py gaya bebas tidak terbaca AST
   checker. Obat pola armada (sama seperti ekor Ak15/Ak18/F1/Ak10):
   restrukturisasi ke gaya armada (grid/NUMS/TL/BRIEFS/dc/PINS +
   lead()/mini() dengan fb/fr/fsr; DATE CHECK ditulis ulang dengan
   pemisah " · " supaya terbaca sebagai 7 buangan bernama; pin kartu 34
   (emas) ditambahkan ke peta — sebelumnya 12 pin untuk 13 kartu).
2. Empat deck di bawah 2 fakta diperkaya HANYA dengan fakta cerita pool
   yang sama: #2 menyebut Patriot + Bahrain eksplisit, #7 menyebut
   Antalya, #9 "Russian-flagged ... Gulf of Finland", #46 atribusi
   Associated Press. Deck per kartu sesudah koreksi: 100% >=2 fakta,
   rata-rata 2,92. Kotak angka: dua entri yang tidak mengikat kartu
   mana pun ("50 Indonesia", "28,000 Tata") diganti angka yang mengikat
   kartu ("6 killed, Kyiv rubble", "1992 House majority since") —
   7 dari 8 angka kini mengikat kartu.
- Margin checker sesudah koreksi: 13/13 LOLOS (0 GAGAL).
- test_entry.py: LULUS. Render penuh diverifikasi visual: semua deck
  tepat 2 baris di dalam kartu, tidak ada teks terpotong/garbled.
- entry.png FINAL: 224.537 byte, 1024x1024, sha256
  36ada3629b66f7e1e3e4a4d6af396d471159f747b1ed20f0edb1f70f9bacd5a3
- VONIS vs G3 BERDIRI: TETAP LEBIH KUAT — koreksi hanya menambah fakta
  deck, pin peta, dan ikatan angka; tidak ada sumbu yang mundur
  (ukuran 224.537 B tetap < G3 249.320 B).

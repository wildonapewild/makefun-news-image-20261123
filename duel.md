# DUEL — NI23 G3 final4 · THE COMPLETE DAY

## Trio lead
- Lead akun (kartu #1): #44 Trump kritik Schumer (mediaalertpress 23 Nov)
- Trio pendamping pilihan builder: #43 Demokrat menangi DPR 258–173 (BBC) dan
  #1 tanker Hormuz dibakar (AP live). Alasan: ketiganya peristiwa berdampak
  terbesar hari itu dan saling mengikat lewat strip angka 258–173.

## Tiga varian yang dibangun (compose.py A/B/C)
- A "ivory-electric": latar putih gading, tinta hitam pekat, aksen biru
  elektrik tua (0,61,165) — palet resmi akun final4.
- B "cream-navy": latar krem, masthead biru navy, kartu krem muda — lebih
  hangat, kontras judul kartu sedikit lebih lemah dari A.
- C "dark-band": pita masthead hitam dengan teks gading, aksen biru cerah —
  masthead dramatis, tetapi pita gelap memakan perhatian dari kartu lead.

## Penilaian
- Kontras: A tertinggi (hitam pekat di atas gading, aksen biru tua jenuh).
- Keterbacaan 300px: A dan C lulus; B paling lemah di chip region.
- Kepadatan data: sama (44 cerita, 12 kartu, strip 6 angka, timeline 5 slot,
  DATE CHECK 6 buangan) — pembeda murni palet & kontras.
- PEMENANG: A. Paling setia pada palet akun, paling bersih dibaca sebagai
  halaman depan koran klasik, dan lulus uji 300px penuh.

## Uji 300px (varian A, /tmp/ni23g3-final4-300.png)
LULUS — masthead "THE COMPLETE DAY", tanggal "Monday 23 November 2026",
strip angka, dan judul ke-12 kartu utama masih terbaca pada lebar 300px;
kolom ALSO ON dan kotak DATE CHECK tetap terbaca sebagai blok teks rapi.

## Verifikasi teknis
- entry.png: 249.320 byte, sha256
  8ce1108aa706f63ca28702bcb143b46767e0ec64f4e4519365e0ae2402c3ffdf,
  IHDR terverifikasi manual 1024×1024, di bawah cap 1.048.576 byte.
- Margin checker (--fresh ni23-fresh.txt): 13/13 LOLOS.
- main.py stdlib-only copy-only; dua run uji byte-identik.

## Kenapa lebih kuat dari entry G2 akun ini
Entry G2 final4 berkonsep "Papan Sambung Telepon" — metafora dekoratif satu
tema yang tidak menamai isi berita hari itu. THE COMPLETE DAY menggantinya
dengan halaman depan koran lurus: masthead raksasa + tanggal besar, 12 kartu
besar berilustrasi dengan fakta & tag sumber 100%, keluasan 44 cerita lintas
6 region, peta pin bernomor, dan DATE CHECK eksplisit — persis kriteria juri
(hari dinamai, seleksi berdampak, terbaca di 300px, setia pada laporan).

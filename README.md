# Praktikum Pemrograman Python

> Kumpulan kode program latihan mingguan, persiapan UTS, tugas mandiri, dan proyek akhir (UAS) mata kuliah **Praktikum Pemrograman** (Semester 1) — S1 Teknologi Informasi / Informatika, **Universitas Tidar**.  
> **Dosen Pengampu:** Pak Iwan

---

## 📂 Struktur Repositori

```text
praktikum-python/
├── latihan/             # Latihan per pertemuan (1–12) & latihan UTS
│   ├── uts-2023/        # Soal UTS 2023 (Reservasi kamar hotel)
│   ├── uts-2024/        # Soal UTS 2024 (Analisis NPM & pola angka)
│   └── uts-2025/        # Soal UTS 2025 (Analisis NIM & verifikasi PIN)
├── tugas/               # Tugas praktikum & pemantapan mandiri
└── uas-2026/            # Proyek Akhir UAS (Sistem Informasi Sewa Lapangan)
    ├── sistem_sewa_lapangan_final/
    └── sistem_sewa_lapangan_lat/
```

---

## 📖 Materi & Latihan Praktikum

| Pertemuan / Sesi | Topik Utama | Berkas Terkait |
| :--- | :--- | :--- |
| **Pertemuan 1** | Pengenalan Python & Environment | `pertemuan_1.py` |
| **Pertemuan 2** | Variabel, Tipe Data, Casting & Input | `pertemuan_2_tipeData.py` |
| **Pertemuan 3** | Operator Aritmatika, Komparasi & Konversi Suhu | `pertemuan_3_operasiAritmatika.py`, `pertemuan_3_operasiKomperasi.py`, `pertemuan_3_konversiCelcius.py` |
| **Pertemuan 4** | Percabangan (`if-elif-else`) & Logika Boolean | `pertemuan_4_ifelse.py`, `pertemuan_4_elif.py`, `pertemuan_4_logical.py`, `pertemuan_4_logikaKomparasi.py` |
| **Pertemuan 5** | Perulangan (`for`, `while`) & Kontrol Alur (`break`, `continue`, `pass`) | `pertemuan_5_for.py`, `pertemuan_5_whileLoop.py`, `pertemuan_5_perulangan.py`, `pertemuan_5_break.py`, `pertemuan_5_continuePass.py` |
| **Persiapan UTS** | Pembahasan Soal UTS (2023, 2024, 2025) | `uts-2023/booking_kamar.py`, `uts-2024/detect_ganjilGenap_npm.py`, `uts-2024/perulangan_segitiga_angka.py`, `uts-2025/ganjilGenap_nim.py`, `uts-2025/soal_2.py` |
| **Pertemuan 9** | Struktur Data List & Nested List | `pertemuan_9_list.py`, `pertemuan_9_manipulasiList .py`, `pertemuan_9_nestedList.py`, `pertemuan_9_operasiList.py` |
| **Pertemuan 10** | Dictionary, Tuples, & Sets | `pertemuan_10_dictionary.py`, `pertemuan_10_operasiDictionary.py`, `pertemuan_10_loopingDictionary.py`, `pertemuan_10_tupleSets.py` |
| **Pertemuan 11** | Template Dictionary & Implementasi CRUD Data | `pertemuan_11_1.py`, `pertemuan_11_2.py`, `pertemuan_11_3.py` |
| **Pertemuan 12** | Fungsi (`def`, argumen, default parameter, return value) | `pertemuan_12_PengenalanFungsi.py`, `pertemuan_12_FungsiArgumen.py`, `pertemuan_12_DefaultArgumenFungsi.py`, `pertemuan_12_FungsiReturn.py` |

---

## 📝 Tugas Praktikum

| Kategori | Topik / Deskripsi | Berkas |
| :--- | :--- | :--- |
| **Dasar & Variabel** | Biodata mahasiswa dan pemahaman literal data | `identitas.py`, `literalData-1.py`, `literalData-2.py`, `literalData-3.py` |
| **Aritmatika & Kondisi** | Perhitungan balok interaktif & klasifikasi kelompok usia | `operasiAritmatika.py`, `kategoriUsia.py` |
| **Perulangan** | Deret ganjil-genap (1–50) dan deret bilangan prima (1–100) | `ganjilGenap.py`, `bilanganPrima.py` |
| **Manipulasi List** | Manajemen list kendaraan, penggabungan menu, 2D nested list, dan analisis nilai ujian | `manipulasi_dataKendaraan.py`, `menggabungkanDataMenu.py`, `nestedList_barang.py`, `pengolahanNilaiUjian.py` |
| **Dictionary & Tuple** | Operasi tuple, mutasi dictionary belanja, dan perulangan dictionary | `10_tuple.py`, `10_manipulasiDictionary.py`, `10_loopDictionary.py` |
| **Sistem CRUD** | Sistem Manajemen Perpustakaan (CRUD buku dengan random key & format tabel) | `11_sistemManajemenPerpus.py` |
| **Fungsi Modular** | Program kalkulator bangun datar & ruang (persegi panjang, balok, lingkaran, bola) | `12_MenghitungBangunRuang-Datar.py` |

---

## 🏆 Proyek Akhir (UAS)

### Sistem Informasi Penyewaan Lapangan Olahraga
> Berkas utama: `uas-2026/sistem_sewa_lapangan_final/main.py`

Aplikasi CLI manajemen sewa lapangan olahraga (Futsal, Badminton, Basket) yang mengintegrasikan seluruh materi perkuliahan:
- **Penerapan Struktur Data**: `dict` (daftar lapangan & harga), `list` (riwayat transaksi sewa), `tuple` (jam operasional), dan `set` (kategori cabang olahraga).
- **Fitur Utama**:
  - Pengecekan ketersediaan jadwal dan validasi jam operasional.
  - Perhitungan otomatis durasi sewa, diskon member/event, dan total biaya.
  - Cetak struk invoice dan rekapitulasi transaksi penyewaan.

---

## ⚡ Cara Menjalankan Kode

Pastikan telah menginstal [Python 3.x](https://www.python.org/).

1. **Clone repositori:**
   ```bash
   git clone https://github.com/alsyakd/praktikum-python.git
   cd praktikum-python
   ```

2. **Jalankan latihan atau tugas:**
   ```bash
   # Menjalankan latihan fungsi
   python latihan/pertemuan_12_FungsiReturn.py

   # Menjalankan tugas sistem perpustakaan
   python tugas/11_sistemManajemenPerpus.py
   ```

3. **Jalankan Proyek Akhir (UAS):**
   ```bash
   python uas-2026/sistem_sewa_lapangan_final/main.py
   ```

---

## 👤 Author

- **Nama**: Alsya Kanaya Dzikra  
- **NIM**: 2605060075  
- **Program Studi**: S1 Teknologi Informasi / Informatika  
- **Institusi**: Universitas Tidar (UNTIDAR)  
- **GitHub**: [@alsyakd](https://github.com/alsyakd)

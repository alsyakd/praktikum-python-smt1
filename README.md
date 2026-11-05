# Praktikum Pemrograman Python — Semester 1

Repository ini berisi kumpulan kode program latihan mingguan, latihan persiapan Ujian Tengah Semester (UTS), dan tugas praktikum pemrograman Python untuk **Semester 1** di Program Studi Teknologi Informasi / Informatika, Universitas Tidar (Dosen/Pengampu: Pak Iwan).

---

## 📑 Daftar Isi

- [Struktur Direktori](#-struktur-direktori)
- [Topik Pertemuan (Topics Covered)](#-topik-pertemuan-topics-covered)
- [Rincian Materi & Latihan](#-rincian-materi--latihan)
  - [1. Latihan Praktikum Per Pertemuan](#1-latihan-praktikum-per-pertemuan)
  - [2. Latihan Soal Persiapan UTS](#2-latihan-soal-persiapan-uts)
  - [3. Tugas Praktikum & Mandiri](#3-tugas-praktikum--mandiri)
- [Cara Menjalankan Kode (How to Run)](#-cara-menjalankan-kode-how-to-run)
- [Author](#-author)

---

## 🗂 Struktur Direktori

```text
praktikum-python/
├── latihan/                                    # Latihan mingguan & persiapan UTS
│   ├── pertemuan_1.py                          # Hello World
│   ├── pertemuan_2_tipeData.py                 # Variabel, tipe data, casting & input
│   ├── pertemuan_3_konversiCelcius.py          # Konversi suhu (Celcius ke R, F, K)
│   ├── pertemuan_3_operasiAritmatika.py        # Operator aritmatika dasar
│   ├── pertemuan_3_operasiKomperasi.py         # Operator perbandingan / komparasi
│   ├── pertemuan_4_elif.py                     # Percabangan if-elif-else bertingkat
│   ├── pertemuan_4_ifelse.py                   # Percabangan kondisional if-else
│   ├── pertemuan_4_logical.py                  # Operator logika (not, or, and, xor)
│   ├── pertemuan_4_logikaKomparasi.py          # Gabungan logika & rentang komparasi
│   ├── pertemuan_5_break.py                    # Penghentian perulangan (break)
│   ├── pertemuan_5_continuePass.py             # Penggunaan continue & pass
│   ├── pertemuan_5_for.py                      # Perulangan for (range & list)
│   ├── pertemuan_5_perulangan.py               # Dasar perulangan dan kontrol alur
│   ├── pertemuan_5_whileLoop.py                # Perulangan while berdasarkan kondisi
│   ├── pertemuan_9_list.py                     # Definisi list & list comprehension
│   ├── pertemuan_9_manipulasiList .py          # Akses index, insert, extend, pop, remove
│   ├── pertemuan_9_nestedList                  # Konsep nested list (list 2 dimensi)
│   ├── pertemuan_9_operasiList.py              # Operasi count, index, sort, reverse
│   ├── uts-2023/
│   │   └── booking_kamar.py                    # Sistem reservasi kamar hotel & diskon member
│   ├── uts-2024/
│   │   ├── detect_ganjilGenap_npm.py           # Penghitung digit genap & ganjil dari NPM
│   │   └── perulangan_segitiga_angka.py        # Pola segitiga perkalian bersarang
│   └── uts-2025/
│       ├── ganjilGenap_nim.py                  # Analisis bilangan ganjil & genap dari NIM
│       └── soal_2.py                           # Sistem verifikasi kode & PIN (maks 5 percobaan)
├── tugas/                                      # Tugas praktikum mandiri
│   ├── identitas.py                            # Menampilkan biodata & identitas mahasiswa
│   ├── literalData-1.py                        # Latihan tipe data literal 1
│   ├── literalData-2.py                        # Latihan tipe data literal 2
│   ├── literalData-3.py                        # Latihan tipe data literal 3
│   ├── operasiAritmatika.py                    # Menghitung volume, luas, keliling balok
│   ├── ganjilGenap.py                          # Menampilkan deret ganjil & genap (1-50)
│   ├── bilanganPrima.py                        # Menampilkan deret bilangan prima (1-100)
│   ├── kategoriUsia.py                         # Klasifikasi kelompok usia input user
│   ├── manipulasi_dataKendaraan.py             # Manipulasi list kendaraan (append, insert, pop, update)
│   ├── menggabungkanDataMenu.py                # Penggabungan list menu dengan extend()
│   ├── nestedList_barang.py                    # Akses & iterasi nested list data barang dan harga
│   └── pengolahanNilaiUjian.py                 # Pengolahan list nilai (index, count, sort, reverse)
└── README.md
```

---

## 📚 Topik Pertemuan (Topics Covered)

| Pertemuan / Sesi | Topik Utama | Deskripsi Materi |
| :---: | :--- | :--- |
| **Pertemuan 1** | Introduction & Environment | Pengenalan dasar Python, eksekusi file, output `Hello World`. |
| **Pertemuan 2** | Variables & Data Types | Deklarasi variabel, tipe data (`int`, `float`, `str`, `bool`, `complex`), type casting, dan `input()`. |
| **Pertemuan 3** | Operators & Temperature Conversion | Operator aritmatika (`+`, `-`, `*`, `/`, `%`, `**`, `//`), perbandingan (`==`, `!=`, `<`, `>`, `<=`, `>=`), dan konversi suhu. |
| **Pertemuan 4** | Conditionals & Logic | Percabangan `if`, `elif`, `else`, operator logika (`and`, `or`, `not`, `xor`), dan evaluasi rentang nilai komparasi. |
| **Pertemuan 5** | Loops & Loop Control | Perulangan `for` dan `while`, penanganan iterasi dengan statement `break`, `continue`, dan `pass`. |
| **UTS Preparation** | Midterm Exam Practice | Pembahasan soal latihan UTS tahun 2023, 2024, dan 2025 (studi kasus reservasi hotel, parsing NPM/NIM, nested loop, autentikasi). |
| **Pertemuan 9** | Lists & Nested Lists | Struktur data list, list comprehension, manipulasi elemen (`insert`, `extend`, `remove`, `pop`), operasi bawaan list (`sort`, `reverse`, `count`, `index`), dan konsep nested list (2D list). |

---

## 🔍 Rincian Materi & Latihan

### 1. Latihan Praktikum Per Pertemuan

#### Pertemuan 1 s/d 5: Dasar Pemrograman & Kontrol Alur
- **`pertemuan_1.py`**: Perintah cetak teks pertama ke layar.
- **`pertemuan_2_tipeData.py`**: Berbagai tipe data bawaan Python, perubahan tipe (casting), dan pengambilan input dari terminal.
- **`pertemuan_3_konversiCelcius.py`**: Menghitung konversi temperatur dari Celcius ke Reamur, Fahrenheit, dan Kelvin.
- **`pertemuan_3_operasiAritmatika.py`**: Berbagai operasi aritmatika dasar hingga pembagian bulat (*floor division*).
- **`pertemuan_3_operasiKomperasi.py`**: Evaluasi nilai boolean dari operator perbandingan serta identitas (`is`, `is not`).
- **`pertemuan_4_ifelse.py` & `pertemuan_4_elif.py`**: Penentuan keputusan alur program dengan blok kondisi tunggal maupun multi-kondisi.
- **`pertemuan_4_logical.py` & `pertemuan_4_logikaKomparasi.py`**: Logika boolean dan logika rentang gabungan/irisan daerah angka.
- **`pertemuan_5_for.py` & `pertemuan_5_whileLoop.py`**: Pengulangan kode dengan batas range maupun perulangan berbasis kondisi.
- **`pertemuan_5_break.py` & `pertemuan_5_continuePass.py`**: Interupsi perulangan lebih dini atau melompati iterasi tertentu.

#### Pertemuan 9: List & Manipulasi Data
- **`pertemuan_9_list.py`**: Pembuatan list tipe seragam, campuran, konversi objek `range` ke list, serta penggunaan *list comprehension* dengan filter `if`.
- **`pertemuan_9_manipulasiList .py`**: Akses indeks positif & negatif, menghitung panjang data (`len`), penyisipan nilai (`insert`), penggabungan list (`extend`), pengubahan data, dan penghapusan (`remove`, `pop`).
- **`pertemuan_9_nestedList`**: Representasi data matriks / list 2 dimensi dan teknik iterasi untuk menampilkan atribut baris per baris.
- **`pertemuan_9_operasiList.py`**: Mengurutkan data list (`sort`), membalik urutan (`reverse`), menghitung frekuensi kemunculan elemen (`count`), dan mencari lokasi indeks elemen (`index`).

---

### 2. Latihan Soal Persiapan UTS

- **UTS 2023 (`uts-2023/booking_kamar.py`)**  
  Program entri data reservasi tamu Hotel UNTIDAR dengan pilihan tipe kamar (*Suite, Superior, Deluxe*), kalkulasi lama sewa, kalkulasi potongan diskon member (20%), serta pencetakan rekap invoice pembayaran.
- **UTS 2024 (`uts-2024/detect_ganjilGenap_npm.py`)**  
  Program analisis digit Nomor Pokok Mahasiswa (NPM) untuk menghitung total angka genap dan ganjil yang terkandung di dalamnya.
- **UTS 2024 (`uts-2024/perulangan_segitiga_angka.py`)**  
  Program pembentukan pola matriks segitiga berbasis perulangan bersarang (*nested loop*) dengan kalkulasi perkalian baris dan kolom `i * j`.
- **UTS 2025 (`uts-2025/ganjilGenap_nim.py`)**  
  Program iterasi string digit NIM untuk membedakan serta menghitung frekuensi digit bernilai ganjil dan genap.
- **UTS 2025 (`uts-2025/soal_2.py`)**  
  Sistem autentikasi keamanan kode dan PIN dengan pembatasan maksimal 5 kali percobaan gagal sebelum sistem terkunci otomatis (*lockout*).

---

### 3. Tugas Praktikum & Mandiri

- **`identitas.py`**: Menampilkan informasi lengkap biodata mahasiswa (Nama, NIM, Rombel, Jurusan, Fakultas, dan Universitas).
- **`literalData-1.py`, `literalData-2.py`, `literalData-3.py`**: Latihan pemahaman literal data, format cetak, dan karakter escape pada Python.
- **`operasiAritmatika.py`**: Program interaktif untuk menghitung volume, luas permukaan, dan keliling balok dari input panjang, lebar, dan tinggi, dilengkapi dengan perbandingan luas dan volume menggunakan percabangan.
- **`ganjilGenap.py`**: Menghasilkan deret bilangan ganjil dan bilangan genap dari angka 1 hingga 50.
- **`bilanganPrima.py`**: Menentukan dan menampilkan seluruh bilangan prima dalam rentang 1 sampai 100.
- **`kategoriUsia.py`**: Mengelompokkan usia inputan pengguna ke dalam kategori balita, anak-anak, remaja, dewasa, atau lansia.
- **`manipulasi_dataKendaraan.py`**: Implementasi operasi penambahan (`append`, `insert`), penghapusan (`pop`), pembaruan nilai, dan penghitungan panjang pada list kendaraan.
- **`menggabungkanDataMenu.py`**: Menggabungkan dua kelompok list (menu utama dan menu tambahan) menggunakan method bawaan `.extend()`.
- **`nestedList_barang.py`**: Pengelolaan tabel barang dan harga menggunakan nested list 2D, akses nilai menggunakan indeks baris-kolom, serta iterasi tampilan data.
- **`pengolahanNilaiUjian.py`**: Analisis kumpulan nilai ujian siswa: pencarian indeks skor tertentu, penghitungan frekuensi nilai, pengurutan menaik (*ascending*), dan pengurutan menurun (*descending*).

---

## 🚀 Cara Menjalankan Kode (How to Run)

Pastikan Python 3 sudah terpasang di perangkat Anda. Buka terminal atau Command Prompt pada direktori utama repository, lalu jalankan perintah berikut:

### Menjalankan Latihan Mingguan
```bash
# Contoh menjalankan latihan pertemuan 1
python latihan/pertemuan_1.py

# Contoh menjalankan latihan modul list (Pertemuan 9)
python latihan/pertemuan_9_list.py
python "latihan/pertemuan_9_manipulasiList .py"
python latihan/pertemuan_9_operasiList.py
```

### Menjalankan Latihan Soal UTS
```bash
# Simulasi booking kamar hotel (UTS 2023)
python latihan/uts-2023/booking_kamar.py

# Validasi kode & PIN (UTS 2025)
python latihan/uts-2025/soal_2.py
```

### Menjalankan Tugas Praktikum
```bash
# Program kategori usia
python tugas/kategoriUsia.py

# Program manipulasi nested list barang
python tugas/nestedList_barang.py

# Program pengolahan nilai ujian
python tugas/pengolahanNilaiUjian.py
```

---

## 👤 Author

- **Nama**: Alsya Kanaya Dzikra  
- **NIM**: 2605060075  
- **Program Studi**: S1 Teknologi Informasi / Teknik Informatika  
- **Fakultas**: Fakultas Teknik  
- **Perguruan Tinggi**: Universitas Tidar (UNTIDAR)  
- **GitHub**: [@alsyakd](https://github.com/alsyakd)

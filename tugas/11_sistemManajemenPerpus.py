import datetime
import string
import random

data_perpustakaan = {}
while True:
    print("\n" + "=" * 40)
    print(f"{'SISTEM MANAJEMEN PERPUSTAKAAN':^40}")
    print("=" * 40)

    judul = input("Judul Buku: ")
    penulis = input("Penulis: ")
    tahun_terbit = int(input("Tahun Terbit: "))
    TAHUN = int(input("Tahun Terakhir Pinjam: "))
    BULAN = int(input("Bulan Terakhir Pinjam: "))
    TANGGAL = int(input("Tanggal Terakhir Pinjam: "))
    tanggal_pinjam = datetime.datetime(TAHUN, BULAN, TANGGAL)
    status = input("Status (TERSEDIA/TIDAK): ")
   
    kode_buku = ''.join(
        random.choice(string.ascii_uppercase) for i in range(6)
    )
 
    KEY = (kode_buku, tahun_terbit)
  
    buku = {
        "judul": judul,
        "penulis": penulis,
        "tahun_terbit": tahun_terbit,
        "tanggal_terakhir_pinjam": tanggal_pinjam,
        "status": status
    }
  
    data_perpustakaan.update({KEY: buku})
 
    print("\n" + "=" * 70)
    print(f"{'DATA BUKU PERPUSTAKAAN':^70}")
    print("=" * 70)
    print(f"{'KEYS':<20} {'JUDUL BUKU':<20} {'PENULIS':<20} {'TAHUN':<8} {'TANGGAL PINJAM':<15} {'STATUS'}")
    print("-" * 100)
    for KEY in data_perpustakaan:
        JUDUL = data_perpustakaan[KEY]["judul"]
        PENULIS = data_perpustakaan[KEY]["penulis"]
        TAHUN = data_perpustakaan[KEY]["tahun_terbit"]
        TANGGAL = data_perpustakaan[KEY]["tanggal_terakhir_pinjam"].strftime("%x")
        STATUS = data_perpustakaan[KEY]["status"]
        print(f"{KEY!s:<20} {JUDUL:<20} {PENULIS:<20} {TAHUN:<8} {TANGGAL:<15} {STATUS}")
    print("\n")
    is_done = input("Mau tambah buku lagi (y/n)? ")
    if is_done == "n":
        break
print("\nProgram manajemen perpustakaan selesai. Terima kasih!")
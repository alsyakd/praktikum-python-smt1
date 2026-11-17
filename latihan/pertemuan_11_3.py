
import datetime
import os
import string
import random

# Template dictionary mahasiswa
mahasiswa_template = {
    'nama': 'nama',
    'nim': '00000000',
    'sks_lulus': 0,
    'lahir': datetime.datetime(1111, 1, 11)
}

data_mahasiswa = {}

while True:
    print(f"{'SELAMAT DATANG':^60}")
    print(f"{'DATA MAHASISWA':^60}")
    print("-" * 60)

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())

    mahasiswa['nama'] = input("Nama Mahasiswa: ")
    mahasiswa['nim'] = input("NIM Mahasiswa: ")
    mahasiswa['sks_lulus'] = int(input("SKS Lulus: "))

    TAHUN_LAHIR = int(input("Tahun lahir (YYYY): "))
    BULAN_LAHIR = int(input("Bulan lahir (1-12): "))
    TANGGAL_LAHIR = int(input("Tanggal lahir (1-31): "))

    mahasiswa['lahir'] = datetime.datetime(
        TAHUN_LAHIR,
        BULAN_LAHIR,
        TANGGAL_LAHIR
    )

    KEY = ''.join(
        random.choice(string.ascii_uppercase)
        for i in range(6)
    )

    data_mahasiswa.update({KEY: mahasiswa})

    # Menampilkan seluruh data mahasiswa
    print(f"\n{'KEY':<8} {'Nama':<17} {'NIM':<12} {'SKS Lulus':<12} {'Tanggal Lahir':<15}")
    print("-" * 65)

    for KEY in data_mahasiswa:
        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks_lulus']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%d-%m-%Y")

        print(f"{KEY:<8} {NAMA:<17} {NIM:<12} {SKS:<12} {LAHIR:<15}")

    print("\n")

    is_done = input("Mau tambah lagi bro (y/n)? ").lower()

    if is_done == "n":
        break

    print("\n")

print("\nAkhir dari program, terima kasih!")

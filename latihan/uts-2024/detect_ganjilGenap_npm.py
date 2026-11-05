# Meminta input NPM dari user
npm = input("Masukkan NPM Anda: ")

# Inisialisasi penghitung bilangan genap dan ganjil
genap = 0
ganjil = 0

# Lakukan perulangan untuk setiap karakter/digit dalam NPM
for digit in npm:
    # Pastikan karakter yang diperiksa adalah angka
    if digit.isdigit():
        angka = int(digit)
        # Jika angka habis dibagi 2, maka genap (termasuk 0)
        if angka % 2 == 0:
            genap += 1
        else:
            ganjil += 1

# Menampilkan hasil output
print(f"Jumlah bilangan genap: {genap}")
print(f"Jumlah bilangan ganjil: {ganjil}")

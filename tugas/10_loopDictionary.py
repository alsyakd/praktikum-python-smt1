print("PROGRAM LOOPING DICTIONARY")

# A. Membuat dictionary keranjang
keranjang = {
    "apel": 5000,
    "pisang": 3000,
    "jeruk": 7000,
    "anggur": 15000
}
# B. Menampilkan nama barang dan harganya
for barang, harga in keranjang.items():
    print(f"Harga {barang}: Rp {harga}")
# C. Menghitung total belanja
total = 0
for harga in keranjang.values():
    total += harga
print("Total belanja: Rp", total)
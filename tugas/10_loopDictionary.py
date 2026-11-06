print("PROGRAM LOOPING DICTIONARY")

# a. Buatlah dictionary bernama keranjang dengan data harga buah berikut: {"apel": 5000, "pisang": 3000, "jeruk": 7000, "anggur": 15000}
keranjang = {
    "apel": 5000,
    "pisang": 3000,
    "jeruk": 7000,
    "anggur": 15000
}

# b. Gunakan perulangan untuk menampilkan setiap barang dan harganya dengan format: "Harga apel: Rp 5000"
total_belanja = 0
for buah, harga in keranjang.items():
    print(f"Harga {buah}: Rp {harga}")
    total_belanja += harga

# c. Tampilkan total belanja
print(f"\nTotal belanja: Rp {total_belanja}")
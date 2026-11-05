data_barang = [["Buku", 5000], ["Pensil", 2000], ["Penggaris", 3000]]

# a. Tampilkan harga dari "Pensil" menggunakan indeks spesifik
# "Pensil" berada di baris indeks ke-1, dan harganya berada di kolom indeks ke-1
harga_pensil = data_barang[1][1]
print(f"a. Harga dari 'Pensil': {harga_pensil}")

print("\nb. Menampilkan seluruh data barang:")
# b. Gunakan perulangan untuk membaca data satu per satu
for barang in data_barang:
    nama = barang[0]
    harga = barang[1]
    print(f"Nama: {nama}, Harga: {harga}")
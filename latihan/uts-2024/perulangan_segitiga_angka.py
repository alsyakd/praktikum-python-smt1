# Menentukan jumlah baris segitiga
jumlah_baris = 10

# Perulangan luar untuk mengatur baris (i dari 1 sampai 10)
for i in range(1, jumlah_baris + 1):
    # Perulangan dalam untuk mengatur kolom pada setiap baris (j dari 1 sampai i)
    for j in range(1, i + 1):
        # Mencetak hasil perkalian i * j dengan spasi di akhirnya
        print(i * j, end=" ")
    # Berpindah ke baris baru setelah satu baris selesai dicetak
    print()

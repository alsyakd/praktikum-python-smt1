angka = [75, 80, 90, 75, 85, 100, 65]

# a. Cari tahu di indeks ke berapa skor 100 berada
indeks_100 = angka.index(100)

# b. Hitung ada berapa banyak siswa yang mendapatkan skor 75
jumlah_75 = angka.count(75)

# c. Urutkan list dari nilai terkecil hingga terbesar
angka.sort()
print("Urutan terkecil ke terbesar:", angka)

# d. Balikkan urutan list (terbesar ke terkecil)
angka.reverse()
print("Urutan terbesar ke terkecil:", angka)

print("Indeks skor 100:", indeks_100)
print("Banyak siswa nilai 75:", jumlah_75)
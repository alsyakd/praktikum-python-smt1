menu_utama = ["Nasi Goreng", "Mie Ayam"]
menu_tambahan = ["Kerupuk", "Es Teh"]

# Menggabungkan menu_tambahan ke dalam menu_utama menggunakan fungsi extend()
menu_utama.extend(menu_tambahan)

# Menampilkan hasil gabungan
print("Hasil menu gabungan:", menu_utama)
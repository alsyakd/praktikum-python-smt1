kendaraan = ['motor', 'mobil', 'sepeda', 'bus']

# a. Tambahkan 'truk' di akhir list
kendaraan.append('truk')

# b. Sisipkan 'becak' pada index ke-1
kendaraan.insert(1, 'becak')

# c. Hapus data yang berada paling belakang dari list tersebut
kendaraan.pop()

# d. Ubah elemen 'sepeda' menjadi 'skuter'
idx = kendaraan.index('sepeda')
kendaraan[idx] = 'skuter'

# e. Tampilkan informasi jumlah total data di dalam list tersebut
print("Isi list akhir:", kendaraan)
print("Jumlah total data:", len(kendaraan))
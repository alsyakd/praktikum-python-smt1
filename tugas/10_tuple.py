print("PROGRAM TUPLE DAN SET")

print("1. Tuple")
# a. Buatlah sebuah Tuple bernama mahasiswa yang berisi 3 data diri Anda
mahasiswa = ("John Doe", "123456789", "Teknik Informatika")

# b. Tampilkan data NIM dan Prodi ke layar dengan cara mengakses indeksnya
print(f"NIM: {mahasiswa[1]}")
print(f"Prodi: {mahasiswa[2]}")

# c. Coba jalankan kode mahasiswa[2] = "Teknologi Informasi". Amati pesan error yang muncul, lalu jelaskan mengapa hal tersebut terjadi
mahasiswa[2] = "Teknologi Informasi" 

# Error: TypeError: 'tuple' object does not support item assignment
# Penjelasan: Tuple bersifat immutable, artinya data di dalamnya tidak dapat diubah setelah dibuat. Oleh karena itu, mencoba mengubah nilai pada indeks tertentu akan menghasilkan error. 

# d. Buatlah sebuah Set bernama nilai_angka dari barisan angka berikut: 10, 4, 3, 2, 4, 10, 7, 5. Cetak nilai_angka ke layar dan jelaskan apa yang terjadi pada angka 10 dan 4 yang ditulis dua kali!
nilai_angka = {10, 4, 3, 2, 4, 10, 7, 5}
print(f"Set nilai_angka: {nilai_angka}")

# Penjelasan: Set adalah kumpulan data yang unik, sehingga angka 10 dan 4 yang ditulis dua kali hanya akan muncul satu kali dalam set. Set tidak memperbolehkan duplikasi elemen.




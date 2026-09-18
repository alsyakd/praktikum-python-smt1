# 1. Buat program yang menampilkan bilangan ganjil dan genap dari 1 sampai 50 menggunakan perulangan! 

print("PROGRAM MENAMPILKAN BILANGAN GANJIL DAN GENAP DARI 1 SAMPAI 50\n")
for i in range(1, 51):
    if i % 2 == 0:
        print(f"{i} adalah bilangan genap")
    else:
        print(f"{i} adalah bilangan ganjil")
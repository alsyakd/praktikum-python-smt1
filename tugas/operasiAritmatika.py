# Latihan - Operasi Aritmatika

print("PROGRAM MENGHITUNG LUAS, VOLUME DAN KELILING BALOK\n")

panjang = 12
lebar = 5
tinggi = 8

print("Panjang balok adalah", panjang)
print("Lebar balok adalah", lebar)
print("Tinggi balok adalah", tinggi)

print("\n===============================\n")

## a. Hitunglah luas, volume dan keliling dari bangunan tersebut! 

# menghitung luas balok
luas = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
print("Luas balok adalah 2  * (p * l + p * t + l * t) =", luas)

print("\n===============================\n")

# menghitung volume balok
volume = panjang * lebar * tinggi
print("Volume balok adalah p * l * t =", volume)

print("\n===============================\n")

# menghitung keliling balok
keliling = 4 * (panjang + lebar + tinggi)
print("Keliling balok adalah 4 * (p + l + t) =", keliling)

print("\n===============================\n")

## b. Apakah luas bangunan tersebut lebih luas dari 50? 

luas_lebih_dari_50 = luas > 50
print("Apakah luas > 50? :", luas_lebih_dari_50)

## c. Apakah volume tersebut bernilai 480?

volume_lebih_dari_480 = volume == 480
print("Apakah volume == 480? :", volume_lebih_dari_480)

print("\nAUTHOR: ALSYA KANAYA DZIKRA - 2605060075\n")
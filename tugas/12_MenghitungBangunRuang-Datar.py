import math

# Fungsi menghitung luas persegi panjang
def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

# Fungsi menghitung volume balok
def volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

# Fungsi menghitung luas lingkaran
def luas_lingkaran(jari_jari):
    return math.pi * jari_jari ** 2

# Fungsi menghitung volume bola
def volume_bola(jari_jari):
    return (4 / 3) * math.pi * jari_jari ** 3

# Program utama
print("=== PROGRAM PERHITUNGAN MENGGUNAKAN FUNGSI ===")
# Luas persegi panjang
print("\n1. Luas Persegi Panjang")
panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))
hasil_luas = luas_persegi_panjang(panjang, lebar)
print(f"Luas persegi panjang = {hasil_luas}")

# Volume balok
print("\n2. Volume Balok")
panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))
tinggi = float(input("Masukkan tinggi: "))
hasil_volume = volume_balok (panjang, lebar, tinggi)
print(f"Volume balok = {hasil_volume}")

# Luas lingkaran
print("\n3. Luas Lingkaran")
jari_jari = float(input("Masukkan jari-jari: "))
hasil_luas_lingkaran = luas_lingkaran(jari_jari)
print(f"Luas lingkaran = {hasil_luas_lingkaran:.2f}")

# Volume bola
print("\n4. Volume Bola")
jari_jari = float(input("Masukkan jari-jari: "))
hasil_volume_bola = volume_bola(jari_jari)
print(f"Volume bola = {hasil_volume_bola:.2f}")
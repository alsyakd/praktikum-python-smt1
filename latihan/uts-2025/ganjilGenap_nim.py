print("PROGRAM MENGHITUNG JUMLAH ANGKA GANJIL DAN GENAP DARI NIM")

nim = input("Masukkan NIM Anda: ")

genap = 0
ganjil = 0

for digit in nim:
  if digit.isdigit():
    angka = int(digit)
    if angka % 2 == 0:
      genap += 1
    else:
       ganjil += 1
       print(f"jumlah ganjil: {ganjil}")
       print(f"jumlah genap: {genap}")
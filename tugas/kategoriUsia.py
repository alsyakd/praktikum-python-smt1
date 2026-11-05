print("PROGRAM MENGKATEGORIKAN USIA\n")

usia = int(input("Masukkan usia Anda: "))

if usia < 0:
    print("Usia tidak valid")
elif usia >= 0 and usia <= 12:
    print("Anda termasuk anak-anak")
elif usia >= 13 and usia <= 17:
    print("Anda termasuk remaja")
elif usia >= 18 and usia <= 59:
    print("Anda termasuk dewasa")
else:
    print("Anda termasuk lansia")

print("\nAUTHOR: ALSYA KANAYA DZIKRA - 2605060075\n")
# Default argument

# def fungsi(argument):
# def fungsi(argument = nilai default):

# contoh 1
def say_hello(nama = "Ojul"):
  print(f"Hello {nama}")

say_hello("Ucup")
say_hello()

# contoh 2
def sapa_dia(nama, pesan = "Apa kabar?"):
  # fungsi dengan satu input biasa, dan satu default arg
  print(f"hai {nama}, {pesan}")

sapa_dia("Nanda","Selamat pagi")
sapa_dia("Budi")

# contoh 3
def hitung_pangkat(angka, pangkat):
  hasil = angka**pangkat
  return hasil

print(hitung_pangkat(2,4))

hasil = hitung_pangkat(pangkat=3, angka=5)
print(hasil)

# contoh 4
def faktorial(input_1=1,input_2=2,input_3=3,input_4=4):
  hasil = input_1 * input_2 * input_3 * input_4
  return hasil

print(faktorial())
print(faktorial(input_3 = 10))
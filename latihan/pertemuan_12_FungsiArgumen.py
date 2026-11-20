## --- Fungsi dengan argumen ---

## def nama_fungsi(argumen)

# Badan fungsi
def hello_world(nama):
#fungsi hello world menerima
  print(f"Selamat datang di Dunia, {nama}")

hello_world("ucup")

def tambah(angka_1, angka_2):
# fungsi tambah
  hasil = angka_1 + angka_2
  print(f"{angka_1} + {angka_2} = {hasil}")

tambah(1,8)

def say_hi(list_peserta):
  #fungsi say hi
  data_peserta = list_peserta.copy()
  for peserta in data_peserta:
    print(f"Selamat datang {peserta}")

kumpulan_mahasiswa = ["Budi", "Tono", "Joko"]

say_hi(kumpulan_mahasiswa)

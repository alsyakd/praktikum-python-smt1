## --- Operasi LIST ---

# index 0(-3)   1(-2)   2(-1)
data = ["Ucup", "Adit", "Dudung"]

# mengambil data dari list
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir adalah = {data_terakhir}")

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

# manipulasi data list

# menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah = \n{data}")

# data.insert(posisi, item)

data.insert(1, "Asep")
print(f"data sesudah ditambah = \n{data}")

# menambahkan list dengan list
data_baru = ["Luffy", "Zoro", "Nami"]
data.extend(data_baru)
print(f"data gabungan = \n{data}")

# merubah data
# kita ubah data 2 menjadi jarwo
data[2] = "jarwo"
print(f"data rubah = \n{data}")

# mengubah data
data.remove("Ucup")
print(f"data hapus = \n{data}")

# menghapus data paling belakang
data.pop()
print(f"data akhir = \n{data}")
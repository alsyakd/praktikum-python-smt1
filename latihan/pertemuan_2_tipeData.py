# Variabel adalah tempat menyimpan data # menaruh / assignment nilai # di python tidak perlu deklarasi  
a = 10 
x = 5 
panjang = 1000 

# pemanggilan pertama 
print("Nilai a = ", a) 
print("Nilai x = ", x) 
print("Nilai panjang = ", panjang) 

# penamaan      
nilai_y = 15 

# dengan menggunakan underscore   
juta10 = 10000000 # ini boleh   
nilaiZ = 17.5 # ini boleh  

# pemanggilan kedua  
print("Nilai a = ", a) 
a = 7  
print("Nilai a = ", a)   

# assignment indirect  
b = a  
print("Nilai b = ", b) 

# a = 10, a adalah variabel dengan nilai 10

# tipe data: Angka satuan yang gak ada komanya (integer)
data_integer = 1
print("data:", data_integer)
print("- bertipe:", type(data_integer))

#tipe data: Angka yang ada komanya (float)
data_float = 1.5
print("data:", data_float)
print("- bertipe:", type(data_float))

#tipe data: Kumpulan karakter (string)
data_string = "ucup"
print("data:", data_string)
print("- bertipe:", type(data_string))

#tipe data: biner true/false (boolean)
data_bool = True   
print("data:", data_bool)
print("- bertipe:", type(data_bool))

# # tipe data khusus

# bilangan kompleks
data_complex = complex(5,6)
print("data:", data_complex)
print("- bertipe:", type(data_complex))

# # tipe data dari bahasa C
from ctypes import c_double

data_c_double = c_double(10.5)
print("data:", data_c_double)
print("- bertipe:", type(data_c_double))

# Kita belajar Casting
# merubah dari tipe data ke tipe data lain
# tipe data = int, float, str, bool

# INTEGER ke Tipe data lain

data_int = 9

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) #akan false jika nilai integer = 0

print("data = ", data_float, "type = ", type(data_float))
print("data = ", data_str, "type = ", type(data_str))
print("data = ", data_bool, "type = ", type(data_bool))

# FLOAT ke Tipe data lain

data_float = 9.2

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float) #akan false jika nilai float = 0

print("data = ", data_int, "type = ", type(data_int))
print("data = ", data_str, "type = ", type(data_str))
print("data = ", data_bool, "type = ", type(data_bool))

# STRING ke Tipe data lain

data_str = "10"

data_int = int(data_str)
data_float = float(data_str)
data_bool = bool(data_str)

print("data = ", data_int, "type = ", type(data_int))
print("data = ", data_float, "type = ", type(data_float))
print("data = ", data_bool, "type = ", type(data_bool))

# input data user

# data yang dimasukkan pasti string
data = input("masukkan data: ")
print("data = ", data, "type = ", type(data))

# jika ingin mengambil int, maka
angka = int(input("masukkan angka: "))
print("data = ", angka, "type = ", type(angka))
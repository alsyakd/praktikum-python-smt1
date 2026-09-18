# Perulangan (loop)  

angka = 1 
print(angka) 
angka = angka + 1 
print(angka) 
angka = angka + 1 
print(angka)  

# for kondisi: 
# aksi  

#dengan list 
angka2 = [0,1,2,3,4] # ini adalah list 
print(angka2)  
for i in angka2:  
  print(f"i sekarang → {i}") #print(f) -> kombinasi text dan variabel 
print("akhiri dari program\n")  

#dengan range 
angka3 = range(5)  
for i in angka3:   
  print(f"i sekarang → {i}") 
print("akhiri dari program\n")

angka4 = range(1,10) 
for i in angka4:   
  print(f"i sekarang → {i}") 
print("akhiri dari program\n")   

# menggunakan string 
data_str = "saya ganteng abiies"  
for huruf in data_str:  
  print(huruf) 
print("akhiri dari program\n") 


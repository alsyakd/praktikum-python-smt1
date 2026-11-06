## --- Looping Dictionary ---  

teman_teman = { "cup": "ucup surucup",  
               "tong": "sotong surotong" , 
               "lur": "lur sedulur"  ,
               "wel": "bung towel"  }  

# looping first try (yang keluar hanya key)
for teman in teman_teman: print(teman) 

# operator untuk mengambil item 
keys = teman_teman.keys() 
print(keys) 

for key in teman_teman.keys(): 
  print(teman_teman.get(key)) 
values = teman_teman.values() 
print(values) 
for value in teman_teman.values(): 
  print(value) 
items = teman_teman.items() 
print(items) 
for item in teman_teman.items(): 
  print(item) 
for key,value in teman_teman.items(): 
  print(f"key = {key}, value = {value}")
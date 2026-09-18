# *
# **
# ***
# ****
# *****

#latihan membuat segitiga 

# 1. Menggunakan for 
sisi = 4 
count = 1 

for i in range(sisi): 
    print("*" * count) 
    count += 1  
# 2. Menggunakan while 
sisi = 4 
count = 1 
while True: 
    print("*" * count) 
    count += 1 
    if count > sisi: 
        break
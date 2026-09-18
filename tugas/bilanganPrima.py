# 2. Buat program yang menampilkan semua bilangan prima antara 1 sampai 100 menggunakan perulangan! 

print("PROGRAM MENAMPILKAN BILANGAN PRIMA DARI 1 SAMPAI 100\n")
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} adalah bilangan prima")
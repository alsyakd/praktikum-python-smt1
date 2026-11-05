# Program Entry Data Hotel UNTIDAR

print("========================================")
print("        HOTEL UNTIDAR - ENTRY DATA")
print("========================================")

# Entry data tamu
nama = input("Nama tamu              : ")
alamat = input("Alamat tamu            : ")
member = input("Member hotel (Y/N)     : ").upper()
lama_menginap = int(input("Lama menginap (malam)  : "))

print("\nPilihan Tipe Kamar:")
print("1. Suite     - Rp1.000.000/malam")
print("2. Superior  - Rp600.000/malam")
print("3. Deluxe    - Rp400.000/malam")

pilihan_kamar = int(input("Pilih tipe kamar (1/2/3): "))

# Menentukan tipe dan harga kamar
if pilihan_kamar == 1:
    tipe_kamar = "Suite"
    harga_kamar = 1000000
elif pilihan_kamar == 2:
    tipe_kamar = "Superior"
    harga_kamar = 600000
elif pilihan_kamar == 3:
    tipe_kamar = "Deluxe"
    harga_kamar = 400000
else:
    print("Pilihan tipe kamar tidak valid.")
    exit()

# Menghitung potongan member
total_harga = harga_kamar * lama_menginap

if member == "Y":
    diskon = total_harga * 20 / 100
else:
    diskon = 0

total_bayar = total_harga - diskon

# Menampilkan hasil entry data
print("\n========================================")
print("          DATA TAMU HOTEL UNTIDAR")
print("========================================")
print("Nama Tamu       :", nama)
print("Alamat          :", alamat)
print("Member          :", member)
print("Lama Menginap   :", lama_menginap, "malam")
print("Tipe Kamar      :", tipe_kamar)
print("Harga Kamar     : Rp{:,.0f}".format(harga_kamar))
print("Total Harga     : Rp{:,.0f}".format(total_harga))
print("Diskon Member   : Rp{:,.0f}".format(diskon))
print("----------------------------------------")
print("Total Bayar     : Rp{:,.0f}".format(total_bayar))
print("========================================")
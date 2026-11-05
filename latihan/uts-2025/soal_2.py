# Deklarasi data kredensial yang valid
KODE_VALID = "7890"
PIN_VALID = "4567"
MAKS_PERCOBAAN = 5

# Melakukan perulangan maksimal 5 kali percobaan
for percobaan in range(1, MAKS_PERCOBAAN + 1):
    kode_input = input(f"\n[Percobaan {percobaan}/{MAKS_PERCOBAAN}] Masukkan kode keamanan: ")
    pin_input = input(f"[Percobaan {percobaan}/{MAKS_PERCOBAAN}] Masukkan PIN: ")
    
    # Validasi kode keamanan dan PIN
    if kode_input == KODE_VALID and pin_input == PIN_VALID:
        print("Akses diberikan!")
        break  # Program langsung berhenti jika sukses
    else:
        print("Kode keamanan atau PIN tidak valid!")
        
        # Jika sudah mencapai batas maksimal 5 kali percobaan dan tetap salah
        if percobaan == MAKS_PERCOBAAN:
            print("Akses ditolak! Sistem terkunci!")

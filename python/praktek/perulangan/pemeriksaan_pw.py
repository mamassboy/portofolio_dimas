def InputanPass ():
    password = input("masukkan nama password anda: ")
    return password

def cekPass ():
    percobaan = 3

    while percobaan > 0:
        password = InputanPass()
        if password == "dimas123":
            print(f"Selamat Datang Di Dimas Store");
            return True
        else:
            percobaan -= 1
            print(f"❌ Password Anda Salah. Sisa percobaan: {percobaan}")
    print("🚫 Akses ditolak, coba lagi nanti.")
    return False    

cekPass()
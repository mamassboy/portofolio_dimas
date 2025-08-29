print("Selamat Datang Di Tempat anda meminta sebuah perintah")

def menu ():
    print("Silahkan Pilih Permintaan Di Bawah Ini")
    print("="*30)
    print("   Menu Permintaan")
    print("="*30)
    print("1. Tampilkan Angka Genap Aja")
    print("2. Tampilkan Angka Ganjil Aja")
    print("3. Hitung Jumlah Huruf Dari  Sebuah Kalimat")
    print("="*30)

menu()
opsi = input("Masukkan Nomor Permintaan Pilihan Anda: ")


if opsi == "1":
    angka_Awal = int(input("Masukkan Angka Mulai: ")) 
    angka_Akhir = int(input("Masukkan Angka Akhir: ")) 
    for i in range (angka_Awal, angka_Akhir):
        if i % 2 == 0:
            print (i);
elif opsi == '2':
    angka_Awal = int(input("Masukkan Angka Mulai: ")) 
    angka_Akhir = int(input("Masukkan Angka Akhir: ")) 
    for i in range (angka_Awal, angka_Akhir):
        if i % 2 != 0:
            print (i);
elif opsi == "3":
    kalimat = input("Masukkan Kalimat yang Kamu ingin Tau jumlah Hurufnya: ") 
    # mengabaikan spasi
    jumlah_Huruf= len(kalimat.replace(" ", ""))
    print(f"Jumlah Huruf Dari Seluruh Kalimat Yang kamu Masukkan Adalah; {jumlah_Huruf} ");
else:
    print("Menu Tidak tersedia")
    menu()



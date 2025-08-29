from fungsi import ucapan_selamat_datang

ucapan_selamat_datang()

while True:
    print('''Pilih Opsi yang ingin kamu lakukan: 
      1. Tambah 
      2. Kurang 
      3. Kali
      4. Bagi''')

    pilihan = input("Masukkan pilihan kamu (1/2/3/4): ").strip()

    if pilihan in ["1", "2", "3", "4"]:
        angka1 = int(input("Masukkan angka pertama: "))
        angka2 = int(input("Masukkan angka kedua: "))

        if pilihan == "1":
            hasil = angka1 + angka2
            print(f"Hasil dari {angka1} + {angka2} = {hasil}")
        elif pilihan == "2":
            hasil = angka1 - angka2
            print(f"Hasil dari {angka1} - {angka2} = {hasil}")
        elif pilihan == "3":
            hasil = angka1 * angka2
            print(f"Hasil dari {angka1} * {angka2} = {hasil}")
        elif pilihan == "4":
            if angka2 == 0:
                print("Error: Tidak bisa membagi dengan 0.")
            else:
                hasil = angka1 / angka2
                print(f"Hasil dari {angka1} / {angka2} = {hasil}")

    else:
        print("Silakan masukkan angka yang sesuai (1/2/3/4).")

    ulangi = input("Apakah ingin menghitung lagi? (ya/tidak): ").strip().lower()
    if ulangi != "ya":
        print("Terima kasih telah menggunakan kalkulator ini!")
        break

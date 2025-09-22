angka = int (input("Masukkan Angka Yang Ingin Anda Periksa: "))

if angka == 0:
    print(f"{angka} bernilai Nol")
elif angka < 0 :
    print(f"{angka} bernilai Negatif")
else:
    print(f"{angka} bernilai Positif")
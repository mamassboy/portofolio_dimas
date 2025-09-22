angka = int (input("Masukkan Angka Yang Ingin Anda Periksa: "))

if angka == 0:
    sifat = "NETRAL"
elif angka < 0 :
    sifat = "NEGATIF"
else:
    sifat = "POSITIF"

if angka == 0:
    jenis = "NETRAL"
elif angka < 0 :
    jenis = "GANJIL"
else:
    jenis = "GENAP"

print(f"angka {angka} yang anda masukkan memiliki sifat {sifat} dan berjenis {jenis}")
angka = int(input("Masukkan angka yang ingin Anda periksa: "))


# Cek Positif, Negatif, atau Netral
if angka > 0:
    sifat = "Positif" 
elif angka < 0:
    sifat = "Negatif"
else:
    sifat = "Netral"

if angka == 0 :
    print(f'{angka} Adalah Bilangan {sifat}')
else: 
    if angka % 2 == 0:
        jenis = "Genap"
    else:
        jenis = " Ganjil"
    print(f'{angka} Adalah Bilangan {sifat}')
    print("dan")
    print(f'{angka} Adalah Bilangan {jenis}')
        

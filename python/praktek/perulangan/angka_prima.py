awalan = int(input("Masukkan Angka pertama yang ingin ada periksa: "))
akhiran = int(input("Masukkan Angka akhir ingin ada periksa: "))

print(f"Bilangan prima dari {awalan} sampai {akhiran}:")
for angka in range (awalan, akhiran +1):
    if angka > 1: 
        prima = True   # kita asumsikan dulu angkanya prima
        for i in range(2, angka):
            if awalan % i == 0:   # kalau ada pembagi selain 1 dan dirinya
                prima = False
                break

        if prima:
            print(angka , end=" ")
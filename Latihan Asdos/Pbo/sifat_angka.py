class Sifat:
    def __init__(self,awal, akhir):
        self.awal = awal
        self.akhir = akhir

    def GanjilGenap(self):
        for angka in range(self.awal, self.akhir+1):
            if angka < 0 :
                jenis = "Genap" if angka % 2 == 0 else "Ganjil"
                print(f"{angka} Adalah {jenis} dan Angka Negatif")
            elif angka == 0 :
                print(f"{angka} Adalah NOL")
            else:
                jenis = "Genap" if angka % 2 == 0 else "Ganjil"
                print(f"{angka} Adalah {jenis} dan Angka Positif")
    def prima(self):
        print(f"\nBilangan prima dari {self.awal} sampai {self.akhir}:")
        for angka in range (self.awal, self.akhir + 1):
            prima = False
            if angka > 1: 
                prima = True 
                for i in range(2, angka):
                    if angka % i == 0:   # kalau ada pembagi selain 1 dan dirinya
                        prima = False
                        break

            if prima:
                print(angka , end=" ")
        print()




while True:
    print("\nPemeriksaan:")
    print("1. Ganjil Genap,& Positif Negatif")
    print("2. Prima")
    pilihan = input("Pilih: ")


    if pilihan == "1":
        awal = int(input("Masukkan Angka Awal: "))
        akhir = int(input("Masukkan Angka Akhir: "))
        tes = Sifat(awal, akhir)
        tes.GanjilGenap()
        break
    elif pilihan == "2":
        awal = int(input("Masukkan Angka Awal: "))
        akhir = int(input("Masukkan Angka Akhir: "))
        tes = Sifat(awal, akhir)
        tes.prima()
        break
    else:
        print(f"angka yang kamu masukkan tidak valid")





        
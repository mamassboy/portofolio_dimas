
#class mobil
class Mobil :
    def __init__(self, Merk, Nama, Jenis, Harga, Tenaga, BahanBakar):
        self.merk = Merk
        self.nama = Nama
        self.jenis = Jenis
        self.harga = Harga
        self.tenaga = Tenaga
        self.bahanbakar = BahanBakar

    def info(self):
        print(f"Mobil {self.nama} dari merk {self.merk} dengan tipe kendaraan ({self.jenis})")
        print(f"Harga      : Rp{self.harga}")
        print(f"Tenaga     : {self.tenaga}")
        print(f"Bahan Bakar: {self.bahanbakar}")
        print("-" * 30)

a = Mobil('Toyota', 'Inova Hybrid', 'Matic', 599000000, '2000 HS', 'Bensin')
b = Mobil('Mazda','Mazda headback', 'Manual', 460000000, '1500 HS', 'Bensin')
a.info()
b.info()

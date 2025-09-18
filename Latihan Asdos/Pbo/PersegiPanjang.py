class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    
    def luas(self):
        return self.panjang * self.lebar
    def keliling(self):
        return 2*(self.panjang + self.lebar)
    
panjang = int(input("Masukkan Persegi Panjang: "))
lebar = int(input("Masukkan Lebar Persegi Panjang: "))

pp = PersegiPanjang(panjang, lebar)
print("Luas Persegi Panjang:", pp.luas())
print("Keliling Persegi Panjang:",pp.keliling())
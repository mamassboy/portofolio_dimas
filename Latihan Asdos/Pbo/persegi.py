class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi


    def cetak (self):
        print(f"ini sisi{self.sisi * 4}")
    def luas(self):
        return self.sisi * self.sisi

    def keliling(self):
        return self.sisi*4

p1 = Persegi(10)
p1.cetak()
print(f"Luas Persegi: {p1.luas()}")
print(f"Keliling Persegi: {p1.keliling()}")
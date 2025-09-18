class Segitiga:
    def __init__(self, alas, tinggi, sA, sB, sC):
        self.alas = alas
        self.tinggi = tinggi
        self.sisiA = sA
        self.sisiB = sB
        self.sisiC = sC

    def luas(self):
        return 0.5 * self.alas * self.tinggi
    def keliling(self):
        return(self.sisiA + self.sisiB + self.sisiC)
alas =int(input("Masukkan Alas: "))
tinggi =int(input("Masukkan Tinggi: "))
sisiA =int(input("Masukkan sisi A: "))
sisiB=int(input("Masukkan sisi B: "))
sisiC =int(input("Masukkan sisi C: "))

sgt = Segitiga(alas, tinggi, sisiA, sisiB, sisiC)

print(f"Luas Dari Sebuah Segitiga: {sgt.luas()}")
print(f"Keliling Dari Sebuah Segitiga: {sgt.keliling()}")
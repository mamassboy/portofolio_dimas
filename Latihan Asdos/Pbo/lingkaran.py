
class Lingkaran:
    def __init__(self, r):
        self.r = r

    def luas(self):
        return 3.14 * self.r
    def keliling(self):
        return 2 * 3.14 * self.r
    
jari_jari = int(input("Masukkan jari Jari Lingkaran Anda: "))
l = Lingkaran(jari_jari)
print(f"Luas Dari Lingkaran anda yang Berjari-jari {jari_jari} adalah: {l.luas()} ")
print(f"Keliling Dari Lingkaran anda yang Berjari-jari {jari_jari} adalah: {l.keliling()}")
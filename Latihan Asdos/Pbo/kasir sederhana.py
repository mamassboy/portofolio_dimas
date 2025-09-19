class Barang:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def info(self):
        print("=== Daftar Barang ===")
        return f"{self.nama} : Rp{self.harga}"
class Kasir:
    def __init__(self):
        self.daftar_belanja = []

    def tambah_barang(self, barang, jumlah):
        self.daftar_belanja.append((barang, jumlah))

    def struck_belanja(self):
        print("=== Daftar Belanjaan ===")
        for idx, (barang, jumlah) in enumerate(self.daftar_belanja, start=1):
            subtotal = barang.harga * jumlah
            print(f"{idx}.{barang.nama} x {jumlah} = {subtotal}")
        print("="*30)

    def total(self):
        total = 0
        for barang,  jumlah in self.daftar_belanja:
            total+= barang.harga * jumlah            
        return total


b1 = Barang("sabun", 10000 )
b2 = Barang("beras", 20000 )
b3 = Barang("pulut", 150000 )

kasir = Kasir()
kasir.tambah_barang(b1, 5)
kasir.tambah_barang(b2, 5)
kasir.tambah_barang(b3, 5)
kasir.tambah_barang(b1, 1)

kasir.struck_belanja()
print(f"Total Belanja: Rp {kasir.total()}")
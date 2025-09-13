class Barang:
    def __init__(self, nama, harga, stock):
        self.nama = nama
        self.harga = harga
        self.stock = stock

    def cetak_barang(self):
        print("=== Daftar Barang ===")
        print(f"Nama Barang : {self.nama}")
        print(f"Harga Barang : {self.harga}")
        print(f"Stock Barang : {self.stock}")
    def kurangi_stock(self, jumlah):
        if self.stock >= jumlah:
            self.stock -= jumlah
            return True
        else:
            print(f"⚠️ Stock {self.nama} tidak mencukupi!")
            return False

    
class StockBarang:
    def __init__(self):
        self.daftar_barang = []
        self.transaksi = []

    def tambah_barang (self, barang):
        self.daftar_barang.append(barang)

    def cetak_stock_barang(self):
        print("=== Daftar Stock Barang ===")
        for idx, barang in enumerate (self.daftar_barang, start=1):
            print(f'{idx}.{barang.nama}')
        print('='*30)

    def cek_stok_habis(self, batas=5):
        print("\n=== Barang Hampir Habis ===")
        for barang in self.daftar_barang:
            if barang.stock <= batas:
                print(f"{barang.nama} tinggal {barang.stock} lagi!")
        print("="*30)


    def jual_barang(self, nama_barang, jumlah):
        for barang in self.daftar_barang:
            if barang.nama == nama_barang:
                if barang.kurangi_stock(jumlah):
                    total = barang.harga * jumlah
                    self.transaksi.append((barang.nama, jumlah, total))
                    print(f"✅ {jumlah} {barang.nama} terjual. Total: Rp{total}")
                return
        print(f"⚠️ Barang {nama_barang} tidak ditemukan!")

    def laporan_pengeluaran(self):
        print("\n=== Laporan Penjualan Bulanan ===")
        total_semua = 0
        for nama, jumlah, total in self.transaksi:
            print(f"{nama} x{jumlah} = Rp{total}")
            total_semua += total
        print("Total Pengeluaran: Rp", total_semua)
        print("="*30)


# buat barang
b1 = Barang("Hand Sanitizer", 20000, 3)
b2 = Barang("Ban Mobil", 500000, 10)
b3 = Barang("Buah-buahan", 30000, 2)
b4 = Barang("Botol Bayi", 45000, 7)

# buat stock
stock = StockBarang()
stock.tambah_barang(b1)
stock.tambah_barang(b2)
stock.tambah_barang(b3)
stock.tambah_barang(b4)

# cek daftar barang
stock.cetak_stock_barang()

# jual barang
stock.jual_barang("Hand Sanitizer", 2)
stock.jual_barang("Buah-buahan", 1)

# cek stok hampir habis
stock.cek_stok_habis()

# laporan bulanan
stock.laporan_pengeluaran()

    
menu = {
    'Roti':5000,
    'Ayam':30000,
    'Susu':20000
}
def Daftar_Menu ():
    print("="*30)
    print("Daftar Menu")
    print("="*30)
    for nama, harga in menu.items():
        print(f"{nama:<10} : Rp {harga:,}")
    print("="*30)
    print("Ketik 'SELESAI' Untuk mengakhiri")

keranjang_belanja = {}
while True:
        Daftar_Menu()
        produk_pilihan = input("Masukkan Produk Yang Ingin Anda Beli: ").capitalize()

        # Kondisi berhenti
        if produk_pilihan.lower() == "selesai":
            break

        if produk_pilihan in menu:
            try:
                jumlah = int(input(f"Masukkan Jumlah {produk_pilihan}: "))
                keranjang_belanja[produk_pilihan] = keranjang_belanja.get(produk_pilihan, 0) + jumlah
                print(f"--> Berhasil menambahkan {jumlah} {produk_pilihan} ke keranjang.")
            except ValueError:
                print("❌ Jumlah harus berupa angka! Silakan coba lagi.")
        else:
            print("❌ Produk tidak valid! Silakan pilih sesuai daftar.")

# Tampilkan isi keranjang
print("\n" + "="*50)
print("🛒          STRUK BELANJA ANDA          🛒")
print("="*50)

if not keranjang_belanja:
    print("Keranjang Anda masih kosong.")
else:
    total = 0
    for produk, jumlah in keranjang_belanja.items():
        harga = menu[produk] * jumlah
        total += harga
        print(f"- {produk:<10} {jumlah} x Rp{menu[produk]:,} = Rp{harga:,}")
    print("="*50)
    print(f"TOTAL BELANJA : Rp{total:,}")
    print("="*50)

    # Proses pembayaran
    while True:
        try:
            bayar = int(input("Masukkan Uang Pembayaran: Rp"))
            if bayar < total:
                print(f"❌ Uang Anda kurang Rp{total - bayar:,}. Silakan tambahkan.")
            else:
                kembalian = bayar - total
                print("\n✅ Pembayaran Berhasil!")
                print(f"Uang Dibayar : Rp{bayar:,}")
                print(f"Kembalian    : Rp{kembalian:,}")
                print("="*50)
                print("🙏 Terima kasih telah berbelanja 🙏")
                break
        except ValueError:
            print("❌ Input tidak valid! Masukkan angka.")    
    

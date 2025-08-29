rekap = []

while True:
    for i in range(5):
        while True:
            try:
                nilai = int(input("Masukkan angka yang kamu ingin simpan: "))
                break
            except ValueError:
                print("Masukkan angka yang valid.")
        rekap.append(nilai)
    jawab = input("Apakah Anda ingin menambahkan angka lagi? (y/n): ")
    if jawab.lower() == "y":
        while True:
            try:
                tanya = int(input("Mau berapa angka yang ingin Anda tambahkan: "))
                break
            except ValueError:
                print("Masukkan angka yang valid.")
        for i in range(tanya):
            while True:
                try:
                    nilai = int(input("Masukkan angka yang kamu ingin simpan: "))
                    break
                except ValueError:
                    print("Masukkan angka yang valid.")
            rekap.append(nilai)
    elif jawab.lower() == "n":
        print("Anda telah menyelesaikan proses penyimpanan")
        break
print(rekap)
total = sum(rekap)
print(total)

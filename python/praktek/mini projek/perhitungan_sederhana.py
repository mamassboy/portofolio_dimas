print("Halo Selamat Datang Di Kalkulator");
num1 = int(input("Masukkan Angka Pertama: "));

print("Silahkan Pilih Oprasi Perhitungan Di Bawah Ini");
print("="*30)
print("   Menu Oprasi Perhitungan")
print("="*30)
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("5. Persentase")
print("="*30)
oprasi= input('Masukkan Nomor Oprasi Pilihan Anda: ')


num2 = int(input("Masukkan Angka Kedua: "));
penjumlahan = num1 + num2;
pengurangan = num1 - num2;
perkalian = num1 * num2;
pembagian= num1/num2;
persen = int(num2 * (num1/100));

if oprasi == "1":
    print(f"Hasil Dari Penjumlahan {num1} + {num2} adalah : {penjumlahan}");
elif oprasi == "2":
    print(f"Hasil Dari Pengurangan {num1} - {num2} adalah : {pengurangan}");
elif oprasi == "3":
    print(f"Hasil Dari Perkalian {num1} X {num2} adalah : {perkalian}");
elif oprasi == "4":
    print(f"Hasil Dari Pembagian {num1} / {num2} adalah : {pembagian}");
elif oprasi == "5":
    print(f"Hasil Dari Penjumlahan {num1}% dari{num2} adalah : {persen}");
else:
    print("Pilihan Tidak Tersedia");

# Rumus penjumlaha
# penjumlahan = num1 + num2;
# print(f"Hasil Dari Penjumlahan {num1} + {num2} adalah : {penjumlahan}")




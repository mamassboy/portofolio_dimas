umur = int(input("masukkan umur anda: "))

print(f"Umur saya adalah {umur} tahun")

# menghitung massa jenis
panjang= float(input("masukkan panjang balok anda: "))
lebar= float(input("masukkan lebar balok anda: "))
tinggi= float(input("masukkan tinggi balok anda: "))
massa = float(input("masukkan massa balok  anda: "))

volume= panjang * lebar * tinggi


massajenis = massa/volume

print(f"massa jenis balok kamu adalah : {massajenis}")

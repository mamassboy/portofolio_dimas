penjumlahan = 4+3+2+1
print(penjumlahan)


r = int(input("masukkan nilai jari-jari: "))
volume = 4/3 * 3.14 * r**3
print(volume)

jam_masuk = int(input("masukkan jam masuk anda : "))
ketentuan_masuk = jam_masuk = 6 and jam_masuk <= 8
if ketentuan_masuk:
    print("kamu tepat waktu")
else:
    print("kamu telat")
print(ketentuan_masuk)
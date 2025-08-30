#fungsi inputan
def inputan ():
    nama = input("Masukkan Nama Anda: ")
    usia = int(input("Masukkan Umur Anda Saat Ini: "))
    return nama, usia



def cekKategori (nama, usia):
    #kategori
    kategori = ["Anak- Anak", "Remaja", "Dewasa", 'Lansia']
    if usia < 13 :
        print (f"{nama} Adalah Seorang {kategori[0]}")
    elif  13 <= usia <=17:
        print (f"{nama} Adalah Seorang {kategori[1]}")
    elif 18 <= usia <=59:
        print (f"{nama} Adalah Seorang {kategori[2]}")
    elif usia >= 60:
        print (f"{nama} Adalah Seorang {kategori[3]}")
    else:
        print("Inputan Anda Tidak Sesuai, Silahkan Masukkan lagi")
        #memanggil kembali fungsi agar bisa input ulang
        nama, usia =inputan()
        cekKategori(nama, usia)


nama, usia = inputan()
cekKategori(nama, usia)

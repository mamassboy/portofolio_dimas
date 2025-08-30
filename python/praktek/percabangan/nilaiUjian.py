def inputan ():
    nama = input("Masukkan Nama Peserta: ")
    nilai = int(input("Masukkan Nilai Peserta: "))
    return nama, nilai

#panggil fungsi inputan
nama, nilai = inputan()

def cek_nilai (nama, nilai):
    if nilai >= 85 :
        print(f"{nama} Berpredikat A ");
    elif 70 <= nilai <= 84:
        print(f"{nama} Berpredikat B ");
    elif 55 <= nilai <= 69:
        print(f"{nama} Berpredikat C ");
    elif 40 <= nilai <= 54:
        print(f"{nama} Berpredikat D ");
    elif nilai < 40 :
        print(f"{nama} Berpredikat D ");
    else:
        print("Inputan Tidak Sesuai")
        nama, nilai = inputan()
        cek_nilai(nama, nilai)

nama, nilai = inputan()
cek_nilai(nama, nilai)
#membuat sebuah class untuk absensi di sebuah acara

class Mahasiswa:
    def __init__(self, Nim, Nama, Jurusan, JenisKelamin, Stambuk):
        self.nim = Nim
        self.nama = Nama
        self.jurusan =Jurusan
        self.JenisKelamin = JenisKelamin
        self.stambuk = Stambuk

    def cetak(self):
        print(f"Nim: {self.nim}")
        print(f"Nama: {self.nama}")
        print(f"Jurusan: {self.jurusan}")
        print(f"Jenis Kelamin: {self.JenisKelamin}")
        print(f"Stambuk: {self.stambuk}")
        print("="*30)
class Dosen:
    def __init__(self, Nip, Nama, Jabatan, JenisKelamin, NoHP):
        self.nim = Nip
        self.nama = Nama
        self.Jabatan =Jabatan
        self.JenisKelamin = JenisKelamin
        self.NoHP = NoHP

    def cetak(self):
        print(f"Nim: {self.nim}")
        print(f"Nama: {self.nama}")
        print(f"Jabatan: {self.Jabatan}")
        print(f"Jenis Kelamin: {self.JenisKelamin}")
        print(f"No HP: {self.NoHP}")
        print("="*30)

class Absensi:
    def __init__(self):
        self.daftar_hadir = []

    def tambah_daftar_hadir(self, peserta):
        self.daftar_hadir.append(peserta)

    def cetak_absensi(self):
        print("=== Daftar Absensi ===")
        for idx, peserta in enumerate (self.daftar_hadir, start=1):
            print(f"{idx}.{peserta.nama}")
        print("="*30)

    def hitung_jumlah_hadir(self):
            return len(self.daftar_hadir)

# ==== Program Utama ====
absen = Absensi()



mhs1 =Mahasiswa("241110348", "Aulia", "Teknik Informatika", "Perempuan", "24")
mhs1.cetak()

while True:
    print("\nTambah Peserta:")
    print("1. Mahasiswa")
    print("2. Dosen")
    print("3. Selesai")
    pilihan = input("Pilih: ")

    if pilihan == "1":
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        jurusan = input("Masukkan Jurusan: ")
        jk = input("Masukkan Jenis Kelamin: ")
        stambuk = input("Dari Stambuk mana: ")
        mhs = Mahasiswa(nim, nama, jurusan, jk, stambuk)
        absen.tambah_daftar_hadir(mhs)

    elif pilihan == "2":
        nip = input("Masukkan NIP: ")
        nama = input("Masukkan Nama: ")
        jabatan = input("Masukkan Jabatan: ")
        jk = input("Masukkan Jenis Kelamin: ")
        nohp = input("Masukkan No HP: ")
        dos = Dosen(nip, nama, jabatan, jk, nohp)
        absen.tambah_daftar_hadir(dos)

    elif pilihan == "3":
        break
    else:
        print("Pilihan tidak valid!")

# Cetak daftar absensi
absen.cetak_absensi()
print("Jumlah hadir:", absen.hitung_jumlah_hadir())
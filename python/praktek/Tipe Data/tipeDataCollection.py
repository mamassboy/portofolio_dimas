#List dapat menampung berbagai Tipe data, dan bersifat mutable (bisa diubah) serta dapat di akses melalui indexnya 
Variable_list = ["Indonesia",  "Amerika", "Malaysia", "Jepang", "Korea", 1, 3, 5, True, 17.5]

#tuple dapat menampung berbagai Tipe data, dan bersifat immutable ( tidak bisa diubah) serta dapat di akses melalui indexnya
Variable_tuple = ("Joget", "Jajan", "Tidur")

#set tidak terurut sehingga tidak bisa di indexing dan set juga tidak bisa berisi data duplikat, dan dapat di ubah
Variable_set = {"Dimas", 1, 2, 3, 4,5,2}

#Dictionary tipe data yang memerlukan key dan value, bisa di rubah, serta untuk mengambil velue nya kita perlu tau key nya
Varible_Dict = {"nama" : "Dimas", "umur" : 20, "status" : "Mahasiswa"} 



#mencetak isi dari setiap variable
print(Variable_list)
print(Variable_tuple)
print(Variable_set)
print(Varible_Dict)

#mengakses Value menggunakan index
#list
print(Variable_list[2])

#tuple
print(Variable_tuple[-2])


#mengubah value list pada indek 3
Variable_list[3] = 4
#mengubah data dict
Varible_Dict['nama'] = "Arya"

#untuk mengubah isi set kita perlu menghapus valuenya terlebih dahulu lalu kita bisa mengubah value setnya dengan cara menambahnya dan dia akan berada pada posisi terakhir

print("set sebelum di ubah")
print(Variable_set)

#menghapus data pada set dan dapat digunakan juga di list
Variable_set.remove(1)

#menambahkan data ke set
Variable_set.add(70)

#menambahkan data ke list
Variable_list.append("Dimas")

#menambahkan data dict
Varible_Dict ['alamat'] = "Medan"

print("data setelah di ubah")
print(Variable_list)
print(Variable_tuple)
print(Variable_set)
print(Varible_Dict)



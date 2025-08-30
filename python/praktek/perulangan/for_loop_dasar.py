awalan =int(input("Masukkan awalan: "))
akhiran = int(input("Masukkan akhiran: "))


#cek kategori angka
if awalan % 2 != 0: 
    awalan +=1

print("Bilangan genap dari", awalan, "sampai", akhiran, ":")
for i in  range (awalan, akhiran+1 ):
        print (i)

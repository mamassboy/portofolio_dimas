#Konversi angka ke jarak yakni km/hm/dm/cm

jarak = int(input("masukkan angka yang ingin konfersi menjadi satuan km/hm/dm/cm : "))

km = jarak // 100000
sisa = jarak % 100000
hm = sisa // 10000
sisa1 = sisa % 10000
dm = sisa1 // 1000
cm = sisa1 % 1000

print(f'''{km} km
          {hm} hm
          {dm} dm
          {cm} cm''')



#konversi angka ke satuan waktu

angka=int(input("masukkan angka yang ingin anda konversi: "))

hari = angka // 86400
sisawaktu = angka % 86400
jam = sisawaktu // 3600
sisawaktu1 = sisawaktu % 3600
menit = sisawaktu1 // 60
detik = sisawaktu1 % 60

print(f'''{hari} hari
          {jam} jam
          {menit} menit 
          {detik} detik ''')


# Konversi Luas ke km²-hm²-dam²-m²

luas=int(input("masukkan luas yang ingin anda konversi: "))
km2= luas // 10**6
sisajarak = luas % 10**6
hm2 = sisajarak // 10**4
sisajarak1 = sisajarak % 10**4
dam2 = sisajarak1 // 10**2
m = sisajarak1 % 10**2

print(f'''{km2} km²
          {hm2} hm²
          {dam2} dam²
          {m} m²''')


# Konversi Panjang ke Mil-Yard-Feet-Inch

panjang=int(input("masukkan panjang yang ingin anda konversi: "))
mil = panjang // 63360
sisajarak2 = panjang % 63360
yard = sisajarak2 // 36
sisajarak3 = sisajarak2 % 36
foot = sisajarak3 // 12
inch = sisajarak3 % 12

print(f'''{mil} mill
          {yard} yard
          {foot} foot
          {inch} inch''')
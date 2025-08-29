nama = input("Siapa nama kamu?: ").strip()
while not nama:
    nama = input("Siapa nama kamu?: ").strip()
print(f"Halo {nama}!")

umur = input("Berapa umur kamu?: ").strip()
while not umur.isdigit():
    umur = input("Masukkan umur yang valid (angka): ").strip()
print(f"Ooo salam kenal yaa {nama} yang berusia {umur} tahun!")

# Memasukkan lebih dari satu hobi
hobi = []
while True:
    hobies = input("Sebutkan hobi kamu (ketik 'selesai' jika sudah): ").strip()
    if hobies.lower() == "selesai":
        break
    hobi.append(hobies)

print(f"Bagus banget, hobi kamu: {', '.join(hobi)}")

# Pertanyaan tentang Machine Learning
while True:
    question = input('Apakah kamu mau jadi ahli Machine Learning? (ya/tidak): ').strip().lower()
    if question in ['ya', 'tidak']:
        break
    print("Masukkan jawaban yang benar (ya/tidak)!")

if question == 'ya':
    print("Wihh baguss banget! Tau aja peluang bagus.")
    while True:
        lanjut = input('Apakah kamu mau melanjutkan belajar? (ya/tidak): ').strip().lower()
        if lanjut in ['ya', 'tidak']:
            break
        print("Masukkan jawaban yang benar (ya/tidak)!")
    
    if lanjut == 'ya':
        print("Oke deee, kita lanjutkan!")
    else:
        print("Oke deee, kita berhenti dulu.")

else:
    print("Okee deee, kamu bisa jadi apa aja yang kamu mau!")

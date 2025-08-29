import random
from fungsi import welcome_message

welcome_message()
nama_user = input("Masukkan nama anda: ")

gosth_position = random.randint(1, 5)

nomor_goa = 5
jumlah_goa = " ".join(str(i + 1).center(5) for i in range(nomor_goa))

while True:
    bentuk_goa = ['|_|' for _ in range(nomor_goa)]
    print(f''' Halo {nama_user}
    Pilih Goa mana yang terdapat hantu
        {'   '.join(bentuk_goa)}  
        {jumlah_goa}
    ''')
    
    try:
        pilihan = int(input("Masukkan pilihan anda: "))
        if pilihan < 1 or pilihan > nomor_goa:
            print("Pilihan tidak valid. Silakan pilih nomor goa yang tersedia.")
            continue
    except ValueError:
        print("Harap masukkan angka yang valid.")
        continue
    
    jawaban = input("Apakah anda sudah yakin dengan jawaban anda (y/n)? : ").lower()
    
    if jawaban == "y":
        bentuk_goa[gosth_position - 1] = '|0_0|'
        print(f'''
        {'   '.join(bentuk_goa)}  
        {jumlah_goa}
        ''')
        
        if pilihan == gosth_position:
            print(f"Selamat, Anda telah memilih goa yang terdapat hantu nya!")
        else:
            print(f"Maaf, Anda telah memilih goa yang tidak terdapat hantu nya")
        print(f"Pilihan Anda: Goa ke {pilihan}")
        print(f"Posisi hantu: Goa ke {gosth_position}")
        
        jawaban1 = input("Apakah anda ingin bermain lagi? (y/n): ").lower()
        if jawaban1 == "y":
            gosth_position = random.randint(1, 5)  # Acak ulang posisi hantu
            continue
        else:
            print("Terima kasih telah bermain!")
            break
    elif jawaban == "n":
        continue
    else:
        print("Maaf, jawaban anda tidak valid. Silakan masukkan jawaban yang benar.")

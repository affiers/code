import random


welcome_message = "WELCOME TO CUYPY GAMES"
cuypy_position = random.randint(1,4)

print ("============================")
print(f"== {welcome_message} ==")
print ("============================")

nama_user = input("masukkan nama kamu: ") 

print (f'''
halo {nama_user}! Coba perhatikan goa dibawah ini 
|_| |_| |_| |_|  
''') 

pilihan_user = int(input("Menurut kamu di goa nomor berapa CUYPY berada? [1 / 2 / 3 / 4]: "))

print(f"pilihan kamu adalah {pilihan_user}")

if pilihan_user == cuypy_position:
    print(f"SELAMAT {nama_user} KAMU MENANG! Posisi Cuypy ada di {cuypy_position} dan pilihanmu adalah {pilihan_user}.")
else:
    print(f"KAMU KALAH! CUYPY BERADA DI {cuypy_position} DAN PILIHANMU BUKAN DISITU")



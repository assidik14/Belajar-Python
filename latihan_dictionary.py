import datetime as dt
import os
import string
import random

operatingSystem = os.name

# Template mahasiswa
mahasiswa_template = {
    'nama':'nama',
    'nim':'00000000',
    'sks':0,
    'lahir':dt.datetime(1111,11,1)
}

# Dictionary kosong untuk menyimpan data mahasiswa
data_mahasiswa = {}

while True:

    match operatingSystem:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    print(5*"-", " Data mahasiswa ", 5*"-")
    print(28*"=")

    # Dictionary mahasiswa untuk menampung input dari user berdasarkan key yang diambil dari dictionary mahasiswa_template
    mahasiswa = dict.fromkeys(mahasiswa_template.keys())

    # Input user
    mahasiswa['nama'] = input("Masukan Nama mahasiswa : ")
    mahasiswa['nim'] = input("Masukan NIM mahasiswa : ")
    mahasiswa['sks'] = int(input("Masukan SKS lulus : "))
    tanggal = int(input("Masukan tanggal lahir (1-31) : "))
    bulan = int(input("Masukan bulan lahir (1-12) : "))
    tahun = int(input("Masukan tahun lahir (yyyy) : "))
    mahasiswa['lahir'] = dt.datetime(tahun, bulan, tanggal)

    # Membuaut key random untuk data mahasiswa sebanyak 6 karakter string
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))

    # Update input kedalam dictionary data mahasiswa
    data_mahasiswa.update({KEY:mahasiswa})

    # print(data_mahasiswa)

    print(f"\n{'KEY':<10} {'NAMA':<20} {'NIM':<15} {'SKS':<5} {'LAHIR':<10}")
    print(60*"-")

    # Mengambil dan menampilkan value dari data_mahasiswa
    for data in data_mahasiswa:
        KEY = data
        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

        print(f"{KEY:<10} {NAMA:<20} {NIM:<15} {SKS:<5} {LAHIR:<10}")


    # Kondisi program selesai
    is_done = input("\nApakah selesai (n/y) : ")
    if is_done == "y" or is_done == "Y":
        break

print(28*"=")
print("Program selesai")
import os

# Fungsi
def judul():
    '''Fungsi menampilkan judul aplikasi'''
    print(f"{'SELAMAT DATANG':^30}")
    print(f"{'APLIKASI RUMUS PERSEGI PANJANG':^30}")
    print(30*"=")

def input_user():
    '''Fungsi untuk mengambil input dari user'''
    panjang = int(input("Masukan panjang \t : "))
    lebar = int(input("Masukan lebar \t\t : "))
    return panjang, lebar

def hitung(panjang, lebar):
    '''Fungsi menghitung rumus persegi panjang'''
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling

def hasil(luas, keliling):
    '''Fungsi menampilkan hasil perhitungan'''
    print(f"Luas persegi panjang \t : {luas}")
    print(f"Keliling persegi panjang : {keliling}")


# Main App
sistem_operasi = os.name

while True:

    if sistem_operasi == "posix":
        os.system("clear")
    else:
        os.system("cls")

    judul()
    panjang, lebar = input_user()
    luas, keliling = hitung(panjang, lebar)
    print(30*"-")
    hasil(luas, keliling)
    print(30*"-")
    is_done = input("Apakah selesai (y/n) \t : ")
    if is_done == "y" or is_done == "Y":
        break

print(30*"-")
print("Program selesai")
print(30*"-")
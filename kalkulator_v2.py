import os

# Global Variable
sisop = os.name


# Functions
def separator():
    print(30*"=")

def menu():
    print(7*"=" + " Kalkulator V2 " + 8*"=")
    separator()
    for i in range(9):
        i += 1
        match i :
            case 1 : print(f"{i}. Operasi Penjumlahan")
            case 2 : print(f"{i}. Operasi Pengurangan")
            case 3 : print(f"{i}. Operasi Perkalian")
            case 4 : print(f"{i}. Operasi Pembagian")
            case 5 : print(f"{i}. Operasi Modulus (Sisa pembagian)")
            case 6 : print(f"{i}. Operasi Floor Division (Pembagian di bulatkan ke bawah)")
            case 7 : print(f"{i}. Operasi Exponen (Pangkat)")
            case 8 : print(f"{i}. Rumus Persegi Panjang")
            case 9 : print(f"{i}. Rumus Persegi")
    separator()

def penjumlahan(x, y):
    hasil = x + y
    print(f"Hasil dari {x} + {y} = {hasil}")
    return hasil

def pengurangan(x, y):
    hasil = x - y
    print(f"Hasil dari {x} - {y} = {hasil}")
    return hasil

def perkalian(x, y):
    hasil = x * y
    print(f"Hasil dari {x} x {y} = {hasil}")
    return hasil

def pembagian(x, y):
    hasil = x / y
    print(f"Hasil dari {x} : {y} = {hasil:.2f}")
    return hasil

def modulus(x, y):
    hasil = x % y
    print(f"Hasil dari {x} Mod {y} = {hasil}")
    return hasil

def floordiv(x, y):
    hasil = x // y
    print(f"Hasil dari {x} Floor Division {y} = {hasil}")
    return hasil

def exponen(x, y):
    hasil = x ** y
    print(f"Hasil dari {x} Pangkat {y} = {hasil}")
    return hasil

def persgiPanjang(x, y):
    luas = x * y
    keliling = 2 * (x + y)
    print(f"Luas Persegi Panjang = {x} x {y} = {luas}")
    print(f"Keliling Persegi Panjang = 2 x ({x} + {y}) = {keliling}")
    return luas, keliling

def persegi(x):
    luas = x * x
    keliling = 4 * x
    print(f"Luas Persegi = {x} x {x} = {luas}")
    print(f"Keliling Persegi = 4 x {x} = {keliling}")
    return luas, keliling


# Main App
if __name__ == "__main__":

    while (True):

        match sisop:
            case "posix" : os.system("clear")
            case "nt" : os.system("cls")

        menu()

        pilihMenu = int(input("Masukan operasi : "))
        
        if pilihMenu <= 0 or pilihMenu > 9:
            while pilihMenu <=0 or pilihMenu > 9:
                print("Opps, operasi yang kamu pilih salah!!")
                pilihMenu = int(input("Masukan operasi lagi: "))
        
            separator()

        match pilihMenu :
            case 1 : print("Kamu pilih operasi penjumlahan")
            case 2 : print("Kamu pilih operasi pengurangan")
            case 3 : print("Kamu pilih operasi perkalian")
            case 4 : print("Kamu pilih operasi pembagian")
            case 5 : print("Kamu pilih operasi modulus")
            case 6 : print("Kamu pilih operasi floor division")
            case 7 : print("Kamu pilih operasi exponen")
            case 8 : print("Kamu pilih rumus persegi panjang")
            case 9 : print("Kamu pilih rumus persegi")

        if pilihMenu <= 7:
            angka1 = int(input("Masukkan angka pertama : "))
            angka2 = int(input("Masukkan angka kedua : "))
        elif pilihMenu == 8:
            angka1 = int(input("Masukkan Panjang : "))
            angka2 = int(input("Masukkan Lebar : "))
        elif pilihMenu == 9:
            sisi = int(input("Masukkan Sisi : "))

        match pilihMenu :
            case 1 : penjumlahan(angka1, angka2)
            case 2 : pengurangan(angka1, angka2)
            case 3 : perkalian(angka1, angka2)
            case 4 : pembagian(angka1, angka2)
            case 5 : modulus(angka1, angka2)
            case 6 : floordiv(angka1, angka2)
            case 7 : exponen(angka1, angka2)
            case 8 : persgiPanjang(angka1, angka2)
            case 9 : persegi(sisi)

        separator()
        selesai = input("Apakah selesai (y/n) : ")
        if selesai == 'y' or selesai == "Y":
            break

    separator()
    print("Program Selesai")
    separator()
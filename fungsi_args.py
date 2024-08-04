'''
ARGS pada fungsi
1. ARGS adalah argument atau parameter pada sebuah fungsi, dimana argument tersebut mengizinkan kita untuk memberikan banyak nilai untuk diolah oleh fungsi tersebut.
2. ARGS menggunakan symbol * sebelum variable arguman contohnya : *friends.
3. ARGS bertipe tuples variable, sehingga datanya bisa di iterasi
'''

# Contoh tidak menggunakan ARGS
def tambah(angka1:int, angka2:int, angka3:int)->int:
    '''Fungsi tambah tanpa menggunakan ARGS'''
    hasil = angka1 + angka2 + angka3
    return hasil

hasilnya = tambah(1, 2, 3) # Argument / Parameter itu harus sesuai dengan argumen yg di inisialisasi pada fungi, dalam case ini fungsi tambah memiliki 3 argumen
print(f"Hasil fungsi tanpa ARGS = {hasilnya}")


# Contoh menggunakan ARGS
def penjumlahan(*kumpulan_angka:int)->int:
    '''Fungsi tambah menggunakan ARGS'''
    print(f"Ini adalah variable kumpulan angka = {kumpulan_angka}") # Ini untuk membuktikan bahwa variabel kumpulan angka berisi beberapa nilai
    print(f"Type variable kumpulan angka = {type(kumpulan_angka)}") # Ini untuk membuktikan bahwa variable kumpulan angka bertipe tuple
    for angka in kumpulan_angka:
        angka += angka
    return angka

hasilnya_lagi = penjumlahan(1, 2, 3, 4)
print(f"Hasil fungsi menggunakan ARGS = {hasilnya_lagi}")


# Contoh lain menggunakan ARGS
def sapa (*teman_teman:str)->str:
    '''Fungsi sapa teman menggunakan ARGS'''
    for teman in teman_teman:
        print(f"Hallo {teman}")

sapa("Ucup", "Otong", "Udin", "Odah", "Asep")
'''
KWARGS pada fungsi
1. KWARGS adalah argument atau parameter pada sebuah fungsi, dimana argument tersebut mengizinkan kita untuk memberikan banyak nilai untuk diolah oleh fungsi tersebut.
2. KWARGS menggunakan symbol ** sebelum variable arguman contohnya : **friends.
3. KWARGS bertipe dictionary variable, sehingga datanya memiliki key dan value
'''

# Contoh fungsi tanpa KWARGS
def teman_teman(nama, tinggi, berat):
    '''Fungi tanpa KWARGS'''
    print(f"si {nama}, tingginya {tinggi} dan beratnya {berat}")

teman_teman("Ucup", 170, 56)

# Contoh fungsi dengan KWARGS
def MyFriends(**kwargs):
    '''Fungsi dengan KWARGS'''
    nama = kwargs['nama']
    tinggi = kwargs['tinggi']
    berat = kwargs['berat']
    print(f"si {nama}, tingginya {tinggi} dan beratnya {berat}")

MyFriends(nama="Otong", tinggi=165, berat=50)


# Contoh lain KWARGS
def math(*kumpulan_angka:int, **operasi:str)->int: # *kumpulan_angka = tuples, **operasi = dictionary
    if operasi["opsi"] == "tambah": # Jika variable operasi dengan keys opsi nilainya 'tambah'
        print("Operasi penjumlahan")
        hasil = 0 # variable hasil untuk menyimpan hasil penjumlahan variable kumpulan_angka
        for angka in kumpulan_angka: # Maka iterasi kumpulan_angka dengan variable angka
            hasil += angka # jumlah kan semua variable angka, disimpan dalam variable hasil
    elif operasi["opsi"] == "kali": # Jika variable operasi dengan keys opsi nilainya 'kali'
        print("Operasi perkalian")
        hasil = 1 # variable hasil untuk menyimpan hasil penjumlahan variable kumpulan_angka
        for angka in kumpulan_angka: # Maka iterasi kumpulan_angka dengan variable angka
            hasil *= angka # kali kan semua variable angka, disimpan dalam variable hasil
    else:
        print("Tidak ada opsi yg dipilih")
    
    return hasil # kembalikan variable hasil

hasilnya = math(1,2,3,4,opsi="tambah")
print(hasilnya)
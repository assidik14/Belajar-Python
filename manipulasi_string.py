# Menyambung string (Concatenate)
nama_depan = input("Masukan nama depan : ")
nama_tengah = input("Masukan nama tengah : ")
nama_belakang = input("Masukan nama belakang : ")
nama_lengkap = nama_depan + " " + nama_tengah + " " + nama_belakang

print ("Hallo, " + nama_lengkap)

# Menghitung panjang string
panjang = len(nama_lengkap)
print ("Panjang nama lengkap = "+ str(panjang) + " karakter")

# Indexing (Mengambil data dari string, dimulai dari index ke-0)
index = int(input("Mau index ke berapa = "))
print("Indek ke-" + str(index) + " dari " + nama_lengkap + " adalah = " + nama_lengkap[index] )

# Range atau slicing
slice_pertama = int(input("Slice awal = "))
slice_kedua = int(input("Slice akhir = "))
print("Potongan karakter ke-" + str(slice_pertama) + " sampai dengan karakter ke-" + str(slice_kedua) + " dari " + nama_lengkap + " adalah = " + nama_lengkap[slice_pertama:slice_kedua])

# Melihat karakter dengan nilai ASCII Code paling besar
print("Karakter dengan nilai paling besar adalah = " + max(nama_lengkap))
print("Dengan nilai ASCII nya adalah " + str(ord(max(nama_lengkap))))

# Melihat karakter dengan nilai ASCII Code paling kecil
print("Karakter dengan nilain paling kecil adalah = " + min(nama_lengkap))
print("Dengan nilai ASCII nya adalah " + str(ord(min(nama_lengkap))))

# Cara mengecek nilai ASCII sebagai karakter
nilai_ascci = int(input("Masukan nilai ASCII yang akan di konversi sebagai karakter : "))
print("Karakter untuk ASCII Code dari " + str(nilai_ascci) + " adalah = " + chr(nilai_ascci))

# Operator untuk string :
# 1. Cek ada karakter atau string dalam string
c_kecil = "c"
cek1 = c_kecil in nama_lengkap
print ("Karakter " + c_kecil + " ada di " + nama_lengkap + " = " + str(cek1))

c_besar = "C"
cek2 = c_besar in nama_lengkap
print ("Karakter " + c_besar + " ada di " + nama_lengkap + " = " + str(cek2))

# 2. Cek tidak ada karakter atau string dalam string
d_kecil = "d"
cek3 = d_kecil not in nama_lengkap
print ("Karakter " + d_kecil + " tidak ada di " + nama_lengkap + " = " + str(cek3))

d_besar = "D"
cek4 = d_besar not in nama_lengkap
print ("Karakter " + d_besar + " tidak ada di " + nama_lengkap + " = " + str(cek4))

# Mengulang string
ulang_ketawa = int(input("Mau ketawa berapa kali = "))
ketawa = "wk"
print ("Ulang ketawa sebanyak " + str(ulang_ketawa) + " = " + 10*ketawa)
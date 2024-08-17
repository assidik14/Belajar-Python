'''Global dan Local Scope'''

nama_global = "Otong" # Ini adalah variabel global bisa di panggil dimanapun

def tes():
    '''Fungsi untuk tes variable global'''
    nama_local = "Ucup" # Ini adalah variable local di dalam fungsi, hanya bisa dipanggil didalam fungsi tes()
    print(f"{nama_global} adalah variable global")
    print(f"{nama_local} adalah variable local")

tes()

# Contoh
angka = 1 # global variable dengan nama angka

def ubah_angka(nilai_baru):
    '''Fungsi merubah nilai variable global'''
    global angka # Perintah ini artinya adalah meng-akses global variable dengan nama angka
    angka = nilai_baru

print(f"Sebelum di ubah = {angka}")
ubah_angka(10)
print(f"Setelah di ubah = {angka}")

# Catatan :
# Ini hanya berlaku di fungsi
# Tidak berlaku pada for loop dan if
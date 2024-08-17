# File __init__.py adalah file dalam package yang mana akan mengeksekusi perintah pertama kali saat package di import

import sains

hasil_gaya = sains.fisika.gaya(10, 95)
print(f"Hasil Gaya = {hasil_gaya}")

hasil_tambah = sains.matematika.tambah(1,2,3,4,5)
print(f"Hasil tambah = {hasil_tambah}")

hasil_kali = sains.matematika.kali(1,2,3,4,5)
print(f"Hasil kali = {hasil_kali}")

pangkat_2 = sains.matematika.pangkat(2)
print(f"Hasil 5 pangkat 2 = {pangkat_2(5)}")
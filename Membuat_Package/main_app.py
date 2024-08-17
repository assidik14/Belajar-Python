# Package adalah tempat dimana kita meletakan kumpulan module-module yang kita buat

# Meng-import package sains module matematika
import sains.matematika

hasil_tambah = sains.matematika.tambah(1,2,3,4,5)
print(f"Hasil penjumlahan dari package sains, module matematika, fungsi tambah = {hasil_tambah}")

# Meng-import package sains module fisika menggunakan from
from sains import fisika

hasil_gaya = fisika.gaya(90, 10)
print(f"Gaya adalah = {hasil_gaya}")
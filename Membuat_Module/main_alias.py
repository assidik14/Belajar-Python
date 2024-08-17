# Import fungsi tertentu dari module matematika menggunakan alias
# Jika import menggunakan alias tidak bisa sekaligus, harus satu-satu
from matematika import tambah as penjumlahan
from matematika import kali as perkalian
from matematika import pangkat as perpangkatan

hasil_jumlah = penjumlahan(1,2,3,4,5)
print(f"Hasil penjumlahan adalah = {hasil_jumlah}")

hasil_kali = perkalian(1,2,3,4,5)
print(f"Hasil perkalian adalah = {hasil_kali}")

pangkat_3 = perpangkatan(3)
print(f"Hasil dari 3 pangkat 3 adalah = {pangkat_3(3)}")
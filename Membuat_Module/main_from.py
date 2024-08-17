# Import fungsi tertentu dari module matematika menggunakan from
from matematika import tambah, kali

hasil_jumlah = tambah(1,2,3,4,5)
print(f"Hasil penjumlahan adalah = {hasil_jumlah}")

hasil_kali = kali(1,2,3,4,5)
print(f"Hasil perkalian adalah = {hasil_kali}")

# Fungsi pangkat tidak berjalan karena fungsi belum di import dari module matematika
# pangkat_3 = matematika.pangkat(3)
# print(f"Hasil dari 3 pangkat 3 adalah = {pangkat_3(3)}")
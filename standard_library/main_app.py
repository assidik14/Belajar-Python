import datetime # Library ini digunakan untuk mengambil format waktu

data_waktu = datetime.datetime.now()
print(f"Datetime now : {data_waktu}")
print(f"Tahun : {data_waktu.year}")
print(f"Hari : {data_waktu.strftime('%A')}")


from collections import Counter # Libary ini digunakan untuk melakukan counting dengan mudah

# Studi kasus
data_list = ['a', 'b', 'e', 's', 'a', 't', 'x', 'q', 'a', 'c', 'd', 'v', 'a']

# Jika kita counting / menghitung jumlah suatu huruf dari data_list tanpa standard libarary, maka akan seperti ini
count = 0
for data in data_list:
    if data == 'a':
        count += 1

print(f"Jumlah huruf a = {count}")
# Jadinya ribed...

# Dengan standard library yang sudah disediakan, maka akan menjadi seperti ini
data_count = Counter(data_list)
print(data_count) # Dapat kita simpulkan bahwa counter ini sudah secara otomatis melakukan count tiap element data_list dalam bentuk dictionary
# Jadi jika kita ingin meng-counter huruf a misalnya menjadi seperti :
print(f"Jumlah huruf a = {data_count['a']}")

import io # Ini adalah standard library yang sudah disediakan oleh pyhton terkait tentang input/output file

file = io.open("standard_library/tes.txt", "r", encoding="utf-8") # Open file tes.txt
baca_tes_txt = file.read() # Baca file tes.txt
print(baca_tes_txt) # Tampilkan isi file tes.txt
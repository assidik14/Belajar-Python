'''Membaca file external'''

print(3*"-", " Membaca file.txt ", 3*"-")

# Membuka file.txt dengan mode read only
file = open("Read_External_File/file.txt", mode="r", encoding="utf-8")

# Mengecek apakah file.txt bisa di baca atau tidak :
print(f"Status read = {file.readable()}")

# Mengecek apakah file.txt bisa di tulis atau tidak :
print(f"Status write = {file.writable()}") # ini akan false / tidak bisa ditulis karena file.txt di open dalam mode read-only

print(file.read()) # Membaca file.txt secara keseluruhan
# print(file.readline()) # Membaca file.txt baris per-baris
# print(file.readlines()) # Membaca isi file dalam bentuk list

# Catatan :
# Setiap file open, itu harus di close kembali dengan cara :
print(f"Apakah file.txt sudah di close = {file.closed}") # Ini digunakan untuk mengecek apakah file sudah di close
file.close() # Ini digunakan untuk menutup / meng-close file
print(f"Apakah file.txt sudah di close = {file.closed}")

# Catatan :
# Jika kita melakukan hal di atas maka akan ribed, karena setiap kita membuka file itu harus di close lagi
# Maka ada sebuah teknik, dimana ketika kita membuka file maka kita tidak perlu melakukan close
# Yaitu kita open file dengan menggunakan with

print("\n", 3*"-", " Membaca file.txt dengan with ", 3*"-")

with open("Read_External_File/file.txt", mode="r", encoding="utf-8") as file:
    content = file.read()
    print(content)
    print(f"Apakah file.txt sudah di close = {file.closed}") # Code yang ada di dalam with, maka file.txt akan open

print(f"Apakah file.txt sudah di close = {file.closed}") # Tapi jika kita menulis code diluar with maka file.txt otomatis akan close
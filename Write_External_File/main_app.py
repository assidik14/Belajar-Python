'''Menulis ke external file'''

# 1. Mode write
with open("Write_External_File/data1.txt", mode="w", encoding="utf-8") as file:
    file.write("Hallo, tulisan ini akan di tulis pada file data1.txt")


with open("Write_External_File/data1.txt", mode="w", encoding="utf-8") as file:
    file.write("Tulis ke file data1.txt lagi, maka tulisan sebelumnya di overwrite tulisan ini")

# Catatan :
# Dia akan membuat file baru jika sebelumnya tidak ada
# Lalu akan meng-overwrite isinya

# 2. Mode append
with open("Write_External_File/data1.txt", mode="a", encoding="utf-8") as file:
    file.write("\nTulisan ini ditambahkan ke file data1.txt dengan mode append")

with open("Write_External_File/data1.txt", mode="a", encoding="utf-8") as file:
    file.write("\nTambah lagi dengan append")

# Catatan :
# Jika menggunakan mode append, maka isinya tidak akan di overwrite

# 3. Mode r+
with open("Write_External_File/data2.txt", mode="w", encoding="utf-8") as file:
    file.write("Baris-1\n")

with open("Write_External_File/data2.txt", mode="a", encoding="utf-8") as file:
    file.write("Baris-2")

with open("Write_External_File/data2.txt", mode="r+", encoding="utf-8") as file:
    file.write("Baris-3")
    print(f"Apakah file bisa di baca = {file.readable()}")
    print(file.read())

# Catatan :
# Mode r+, akan menimpa isi dari file data2.txt sesuai panjang datanya
# Dengan mode r+ maka file data2.txt juga bisa di baca(readable)
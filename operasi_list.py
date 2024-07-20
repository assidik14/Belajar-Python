angka = [3,1,4,5,6,8,4,2,1,3,5,4,6,9,4,7,5,3,1,5,6,4,7]
# print(angka)

# 1. count data
# jumlah_angka_4 = angka.count(4)
# print(jumlah_angka_4)

# 2. ambil posisi data (index ke berapa)
data = ["Otong", "Asep", "Dudung", "Odah", "Jajang"]
# print(data)
# index_dudung = data.index("Dudung")
# print(f"Dudung ada di index ke-{index_dudung}")

# 3. mengurutkan list
print(f"Data integer sebelum di urutkan = \n{angka}")
print(f"Data string sebelum di urutkan = \n{data}")

urutkan_data_int = angka.sort()
urutkan_data_str = data.sort()

print(f"Data integer sesudah di urutkan = \n{angka}")
print(f"Data string sesudah di urutkan = \n{data}")

# 4. mengurutkan list dari belakang

urutkan_data_int = angka.reverse()
urutkan_data_str = data.reverse()

print(f"Data integer di urutkan dari belakang = \n{angka}")
print(f"Data string di urutkan dari belakang = \n{data}")

# catatan : untuk mengurutkan data dari belakang, maka data harus di sort dulu
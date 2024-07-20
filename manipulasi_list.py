data = ["Ucup", "Otong", "Odah"]
#Index   0(-1)   1(-2)    2(-1)

print(data)

# 1. Indexing
data_0 = data[0]
print(data_0)

data_terakhir = data[-1]
print(data_terakhir)

# 2. Mengambil info jumlah data list
jumlah_data = len(data)
print(f"Panjang data adalah {jumlah_data}")

# 3. Menambahkan item sesuai posisi
tambah_data = data.insert(2,"Asep")
print(data)

tambah_diakhir = data.append("Jajang")
print(data)

# 4. Menggabungkan list
data2 = ["Ujang", "Dadang"]
gabung_list = data.extend(data2)
print(data)

# 5. Merubah data sesuai index
data[2] = "Cecep"
print(data)

# 6. Menghapus data
hapus_data = data.remove("Cecep") # Case sensitive
print(data)

# 7. Menghapus data terakhir
hapus_terakhir = data.pop()
print(data)
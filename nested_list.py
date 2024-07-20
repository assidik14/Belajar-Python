# Nested list atau  List bersarang atau list 2 Dimensi

# list_biasa = [1,2,3,4,5]

# list_a = [1,2]
# list_b = [3,4,5]

# list_2d = [list_a, list_b]

# print(f"List biasa = {list_biasa}")
# print(f"List 2 Dimensi = {list_2d}")

# Contoh penggunaan 

mahasiswa_1 = ["Ucup", 25, "Laki-laki", "Informatika"]
mahasiswa_2 = ["Jajang", 27, "Laki-laki", "Ekonomi"]
mahasiswa_3 = ["Odah", 24, "Perempuan", "Akutansi"]

mahasiswa = [mahasiswa_1, mahasiswa_2, mahasiswa_3]
# print(f"List mahasiswa = {mahasiswa}")

for data_mahasiswa in mahasiswa:
    print(f"Nama \t\t: {data_mahasiswa[0]}")
    print(f"Umur \t\t: {data_mahasiswa[1]}")
    print(f"Gender \t\t: {data_mahasiswa[2]}")
    print(f"Jurusan \t: {data_mahasiswa[3]}\n")
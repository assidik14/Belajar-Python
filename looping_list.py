# looping dari list

kumpulan_angka = [3,2,1,4,5,4,6,5,1,2,7,8,9,6,5]
kumpulan_peserta = ["ucup", "dadang", "Asep", "Odah", "Otong"]

# 1. For loop
# for angka in kumpulan_angka:
#     print(f"Angka = {angka}")

# for peserta in kumpulan_peserta:
#     print(f"Nama Peserta = {peserta}")



# 2. For loop dan Range

# panjang_list = len(kumpulan_angka)
# for angka in range(panjang_list):
#     print(f"Angka = {kumpulan_angka[angka]}")

# 3. While loop
# panjang_list = len(kumpulan_angka)
# i = 0
# while i < panjang_list:
#     print(f"angka = {kumpulan_angka[i]}")
#     i += 1

# 4. list comprehension
# [print(f"angka = {angka}") for angka in kumpulan_angka]
# [print(f"Nama peserta = {i}") for i in kumpulan_peserta]

# 5. Enumerate, dimana akan mengambil index dan datanya
for index, data in enumerate(kumpulan_peserta):
    print(f"Index = {index}, datanya = {data}")

for x, y in enumerate(kumpulan_angka):
    print(f"index = {x}, datanya = {y}")
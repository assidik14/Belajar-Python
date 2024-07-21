print("Duplikasi nested list menggunakan copy")
print(10*"-")

peserta_1 = ["Odah", "Ucup"]
peserta_2 = ["'Udin", "Asep"]

peserta = [peserta_1, peserta_2]
peserta_copy = peserta.copy()   # Copy nested list

print(f"List asli = {peserta}")
print(f"List copy = {peserta_copy}")

# Secara sekilas memang ID nested list berbeda
print(f"ID asli = {hex(id(peserta))}")
print(f"ID copy = {hex(id(peserta_copy))}")

# Tapi kalo di liat lebih dalam (list dalam nested list), ternyata ID nya masih sama
print(f"ID isi nested list peserta list peserta_1 asli = {hex(id(peserta[0]))}")
print(f"ID isi nested list peserta_copy list peserta_1 copy = {hex(id(peserta_copy[0]))}")

# Maka datanya masih berkaitan

print("\n",10*"=","\n")

print("Duplikasi nested list menggunakan deepcopy")
print(10*"-")

# Teknik duplikasi nested list menggunakan deepcopy

# 1. Import deepcopy
from copy import deepcopy

peserta_deepcopy = deepcopy(peserta)

print(f"List asli = {peserta}")
print(f"List deepcopy = {peserta_deepcopy}") # 2. Copy nested list menggunakan deepcopy

# Terlihat bahwa ID nested berbeda
print(f"ID asli = {hex(id(peserta))}")
print(f"ID deepcopy = {hex(id(peserta_deepcopy))}")

# Dan ID list dalam nested list juga berbeda
print(f"ID isi nested list peserta list peserta_1 asli = {hex(id(peserta[0]))}")
print(f"ID isi nested list peserta_deepcopy list peserta_1 copy = {hex(id(peserta_deepcopy[0]))}")

# Artinya data nya sama tapi tidak saling terikat
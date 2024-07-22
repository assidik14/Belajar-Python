# Data collection selain list adalah tuples dan sets

# 1. Tuples
data_tuples = (3,2,1,4,5,6,9,8,7,7)
print(data_tuples)

# Karakteristik :

# Menggunakan tanda ()

# Mendukung indexing
# print(data_tuples[1])

# Datanya tidak bisa rubah, dihapus, ataupun di tambah
# data_tuples[1] = 3 # ini akan error

# Datanya bisa mengandung data yang sama dalam sebuah tuples
# angka_7 = data_tuples.count(7)
# print(angka_7)


# 2. Sets
data_sets = {6,5,4,1,1,2,2,3,6,8,7,9,5,5}
print(data_sets)

# Karakteristik :

# Menggunakan tanda {}

# Tidak mendukung indexing
# print(data_sets[1]) # ini akan error

# Datanya tidak bisa rubah tapi bisa dihapus dan di tambah
data_sets.remove(9)
data_sets.pop()
data_sets.add(10)

print(data_sets)

# Datanya tidak bisa mengandung data yang sama dalam sebuah sets

# 1. list
# angka = [1, 2, 3]
# print(angka)

# 2. list pake range()
# data_range = range(0, 10, 2) # (start, stop, step)
# angka = list(data_range)
# print(angka)

# 3. list pake for (list comprehension)
# angka = [i for i in range(0, 10)]
# print(angka)

# 4. list for-if
angka = [i for i in range(10) if i % 2 == 1]
print(angka)
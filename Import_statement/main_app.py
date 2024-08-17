# Import
# Fungsinya adalah untuk mengambil program dari luar / external file .py

# 1. Untuk menyambung program
# Import program_print.py
import program_print

# 2. Import dengan data
import variable
print(variable.data) # variable dengan nama data, ada pada namespace variable

# 3. Import dengan fungsi
import matematika
hasil = matematika.tambah(4,5) # Fungsi tambah ada pada namespace matematika
print(hasil)
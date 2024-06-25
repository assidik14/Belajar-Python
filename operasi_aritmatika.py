a = 10
b = 3


print ("==== OPERASI ARITMATIKA STANDAR ====")

# Operasi Penjumlahan +
hasil_penjumlahan = a + b
print("Hasil dari ", a," + ", b, "=", hasil_penjumlahan)
print(type(hasil_penjumlahan))

# Operasi Pengurangan -
hasil_pengurangan = a - b
print("Hasil dari ", a," - ", b, "=", hasil_pengurangan)
print(type(hasil_pengurangan))

# Operasi Perkalian *
hasil_perkalian = a * b
print("Hasil dari ", a," * ", b, "=", hasil_perkalian)
print(type(hasil_perkalian))

# Operasi Pembagian /
hasil_pembagian = a / b
print("Hasil dari ", a," * ", b, "=", hasil_pembagian)
print(type(hasil_pembagian)) # Keren-nya Python adalah, hasilnya otomatis menjadi FLOAT


print ("==== OPERASI ARITMATIKA KHUSUS ====")

# Operasi eksponen (PANGKAT) **
hasil_pangkat = a ** b
print("Hasil pangkat dari ", a," ** ", b, "=", hasil_pangkat)
print(type(hasil_pangkat))

# Operasi Modulus (SISA PEMBAGIAN) %
hasil_mod = a % b
print("Hasil modulus ", a," % ", b, "=", hasil_mod)
print(type(hasil_mod))

# Operasi Floor Division (PEMBAGIAN YANG DIBULATKAN KEBAWAH), keblikan dari modulus //
hasil_floordiv = a // b
print("Hasil Floor Division ", a," // ", b, "=", hasil_floordiv)
print(type(hasil_floordiv))


# PRIORiTAS OPERASI
# 1. ()
# 2. Eksponen
# 3. Perkalian, Pembagian, Floor Divison, Modulus
# 4. Pertambahan, Pengurangan
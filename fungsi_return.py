# return adalah nilai kembali dari fungsi

# Dalam matematika :
# y = f(x)
# atau dibaca :
# hasil = fungsi(parameter atau input)

# def nama_fungsi(input):
    # badan fungsi
    # return output

# Contoh fungsi tidak menggunakan return
def pengurangan(angka1, angka2):
    hasil = angka1 - angka2
    print(hasil)

print(pengurangan(4,3))

x = pengurangan(4,3)
print(x)

print("\n")

# Contoh fungsi menggunakan return
def penjumlahan(angka1, angka2):
    hasil = angka1 + angka2
    return hasil

print(penjumlahan(4,3)) # print menampilkan nilai kembali dari penjumlahan 4 + 3

y = penjumlahan(4,3) # y adalah nilai kembali dari penjumlahan 4 + 3
print(y)

# Sehingga kita bisa membuat perhitungan yg lebih rumit
z = 3 * penjumlahan(7,2) / 2
print(z)


# Contoh lain
def perkalian(angka1, angka2):
    return angka1 * angka2

a = perkalian(2,4)
print(a)


# Fungsi dengan banyak return
def operasi_matematika(angka1, angka2):
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2

    return tambah, kurang, kali, bagi

k, l, m, n = operasi_matematika(8,3)

print(f"Hasil tambah = {k}")
print(f"Hasil kurang = {l}")    
print(f"Hasil kali = {m}")
print(f"Hasil bagi = {n}")


# Kesimpulannya :
# Input -> Fungsi -> Output
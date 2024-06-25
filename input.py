# Jika kita hanya menggunakan input, maka typedata-nya pasti STRING
# nama = input("Masukkan nama : ")
# kota = input("Di kota mana kamu tingga : ")
# print ("Typedata nama adalah ", type(nama), "dan Typedata kota adalah", type(kota))
# print ("Hallo, ", nama)
# print (kota, "adalah tempat yang bagus")

# Jika kita ingin mengambil input dari user menggunakan typedata integer, maka harus menggunakan input didalam integer
# angka = int(input("Masukkan angka : ")) # Data yang dimasukkan harus berupa angka
# print("Typedata angka adalah ", type(angka))
# print("Variabel angka ber-nilai = ", angka)

# Jika kita ingin mengambil input dari user berupa boolean
value_boolean = bool(int(input("Masukkan nilai : "))) # HARUS DI CASTING DULU MENJADI INTEGER
print("Typedata-nya adalah : ", type(value_boolean))
print("Nilai nya adalah : ", value_boolean)
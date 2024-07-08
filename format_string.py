## 
# Sebelumnya jika kita ingin menggabungkan data dalam format string,
# kita menggunakan concat (+) tapi ini hanya berlaku sesama string,
# sehingga jika kita melakukan concate dengan variable lain harus di casting dulu ke format string.
# Dengan format, jika kita ingin menggabungkan data varibale dalam format string,
# kita tidak perlu lagi melakukan casting

# contoh generic
nama = "Ucup"
Kota = "Jakarta"
Umur = 25

concat_string = "Nama saya " + nama + ", saya tinggal di kota " + Kota + ", usia saya " + str(Umur) + " tahun" # karena umur bernilai integer, maka harus di casting ke string
print(concat_string)

format_string = f"Nama saya {nama}, saya tinggal di kota {Kota}, usia saya {Umur} tahun" # umur tidak perlu di casting
print(format_string)

cek_lower = nama.islower()
print(f"Apakah {nama} huruf kecil semua = {cek_lower}")

cek_upper = nama.isupper()
print(f"Apakah {nama} huruf besar semua = {cek_upper}")

cek_title = nama.istitle()
print(f"Apakah {nama} diawali dengan huruf besar = {cek_title}")

cek_number = str(Umur).isdecimal()
print(f"Apakah {Umur} berupa angka = {cek_number}")

# Bilangan ribuan
harga = 10000
print(f"Harga = {harga}") # Bilangan ribuan tanpa koma
print(f"Harganya = {harga:,}") # Bilangan ribuan menggunakan koma

# Bilangan desimal
angka = 2024.54321
format_str = f"angka = {angka:.3f}" # :3.f artinya menampilkan 3 angka di belakang koma, bisa atur mau berapapun angka di belakang koma
print(format_str)

# Leading Zero
angka = 2024.54321
format_str = f"angka = {angka:010.3f}" # 
print(format_str)

# Menampilkan tanda plus(+) atau minus(-)
angka_minus = -10
angka_plus = +10
format_minus = f"Angka minus = {angka_minus:+d}" # :+d artinya tampilkan minus / plus di depan angka
format_plus = f"Angka plus = {angka_plus:+d}"
print (format_minus) 
print (format_plus)

# memformat persen
persen = 0.045
format_persen = f"Persen = {persen:.2%}" # .2 artinya tampilkan 2 angka di belakang koma, % artinya tampilkan dalam presentase
print(format_persen)

# Operasi aritmatika
harga = 10000
jumlah = 5
format_str = f"Harga = Rp. {harga * jumlah:,}"
print(format_str)

# Format binary, octal, dan hexadecimal
angka = 255
format_binary = f"Binary = {bin(angka)}"
fornat_octal = f"Octal = {oct(angka)}"
format_hexadecimal = f"Hexadecimal = {hex(angka)}"
print(format_binary)
print(fornat_octal)
print(format_hexadecimal)
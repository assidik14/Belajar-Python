data_nama = "santoso"
data_umur = 25
data_tinggi = 150

data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi badan = {data_tinggi}"
print (data_string)

# String multiline menggunakan enter, newline, atau \n
print(5*"=" + " Multiline menggunakan tanda backslash n " + 5*"=")
data_string = f"nama = {data_nama}\numur = {data_umur}\ntinggi badan = {data_tinggi}"
print (data_string)

# String multiline menggunakan double kutip 3x atau single kutip 3x (Kutip Triplets)
print(5*"=" + " Multiline menggunakan kutip triplets " + 5*"=")
data_string = f'''
nama         = {data_nama}
umur         = {data_umur}
tinggi badan = {data_tinggi}
'''
print (data_string)

# Mengatur width rata kanan berdasarkan panjang karakter yang kita atur
print(5*"=" + " Mengatur width " + 5*"=")
data_string = f'''
nama         = {data_nama}
umur         = {data_umur:>7}
tinggi badan = {data_tinggi:>7}
'''
print (data_string)

# List adalah array di python, diakses menggunakan index => sociative array
# Dictionary, diakses menggunakan identifier yaitu KEY => associative array

# contoh_dictionary = {
#     'KEY1' : 'VALUE1',
#     'KEY2' : 'VALUE2'
# }

# print(contoh_dictionary)
# print(contoh_dictionary["KEY1"])
# print(contoh_dictionary.keys())
# print(contoh_dictionary.values())
# print(contoh_dictionary.items())

data_dict = {
    'tkj' : 'Teknik komputer jaringan',
    'pm' : 'Pemasaran',
    'ak' : 'Akutansi',
    'ap' : 'Administrasi perkantoran'
}

# Panjang dictionary
panjang_dict = len(data_dict)
print(f"Panjang dictionary = {panjang_dict}")

# Cek key dalam dict
key = 'pm'
cek_key = key in data_dict
print(f"Apakah {key} ada pada dictionary : {cek_key}")

key = 'ti'
cek_key = key in data_dict
print(f"Apakah {key} ada pada dictionary : {cek_key}")

# Mengakses value menggunakan get
print(data_dict.get("tkj"))
print(data_dict.get("ti")) # walaupun key-nya tidak ada tpi tidak error
print(data_dict.get("ti", "Key tidak ada!!")) # kita juga bisa menambahkan message

# Update data dict
print(data_dict.get("pm"))
data_dict["pm"] = "Bisnis dan pemasaran"
print(data_dict.get("pm"))
data_dict["ti"] = "Teknik informatika" # ini akan menambah data karena key sebelumnya tidak ada
print(data_dict)

# Update data dengan fungsi update
update_data = data_dict.update({"ti":"Informatika"})
print(data_dict)
update_data = data_dict.update({"si":"Sistem informasi"})
print(data_dict)

# Delete data dictionary
del data_dict["si"]
print(data_dict)


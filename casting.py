# Casting adalah merubah sebuah type data menjadi type data lain

print("==== INTEGER ====")
# type data integer
data_integer = 7
print ("isi datanya adalah = ", data_integer)
print ("Tipe datanya adalah = ", type(data_integer))

# Merubah yang tadinya type data-nya integer menjadi type data float
data_float = float(data_integer)
print ("isi datanya adalah = ", data_float)
print ("Tipe datanya adalah = ", type(data_float))

# Merubah yang tadinya type data-nya integer menjadi type data string
data_string = str(data_integer)
print ("isi datanya adalah = ", data_string)
print ("Tipe datanya adalah = ", type(data_string))

# Merubah yang tadinya type data-nya integer menjadi type data boolean
data_boolean = bool(data_integer)
print ("isi datanya adalah = ", data_boolean) # Data boolean bernilai True/False, jika value-nya selain 0 maka hasilnya True
print ("Tipe datanya adalah = ", type(data_boolean))


print("==== FLOAT ====")
# type data floar
value_float = 7.9
print ("isi datanya adalah = ", value_float)
print ("Tipe datanya adalah = ", type(value_float))

# Merubah data float menjadi integer
value_integer = int(value_float)
print ("isi datanya adalah = ", value_integer) # Data float jika di konversi (casting) menjadi integer maka nilainya akan di bulatkan ke BAWAH
print ("Tipe datanya adalah ", type(value_integer))


print("==== BOOLEAN ====")
value_boolean = True
print ("isi datanya adalah = ", value_boolean)
print ("Tipe datanya adalah = ", type(value_boolean))

menjadi_integer = int(value_boolean)
print ("isi datanya adalah = ", menjadi_integer) # Data boolean jika bernilai True, dicasting menjadi integer maka hasilnya 1. Data boolean jika bernilai False, dicasting menjadi integer maka hasilnya 0
print ("Tipe datanya adalah = ", type(menjadi_integer))

menjadi_string = str(value_boolean)
print ("isi datanya adalah = ", menjadi_string) # Data boolean jika dicasting menjadi string, maka akan bernilai karakter "True" atau "False"
print ("Tipe datanya adalah = ", type(menjadi_string))


print("==== STRING ====")
value_string = "" # Karakter
print ("isi datanya adalah = ", value_string)
print ("Tipe datanya adalah = ", type(value_string))

jadi_integer = int(value_string)
print ("isi datanya adalah = ", jadi_integer) # Untuk merubah string menjadi integer, string harus bernilai karaker angka
print ("Tipe datanya adalah = ", type(jadi_integer))

jadi_boolean = bool(value_string)
print ("isi datanya adalah = ", jadi_boolean) # Jika string memiliki nila, maka boolean akan bernilai True, jika string tidak memiliki nilai "" maka boolean akan bernilai False
print ("Tipe datanya adalah = ", type(jadi_boolean))
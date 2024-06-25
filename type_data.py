# di python tidak ada deklarasi data
# int a = 7 # tidak ada seperti ini

# Integer
data_integer = 7
print ("isi datanya adalah = ", data_integer)
print ("Tipe datanya adalah = ", type(data_integer))

# Float (angka berkoma)
data_float = 1.5
print ("isi datanya = ", data_float)
print ("Tipe datanya adalah = ", type(data_float))

# String (karakter)
data_string = "testing"
print ("isi datanya = ", data_string)
print ("Tipe datanya adalah = ", type(data_string))

# Boolean (Trus/False)
data_boolean = True
print ("isi datanya = ", data_boolean)
print ("Tipe datanya adalah = ", type(data_boolean))

# Bilangan complex (Menggunakan data imaginer)
data_complex = complex(5, 7) # 7 adalah data imaginer-nya
print ("isi datanya = ", data_complex)
print ("Tipe datanya adalah = ", type(data_complex))

# Python bisa menggunakan type data dari bahasa C
from ctypes import c_double
data_c_double = c_double(10.5)
print ("isi datanya = ", data_c_double)
print ("Tipe datanya adalah = ", type(data_c_double))
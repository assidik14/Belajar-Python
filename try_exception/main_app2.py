# Membuat exception sendiri

from numbers import Number
def tambah(a,b):
    if not isinstance(a, Number) or not isinstance(b, Number):
        raise "Input harus angka"
    return a+b

print(tambah(5,"v"))
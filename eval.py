# Menggunakan Eval, built-in python
# print(5*"-", "Menggunakan Eval", 5*"-")

# expression = input("Masukan operasi matimatika : ")

# hasil = str(eval(expression))
# print(f"{expression} = {hasil}")

# print(28*"-")


# Menggunakan literal_eval
from ast import literal_eval
print(5*"-", "Menggunakan Literal Eval", 5*"-")

angka1 = int(input("Masukkan angka pertama : "))
angka2 = int(input("Masukkan angka kedua : "))

hasil = angka1 + angka2

print(hasil)
print(literal_eval(f"{hasil}"))

print(37*"-")
angka = []

# user_input1 = int(input("Masukkan angka                     : "))
# user_input2 = input("Masukkan operator (+ | - | : | x)  : ")
# user_input3 = int(input("Masukkan angka                     : "))

angka.append(int(input("Masukkan angka                     : ")))
angka.append(input("Masukkan operator (+ | - | : | x)  : "))
angka.append(int(input("Masukkan angka                     : ")))

match angka[1]:
    case "+" : hasil = angka[0] + angka[2]
    case "-" : hasil = angka[0] - angka[2]
    case ":" : hasil = angka[0] / angka[2]
    case "x" : hasil = angka[0] * angka[2]

print(10*"-")
print(f"{angka[0]} {angka[1]} {angka[2]} = {hasil}")
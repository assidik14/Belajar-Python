import os

sisop = os.name

if __name__ == "__main__":

    while(True):

        match sisop:
            case "posix": os.system("clear")
            case "nt": os.system("cls")

        print(43*"=")
        print(10*"=" + " Kalkulator using list " + 10*"=")
        print(43*"=")

        angka = []

        angka.append(int(input("Masukkan angka                     : ")))
        angka.append(input("Masukkan operator (+ | - | / | *)  : "))
        while len(angka[1]) > 0 and angka[1] != "+" and angka[1] != "-" and angka[1] != "/" and angka[1] != "*":
            print("operator salah")
            del angka[1]
            angka.append(input("Masukkan operator (+ | - | / | *)  : "))
        angka.append(int(input("Masukkan angka                     : ")))

        match angka[1]:
            case "+" : hasil = angka[0] + angka[2]
            case "-" : hasil = angka[0] - angka[2]
            case "/" : hasil = angka[0] / angka[2]
            case "*" : hasil = angka[0] * angka[2]

        print(43*"-")
        print(f"{angka[0]} {angka[1]} {angka[2]} = {hasil}")
        print(43*"-")

        is_done = input("Apakah selesai (y/n) : ")
        if is_done == "y" or is_done == "Y":
            break

    print(43*"=")
    print("Program close")
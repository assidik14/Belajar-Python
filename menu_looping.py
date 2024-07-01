import os

if __name__== "__main__":

    while(True):

        sistem_operasi = os.name
        match sistem_operasi:
            case "posix": os.system("clear")
            case "nt": os.system("cls")

        print("Membuat menu menggunakan looping")
        print("--------------------------------")
        for i in range(5):
            i = i + 1
            match i:
                case 1: print(i, ". menu ", i)
                case 2: print(i, ". menu ", i)
                case 3: print(i, ". menu ", i)
                case 4: print(i, ". menu ", i)
                case 5: print(i, ". menu ", i)
        print("--------------------------------")
        
        i = int(input("pilih menu : "))
        print("--------------------------------")
        while i > 5:
            if i > 5:
                print("maaf menu yg kamu pilih tidak tersedia, silakan pilih lagi")
                print("--------------------------------")
                i = int(input("pilih menu : "))
                print("--------------------------------")

        match i:
            case 1: print("kamu pilih menu ", i)
            case 2: print("kamu pilih menu ", i)
            case 3: print("kamu pilih menu ", i)
            case 4: print("kamu pilih menu ", i)
            case 5: print("kamu pilih menu ", i)
    
        print("--------------------------------")

        selesai = input("Apakah selesai (y/n) : ")
        if selesai == "y" or selesai == "Y":
            break
    
    print("--------------------------------")
    print("Program seleai")

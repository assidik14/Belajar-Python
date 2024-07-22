# Program list buku

daftar_buku = []
while True:

    judul = input("Masukan judul \t\t: ")
    penulis = input("Masukan penulis \t: ")

    input_buku = [judul, penulis]

    daftar_buku.append(input_buku)

    print( "\n" + 30*"=" + " Daftar Buku " + 30*"=")
    print(73*"=")
    print("NO\t|\t Judul Buku \t|\t Penulis")
    print(73*"-")

    for index, buku in enumerate(daftar_buku):
        print(f"{index + 1}\t|\t {buku[0]} \t|\t {buku[1]}")
    
    print(73*"=" + "\n")

    selesai = input("Apakah selesai (y/n) \t: ")
    if selesai == "y" or selesai == "Y":
        break
print("Program Selesai !!")
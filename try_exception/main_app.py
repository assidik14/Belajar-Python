# Exception akan terjadi saat program mengalami error saat runtime

# Contoh untuk menangkap exception :
# input_user = int(input("Masukan angka : "))
# hasil = 0

# try:
#     hasil = 10 / input_user
#     print(f"Hasilnya adalah = {hasil}")

# except Exception as errormessage:
#      print(errormessage)
#      print("Input tidak boleh 0")


## Contoh implementasi di aplikasi
# while(True):
#     input_user = int(input("Masukan angka pembagi : "))
#     hasil = 0

#     try:
#         hasil = 10 / input_user
#         print(f"Hasilnya adalah = {hasil}")
#         is_done = input("Apakah selesai (y/n) ? ")
#         if is_done == "y" or is_done == "Y":
#             break
    
#     except ZeroDivisionError as errormessage:
#         print(errormessage)
#         print("Input adalah 0, silakan masukan input lagi")

# print ("Program selesai")


## Contoh lagi
try:
    with open("try_exception/data1.txt", mode="r", encoding="utf-8") as file:
        print(f"Isi file-nya adalah : \n {file.read()}")

except Exception as ErrorMessage:
    print("File tidak ditemukan, membuat file baru.....")
    with open("try_exception/data1.txt", mode="w", encoding="utf-8") as file:
        file.write("## Ini adalah file baru ##")

print("Program Selesai")
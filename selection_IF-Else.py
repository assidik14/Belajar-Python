## 1. if tanpa else
# nama = input("Masukkan nama kamu : ")
# umur = int(input("Berapa umur kamu : "))

# if umur < 17:                                     # Kondisi
#     print(f"Hai {nama}, kamu belum punya KTP")    # Aksi True

# print ("Program selesai")


## 2. if menggunakan else
# nama = input("Masukkan nama kamu : ")
# umur = int(input("Berapa umur kamu : "))

# if umur < 17:                                     # Kondisi 
#     print(f"Hai {nama}, kamu belum punya KTP")    # Aksi True
# else :                                            
#     print(f"Hai {nama}, kamu sudah punya KTP")    # Aksi False

# print ("Program selesai")


## 3. if menggunakan elif dan else
nama = input("Masukkan nama kamu : ")
umur = int(input("Berapa umur kamu : "))

if umur < 17:                                       # Kondisi 1
    print(f"Hai {nama}, kamu belum punya KTP")      # Aksi 1, jika True
elif umur >= 17 and umur <= 25:                     # Kondisi 2
    print(f"Hai {nama}, kamu sudah dewasa")         # Aksi 2, jika True
else :                                              
    print(f"Hai {nama}, kamu sudah tua, wkwkwk")    # Aksi jika semua kondisi False

print ("Program selesai")
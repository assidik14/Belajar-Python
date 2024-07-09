## 1. if tanpa else
# nama = input("Masukkan nama kamu : ")
# umur = int(input("Berapa umur kamu : "))

# if umur < 17:
#     print(f"Hai {nama}, kamu belum punya KTP")

# print ("Program selesai")


## 2. if menggunakan else
# nama = input("Masukkan nama kamu : ")
# umur = int(input("Berapa umur kamu : "))

# if umur < 17:
#     print(f"Hai {nama}, kamu belum punya KTP")
# else :
#     print(f"Hai {nama}, kamu sudah punya KTP")

# print ("Program selesai")


## 3. if menggunakan elif dan else
nama = input("Masukkan nama kamu : ")
umur = int(input("Berapa umur kamu : "))

if umur < 17:
    print(f"Hai {nama}, kamu belum punya KTP")
elif umur >= 17 and umur <= 25:
    print(f"Hai {nama}, kamu sudah dewasa")
else :
    print(f"Hai {nama}, kamu sudah tua, wkwkwk")

print ("Program selesai")
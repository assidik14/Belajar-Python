# angka = 0

# while angka < 5:
#     print ("Angka = ", angka)
#     angka += 1

#     if angka == 3:
#         print ("Belajar Break")
#         break

#     print ("Looping")

# print ("Selesai")

count = int(input("Mau berapa looping : "))
angka = 0
while True:
    angka += 1
    print (f"Count ke-{angka}")
    if angka == count:
        break
print("Selesai")
    
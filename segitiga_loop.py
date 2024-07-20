# 1. For loop

sisi = 10

# Segitiga siku-siku
# for i in range(sisi):
#     i += 1
#     print("+" * i)

# Segitiga sama sisi
# spasi = int(sisi/2)
# for i in range(sisi):
#     i += 1
#     if i %2 == 1:
#         print(" "*spasi, "+" * i)
#         spasi -= 1

# 2. While loop

# Segitiga siku-siku
count = 1

# while True:
#     print("+" * count)
#     count += 1
#     if count > sisi:
#         break

spasi = int(sisi/2)
# Segitiga sama sisi
while True:
    if count % 2 == 1:
        print(" "*spasi, "+" * count)
        spasi -= 1

    count += 1
    if count > sisi:
        break
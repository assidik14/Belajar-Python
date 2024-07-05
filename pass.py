# Pass berfungsi sebagai dummy, sehingga tidak akan di eksekusi

angka = 0
while angka < 5:
    angka += 1
    if angka == 3:
        print ("Belajar Pass")
    print ("Angka = ", angka)


nomor = 0
while nomor < 5:
    nomor += 1
    if nomor == 3:
        pass # Tidak akan di eksekusi
    print ("Anka = ", nomor)
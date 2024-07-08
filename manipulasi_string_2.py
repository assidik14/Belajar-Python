# Operator dalam bentuk method


data = "Jakarta adalah Ibukota Negara Indonesia"
jumlah_huruf_a = data.count("a")    # Mencari jumlah karakter a pada kalimat dalam variabel data, dimana data adalah object-nya dan count adalah method-nya. Hasilnya adalah integer
print("Jumlah karakter 'a' pada '" + data + "' adalah = " + str(jumlah_huruf_a))

## Merubah case string
# Merubah menjadi upper case
negara = "indonesia"
negara = negara.upper()
print ("Kami adalah rakyat " + negara)

# Merubah menjadi lower case
alay = "Hey BrOoOowWW"
alay = alay.lower()
print (alay)

## Pengecekkan is method
salam = "hellow brader"
is_lower = salam.islower() # hasilnya adalah boolean
print ("Apakah '" + salam + "' adalah lower case = " + str(is_lower))
is_upper = salam.isupper() # hasilnya adalah boolean
print ("Apakah '" + salam + "' adalah upper case = " + str(is_upper))

## Method-method lain
# isalpha() = Digunakan untuk mengecek apakah semuanya huruf
# isalnum() = Digunakan untuk mengecek apakah kombinasi huruf dan angka
# isdecimal() = Digunakan untuk mengecek apakah hanya angka
# isspace() = Digunakan untuk mengecek apakah ada spasi, tab, newline
# istitle() = Digunakan untuk mengecek apakah kata dimulai dengan huruf besar
# startswith() = Digunakan untuk mengecek awal kalimat
# endswith() = Digunakan untuk mengecek akhir kalimat

judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle() # Akan True, jika semua kalimat dimulai dengan huruf besar, jika ada salah satu kalimat tidak dimulai dengan huruf besar maka akan False
print (judul + " is title = " + str(cek_judul))

command_update = "Sudo apt update".startswith("sudo") # akan menghasilkan boolean dan sensitif case
print ("sudo = " + str(command_update)) # akan False karena command diawali huruf besar

command_upgrade = "sudo apt upgrade".endswith("upgrade")
print ("upgrade = " + str(command_upgrade))

install_python = "sudo apt install python2"
cek_sudo = install_python.startswith("sudo")
cek_python = install_python.endswith("python3")
print ("Apakah '" + install_python + "' diawali sudo = " + str(cek_sudo))
print ("Apakah '" + install_python + "' diakhiri 'python3' = " + str(cek_python))

pembatas = 10*"=" + " Pembatas " + 10*"="
print (pembatas)

## Penggabungan komponen join() split() pada list
# Gabung join()
data_list = ["I", "Love", "You"]
print (data_list)
gabung_pake_koma = ",".join(data_list)
print (gabung_pake_koma)
gabung_pake_spasi = " ".join(data_list)
print (gabung_pake_spasi)

# Pisah split() = akan otomatis menjadi list lagi
pisah_koma = gabung_pake_koma.split(",")
print (pisah_koma)
pisah_spasi = gabung_pake_spasi.split()
print (pisah_spasi)

## Alokasi karakter rjust(), ljust(), center()
rata_kanan = "kanan".rjust(10) # Nilai 10 adalah total karakter, bebas mau berapa aja
print("'" + rata_kanan + "'")

rata_kiri = "kiri".ljust(5) # Nilai 5 adalah total karakter, bebas mau berapa aja
print("'" + rata_kiri + "'")

tengah = "tengah".center(10) # Nilai 10 adalah total karakter, bebas mau berapa aja
print("'" + tengah + "'")

tengah_bukan_spasi = "tengah".center(20, "=")
print(tengah_bukan_spasi)

rata_kanan_bukan_spasi = "kanan".rjust(20, ":")
print(rata_kanan_bukan_spasi)

rata_kiri_bukan_spasi = "kiri".ljust(20, "#")
print(rata_kiri_bukan_spasi)


# stip()
tengah_bukan_spasi = tengah_bukan_spasi.strip("=")
print(tengah_bukan_spasi)

rata_kanan_bukan_spasi = rata_kanan_bukan_spasi.strip(":")
print(rata_kanan_bukan_spasi)

rata_kiri_bukan_spasi = rata_kiri_bukan_spasi.strip("#")
print(rata_kiri_bukan_spasi)
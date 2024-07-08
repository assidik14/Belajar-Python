import datetime as dt

print (10 * "=" + " Masukkan umur, bulan, dan tahun lahir Anda " + 10 * "=")

tanggal = int(input("Tanggal lahir \t = "))
bulan = int(input("Bulan lahir \t = "))
tahun = int(input("Tahun lahir \t = "))

print (10 * "=" + " Today " + 10 * "=")

today = dt.date.today()
print (f"Hari ini tanggal \t = {today}")
print (f"Hari ini adalah \t = {today:%A}")

print (10 * "=" + " Tanggal Lahir Anda " + 10 * "=")

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print (f"Tanggal lahir Anda \t = {tanggal_lahir}")
print (f"Hari lahir Anda \t = {tanggal_lahir:%A}")

print (10 * "=" + " Umur Anda " + 10 * "=")
umur_hari = today - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30
print (f"Umur Anda hari ini \t = {umur_tahun} tahun, {umur_bulan_sisa} bulan")

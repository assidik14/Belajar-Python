'''Import Module'''
import os
import datetime as dt

# Function
def clear_console():
    '''Fungsi untuk clear terminal atau console'''
    sistem_operasi = os.name
    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

def header():
    '''Fungsi menampilkan judul aplikasi'''
    judul = "APLIKASI MENGHITUNG BODY MASS INDEX"
    print(f"{'SELAMAT DATANG':^50}")
    print(f"{judul:^50}")
    print(50*"=")

def user_input():
    '''Fungsi mengambil data user'''
    nama = input("Masukan nama kamu \t\t : ")
    tanggal = int(input("Masukan tanggal lahir (1-31) \t : "))
    bulan = int(input("Masukan bulan lahir (1-12) \t : "))
    tahun = int(input("Masukan tahun lahir (yyyy) \t : "))
    bb = int(input("Masukan berat badan \t\t : "))
    tb = int(input("Masukan tinggi badan \t\t : "))
    lahir = dt.date(tahun, bulan, tanggal)
    print(50*"-")
    print("1. Laki-laki")
    print("2. Perempuan")
    print(50*"-")
    gender = int(input("Masukan gender (1/2) \t\t : "))
    while gender != 1 and gender !=2:
        print("Gender Salah!!, silakan ulang")
        gender = int(input("Masukan gender (1/2) \t\t : "))
    print(50*"-")
    return nama, lahir, gender, bb, tb

def hitung_umur(tgl_lahir_user):
    '''Fungsi untuk menghitung umur user'''
    today = dt.date.today()
    umur_hari = today - tgl_lahir_user
    umur_tahun = umur_hari.days // 365
    umur_bulan_sisa = (umur_hari.days % 365) // 30
    print (f"Umur kamu sekarang \t: {umur_tahun} tahun, {umur_bulan_sisa} bulan")

def hitung_bmi(berat_badan, tinggi_badan):
    '''Fungsi menghitung BMI'''
    bmi = (berat_badan / (tinggi_badan ** 2)) * 10000
    return bmi

def bmi_score(nama, score):
    '''Fungsi score bmi'''
    if score < 18.5:
        print(f"""
Wah, kamu Underweight {nama}!!
Kamu terlalu kurus, kamu harus perbanyak makan
makanan bergizi dan berprotein tinggi
""")
    elif score >= 18.5 and score <= 24.9:
        print(f"""
Selamat, kamu Normal {nama}!!
Pertahankan pola hidupmu saat ini dan lengkapi
dengan asupan yang baik dan tetap berolahraga
""")
    elif score >= 25.0 and score <= 29.9:
        print(f"""
Wah kamu Overheight {nama}!!
Jaga pola makan dan perbanyak aktivitas olahragamu
agar pembakaran lemak menjadi lebih optimal
""")
    elif score >= 30.0:
        print(f"""
Gawat, kamu Obesity {nama}!!
Kamu terlalu gemuk, masuk dalam kategori obesitas.
Kurangi asupan dan perbanyak olahraga serta aktivitas
di luar ruangan
""")

# Main App
if __name__ == "__main__":
    while True:
        clear_console()
        header()
        nama_user, lahir_user, gender_user, bb_user, tb_user  = user_input()

        if gender_user == 1:
            print(f"Hai broo {nama_user}, terimakasih sudah mengisi data \n")
        else:
            print(f"Hai sist {nama_user}, terimakasih sudah mengisi data \n")

        print(f"Hari ini adalah \t: {dt.date.today():%A}, {dt.date.today()}")
        print(f"Kamu lahir pada \t: {lahir_user:%A}, {lahir_user}")
        hitung_umur(lahir_user)
        bmi_user = hitung_bmi(bb_user, tb_user)
        print(f"Score BMI kamu \t\t: {bmi_user:.1f}")
        print(50*"-")
        bmi_score(nama_user ,bmi_user)

        print(50*"-")
        is_done = input("Apakah selesai (y/n) \t: ")
        if is_done == "y" or is_done == "Y":
            break

    print(50*"-")
    print(f"{'Program Selesai':^50}")
    print(50*"-")
# Akhir program
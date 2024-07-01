import os

if __name__ == "__main__":

    while(True): # Jika kondisi benar

        sistem_operasi = os.name # Deklarasi sistem operasi
        match sistem_operasi:
            case "posix": os.system("clear") # Jika Linux jalankan "clear"
            case "nt": os.system("cls") # Jika Windows jalankan "cls"

        print("======= Aplikasi kalkulator sederhana =======")
        print("---------------------------------------------")
        for operasi in range(4): # Looping variabel operasi sebanyak 4x, dimulai dari 0
            operasi = operasi + 1 # Increment variabel operasi
            match operasi:
                case 1: print(operasi, ". Tambah") # Looping pertama
                case 2: print(operasi, ". Kurang") # Looping kedua
                case 3: print(operasi, ". Kali") # Looping ketiga
                case 4: print(operasi, ". Bagi") # Looping keempat
    
        print("---------------------------------------------")
        operasi = int(input("Pilih operasi : ")) # Input nilai variabel operasi, sebagai integer

        while operasi > 4 or operasi <= 0: # Looping nilai variabel operasi ketika nilainya > 4 atau <= 0
            if operasi > 4 or operasi <= 0 : # Jika nilai variabel operasi > 4 atau <= 0
                print("---------------------------------------------")
                print("Operasi yang kamu pilih tidak tersedia, silakan pilih lagi!") # Maka kasih tau user, nilainya salah
                print("---------------------------------------------")
                operasi = int(input("Pilih operasi : ")) # Dan harus di input ulang, sesuai menu. Jika benar maka program akan dilanjutkan

        print("---------------------------------------------")
        angka_pertama = int(input("Masukkan angka pertama : ")) # Input angka pertama
        angka_kedua = int(input("Masukkan angka kedua : ")) # Input angka kedua

        print("=============================================")

        match operasi: # Sesuaikan operasi dengan yang di pilih user
            case 1: # Jika yg di pilih 1
                hasil = angka_pertama + angka_kedua # Maka lakukakn operasi penjumlahan
                print("Hasil dari ", angka_pertama, " + ", angka_kedua, " = ", hasil) # Tampilkan hasilnya
            case 2: # Jika yang dipilih 2
                hasil = angka_pertama - angka_kedua # Maka lakukan operasi pengurangan
                print("Hasil dari ", angka_pertama, " - ", angka_kedua, " = ", hasil) # Tampilkan hasilnya
            case 3: # Jika yang dipilih 3
                hasil = angka_pertama * angka_kedua # Maka lakukan operasi perkalian
                print("Hasil dari ", angka_pertama, " x ", angka_kedua, " = ", hasil) # Tampilkan hasilnya
            case 4: # Jika yang dipilih 4
                hasil = angka_pertama / angka_kedua # Maka lakukan operasi pembagian
                print("Hasil dari ", angka_pertama, " : ", angka_kedua, " = ", hasil) # Tampilkan hasilnya

        print("=============================================")

        selesai = input("Apakah selesai (y/n) : ") # Minta input program selesai atau tidak
        if selesai == "y" or selesai == "Y": # Jika selesai
            break # Maka break, dan program selesai. Jika tidak maka akan looping kembali
    
    print("============== Program Selesai ==============")

import os

if __name__== "__main__":
        sistem_operasi = os.name

        while(True):
        
            match sistem_operasi:
                case "posix": os.system("clear")
                case "nt": os.system("cls")

            print ("========== MENU ==========")
            print ("==========================")
            print (f"1. Cek Partisi Hardisk")
            print (f"2. Cek Memmory")
            print (f"3. Cek Tanggal")
            print (f"4. Cek Hostname")
            print (f"5. Cek IP")
            print (f"6. Cek Hardisk")
            print ("==========================")

            user_options = input ("Masukkan option : ")

            print ("==========================\n")
            
            match sistem_operasi:
                case "posix":
                        match user_options:
                            case "1": os.system("df -h")
                            case "2": os.system("free -m")
                            case "3": os.system("timedatectl")
                            case "4": os.system("hostnamectl")
                            case "5": os.system("ifconfig")
                            case "6": os.system("lsblk")
                case "nt":
                        match user_options:
                            case "1": os.system("systeminfo")
                            case "2": os.system("systeminfo")
                            case "3": os.system("systeminfo")
                            case "4": os.system("systeminfo")
                            case "5": os.system("systeminfo")
                            case "6": os.system("systeminfo")
            
            print ("\n==========================\n")
            
            is_done = input("Apakah selesai (y/n) : ")
            if is_done == "y" or is_done == "Y":
                 break
            
        print("Program selesai")

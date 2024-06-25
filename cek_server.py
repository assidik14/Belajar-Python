import os
import getpass

target = input("Masukkan IP server target : ")
username = input("Masukkan username server : ")
password = getpass.getpass("Masukkan password server : ")

while(True):
            
            os.system("clear")

            print ("========== info =========\n")
            print (f"Server     : ", target)
            print (f"Credential : ", username)
            print ("\n======== Command ========")
            print ("=========================")
            print (f"1. Cek Partisi Hardisk")
            print (f"2. Cek Memmory")
            print (f"3. Cek Tanggal")
            print (f"4. Cek Hostname")
            print (f"5. Cek IP")
            print (f"6. Cek Hardisk")
            print (f"7. Cek NFS Export List")
            print (f"8. Cek Service Docker")
            print (f"9. Cek Container")
            print (f"10. Cek Login Aktif")
            print ("=========================")

            user_options = input ("Masukkan option : ")

            print ("=========================\n")
            
            
            match user_options:
                case "1": os.system("sshpass -p "+password+" ssh -o StrictHostKeyChecking=no "+username+"@"+target+" df -h")
                case "2": os.system("sshpass -p "+password+" ssh -o StrictHostKeyChecking=no "+username+"@"+target+" free -m")
                case "3": os.system("sshpass -p "+password+" ssh -o StrictHostKeyChecking=no "+username+"@"+target+" timedatectl")
                case "4": os.system("sshpass -p "+password+" ssh -o StrictHostKeyChecking=no "+username+"@"+target+" hostnamectl")
                case "5": os.system("sshpass -p "+password+" ssh -o StrictHostKeyChecking=no "+username+"@"+target+" ifconfig")
                case "6": os.system("sshpass -p "+password+" ssh -o StrictHostKeyChecking=no "+username+"@"+target+" lsblk")
                case "7": os.system("sshpass -p "+password+" ssh -o StrictHostKeyChecking=no "+username+"@"+target+" showmount -e "+target)
                case "8": os.system("sshpass -p "+password+" ssh -o StrictHostKeyChecking=no "+username+"@"+target+" service docker status")
                case "9": os.system("sshpass -p "+password+" ssh -o StrictHostKeyChecking=no "+username+"@"+target+" docker ps -a")
                case "10": os.system("sshpass -p "+password+" ssh -o StrictHostKeyChecking=no "+username+"@"+target+" w")
            
            print ("\n=========================\n")
            
            is_done = input("Apakah selesai (y/n) : ")
            if is_done == "y" or is_done == "Y":
                 break
            
print("Program selesai")
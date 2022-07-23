import os

mac = input("Masukkan MAC Address : ")
macvendors = os.system(f"curl https://api.macvendors.com/{mac}")
print(macvendors)

## Teknik menduplikat list

list_a = ["Otong", "Asep", "Dudung", "Odah", "Jajang"]
print(list_a)

list_b = list_a # Duplikasi list a ke list b
print(list_b)

list_a[1]="Cecep" # Merubah data list a

print(list_a)
print(list_b) # Maka list b juga akan ikut berubah

list_b.sort() # Bahkan jika kita rubah list b, list a juga akan ikut berubah
print(list_a)
print(list_b)

# Mengapa bisa begitu ???
# Coba kita cek address nya

print(f"Address list a = {hex(id(list_a))}") # Cek address id list a
print(f"Address list b = {hex(id(list_b))}") # Cek address id list b

# Ternyata Address ID nya IDENTIK
# Artinya list b tidak membuat list baru, karena list b memiliki address yang sama dengan list a

# Cara meng-copy-nya adalah dengan fungi copy()

list_c = list_a.copy()

# Sehingga datanya identik
print(list_a)
print(list_b)
print(list_c)

# Tapi address nya berbeda
print(f"Address list a = {hex(id(list_a))}") # Cek address id list a
print(f"Address list b = {hex(id(list_b))}") # Cek address id list b
print(f"Address list c = {hex(id(list_c))}") # Cek address id list c

# Artinya list akan membuat list baru tapi dengan data yang sama


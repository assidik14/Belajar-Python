# Fungsi atau Method

# def nama_fungsi(argument / parameter):
    # badan fungsi

# Ini akan error karena fungsi di panggil sebelum di definisikan.
# halo_dunia()
# hello_world("Ucup")

# Fungsi tanpa parameter
def halo_dunia():
    print("Hallo Dunia!!")

# Fungsi dengan parameter
def hello_world(nama):
    print(f"Hello World {nama}")

halo_dunia()
hello_world("Ucup")

# Catatan :
# Karena python adalah interpreter language, maka untuk memanggil fungsi, fungsi harus di definisikan terlebih dulu
# Argument atau parameter bisa berupa variable apa saja, termasuk collection variable seperti list, tuples, sets, dan dictionary
# Parameter fungsi boleh lebih dari 1

# Contoh

# Definisikan fungsi say_hi
def say_hi(friends):
    for friend in friends:
        print(f"Hi {friend} !!")

# Deklarasi variable menggunakan list
teman_teman = ['Ucup', 'Otong', 'Odah', 'Asep']

# Panggil fungsi dengan parameter list
say_hi(teman_teman)
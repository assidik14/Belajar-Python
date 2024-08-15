# Fungsi biasa
def f_kuadrat(angka:int)->int:
    '''Fungsi kuadrat dengan fungsi biasa'''
    hasil = angka**2
    return hasil

hasil_fungsi_biasa = f_kuadrat(3)
print(f"Hasil kuadrat fungsi biasa = {hasil_fungsi_biasa}")

# Fungsi lambda
kuadrat = lambda angka : angka**2
hasil_fungsi_lambda = kuadrat(3)
print(f"Hasil kuadra fungsi lambda = {hasil_fungsi_lambda}")

# Fungsi lambda dengan multiple argumen
kuadrat = lambda angka, pangkat : angka**pangkat
hasil_2pangkat3 = kuadrat(2,3)
print(f"Hasil fungsi kuadrat dengan lambda multiple argumen = {hasil_2pangkat3}")

# Sorting dengan fungsi (LEBIH RIBED)
data_list = ["Otong", "Ucup", "Dudung"]
data_list.sort()
print(f"Sorted list biasa by urutan alphabet huruf depan = {data_list}")


def panjang_nama(nama):
    '''Fungsi untuk menghitung panjang nama'''
    return len(nama)

data_list.sort(key=panjang_nama)
print(f"Sorted list biasa by panjang nama = {data_list}")

# Sorting dengan lambda (LEBIH SIMPEL)
data_list = ["Otong", "Ucup", "Dudung"]
data_list.sort(key=lambda nama : len(nama))
print(f"Sorted list dengan lambda by panjang nama = {data_list}")

# Filter list
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]

# Filter list dengam fungsi biasa (LEBIH RIBED)
def kurang_dari5 (angka):
    '''Fungsi untuk memfilter list kurang dari 5'''
    return angka < 5

data_angka_kurangdari5 = list(filter(kurang_dari5, data_angka))
print(f"Filter list kurang dari 5 dengan fungsi biasa = {data_angka_kurangdari5}")

# Filter list dengan lambda (LEBIH SIMPEL)
data_angka_kurangdari5 = list(filter(lambda x : x < 5, data_angka))
print(f"Filter list kurang dari 5 dengan lambda = {data_angka_kurangdari5}")

# Filter list angka genap
angka_genap = list(filter(lambda x : x % 2 == 0, data_angka))
print(f"Angka genap = {angka_genap}")

# Filter list angka ganjil
angka_ganjil = list(filter(lambda x : x % 2 != 0, data_angka))
print(f"Angka ganjil = {angka_ganjil}")

# Filter list angka kelipatan 3
angka_kelipatan3 = list(filter(lambda x : x % 3 == 0, data_angka))
print(f"Angka keipatan 3 = {angka_kelipatan3}")

# Anonymous Function
# Currying -> Haskell Curry

# Fungsi biasa
def pangkat_biasa(angka, pangkat):
    '''Fungsi pangkat biasa'''
    hasil = angka ** pangkat
    return hasil

print(f"Fungsi pangka biasa = {pangkat_biasa(5, 2)}")

# Dengan currying bisa membuat fungsi menjadi dynamic tidak fix, dan kita bisa meng-assign variabel menjadi fungsi...
# Fungsi dengan currying :
def pangkat_currying(pangkat):
    '''Fungsi pangkat dengan currying'''
    return lambda angka : angka ** pangkat

pangkat2 = pangkat_currying(2)
print(f"5 pangkat 2 adalah {pangkat2(5)}")
print(f"3 pangkat 2 adalah {pangkat2(3)}")

pangkat3 = pangkat_currying(3)
print(f"5 pangkat 3 adalah {pangkat3(5)}")

print(f"Pangkat bebas {pangkat_currying(4)(5)}") # Ini dibaca 5 pangkat 4
'''Ini adalah module matematika'''



def tambah(*args):
    '''Fungsi penjumlahan'''
    hasil = 0
    for angka in args:
        hasil += angka

    return hasil



def kali(*args):
    '''Fungsi perkalian'''
    hasil = 1
    for angka in args:
        hasil *= angka
        
    return hasil



def pangkat(power):
    '''Fungsi pangkat'''
    return lambda angka : angka ** power
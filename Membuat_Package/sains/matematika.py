'''Module matematika'''

def tambah(*args:int)->int:
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
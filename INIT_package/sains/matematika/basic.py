'''Module matematika basic'''

def tambah (*args):
    '''Fungsi penjumlahan'''
    hasil = 0
    for data in args:
        hasil += data
    
    return hasil


def kali (*args):
    '''Fungsi perkalian'''
    hasil = 1
    for data in args:
        hasil *= data

    return hasil
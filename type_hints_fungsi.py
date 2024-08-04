'''Type Hints pada fungsi'''

def fungsi_tanpa_typehints(argument):
    '''Fungi kuadrat tanpa typehints'''
    hasil = argument ** 2
    return hasil

def fungsi_dengan_typehints(argument:int) -> int:
    '''Fungsi kuadrat dengan typehints'''
    hasil = argument ** 2
    return hasil

print(fungsi_tanpa_typehints(2))
print(fungsi_dengan_typehints(2))

'''
Catatan :
1. Typehint akan terlihat ketika fungsi diarahkan menggunakan mouse (di hover), sebagai informasi dari fungsi tersebut
2. Tujuannya untuk dokumentasi penggunaan fungsi
3. Penggunaan typehints tidak akan mempengaruhi hasil, tapi akan sangat berguna untuk dokumentasi dan kerapihan aplikasi yang kita buat
4. Informasi yang ditampilkan berupa type data apa yang harus digunakan oleh argument, dan akan mengembalikan data dengan type data apa
'''
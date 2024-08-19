# __main__ adalah untuk top level code environment

# __name__ = "__main__"

## __name__ pada file program utama (main app)
print(f"Nilai __name__ pada main_app.py = {__name__}")

## __name__ pada file fungsi.py
import fungsi

### Contoh penggunaan __main__ pada file program utama
if __name__ == "__main__":

    def fungsi_tambah(a:int,b:int)->int:
        return a+b
    
    hasil = fungsi_tambah(5,2)
    print(f"Hasil = {hasil}")

import package
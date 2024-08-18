'''Tkinter adalah standard library untuk membuat GUI di python'''

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Init
window = tk.Tk() # Window App (object window)
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False, False)
window.title("Sapa!!")

# Variable dan fungsi
NAMA_DEPAN = tk.StringVar() # Variable untuk menyimpan input nama dari user
NAMA_BELAKANG = tk.StringVar() # Variable untuk menyimpan input nama dari user

def click_tombol():
    '''Fungsi yang di panggil saat tombol di click'''
    pesan = f"Hallo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, keren!!!"
    showinfo(message=pesan, title="Sapa!!!")

# Frame input
input_frame = ttk.Frame(window)
# Penempatan (Grid, Pack, Place)
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

# Komponen-komponen :
# 1. Label untuk nama depan
label_nama_depan = ttk.Label(input_frame, text="Nama Depan : ")
label_nama_depan.pack(padx=10, fill="x", expand=True)

# 2. Entry nama depan
entry_nama_depan = ttk.Entry(input_frame, textvariable=NAMA_DEPAN)
entry_nama_depan.pack(padx=10, fill="x", expand=True)

# 3. Label untuk nama belakang
label_nama_belakang = ttk.Label(input_frame, text="Nama Belakang : ")
label_nama_belakang.pack(padx=10, fill="x", expand=True)

# 4. Entry nama belakang
entry_nama_belakang = ttk.Entry(input_frame, textvariable=NAMA_BELAKANG)
entry_nama_belakang.pack(padx=10, fill="x", expand=True)

# 5. Tombol
tombol_sapa = ttk.Button(input_frame, text="Sapa !!!", command=click_tombol)
tombol_sapa.pack(padx=10, pady=10, fill="x", expand=True)

# Mainloop Window
window.mainloop()
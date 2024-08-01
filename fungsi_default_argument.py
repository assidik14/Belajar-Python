# Fungsi tanpa argumen
def hello_world():
    print("Hello World !!")

# Fungsi dengan argumen
def hello(nama):
    print(f"Hello, {nama}")

# Fungsi dengan default argumen
def sapa(nama="Guest"):
    print(f"Hai, {nama}")

# Memanggil fungsi tanpa argumen
hello_world()

# Memanggil fungsi dengan argumen tanpa argumen
# hello() -> akan error jika tidak ada argumen

# Memamnggil fungsi dengan default argumen tanpa argumen
sapa() # Walaupun tidak ada argumen, tidak error karena menggunakan default argumen

# Memanggil fungsi dengan default argumen dengan argumen
sapa("ucup")

# Note :
# Fungsi dengan defult argumen, bisa memiliki lebih dari 1 argumen
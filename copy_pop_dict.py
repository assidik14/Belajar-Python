kumpulan_jurusan = {
    'tkj' : 'Teknik komputer jaringan',
    'pm' : 'Pemasaran',
    'ak' : 'Akutansi',
    'ap' : 'Administrasi perkantoran'
}

# Copy dictionary
department = kumpulan_jurusan.copy()
print (f"Kumpulan jurusan = {kumpulan_jurusan.items()}")
print (f"Department = {department.items()}")

# Pop dictionary berdasarkan key
data_tkj = department.pop("tkj")
print (f"Data TKJ = {data_tkj}")
print (f"data department sekarang = {department}")

# Pop dictionary terakhir, berdasarkan item
data_terakhir = department.popitem()
print (f"Data terakhir = {data_terakhir}")
print (f"data department sekarang = {department}")
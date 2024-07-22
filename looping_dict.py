kumpulan_jurusan = {
    'tkj' : 'Teknik komputer jaringan',
    'pm' : 'Pemasaran',
    'ak' : 'Akutansi',
    'ap' : 'Administrasi perkantoran'
}

# for jurusan in kumpulan_jurusan:    # yang tampil hanya key nya
#     print(jurusan)

# for jurusan in kumpulan_jurusan.keys(): # Mengambil value berdasarkan looping key-nya
#     print(kumpulan_jurusan.get(jurusan))

# for jurusan in kumpulan_jurusan.values(): # Mengambil valude berdasarkan looping value-nya
#     print(jurusan)

for key, value in kumpulan_jurusan.items(): # Mengambil key dan value nya
    print(f"Key = {key}, Value = {value}")
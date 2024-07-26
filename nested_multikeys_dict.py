import datetime as dt

mahasiswa1 = {
    'nama':'Ucup Kuncup',
    'nim':'14512013007',
    'sks':120,
    'beasiswa':True,
    'lahir': dt.datetime(2001,5,17)
}

mahasiswa2 = {
    'nama':'Otong Sotong',
    'nim':'14512013010',
    'sks':100,
    'beasiswa':False,
    'lahir': dt.datetime(2003,9,10)
}

mahasiswa3 = {
    'nama':'Asep Kasep',
    'nim':'14512013020',
    'sks':99,
    'beasiswa':True,
    'lahir': dt.datetime(2000,8,20)
}

mahasiswa = {
    'MAH001':mahasiswa1,
    'MAH002':mahasiswa2,
    'MAH003':mahasiswa3
}

print(f"{'KEY':<6} {'NAMA':<20} {'NIM':<15} {'BEASISWA':^15} {'LAHIR':<15}")
print(70*"-")

for key in mahasiswa.keys():
    KEY = key
    NAMA = mahasiswa[key]['nama']
    NIM = mahasiswa[key]['nim']
    BEASISWA = mahasiswa[key]['beasiswa']
    LAHIR = mahasiswa[key]['lahir'].strftime("%x")

    print(f"{KEY:<6} {NAMA:<20} {NIM:<15} {BEASISWA:^15} {LAHIR:<15}")
    
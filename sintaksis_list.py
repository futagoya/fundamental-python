"""
Memakai List
"""

daftar_buku = ['Naruto', 'One Piece', 'Batman', 'Superman']

print('Melihat variabel')
print(daftar_buku)

print('\nMenggunakan for in')
for buku in daftar_buku:
    print(buku)

print('\nMenampilkan sesuai indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[3])

print('\nMenampilkan menggunakan for in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMenambah 1 buku')
daftar_buku.append('Sains Kelas 6')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\n Clear list')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nGanti elemen buku')
daftar_buku = ['Naruto', 'One Piece', 'Batman', 'Superman']
daftar_buku[0] = 'Naruto 2'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nHilangkan buku kedua')
buku = daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMunculkan buku yang hilang')
print(buku)

print('\nPop')
daftar_buku.pop()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
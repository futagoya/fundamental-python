print('\nperintah Del')
daftar_buku = ['Naruto', 'One Piece', 'Batman', 'Superman']
del daftar_buku[1]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nperintah Del list comprehension')
daftar_buku = ['Naruto', 'One Piece', 'Batman', 'Superman']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nperintah Del list comprehension')
daftar_buku = ['Naruto', 'One Piece', 'Batman', 'Superman']
del daftar_buku[0::2]  # Start:Stop:Step
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru')
daftar_buku = ['Naruto', 'One Piece', 'Batman', 'Superman']
daftar_buku_baru = daftar_buku [:]
del daftar_buku[:]  # Start:Stop:Step
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])





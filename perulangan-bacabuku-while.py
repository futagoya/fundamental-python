"""
Perulangan
"""

jumlah_buku = 10
print('Ibu berkata, "Baca semua bukumu"')

jumlah_buku_dibaca = 0
print(f"Jumlah buku yang sudah dibaca adalah {jumlah_buku_dibaca}")

while jumlah_buku_dibaca < jumlah_buku:
    jumlah_buku_dibaca = jumlah_buku_dibaca + 1
    print(f"Buku ke {jumlah_buku_dibaca} sudah dibaca")

print(f"Buku yang sudah dibaca adalah {jumlah_buku_dibaca} buku")
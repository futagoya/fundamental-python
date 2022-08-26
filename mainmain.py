# Percabangan
jumlah_botol_susu = 99
jumlah_telur = 88

print(f"Jumlah susu {jumlah_botol_susu} botol")
print(f"Jumlah telur {jumlah_telur} butir")

if jumlah_botol_susu > 0:
    print("Budi mengecek harganya, ternyata uangnya cukup")
    if jumlah_telur == 0:
        print("Budi membeli 1 botol susu")
    else:
        print("Budi membeli 6 botol susu")
else:
    print("Budi tidak jadi membeli susu")

print("Budi pulang ke rumah")
print("Budi memberikan hasil belanjaannya")
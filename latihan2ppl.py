# Rachel Setyawan Hanapi

nama = "Rachel Setyawan"
no_absen = 22
n_akhir = int(input("Nilai Akhir: "))

# Hasil Output

print ("NAMA:", nama)
print ("NOMOR ABSEN:", no_absen)
print ("NILAI AKHIR:", n_akhir)
print ("KETERANGAN:")

if n_akhir >= 77:
    print ("Kamu Lulus")
elif n_akhir < 77:
    print ("Kamu tidak Lulus")
else:
    print("Masukan dengan benar")

nilai_awal = int(input("Masukkan nilai awal: "))
nilai_akhir = int(input("Masukkan nilai akhir: "))

for a in range (nilai_awal, nilai_akhir):
    if nilai_awal % 3 != 0 or nilai_akhir % 7 != 0:
        print (a, end=" ")
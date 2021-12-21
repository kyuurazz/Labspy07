from view.lihat_data import *

while True:
    c = input("\nA)dd, E)dit, S)earch, D)elete L)ist, Q)uit: ")

    if c.lower() == 'a' or c.lower() == 'A':
        tambah_data()

    elif c.lower() == 'e' or c.lower() == 'E':
        ubah_data()

    elif c.lower() == 's' or c.lower() == 'S':
        cetak_hasil_pencarian()

    elif c.lower() == 'd' or c.lower() == 'D':
        hapus_data()

    elif c.lower() == 'l' or c.lower() == 'L':
        cetak_daftar_nilai()

    elif c.lower() == 'q' or c.lower() == 'Q':
        break

    else:
        print("Silahkan pilih menu yang tersedia")
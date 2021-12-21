class data_mahasiswa:
    nama = ""
    nim = ""
    tugas = ""
    uts = ""
    uas = ""


mahasiswa = {}
def tambah_data():
    global mahasiswa
    mhsw = data_mahasiswa()
    nama = input("Nama        : ")
    mhsw.nim = input("NIM         : ")
    mhsw.uts = int(input("Nilai UTS   : "))
    mhsw.uas = int(input("Nilai UAS   : "))
    mhsw.tugas = int(input("Nilai Tugas : "))
    mhsw.akhir = mhsw.tugas * 30/100 + mhsw.uts * 35/100 + mhsw.uas * 35/100
    mahasiswa[nama] = mhsw.nim, mhsw.tugas, mhsw.uts, mhsw.uas, mhsw.akhir
    return mahasiswa


def ubah_data():
    nama = input("Masukkan Nama: ")
    if nama in mahasiswa.keys():
        nim = input("NIM         : ")
        uts = int(input("Nilai UTS   : "))
        uas = int(input("Nilai UAS   : "))
        tugas = int(input("Nilai Tugas : "))
        akhir = tugas * 30/100 + uts * 35/100 + uas * 35/100
        mahasiswa[nama] = nim, tugas, uts, uas, akhir
    else:
        print("Nama {0} tidak ditemukan".format(nama))


def hapus_data():
    nama = input("Masukkan Nama:  ")
    if nama in mahasiswa.keys():
        del mahasiswa[nama]
    else:
        print("Nama {0} Tidak Ditemukan".format(nama))


def cari_data():
    nama = input("Masukkan Nama        : ")
    if nama in mahasiswa.keys():
        print("=" * 73)
        print("|                             Daftar Mahasiswa                          |")
        print("=" * 73)
        print("| Nama            |       NIM       |  UTS  |  UAS  |  Tugas  |  Akhir  |")
        print("=" * 73)
        print("| {0:15s} | {1:15s} | {2:5d} | {3:5d} | {4:7d} | {5:7.2f} |"
            .format(nama, mahasiswa[nama][0], mahasiswa[nama][1], mahasiswa[nama][2], mahasiswa[nama][3], mahasiswa[nama][4]))
        print("=" * 73)
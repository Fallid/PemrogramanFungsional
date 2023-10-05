# Sistem penilaian mahasiswa

# Tambahkan fungsi untuk menghitung nilai akhir
def hitung_nilai_akhir(var1, var2):
    return (var1 + var2)/2
# Tambahkan fungsi untuk menghitung semua nilai akhir


def hitung_semua_nilai_akhir(dataNilaiMahasiswa):
    totalNilai = {}
    for nama, nilai in dataNilaiMahasiswa.items():
        nilaiAkhir = g = hitung_nilai_akhir(nilai['uts'], nilai['uas'])
        totalNilai[nama] = nilaiAkhir
    return totalNilai

# Fungsi untuk menampilkan hasil nilai akhir


def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama: {}\tNilai Akhir: {:.2f}".format(nama, nilai_akhir))


# Program utama
def main():
    data_mahasiswa = {
        # Data mahasiswa (nama sebagai kunci dan nilai UTS serta UAS sebagai nilai dalam bentuk dictionary)
        'Name': {'uts': 90, 'uas': 90},
        'Pawas': {"uts": 100, 'uas': 100},
        'Izaz': {'uts': 95, 'uas': 95}

    }

    data_nilai_akhir = hitung_semua_nilai_akhir(data_mahasiswa)

    tampilkan_nilai_akhir(data_nilai_akhir)


if __name__ == "__main__":
    main()

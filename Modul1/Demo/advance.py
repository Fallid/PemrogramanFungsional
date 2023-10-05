dataBaseBuku = []
listBukuDipinjam = []
statusBuku = {}


def statusBukuDiPinjam(buku):
    for user, bukuDiPinjam in enumerate(listBukuDipinjam):
        if bukuDiPinjam == buku or bukuDiPinjam == user:
            return True
    return False


def kembalikanBuku(userName):
    if userName in statusBuku:
        listBukuDipinjam.pop()
        statusBuku[userName] ={userName:listBukuDipinjam} 
        print(f"Buku telah dikembalikan")
        return user(userName)
    else:
        return print("Tidak ada buku yang dipinjam")


def pinjamBuku(userName):
    pilihBuku = int(input("Pilih buku yang ingin dipinjam: "))

    # Penyesuaian index dengan buku yang dipilih
    pilihBuku = pilihBuku - 1

    if pilihBuku >= 0 or pilihBuku < len(dataBaseBuku):
        bukuDiPinjam = dataBaseBuku[pilihBuku]
        if not statusBukuDiPinjam(bukuDiPinjam):
            listBukuDipinjam.append(bukuDiPinjam)
            statusBuku[userName] = {userName:listBukuDipinjam}
            print(f"Buku {bukuDiPinjam[0]} berhasil dipinjam")
        else:
            print("Buku sudah dipinjam oleh user lain")
            return main()
    else:
        return print("Buku tidak ditemukan!")
    return user(userName)


def inputBuku(judulBuku, namaPenulis, adminName):
    print("Buku berhasil ditambahkan")
    dataBaseBuku.append((judulBuku, namaPenulis))
    return admin(adminName)


def daftarBukuYangDipinjam(userName):
    print("\n\nDaftar Buku yang Dipinjam")
    if statusBuku and listBukuDipinjam:
        daftarbuku =  statusBuku[userName][userName]
        print("Buku = ", str(daftarbuku)[1:-1])
    else:
        print("Belum ada peminjaman")
    return user(userName)

def daftarBuku():
    print("\n\nDaftar Buku: ")
    for index, buku in enumerate(dataBaseBuku):
        print(f"{index+1}. Judul Buku: {buku[0]}, ", end="")
        print(f"Penulis: {buku[1]}")


def admin(adminName):
    print("\n\nSelamat Datang", adminName)
    print("Menu: \n[1] Input Buku \n[2] Daftar Buku \n[3] Kembali")
    pilihMenu = input("Pilih Menu: ").lower()
    if pilihMenu == "input buku" or pilihMenu == "1":
        judulBuku = input("Judul Buku: ")
        namaPenulis = input("Nama Penulis: ")
        return inputBuku(judulBuku, namaPenulis, adminName)
    elif pilihMenu == "daftar buku" or pilihMenu == "2":
        daftarBuku()
        return admin(adminName)
    elif pilihMenu == "kembali" or pilihMenu == "3":
        return main()
    else:
        print("Unknow error")
        return main()


def user(userName):
    print("\n\nSelamat Datang", userName)
    print(
        "Menu \n[1] Pinjam Buku \n[2] Kembalikan Buku \n[3] Buku yang Dipinjam \n[4] Kembali")
    pilihMenu = input("Pilih Menu: ").lower()
    if pilihMenu == "pinjam buku" or pilihMenu == "1":
        daftarBuku()
        pinjamBuku(userName)
    elif pilihMenu == "kembalikan buku" or pilihMenu == "2":
        kembalikanBuku(userName)
    elif pilihMenu == "buku yang dipinjam" or pilihMenu == "3":
        daftarBukuYangDipinjam(userName)
    elif pilihMenu == "kembali" or pilihMenu == "4":
        return main()
    else:
        return print("Menu yang dipilih tidak ditemukan")


def main():
    # input role user flow 1
    print("Role User \n1.Admin \n2.User")
    roleUser = input("Masukkan role user: ").lower()

    if roleUser == "admin" or roleUser == "1":
        adminUsername = input("Username admin: ")
        adminPassword = input("Password admin: ")

        # validation admin pass and name flow 2
        if adminUsername != adminPassword:
            print("Password tidak valid")
            main()
        else:
            admin(adminUsername)

    elif roleUser == "user" or roleUser == "2":
        userName = input("User Name: ")
        userPassword = input("User Password: ")

        # validation user pass and name flow 2
        if userName != userPassword:
            print("Password tidak valid")
            main()
        else:
            user(userName)
    else:
        print("Unknown Error 404")


main()

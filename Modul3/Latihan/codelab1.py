_author_ = "Ahmad Naufal"
_copyright_ = "Copyright 2023, malang"

data = ["3 minggu 3 hari 7 jam 21 menit", "5 minggu 5 hari 8 jam 11 menit", "7 minggu 1 hari 5 jam 33 menit"]


def konversi(minggu=0):
    def konversi_hari(hari=0):
        def konversi_jam(jam=0):
            def konversi_menit(menit=0):
                return (minggu * 7 * 24 * 60) + (hari * 24 * 60) + (jam * 60) + menit
            return konversi_menit
        return konversi_jam
    return konversi_hari


def split_data(data):
    menit_data = []
    for times in data:
        components = times.split()
        minggu = hari = jam = menit = 0
        
        for i in range(0, len(components), 2):
            if components[i + 1] == "minggu":
                minggu = int(components[i])
            elif components[i + 1] == "hari":
                hari = int(components[i])
            elif components[i + 1] == "jam":
                jam = int(components[i])
            elif components[i + 1] == "menit":
                menit = int(components[i])
        
        konvert = konversi(minggu)(hari)(jam)(menit)
        menit_data.append(konvert)
    return menit_data

    
def main():
    print(split_data(data))

if __name__ == "__main__":
    main()
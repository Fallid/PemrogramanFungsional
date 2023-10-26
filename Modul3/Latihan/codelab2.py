_author_ = "Ahmad Naufal"
_copyright_ = "Copyright 2023, malang"

data = ["3 minggu 3 hari 7 jam 21 menit", "5 minggu 5 hari 8 jam 11 menit", "7 minggu 1 hari 5 jam 33 menit"]

def split_data(data):
    components = data.split()
    integers = [str(components[i]) for i in range(0, len(components), 2)]
    return integers

# Menggunakan filter untuk mengambil nilai integer
nilai_integer = list(filter(None, map(split_data, data)))

# Mencetak nilai integer dalam tiga baris terpisah
def sublist():
    for sublist in nilai_integer:
        print(sublist)

def main():
    sublist()

if __name__ == "__main__":
    main()
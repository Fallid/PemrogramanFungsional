_author_ = "Ahmad Naufal"
_copyright_ = "Copyright 2023, malang"

random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

# Fungsi untuk memeriksa apakah suatu nilai adalah integer
# def is_integer(value):
#     return isinstance(value, int)

# Fungsi untuk memetakan nilai integer menjadi ratusan, puluhan, dan satuan
def map_integer(value):
    ratusan = value // 100
    puluhan = (value // 10) % 10
    satuan = value % 10
    return {'ratusan': ratusan, 'puluhan': puluhan, 'satuan': satuan}

# Memisahkan nilai float, int, dan string
float_values = list(filter(lambda x: isinstance(x, float), random_list))
int_values = list(filter(lambda value: isinstance(value, int), random_list))
string_values = list(filter(lambda x: isinstance(x, str), random_list))
# dictionary = {}
# List = []

# Mencetak hasil
def printHasilFloat(float_values):    
    return f"Data Float : {tuple(float_values)}"
    
def printHasilString(string_values):
    return f"Data String : {[s for s in string_values if s.isalpha()]} "

def main():
    print(printHasilFloat(float_values))
    
    # printHasilInteger(int_values)
    # printHasilInteger(int_values)
    # print(*List)
    print("Data Int : ")
    for result in map(map_integer, int_values):
        print(result)

    print(printHasilString(string_values))
    
if __name__ == "__main__":
    main()
random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

# Fungsi untuk memeriksa apakah suatu nilai adalah integer
def is_integer(value):
    return isinstance(value, int)

# Fungsi untuk memetakan nilai integer menjadi ratusan, puluhan, dan satuan
def map_integer(value):
    ratusan = value // 100
    puluhan = (value // 10) % 10
    satuan = value % 10
    return {'ratusan': ratusan, 'puluhan': puluhan, 'satuan': satuan}

# Memisahkan nilai float, int, dan string
float_values = list(filter(lambda x: isinstance(x, float), random_list))
int_values = list(filter(is_integer, random_list))
string_values = list(filter(lambda x: isinstance(x, str), random_list))

# Mencetak hasil
print("Data Float : ", tuple(float_values))
print("Data Int : ")
for result in map(map_integer, int_values):
    print(result)
print("Data String : ", [s for s in string_values if s.isalpha()])
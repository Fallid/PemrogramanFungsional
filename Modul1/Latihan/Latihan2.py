random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]
list = []
dictionary = {"Satuan ": [], "Puluhan": [], "Ratusan": []}
tuple = ()
for i in random_list:
    if type(i) == float:
        tuple += (i,)
    elif type(i) == str:
        list += (i,)
    elif type(i) == int:
        satuan = i % 10
        puluhan = (i // 10) % 10
        ratusan = i // 100

        dictionary["Satuan "].append(satuan)
        dictionary["Puluhan"].append(puluhan)
        dictionary["Ratusan"].append(ratusan)
    else:
        print("Unknown Error")

print(tuple)
print(list)
print(dictionary)

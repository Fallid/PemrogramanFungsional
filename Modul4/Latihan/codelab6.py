_author_ = "Ahmad Naufal"
_copyright_ = "Copyright 2023, malang"

def point(x,y):
    return x,y
def line_equation_of(p1, M):
    def calculate_c():
        result = p1[0] - M * p1[1]
        return result 
    C = calculate_c()
    return f"y = {M:.2f}x + {C:.2f}"
# Ubah nilai input dengan 3 digit NIM akhir 424 (Genap)
print("Persamaan garis yang melalui titik (4,2) dan bergradien 4:")
print(line_equation_of(point(2, 9),6))
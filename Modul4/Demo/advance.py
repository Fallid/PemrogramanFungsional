_author_ = "Ahmad Naufal"
_copyright_ = "Copyright 2023, malang"

#TODO: DEMO INI UNTUK NIM GENAP

import math
# Global Value
titik_awal_x = lambda x: float(input(x))
titik_awal_y =  lambda y: float(input(y))
titik_awal_z = lambda z: float(input(z))
nilai_tx = lambda tx: float(input(tx))
nilai_ty = lambda ty: float(input(ty))
rotasi_x = lambda rotate_x: float(input(rotate_x))
nilai_sx = lambda sx: float(input(sx))
nilai_sy = lambda sy: float(input(sy))


# Perpindahan atau pergeseran garis
def translasi(tx, ty):
    def decoration(function):
        def transformasi(*args):
            # index [0] = x1 atau y1; index [1] = x2, y2
            new_x1 = args[0][0] + tx
            new_y1 = args[0][1] + ty
            new_x2 = args[1][0] + tx
            new_y2 = args[1][1] + ty
            return function((new_x1, new_y1), (new_x2, new_y2))
        return transformasi
    return decoration

# Rotasi sumbu X
def rotasi(sudut):
    def decoration(function):
        def transformasi(*args):
            # Seluruh data args = [(x1,y1),(x2,y2)]
            x1 = args[0][0]; y1 = args[0][1]; x2 = args[1][0]; y2 = args[1][1]
            radian = math.radians(sudut)
            new_x1 = x1 * math.cos(radian) - y1 * math.sin(radian); new_y1 = x1 * math.sin(radian) + y1 * math.cos(radian)
            new_x2 = x2 * math.cos(radian) - y2 * math.sin(radian); new_y2 = x2 * math.sin(radian) + y2 * math.cos(radian)
            return function((new_x1,new_y1),(new_x2, new_y2))
        return transformasi
    return decoration
# Perbesar Skala
def dilatasi(sx, sy):
    def decoration(function):
        def transformasi(*args):
            # Seluruh data args = [(x1,y1),(x2,y2)]
            x1 = args[0][0]; y1 = args[0][1]; x2 = args[1][0]; y2 = args[1][1]
            new_x1 = x1 * sx; new_y1 = y1 * sy
            new_x2 = x2 * sx; new_y2 = y2 * sy
            return function((new_x1, new_y1),(new_x2, new_y2))
        return transformasi
    return decoration

def point(x,y):
    return x,y

def before_line_equation(p1,p2):
        M = (p2[1] - p1[1]) / (p2[0] - p1[0])
        C = p1[1] - M * p1[0]
        return f"{M:.2f}x, {C:.2f}"

def main():
    while True:
        titik_x = titik_awal_x("Nilai titik X: ")
        titik_y = titik_awal_y("Nilai titik Y: ")
        titik_z = titik_awal_z("Nilai titik Z: ")
        titik_tx = nilai_tx("Nilai tx: ")
        titik_ty = nilai_ty("Nilai ty: ")
        titik_sx = nilai_sx("Nilai sekala sumbu x: ")
        titik_sy = nilai_sy("Nilai sekala sumbu y: ")
        radius = rotasi_x("Nilai derajat sumbu x: ")
        break
    
    @translasi(titik_tx, titik_ty)
    @rotasi(radius)
    @dilatasi(titik_sx, titik_sy)
    def line_equation_of(p1,p2):
        M = (p2[1] - p1[1]) / (p2[0] - p1[0])
        C = p1[1] - M * p1[0]
        return f"{M:.2f}x, {C:.2f}"
    
    print(f"Persamaan garis melalui titik A{titik_x, titik_y}, B{titik_y, titik_z}")
    print(before_line_equation(point(titik_x, titik_y), point(titik_y, titik_z)))
    print("\n\nPersamaan garis baru setelah transformasi: \ny = " ,line_equation_of(point(titik_x,titik_y), point(titik_y,titik_z)))
    

if __name__ == "__main__":
    main()
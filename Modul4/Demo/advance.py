_author_ = "Ahmad Naufal"
_copyright_ = "Copyright 2023, malang"

#TODO: DEMO INI UNTUK NIM GENAP

import math
# Global Value
titik_awal_x = lambda x: float(input(x)); titik_awal_y =  lambda y: float(input(y)); titik_awal_z = lambda z: float(input(z))
nilai_tx = lambda tx: float(input(tx)); nilai_ty = lambda ty: float(input(ty))
nilai_sx = lambda sx: float(input(sx)); nilai_sy = lambda sy: float(input(sy))
rotasi_x = lambda rotate_x: float(input(rotate_x))


# Perpindahan atau pergeseran garis
def translasi(function):
    def transformasi(*args):
        # index [0] = x1 atau y1; index [1] = x2, y2
        tx_ty = args[3]; radius = args[4]; sx_sy = args[4]
        new_x1 = args[0][0] + args[2][0]; new_y1 = args[0][1] + args[2][1]
        new_x2 = args[1][0] + args[2][0]; new_y2 = args[1][1] + args[2][1]
        return function((new_x1, new_y1), (new_x2, new_y2), (tx_ty), (radius),(sx_sy) )
    return transformasi

# Rotasi sumbu X
def rotasi(function):
    def transformasi(*args):
            # Seluruh data args = [(x1,y1),(x2,y2), (radius), (sx,sy)]
            radius = args[2]; sx_sy = args[3]; x1 = args[0][0]; y1 = args[0][1]; x2 = args[1][0]; y2 = args[1][1]
            radian = math.radians(radius)
            new_x1 = x1 * math.cos(radian) - y1 * math.sin(radian); new_y1 = x1 * math.sin(radian) + y1 * math.cos(radian)
            new_x2 = x2 * math.cos(radian) - y2 * math.sin(radian); new_y2 = x2 * math.sin(radian) + y2 * math.cos(radian)
            return function((new_x1,new_y1),(new_x2, new_y2),(sx_sy))
    return transformasi

# Perbesar Skala
def dilatasi(function):
    def transformasi(*args):
            # Seluruh data args = [(x1,y1),(x2,y2)]
            x1 = args[0][0]; y1 = args[0][1]; x2 = args[1][0]; y2 = args[1][1]
            sx = args[2][0]; sy = args[2][1]
            new_x1 = x1 * sx; new_y1 = y1 * sy
            new_x2 = x2 * sx; new_y2 = y2 * sy
            return function((new_x1, new_y1),(new_x2, new_y2))
    return transformasi

def point(fucntion):
        def transformasi(x,y, ty, tx, radius, sx, sy ):
            return fucntion((x[0],x[1]),(y[0],y[1]), (ty,tx), (radius), (sx,sy))
        return transformasi

def before_line_equation(p1,p2):
        M = (p2[1] - p1[1]) / (p2[0] - p1[0])
        C = p1[1] - M * p1[0]
        return f"{M:.2f}x, {C:.2f}"

@point
@translasi
@rotasi
@dilatasi
def line_equation_of(p1,p2):
    M = (p2[1] - p1[1]) / (p2[0] - p1[0])
    C = p1[1] - M * p1[0]
    return f"{M:.2f}x, {C:.2f}"

def main():
    while True:
        titik_x = titik_awal_x("Titik A(x, y) \nNilai titik X: ")
        titik_y = titik_awal_y(f"\nTitik A({titik_x}, y) \nNilai titik Y: ")
        titik_z = titik_awal_z(f"\nTitik B({titik_y}, z) \nNilai titik Z: ")
        titik_tx = nilai_tx("\nNilai tx: ")
        titik_ty = nilai_ty("\nNilai ty: ")
        titik_sx = nilai_sx("\nNilai sekala sumbu x: ")
        titik_sy = nilai_sy("\nNilai sekala sumbu y: ")
        radius = rotasi_x("\nNilai derajat sumbu x: ")
        break
    print(f"\n\nPersamaan garis melalui titik A{titik_x, titik_y}, B{titik_y, titik_z}")
    print(before_line_equation((titik_x, titik_y), (titik_y, titik_z)))
    print("\n\nPersamaan garis baru setelah transformasi: \ny = " ,line_equation_of((titik_x,titik_y),(titik_y,titik_z),(titik_tx),(titik_ty), (radius), (titik_sx), (titik_sy)))

if __name__ == "__main__":
    main()
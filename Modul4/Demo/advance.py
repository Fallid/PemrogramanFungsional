_author_ = "Ahmad Naufal"
_copyright_ = "Copyright 2023, malang"

#TODO: DEMO INI UNTUK NIM GENAP

import math
# Global Value
titik_awal_x = 3.0
titik_awal_y =  4.0
titik_awal_cnth = 5.0
titik_awal_z = 6.0
nilai_tx = 2
nilai_ty = -3
rotasi_x = 60
nilai_sx = 1.5
nilai_sy = 2

# Perpindahan atau pergeseran garis
def translasi(point_x1_y1, point_x2_y2):
    def transformasi(tx, ty):
        # index [0] = x1 atau y1; index [1] = x2, y2
        new_x1 = point_x1_y1[0] + tx
        new_y1 = point_x1_y1[1] + ty
        new_x2 = point_x2_y2[0] + tx
        new_y2 = point_x2_y2[1] + ty
        return [(new_x1, new_y1), (new_x2, new_y2)]
    return transformasi

# Rotasi sumbu X
def rotasi(sudut):
    def rotate_line(point_x1_y1, point_x2_y2):
        x1_rotated, y1_rotated = transformasi(point_x1_y1[0], point_x1_y1[1])
        x2_rotated, y2_rotated = transformasi(point_x2_y2[0], point_x2_y2[1])
        return [(x1_rotated, y1_rotated), (x2_rotated, y2_rotated)]
    def transformasi(x, y):
        radian = math.radians(sudut)
        new_x = x * math.cos(radian) - y * math.sin(radian)
        new_y = x * math.sin(radian) + y * math.cos(radian)
        return new_x, new_y
    return rotate_line

def point(x,y):
    return x,y

def line_equation_of(p1,p2):
    M = (p2[1] - p1[1]) / (p2[0] - p1[0])
    C = p1[1] - M * p1[0]
    return M,C

# Perbesar Skala
def dilatasi(point_x1_y1, point_x2_y2):
    def transformasi(sx, sy):
        new_x1 = point_x1_y1[0] * sx
        new_y1 = point_x1_y1[1] * sy
        new_x2 = point_x2_y2[0] * sx
        new_y2 = point_x2_y2[1] * sy
        return [(new_x1, new_y1), (new_x2, new_y2)]
    return transformasi


def main():
    print(f"Persamaan garis yang melalui titik A({titik_awal_x, titik_awal_y}) dan B({titik_awal_y, titik_awal_z}):")
    # Get The result of line equation
    result_line = line_equation_of(point(titik_awal_x,titik_awal_y), point(titik_awal_cnth,titik_awal_z))
    # Compute Translation of line equation
    new_translation = translasi(point(titik_awal_x, titik_awal_y), point(titik_awal_cnth, titik_awal_z))(nilai_tx, nilai_ty)
    #Compute rotation of X    
    new_rotation = rotasi(rotasi_x)(new_translation[0],new_translation[1])
    new_scale = dilatasi(new_rotation[0], new_rotation[1])(nilai_sx, nilai_sy)
    new_result_line = line_equation_of(new_scale[0], new_scale[1])
    print("Sebelum transoformasi: " + str(result_line))
    print("Translasi: " + str(new_translation))
    print("Translasi[0]: " + str(new_translation[0]))
    print("Translasi[1]: " + str(new_translation[1]))
    print("Rotasi "+ str(new_rotation))
    print("Scale: " + str(new_scale))
    print(f"Setelah transformasi: {new_result_line[0]:.2f}x, {new_result_line[1]:.2f}")
    

if __name__ == "__main__":
    main()
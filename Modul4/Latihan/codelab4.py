_author_ = "Ahmad Naufal"
_copyright_ = "Copyright 2023, malang"

import math
# Function Translasi
def translasi(tx, ty):
    def transformasi(x, y):
        new_x = x + tx
        new_y = y + ty
        return new_x, new_y
    return transformasi

#Function Dilatasi
def dilatasi(sx, sy):
    def transformasi(x, y):
        new_x = x * sx
        new_y = y * sy
        return new_x, new_y
    return transformasi

#Function Rotasi
def rotasi(sudut):
    def transformasi(x, y):
        radian = math.radians(sudut)
        new_x = x * math.cos(radian) - y * math.sin(radian)
        new_y = x * math.sin(radian) + y * math.cos(radian)
        return new_x, new_y
    return transformasi

#Titik awal
x,y = 3,5

#Translasi
translasi_func = translasi (2,-1)
koordinat_translasi_baru = translasi_func (x,y)
print("Koordinat setelah translasi: ",koordinat_translasi_baru)

#Dilatasi
dilatasi_func = dilatasi (2,-1)
koordinat_dilatasi_baru = dilatasi_func (x,y)
print("Koordinat setelah dilatasi: ", koordinat_dilatasi_baru)

#Rotasi
rotasi_func = rotasi(30)
koordinat_dirotasi_baru = rotasi_func (x,y)
print("Koordinat setelah rotasi : ",koordinat_dirotasi_baru)


_author_ = "Ahmad Naufal"
_copyright_ = "Copyright 2023, malang"

def perkalian(a):
  def dengan(b):
    return a * b
  return dengan


def HoF():
  Perkalian = perkalian(2)
  return Perkalian(6)

def currying():
  return perkalian(2)(6)


print(HoF())
print(currying())


print(type(HoF))
print(type(currying))

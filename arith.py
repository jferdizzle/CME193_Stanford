def arith1(x):
    if x <= 0:
        return 0
    elif x <= 10:
        return x
    else:
        return 10


def arith2(x, y):
    if x > y:
        return x*2 + y
    elif y > x:
        return 4*y - 3
    elif x == y:
        return x**3 + x*y


def arith3(x, y, z):
    if x == y or y == z or z == x:
        return 0
    elif x < y < z:
        return 1
    else:
        return 2


def arith4(x, y, z, w):
    if x < y:
        return max(arith2(x, y), arith2(z, w))
    else:
        return arith3(z, y, x) + arith1(w)


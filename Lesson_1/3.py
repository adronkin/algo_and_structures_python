# 3.	По введенным пользователем координатам двух точек вывести
# уравнение прямой вида y = kx + b, проходящей через эти точки.


DOT1_X = int(input('Точка 1. Значение X: '))
DOT1_Y = int(input('Точка 1. Значение Y: '))
DOT2_X = int(input('Точка 2. Значение X: '))
DOT2_Y = int(input('Точка 2. Значение Y: '))

try:
    K = (DOT1_Y - DOT2_Y) / (DOT1_X - DOT2_X)
    B = DOT2_Y - K * DOT2_X

    if K == 0 and B == 0:
        print('y = 0')
    elif K == 0:
        print(f'y = {B}')
    elif K == 1:
        print(f'y = x + {B}')
    elif B == 0:
        print(f'y = {K}x')
    else:
        print(f'y = {K}x + {B}')
except ZeroDivisionError:
    print('У точек одинаковые координаты, построение прямой невозможно')

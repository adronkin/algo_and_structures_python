"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import deque, defaultdict


class HexCalc:
    """Принимает 2 шестнадцатиричных числа, сохраняет в виде deque"""
    def __init__(self, num_1, num_2):
        self.num_1 = deque(num_1)
        self.num_2 = deque(num_2)

    def __add__(self, obj):
        self.num_hex_1 = ''
        for num in self.num_1:
            self.num_hex_1 += num
        return list(hex(int(''.join(self.num_hex_1), 16) + int(''.join(obj.num_2), 16)))[2:]

    def __mul__(self, obj):
        self.num_hex_1 = ''
        for num in self.num_1:
            self.num_hex_1 += num
        return list(hex(int(''.join(self.num_hex_1), 16) * int(''.join(obj.num_2), 16)))[2:]


X = input('Введите первое шастнадцатиричное число: ')
Y = input('Введите второе шастнадцатиричное число: ')
print(f'{X} + {Y} = {("".join(HexCalc(X, Y) + HexCalc(X, Y))).upper()}')
print(f'{X} * {Y} = {("".join(HexCalc(X, Y) * HexCalc(X, Y))).upper()}')

"""
=================== defaultdict ===================
"""

X_DICT = defaultdict(list)
Y_DICT = defaultdict(list)

for sign in range(len(X)):
    X_DICT[sign].append(X[sign])

for sign in range(len(Y)):
    Y_DICT[sign].append(Y[sign])

print(X_DICT.values())
print(Y_DICT.values())
from itertools import chain

TEMP_X = (''.join(list(chain(*X_DICT.values()))))
TEMP_Y = (''.join(list(chain(*Y_DICT.values()))))
HEX_SUM = hex(int(TEMP_X, 16)) + hex(int(TEMP_Y, 16))[2:]
# HEX_MUL = list(hex(int(TEMP_X, 16))) * list(hex(int(TEMP_Y, 16)))[2:]

print(HEX_SUM)
print(TEMP_Y)
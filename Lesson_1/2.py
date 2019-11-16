# 2. Выполнить логические побитовые операции "И", "ИЛИ" и др.
# над числами 5 и 6. Выполнить
# над числом 5 побитовый сдвиг вправо и влево на два знака.


def bit_and(num_1, num_2):
    """Выполняет побитовый 'И'"""
    return num_1 & num_2


def bit_or(num_1, num_2):
    """Выполняет побитовый 'ИЛИ'"""
    return num_1 | num_2


def bit_xor(num_1, num_2):
    """Выполняет побитовый 'Исключающее ИЛИ'"""
    return num_1 ^ num_2


NUM_1 = 5
NUM_2 = 6

print(f'Побитовый "И" = "{bit_and(NUM_1, NUM_2)}"')
print(f'Побитовый "ИЛИ" = "{bit_or(NUM_1, NUM_2)}"')
print(f'Побитовый "Исключающее ИЛИ" = "{bit_xor(NUM_1, NUM_2)}"')

NUM_3 = NUM_1 << 2

print(f'Побитовый "И" = "{bit_and(NUM_3, NUM_2)}"')
print(f'Побитовый "ИЛИ" = "{bit_or(NUM_3, NUM_2)}"')
print(f'Побитовый "Исключающее ИЛИ" = "{bit_xor(NUM_3, NUM_2)}"')

NUM_4 = NUM_1 >> 2

print(f'Побитовый "И" = "{bit_and(NUM_4, NUM_2)}"')
print(f'Побитовый "ИЛИ" = "{bit_or(NUM_4, NUM_2)}"')
print(f'Побитовый "Исключающее ИЛИ" = "{bit_xor(NUM_4, NUM_2)}"')

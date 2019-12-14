"""
1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""

import heapq
from collections import Counter


class Node:
    """Узлы дерева"""
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def walk(self, code, acc):
        """В словаре Code добавляем потомкам префиксы 0 и 1"""
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf:
    """Листья дерева"""
    def __init__(self, char):
        self.char = char

    def walk(self, code, acc):
        """Для листа записываем выстроенный код символа в словарь Code"""
        # '0' если для кодирования введен 1 символ
        code[self.char] = acc or "0"


def huffman_encode(string_for_encode):
    """Кодирование строки методом Хаффмана.
    Возращает словарь с символами и соответствующими им кодами"""
    # Пустой для очереди с приоритетом
    turn = []
    # Перебираем ключи и значения (символ и частота) словаря Counter
    for symb, freq in Counter(string_for_encode).items():
        # Добавляем  очередь частоту (freq), счетчик, уникальный для
        # каждого листа (для исключения ValueError в heapq.heappush), лист.
        turn.append((freq, len(turn), Leaf(symb)))
    # Превращаем список в очередь с приоритетами
    heapq.heapify(turn)
    # Переменная для генирации уникального значения (для исключения ValueError в heapq.heappush)
    count = len(turn)
    # Пока в очереди не менее 2х элементов
    while len(turn) > 1:
        # Извлекаем из очереди 2 элемента с минимальной частотой
        freq1, _count1, left = heapq.heappop(turn)
        freq2, _count2, right = heapq.heappop(turn)
        # Добавляем в очередь новый внутренний узел с потомками (left и right)
        heapq.heappush(turn, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}
    # Если в очереди элементов > 0
    if turn:
        # Сохраняем в очереди корень дерева
        [(_freq, _count, root)] = turn
        # Обходим дерево с корня и заполняем словарь code
        root.walk(code, "")
    return code


def main():
    my_string = input("Введите текст для кодирования: ")
    # Кодируем введенную строку
    code = huffman_encode(my_string)
    # Переменная с закодированой строкой
    encoded = " ".join(code[symb] for symb in my_string)
    # Печатаем каждый символ в алфавитном порядке и его код
    for symb in sorted(code):
        print(f"'{symb}': {code[symb]}")
    # Печатаем закодированную строку
    print(encoded)


if __name__ == "__main__":
    main()

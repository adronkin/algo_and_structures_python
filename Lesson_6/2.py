"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""

from pympler import asizeof
from sys import getsizeof


class Person:
    def __init__(self, name, name2, surname):
        self.name = name
        self.name2 = name2
        self.surname = surname


MAN1 = Person('Иван', 'Пертович', 'Каменев')
print(MAN1.__dict__)
print(f'asizeof - {asizeof.asizeof(MAN1)}')
print(f'getsizeof - {getsizeof(MAN1)}')
MAN1.name_3 = 'Игнатенко'
print(MAN1.__dict__)
print(f'asizeof - {asizeof.asizeof(MAN1)}')
print(f'getsizeof - {getsizeof(MAN1)}')

print('=========================SLOTS=========================')


class PersonSlots:
    __slots__ = ['name', 'name2', 'surname']

    def __init__(self, name, name2, surname):
        self.name = name
        self.name2 = name2
        self.surname = surname


MAN2 = PersonSlots('Иван', 'Пертович', 'Каменев')
print(MAN2.__slots__)
print(f'asizeof - {asizeof.asizeof(MAN2)}')
print(f'getsizeof - {getsizeof(MAN2)}')

"""
=========================СЛОВАРЬ=========================
{'name': 'Иван', 'name2': 'Пертович', 'surname': 'Каменев'}
asizeof - 608
getsizeof - 56
{'name': 'Иван', 'name2': 'Пертович', 'surname': 'Каменев', 'name_3': 'Игнатенко'}
asizeof - 760
getsizeof - 56
==========================SLOTS==========================
['name', 'name2', 'surname']
asizeof - 336
getsizeof - 64
"""
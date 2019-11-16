# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.


def search_letter(num, letter_list):
    """По числу num возвращает символ из строки под номером num"""
    return letter_list[num - 1]


ABC = 'abcdefghijklmnopqrstuvwxyz'

LETTER_NUM = int(input('Ввидите номер буквы: '))
if 1 <= LETTER_NUM <= 26:
    print(f'Под номером {LETTER_NUM} в английском алфавите '
          f'находится буква "{search_letter(LETTER_NUM, ABC)}"')
else:
    print('В английском алфавите 26 букв')

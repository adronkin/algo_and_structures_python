"""5.	Пользователь вводит две буквы. Определить, на каких местах
алфавита они стоят, и сколько между ними находится букв."""


def get_abc_true(letter):
    """Возвращает True, если введен символ алфавита"""
    abc = 'abcdefghijklmnopqrstuvwxyz'
    if letter.lower() in abc:
        return True


def get_letter_num(letter):
    """Возвращает номер символа в алфавите"""
    abc = 'abcdefghijklmnopqrstuvwxyz'
    letter_num = abc.find(letter.lower()) + 1
    return letter_num


def get_count_letter(num_1, num_2):
    """Возвращает кол-во символов между двумя числами не включая сами числа"""
    if num_1 > num_2:
        count = num_1 - num_2
    else:
        count = num_2 - num_1
    if count <= 1:
        return 0
    return count - 1


LETTER_1 = input('Введите букву 1: ')
LETTER_2 = input('Введите букву 2: ')

if get_abc_true(LETTER_1) and get_abc_true(LETTER_2):
    NUM_LETTER_1 = get_letter_num(LETTER_1)
    NUM_LETTER_2 = get_letter_num(LETTER_2)
    print(f'Буква "{LETTER_1}" находится на {NUM_LETTER_1}-м месте в алфавите,'
          f'а буква "{LETTER_2}" на {NUM_LETTER_2}-м')
    print(
        f'Между ними находится {get_count_letter(NUM_LETTER_1, NUM_LETTER_2)} букв')
else:
    print('Введены не символы алфавита')

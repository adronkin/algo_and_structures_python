# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит
# пользователь.


def get_number_sum(num):
    """Возвращает сумму чисел трехзначного числа"""
    num_1 = num // 100
    num_2 = num % 100 // 10
    num_3 = num % 10

    return num_1 + num_2 + num_3


NUMBER = int(input("Введите число: "))
if 100 <= NUMBER <= 999:
    print(f"сумма чисел чмсла {NUMBER} = {get_number_sum(NUMBER)}")
else:
    print("Введите число от 100 до 999")

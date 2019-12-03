"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

from collections import namedtuple


def avg_profit(my_list):
    """Возвращает среднее значение переменный 'q_1 q_2 q_3 q_4' namedtuple"""
    sum_profit = 0
    for i in my_list:
        sum_profit += (i.q_1 + i.q_2 + i.q_3 + i.q_4)
    return sum_profit / len(my_list)


def company_profit(my_list):
    """Возвращает значений переменной 'q_1 q_2 q_3 q_4' namedtuple"""
    sum_profit = (my_list.q_1 + my_list.q_2 + my_list.q_3 + my_list.q_4)
    return sum_profit


COMPANY_COUNT = int(input('Введите кол-во предприятий: '))
CompanyInfo = namedtuple('CompanyInfo', 'name q_1 q_2 q_3 q_4')
COMPANY_LIST = []


for _ in range(COMPANY_COUNT):
    company_name = input('Введите название предприятия: ')
    quarter_1 = int(input(f'Введите прибыль предприятия {company_name} за первый квартал: '))
    quarter_2 = int(input(f'Введите прибыль предприятия {company_name} за второй квартал: '))
    quarter_3 = int(input(f'Введите прибыль предприятия {company_name} за третий квартал: '))
    quarter_4 = int(input(f'Введите прибыль предприятия {company_name} за четвертый квартал: '))
    COMPANY = CompanyInfo(
        name=company_name,
        q_1=quarter_1,
        q_2=quarter_2,
        q_3=quarter_3,
        q_4=quarter_4
    )
    COMPANY_LIST.append(COMPANY)
    COMPANY_COUNT -= 1

AVG_PROFIT = avg_profit(COMPANY_LIST)
print(f'\nПредприятия с прибылью выше среднего значения ({round(AVG_PROFIT, 2)} в год): ')
for company in COMPANY_LIST:
    profit = company_profit(company)
    if profit >= AVG_PROFIT:
        print(f'{company.name} - {profit}')

print(f'Предприятия с прибылью ниже среднего значения ({round(AVG_PROFIT, 2)} в год): ')
for company in COMPANY_LIST:
    profit = company_profit(company)
    if profit < AVG_PROFIT:
        print(f'{company.name} - {profit}')

"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Фирма_1
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Фирма_2
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Фирма_1

Предприятия, с прибылью ниже среднего значения: Фирма_2
"""
from collections import namedtuple

from typing import List

Company = namedtuple('Company', 'name profit1 profit2 profit3 profit4')


def add_company():
    name = input('введите название предприятия:\n')
    profits_str = input('через пробел введите прибыль данного предприятия '
                        'за каждый квартал(всего 4 квартала)\n')
    return Company(name, *map(int, profits_str.split()))


def analyze_companies(companies: List[Company]):
    avg = sum([c.profit1 + c.profit2 + c.profit3 + c.profit4 for c in companies]) / len(companies)
    print(f'средняя годовая прибыль всех предприятий: {avg}')
    print(
        f'предприятия, с прибылью выше среднего значения: '
        f'{" ".join(c.name for c in companies if c.profit1 + c.profit2 + c.profit3 + c.profit4 > avg)}')
    print(
        f'предприятия, с прибылью ниже среднего значения: '
        f'{" ".join(c.name for c in companies if c.profit1 + c.profit2 + c.profit3 + c.profit4 < avg)}')


if __name__ == '__main__':
    count = input('введите количество предприятий для расчета прибыли\n')
    count = int(count)
    companies = [add_company() for i in range(count)]
    analyze_companies(companies)

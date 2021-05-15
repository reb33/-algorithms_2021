"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""


def find_max_prof1(companies):                   # общая сложность  O(n)
    companies_ = dict(companies)                 # O(n)
    max_profs = {}                               # O(1)
    for i in range(3):                           # O(1)
        max_ = ('', 0)                           # O(1)
        for name, prof in companies_.items():    # O(n)
            if prof > max_[1]:                   # O(1)
                max_ = (name, prof)              # O(1)
        companies_.pop(max_[0])                  # O(1)
        max_profs[max_[0]] = max_[1]             # O(1)
    print(max_profs)                             # O(1)


def find_max_prof2(companies):                                             # общая сложность N log N
    profits = sorted(list(companies.values()))                             # O(n) и N log N
    componies_ = dict(companies)                                           # O(n)
    max_profits = {}                                                       # O(1)
    for i in profits[-3:]:                                                 # O(1)
        name = next(n for n in componies_.keys() if componies_[n] == i)    # O(n)
        max_profits[name] = componies_[name]                               # O(1)
        componies_.pop(name)                                               # O(1)
    print(max_profits)                                                     # O(1)


if __name__ == '__main__':
    companies = {
        'likers': 99,
        'looks': 101,
        'limbs': 20,
        'nukerds': 55,
        'fraks': 78,
        'dumps': 97,
        'vials': 220,
        'faks': 2,
        'moon': 33,
        'welcome': 44,
        'cafe': 55,
        'tears': 88,
        'dreams': 12,
        'fun': 111,

    }
    find_max_prof1(companies)
    find_max_prof2(companies)

#     более эффективное решение 1

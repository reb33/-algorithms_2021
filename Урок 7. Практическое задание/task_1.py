"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в
виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""
from random import randint
from timeit import timeit
from typing import List


def simple_bubble(lst: List):
    for i in range(1, len(lst)):
        for j in range(len(lst)-i):
            if lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


def improved_bubble(lst: List):
    for i in range(1, len(lst)):
        is_changed = False
        for j in range(len(lst)-i):
            if lst[j] < lst[j+1]:
                is_changed = True
                lst[j], lst[j+1] = lst[j+1], lst[j]
        if not is_changed:
            break
    return lst


if __name__ == '__main__':
    lst = [randint(-100, 100) for _ in range(10)]
    print(lst)
    print(simple_bubble(lst[:]))
    print(improved_bubble(lst[:]))
    print(timeit(
        'simple_bubble([randint(-100, 100) for _ in range(10)])',
        'from __main__ import simple_bubble, randint'
    ))
    print(timeit(
        'improved_bubble([randint(-100, 100) for _ in range(10)])',
        'from __main__ import improved_bubble, randint'
    ))

# [-3, -52, -71, -74, 7, -72, -6, -21, 56, 20]
# [56, 20, 7, -3, -6, -21, -52, -71, -72, -74]
# [56, 20, 7, -3, -6, -21, -52, -71, -72, -74]
# 24.07557041698601
# 23.12786630995106

# доработка заключается в том что возможен такой вариант когда сортирка уже выполнена
# не доходя до финального шага
# тогда будет выполнен только 1 лишний проход (is_change = False)
# значит улучшение дает результат когда сортировка выполнена на N-2 шаге
# как показывают замеры, улучшение не сильно ускоряет работу на 10000 запусков с разными массивамы

"""Шейкерная сортировка"""

import random
import timeit

'''
разновидность пузырьковой сортировки.
Отличается тем, что просмотры элементов выполняются
один за другим в противоположных направлениях,
при этом большие элементы стремятся к концу массива,
а маленькие - к началу.
'''


def cocktail_sort(lst_obj):
    left = 0
    right = len(lst_obj) - 1
    while left <= right:
        for i in range(left, right):
            if lst_obj[i] > lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        right -= 1
        for i in range(right, left, -1):
            if lst_obj[i-1] > lst_obj[i]:
                lst_obj[i], lst_obj[i-1] = lst_obj[i-1], lst_obj[i]
        left += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]

# замеры 10
print(
    timeit.timeit(
        "cocktail_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit.timeit(
        "cocktail_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit.timeit(
        "cocktail_sort(orig_list[:])",
        globals=globals(),
        number=1000))

"""
0.009604599999999991
0.7762804999999999
97.97526020000001
"""

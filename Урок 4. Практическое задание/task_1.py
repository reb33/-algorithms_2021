"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается
"""
from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_1_optimized(nums):
    new_arr = [el for i, el in enumerate(nums) if i % 2 == 0]
    return new_arr


print(timeit("func_1([i for i in range(100)])", "from __main__ import func_1"))
print(timeit("func_1_optimized([i for i in range(100)])", "from __main__ import func_1_optimized"))

# 13.660981024993816
# 10.718805090989918 - list comprehension выполняется быстрей чем обход по циклу

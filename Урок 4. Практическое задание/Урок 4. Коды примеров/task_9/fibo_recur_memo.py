"""Фибо через рекурсию с мемоизацией через декоратор"""

from timeit import timeit

"""
Хронология вызовов будет такой:
 f(n), f(n-1), f(n-2), f(n-3), f(n-4), …, f(1), f(0), f(1), …, f(n-5), f(n-4), f(n-3), f(n-2).

"""


def memorize(func):
    def wrapper(n_val, memory={}):
        res = memory.get(n_val)
        if res is None:
            res = func(n_val)
            memory[n_val] = res
        return res
    return wrapper


@memorize
def func(n_val):
    if n_val < 2:
        return n_val
    return func(n_val - 1) + func(n_val - 2)


n = 8

print(timeit("func(n)", globals=globals()))

"""0.19176139999999997"""

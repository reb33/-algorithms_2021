"""
2.*	Написать программу сложения и умножения двух шестнадцатиричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)

__mul__
__add__

Пример:
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’]
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

1. вариант
defaultdict(list)
int(, 16)
reduce

2. вариант
class HexNumber:
    __add__
    __mul__

hx = HexNumber
hx + hx
"""
from collections import defaultdict, deque
from itertools import zip_longest


def solution_with_collections(num_s1: str, num_s2: str):
    nums = defaultdict(list)
    nums[1].extend(c for c in num_s1)
    nums[2].extend(c for c in num_s2)
    nums['sum'].extend(s for s in hex(int(''.join(nums[1]), 16) + int(''.join(nums[2]), 16))[2:].upper())
    nums['mul'].extend(s for s in hex(int(''.join(nums[1]), 16) * int(''.join(nums[2]), 16))[2:].upper())
    print(f"""defaultdict
    пользователь ввёл {num_s1} и {num_s2}
    сохранено {nums[1]} и {nums[2]}
    сумма: {nums['sum']}
    произведение: {nums['mul']}
    """)


def solution_with_oop(num_s1: str, num_s2: str):
    class HexNumber:

        def __init__(self, s):
            self.num = s

        def __add__(self, other):
            return hex(int(self.num, 16) + int(other.num, 16))[2:].upper()

        def __mul__(self, other):
            return hex(int(self.num, 16) * int(other.num, 16))[2:].upper()

    num1, num2 = HexNumber(num_s1), HexNumber(num_s2)
    print(f"""OOP
        пользователь ввёл {num_s1} и {num_s2}
        сумма: {num1 + num2}
        произведение: {num1 * num2}
        """)


if __name__ == '__main__':
    number1 = input('введите число в 16 системе\n')
    number2 = input('введите число в 16 системе\n')
    solution_with_collections(number1, number2)
    solution_with_oop(number1, number2)

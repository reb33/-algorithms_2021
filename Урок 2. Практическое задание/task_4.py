"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов: 3, их сумма: 0.75

Подсказка:
Каждый очередной элемент в 2 раза меньше предыдущего и имеет противоположный знак

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def int_input(input_str) -> int:
    num = ''
    while num == '':
        try:
            num = input(input_str + '\n')
            num = int(num)
        except ValueError:
            print('введено не число')
    return num


def sum_of_row(iterator, el=1.0):
    return el if iterator == 0 else el + sum_of_row(iterator - 1, el * -0.5)


if __name__ == '__main__':
    n = int_input('введите число')
    print(f'сумма: {sum_of_row(n-1)}')

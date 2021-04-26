"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все цифры извлечены

Используем операции % //, НЕ ИСПОЛЬЗУЕМ ОПЕРАЦИИ ВЗЯТИЯ ЭЛЕМЕНТА ПО ИНДЕКСУ

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321

Не забудьте проверить и на числах, заканчивающихся нулем.
Пример:
Введите число, которое требуется перевернуть: 1230
Перевернутое число: 0321

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


def revert_number(num, reverted='') -> str:
    reverted += str(num % 10)
    if num // 10 == 0:
        return reverted
    return revert_number(num // 10, reverted)


if __name__ == '__main__':
    x = int_input('введите число')
    print(f'перевернутое число: {revert_number(x)}')

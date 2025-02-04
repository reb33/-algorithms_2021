"""
Проведение сравнительных замеров
"""

import time

def check_1(n):
    """
    Фиксируем отсечки времени до и после выполнения основной логики
    :param n:
    :return: кортеж из результата ф-ции и затраченного времени
    """

    start_val = time.time()
    res = 0

    for i in range(1, n + 1):
        res = res + i

    end_val = time.time()

    return res, end_val - start_val


# результат хорошо повторяем
# для n = 10000
# затрачивается примерно 0.000979 сек
for i in range(5):
    print(f'Операция заняла {check_1(10000)[1]} сек')

print()
# для n = 100000
# затрачивается примерно 0.005877 сек
for i in range(5):
    print(f'Операция заняла {check_1(100000)[1]} сек')

print()
# для n = 100000
# затрачивается примерно 0.065629 сек
for i in range(5):
    print(f'Операция заняла {check_1(1000000)[1]} сек')

"""
На различных итерациях цикла даже на одной и той же машине
мы получаем различные результаты. Почему?

Влияют многие факторы:
1) версия интерпретатора
2) разрядность ОС
3) текущая нагрузка процессора
"""

# Получается абсолютные цифры различаются и на что же ориентироваться?
# Можно выполнить подсчет средней величины времени
# Хотя есть еще один вариант оценки, не привязанный к абсолютным цифрам
# Но об этом позже

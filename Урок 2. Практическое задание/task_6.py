"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Подсказка:
Базовый случай здесь - угадали число или закончились попытки

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
from random import randint


def int_input(input_str) -> int:
    num = ''
    while num == '':
        try:
            num = input(input_str + '\n')
            num = int(num)
        except ValueError:
            print('введено не число')
    return num


def try_guess(attempts, hidden_number):
    user_answer = int_input('введите число')
    if hidden_number == user_answer:
        print('вы угадали')
        return
    if attempts == 10:
        print(f'вы не угадали \nвведенное число {hidden_number}')
        return
    if hidden_number == user_answer:
        return
    if user_answer > hidden_number:
        print('введенное число больше загаданного')
    else:
        print('введенное число меньше загаданного')
    try_guess(attempts+1, hidden_number)


if __name__ == '__main__':
    hidden_num = randint(0, 100)
    try_guess(1, hidden_num)

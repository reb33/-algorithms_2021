"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""
from contextlib import suppress


def check1(cred, login, passw):                  # O(1) - общая сложность
    print(f'Проверка {login} {passw}')           # O(1)
    with suppress(KeyError):                     # O(1)
        if not cred[login][1]:                   # O(1)
            print('Пройдите авторизацию')        # O(1)
            return False                         # O(1)
        return cred[login][0] == passw           # O(1)
    return False                                 # O(1)


def check2(cred: dict, login, passw):            # O(n) - общая сложность
    print(f'Проверка {login} {passw}')           # O(1)
    for k, v in cred.items():                    # O(n)
        if k == login:                           # O(1)
            if not cred[login][1]:               # O(1)
                print('Пройдите авторизацию')    # O(1)
                return False                     # O(1)
            return cred[login][0] == passw       # O(1)
    return False                                 # O(1)


if __name__ == '__main__':
    credentials = {
        'ivan': ('pass', True),
        'vlad': ('pass1', False),
        'marad': ('pass2', True),
        'zagad': ('pass3', True),
        'bayad': ('pass4', False),
        'kirgad': ('pass5', True),
        'zambad': ('pass6', False),
        'serad': ('pass7', True),
        'varnad': ('pas8s', False),
        'kurgad': ('pas9s', True)
    }
    print('Проверки check1')
    print(check1(credentials, 'ivan', 'pass'))
    print(check1(credentials, 'igor', 'megapass'))
    print(check1(credentials, 'zambad', 'pass6'))
    print(check1(credentials, 'kurgad', 'pass'))
    print(check1(credentials, 'serad', 'pass7'))

    print()
    print('Проверки check2')
    print(check1(credentials, 'ivan', 'pass'))
    print(check1(credentials, 'igor', 'megapass'))
    print(check1(credentials, 'zambad', 'pass6'))
    print(check1(credentials, 'kurgad', 'pass'))
    print(check1(credentials, 'serad', 'pass7'))

#     более эффективное решение 1

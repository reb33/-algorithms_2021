# Вариант 3. Использование словарей:

a = {'x':0, 'y':0}
b = {'x':0, 'y':0}
a['x'] = float(input())
a['y'] = float(input())
b['x'] = float(input())
b['y'] = float(input())
summa = {}
mult = {}
summa['x'] = a['x'] + b['x']
summa['y'] = a['y'] + b['y']
mult['x'] = a['x'] * b['x'] - a['y'] * b['y']
mult['y'] = a['y'] * b['x'] + a['x'] * b['y']
print('Сумма:   %.2f+%.2fj' % (summa['x'], summa['y']))
print('Произв.: %.2f+%.2fj' % (mult['x'], mult['y']))

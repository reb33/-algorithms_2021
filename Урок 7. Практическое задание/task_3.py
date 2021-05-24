"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

[5, 3, 4, 3, 3, 3, 3]

[3, 3, 3, 3, 3, 4, 5]

my_lst
new_lts

arr[m]


from statistics import median

[3, 4, 3, 3, 5, 3, 3]


left.clear()
right.clear()


m = 3
len = 7
i
left = []
right = []

left == right and

for i in
    for
    left == right
    left.clear()
    right.clear()


"""
from statistics import median


def med(lst):
    return min(el for i, el in enumerate(lst) if len([j for j in lst[:i]+lst[i+1:] if j <= el]) >= len(lst) // 2)


def main():
    print(median([5, 3, 4, 3, 3, 3, 3]))
    print(med([5, 3, 4, 3, 3, 3, 3]))
    print(median([3, 4, 3, 3, 5, 3, 3]))
    print(med([3, 4, 3, 3, 5, 3, 3]))
    print(median([3, 4, 8, 3, 5, 3, 3, 5, 7, 3, 2, 12, 14, 1, 2]))
    print(med([3, 4, 8, 3, 5, 3, 3, 5, 7, 3, 2, 12, 14, 1, 2]))
    print(median([1, 8, 17, 43, 76, 22, 66, 55, 14, 99, 3]))
    print(med([1, 8, 17, 43, 76, 22, 66, 55, 14, 99, 3]))


if __name__ == '__main__':
    main()

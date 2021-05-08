"""Класс collections.namedtuple()"""

from collections import namedtuple

# 'Resume' - имя кортежа
# создаем шаблон кортежа
RES = namedtuple('Resume', 'id first_name second_name')
print(RES)  # -> <class '__main__.Resume'>
# заполняем шаблон данными
RESUME_PARTS = RES(
    id='1',
    first_name='Ivan',
    second_name='Ivanov'
)
print(type(RESUME_PARTS))
print(RESUME_PARTS.second_name)  # -> Resume(id='1', first_name='Ivan',
                                                    # second_name='Ivanov')
RESUME_PARTS.id = 10  # -> 1

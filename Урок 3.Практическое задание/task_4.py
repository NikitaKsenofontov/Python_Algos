"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""
# Хотел обойти функцию count но по времени не успевал
from random import randint

r = [randint(0, 99) for _ in range(20)]
print(f'Массив: {r}')

number = 0
max_count = 1
for i in r:
    if r.count(i) > max_count:
        max_count = r.count(i)
        number = r[r.index(i)]

if max_count == 1:
    print('Повторяющихся чисел нет')
else:
    print(f'Число {number}, встречается {max_count} раза')

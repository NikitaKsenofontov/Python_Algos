"""
Задание_3.	В массиве случайных целых чисел поменять
местами минимальный и максимальный элементы.

Пример:
В данном массиве чисел максимальное число   88 стоит на
0 позиции, а минимальное число  -49 стоит на    6 позиции
Заменяем их
[88, 26, 41, 75, 23, 52, -49, 60, 69, -18]
В данном массиве чисел максимальное число   88 стоит на
6 позиции, а минимальное число  -49 стоит на    0 позиции
[-49, 26, 41, 75, 23, 52, 88, 60, 69, -18]
"""
from random import randint

array = [randint(-99, 99) for _ in range(20)]
print(f'Старый массив: {array}')
el_max, el_min = 0, 0
for i in array:
    if i > el_max:
        el_max = i
    elif i < el_min:
        el_min = i
array[array.index(el_max)], array[array.index(el_min)] = array[array.index(el_min)], array[array.index(el_max)]
print(f'Новый массив:  {array}')
print(f'Поменяли местами числа {el_max} и {el_min}')

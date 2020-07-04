"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

Подсказка:
1) возьмите 2-3 задачи, реализованные ранее, сделайте замеры на разных входных данных
2) сделайте для каждой из задач оптимизацию (придумайте что можно оптимизировать)
и также выполните замеры на уже оптимизированных алгоритмах
3) опишите результаты - где, что эффективнее и почему.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

import timeit

"""
УРОК 1 Задание 9.
Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""
print('-' * 100)


def maximum_if_else():
    a, b, c = 0, 10, 7
    if b < a < c:
        return a
    elif a < b < c:
        return b
    else:
        return c


def maximum_list(my_list):
    return max(my_list)


test_list = [0, 10, 7]

time1 = timeit.timeit(f'maximum_if_else()', setup='from __main__ import maximum_if_else')
time2 = timeit.timeit(f'maximum_list({test_list})', setup='from __main__ import maximum_list')

print(f'Функция "maximum_if_else" - {time1} mls')
print(f'Функция "maximum_list" - {time2} mls')
print(f'Функция "maximum_if_else" быстрее функции "maximum_list" в {round(time2 / time1, 2)} раз')

"""
Несмотря на более короткий код и использование встроенной функции "max" 
функция "maximum_if_else" быстрее функции "maximum_list". 
Сравнение целых чисел (линейный алгоритм) быстрее перебора массива.
"""

print('-' * 100)

"""
УРОК 2 Задание 3.
Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.

Подсказка:
Используйте арифм операции для формирования числа, обратного введенному

Пример:
Введите число: 123
Перевернутое число: 321

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""


def reverse_math(num):
    new_num = 0
    while num != 0:
        integer = num // 10
        remainder = num % 10
        num = integer
        if new_num == 0:
            new_num = str(remainder)
        else:
            new_num = str(new_num) + str(remainder)
        int(new_num)
    return new_num


def reverse_slice(num):
    num = str(num)
    return num[::-1]


test_number = 4321

time1 = timeit.timeit(f'reverse_math({test_number})', setup='from __main__ import reverse_math', number=100000)
time2 = timeit.timeit(f'reverse_slice({test_number})', setup='from __main__ import reverse_slice', number=100000)

print(f'Функция "reverse_math" - {time1} mls')
print(f'Функция "reverse_slice" - {time2} mls')
print(f'Функция "reverse_slice" быстрее функции "reverse_math" в {round(time1 / time2, 2)} раз')

"""
Функция "reverse_slice" быстрее функции "reverse_math" из-за меньшего кол-ва строк кода, отсутсвия цикла 
и использования массива
"""
print('-' * 100)

"""
УРОК 3 Задание_3.
В массиве случайных целых чисел поменять
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


def array_circle(array):
    el_max, el_min = 0, 0
    for i in array:
        if i > el_max:
            el_max = i
        elif i < el_min:
            el_min = i
    el_max = array.index(el_max)
    el_min = array.index(el_min)
    array[el_max], array[el_min] = array[el_min], array[el_max]
    return array


def array_max_min(array):
    array[array.index(max(array))], array[array.index(min(array))] = \
        array[array.index(min(array))], array[array.index(max(array))]
    return array


def array_max_min_v2(array):
    el_max = max(array)
    el_min = min(array)
    el_max = array.index(el_max)
    el_min = array.index(el_min)
    array[el_max], array[el_min] = array[el_min], array[el_max]
    return array


test_array = [88, 26, 41, 75, 23, 52, -49, 60, 69, -18]


time1 = timeit.timeit(f'array_circle({test_array})', setup='from __main__ import array_circle', number=100000)
time2 = timeit.timeit(f'array_max_min({test_array})', setup='from __main__ import array_max_min', number=100000)
time3 = timeit.timeit(f'array_max_min_v2({test_array})', setup='from __main__ import array_max_min_v2', number=100000)

print(f'Функция "array_circle" - {time1} mls')
print(f'Функция "array_max_min" - {time2} mls')
print(f'Функция "array_max_min_v2" - {time3} mls')

print(f'Функция "array_max_min" быстрее функции "array_circle" в {round(time2 / time1, 2)} раз')
print(f'Функция "array_max_min_v2" быстрее функции "array_max_min" в {round(time2 / time3, 2)} раз')
print(f'Функция "array_max_min_v2" быстрее функции "array_circle" в {round(time1 / time3, 2)} раз')

"""
Несмотря на то, что функция array_max_min сильно короче, она выполняется медленне
из-за большего кол-ва вызовов встроенной функции и большим кол-во входов в массив.
Однако её можно оптимизировать и сделать даже чуть быстрее. 
Функция "array_max_min_v2" быстрее функции "array_circle" благодаря минимально необходимуму кол-ву вызовов
встроенных функций и сведению процесса к стандартному процессу присваивания переменных.
"""
print('-' * 100)

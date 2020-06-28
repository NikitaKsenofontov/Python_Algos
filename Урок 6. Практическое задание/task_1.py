from sys import getsizeof
from random import randint

"""
1.	Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.


ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
"""
x64 Windows 10 Pro
Python 3.8.1
"""

# lesson-03_9
matrix = []

for i in range(15):
    matrix.append([])
    matrix[i].extend([randint(0, 99) for _ in range(15)])

min_list = []
min_list.extend(matrix[0])

for string in matrix:
    print()
    print(('{:4d} ' * len(string)).format(*string))
    i = 0
    for j in string:
        if j < min_list[i]:
            min_list[i] = j
        i += 1

print()
print('min_list')
print(('{:4d} ' * len(min_list)).format(*min_list))
print()

min_list.sort(reverse=True)
print(
    'Максимальный элемент среди минимальных элементов столбцов матрицы: ',
    min_list[0]
)

sum_size_1 = 0
sum_size_2 = 0
sum_size_1 += getsizeof(matrix)
print(f'Переменная matrix занимает {sum_size_1}')
sum_size_2 += getsizeof(min_list)
print(f'Переменная min_list занимает {sum_size_2}')
print('-' * 100)


# lesson-03_7
r = [randint(0, 99) for _ in range(100)]
print(f'Массив: {r}')

min_index_1 = 0
min_index_2 = 1

for i in r:
    if r[min_index_1] > i:
        min_index_2 = min_index_1
        min_index_1 = r.index(i)
    elif r[min_index_2] > i:
        min_index_2 = r.index(i)

print(f'Два наименьших элемента: {r[min_index_1]} и {r[min_index_2]}')

print('Размер листа', getsizeof(r))
print('Размер элемента листа', getsizeof(r[0]))
print('Размер кортежа', getsizeof(tuple(r)))
print('Размер элемента кортежа', getsizeof(tuple(r)[0]))

amount = 0
for size in r:
    amount += getsizeof(size)
print('Размер всех элементов в листе', amount)

"""
Размер листа больше, чем неизменяемый кортеж, с одним набором данных
(912 байт у листа 848 байт у кортежа). Размер не зависит от разрядности чисел.
Зависит от размера массива.
Каждый элемент массива занимает 28 байт. 100 элементов по 28 байт занимают
2800 байт. Это значительно больше размера массива этих данных, т.к. Python
делает оптимизацию и создаёт ссылки на один и тот же объект.
"""
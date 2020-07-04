"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def calculation(item, num, el, s):  # s (sum) - amount
    if item >= num:
        return item, num, el, s
    return calculation(item + 1, num, el / -2, s + el)


def my_func():
    try:
        n = int(input('Введите кол-во элементов для ряда (1 -0.5 0.25 -0.125 ...), для завершения введите 0: '))
        if n == 0:
            return 'Программа завершена'
        if n < 0:
            print('Отрицательное число')
            return my_func()
    except ValueError:
        print('Некорректный ввод')
        return my_func()

    i, element, amount = 0, 1, 0
    i, n, element, amount = calculation(i, n, element, amount)

    if i == n:
        print(f'Сумма элементов ряда: {amount}')
        return my_func()


print(my_func())

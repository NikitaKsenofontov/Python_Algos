"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
import sys
sys.setrecursionlimit(10000)


def first(num):
    if num == 1:
        return num
    elif num > 0:
        return num + first(num-1)


def second(num):
    return num * (num + 1) // 2


n = 1

while True:
    if first(n) == second(n):
        print(f'Для n={n} - True')
    else:
        print(f'Для n={n} - False')
        break
    n += 1

"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def analysis(num, even, odd):  # Подсчет четных и нечетных
    if num == 0:
        return num, even, odd
    integer = num // 10
    remainder = num % 10
    if remainder % 2 == 0:
        return analysis(integer, even + 1, odd)
    return analysis(integer, even, odd + 1)


def separation():  # Разделение на четные и нечетные
    try:
        number = int(input('Введите натуральное число (для выхода введите 0): '))
        if number == 0:
            return 'Программа завершена'
    except Exception:
        print('Некорректный ввод')
        return separation()

    # a - для четных, b - для нечетных
    a, b = 0, 0
    result, a, b = analysis(abs(number), a, b)

    if result is not None:
        print(f'В числе {number} всего {a + b} цифр, из которых {a} четных и {b} нечетных')
        return separation()


print(separation())


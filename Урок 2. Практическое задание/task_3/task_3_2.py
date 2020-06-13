"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def reverse(number, new_number):
    if number == 0:
        return number, new_number
    remainder = number % 10
    if new_number == 0:
        return reverse(number // 10, str(remainder))
    return reverse(number // 10, new_number + str(remainder))


def my_func():
    try:
        num = int(input('Введите число (для выхода введите 0): '))
        if num == 0:
            return 'Программа завершена'
        if num < 0:
            print('Отрицательное число')
            return my_func()

        old_number = num
        new_num = 0
        result, new_num = reverse(num, new_num)

        if result is not None:
            print(f'Чило {old_number} в обратном порядке: {new_num}')
            return my_func()

    except ValueError:
        print('Некорректный ввод')
        return my_func()


print(my_func())

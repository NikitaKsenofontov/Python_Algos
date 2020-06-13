"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.

Подсказка:
Используйте арифм операции для формирования числа, обратного введенному

Пример:
Введите число: 123
Перевернутое число: 321

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
while True:
    try:
        number = int(input('Введите число (для выхода введите 0): '))
        if number == 0:
            print('Программа завершена')
            break
        if number < 0:
            print('Отрицательное число')
            continue

        old_number = number
        new_number = 0

        while number != 0:
            integer = number // 10
            remainder = number % 10
            number = integer
            if new_number == 0:
                new_number = str(remainder)
            else:
                new_number = str(new_number) + str(remainder)
            int(new_number)

        print(f'Чило {old_number} в обратном порядке: {new_number}')
    except ValueError:
        print('Некорректный ввод')

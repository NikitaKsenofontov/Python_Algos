"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

from random import randint
print('Отгадайете чилсло от 0 до 100, у вас 10 попыток')
random_number = randint(0, 100)
count = 1


def guess(user_answer, num, i):
    if user_answer == num:
        return user_answer
    if i >= 10:
        return 'Вы проиграли, не угадав число'
    if user_answer < num:
        return 'Число больше, чем вы указали'
    return 'Число меньше чем вы указали'


def my_func(number, attempts):
    try:
        print(f'Текущая попытка: {attempts}')
        answer = int(input('Введите предположительное число: '))
        if answer < 0:
            print('Введено отрицательное число')
            return my_func(number, attempts)
    except ValueError:
        print('Некорректный ввод')
        return my_func(number, attempts)

    result = guess(answer, number, count)
    if result == number:
        return 'Поздравляем, вы угадали'
    print(result)
    attempts += 1
    if attempts == 10:
        return result
    return my_func(number, attempts)


print(my_func(random_number, count))

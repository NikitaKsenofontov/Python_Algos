"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

from random import randint

print('Отгадайете чилсло от 0 до 100, у вас 10 попыток')
number = randint(0, 100)
count = 1
while count <= 10:
    print(f'Текущая попытка: {count}')
    try:
        answer = int(input('Введите предположительное число: '))
        if answer < 0:
            print('Введено отрицательное число')
            continue
        if answer == number:
            print('Поздравляем, вы угадали')
            break
        elif answer < number:
            print('Число больше, чем вы указали')
        else:
            print('Число меньше чем вы указали')
        count += 1
    except ValueError:
        print('Некорректный ввод')
else:
    print('Вы проиграли, не угадав число')

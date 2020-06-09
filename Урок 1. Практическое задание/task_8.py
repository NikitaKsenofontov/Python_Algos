"""
Задание 8.	Определить, является ли год, который ввел пользователем,
високосным или не високосным.

Подсказка:
Год является високосным в двух случаях: либо он кратен 4,
но при этом не кратен 100, либо кратен 400.

Попробуйте решить задачу двумя способами:
1. Обычное ветвление
2. Тернарный оператор

П.С. - Тернарные операторы, также известные как условные выражения,
представляют собой операторы, которые оценивают что-либо на основе условия,
являющегося истинным или ложным. Он был добавлен в Python в версии 2.5 .
Он просто позволяет протестировать условие в одной строке,
заменяя многострочное if-else, делая код компактным.
"""
try:
    year = int(input('Введите год: '))

    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print(f'{year} - Високосный год')
            else:
                print(f'{year} - Не високосный год')
        else:
            print(f'{year} - Високосный год')
    else:
        print(f'{year} - Не високосный год')
except:
    print('Неккоректный ввод')

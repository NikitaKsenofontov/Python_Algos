"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога

Предприятия, с прибылью ниже среднего значения: Копыта
"""
from collections import deque, defaultdict

# nf - number of fabrics
nf = int(input('Введите кол-во предприятий для расчета прибыли: '))

fabric_names = deque()
fabric_profit = defaultdict(list)
fabric_sum_profit = {}
profit_sum = 0
profit_low_limit = []
profit_up_limit = []

for i in range(nf):
    fabric_names.append(input(f'Введите название предприятия {i + 1}: '))
    fabric_profit[fabric_names[i]].append([int(x) for x in input(f'Введите прыбиль предприятия {i + 1} '
                                                                 'за каждый квартал через пробел '
                                                                 '(всего 4 квартала): ').split()])

    fabric_sum_profit[fabric_names[i]] = sum(fabric_profit[fabric_names[i]][0])
    profit_sum += sum(fabric_profit[fabric_names[i]][0])

print(f'Средняя годовая прибыль всех предприятий: {round((profit_sum / nf),1)}')

for j in range(nf):
    profit_low_limit.append(fabric_names[j]) \
        if fabric_sum_profit[fabric_names[j]] <= (profit_sum / nf) else profit_up_limit.append(fabric_names[j])

print(f'Предприятия, с прибылью выше среднего значения: {profit_up_limit if profit_up_limit else None}')
print(f'Предприятия, с прибылью ниже среднего значения: {profit_low_limit if profit_low_limit else None}')

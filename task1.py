"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.

"""
from sys import argv
script_name, output, rate, bonus = argv
try:
    salary = float(output) * float(rate) + float(bonus)
    print(f'{script_name}\nИтоговая зарплата: {salary}р.')
except ValueError:
    print('Неверные данные')

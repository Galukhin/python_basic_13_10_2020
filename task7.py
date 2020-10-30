"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь
(со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json

sum_profit = 0
cnt_positive_profit = 0
firm_dict = {}
average_dict = {}

with open('task7.txt', 'r', encoding='UTF-8') as data_file:
    while True:
        line = data_file.readline().split()
        if not line:
            break
        firm_name = line[0]
        profit = int(line[2]) - int(line[3])
        firm_dict.update({firm_name: profit})
        if profit >= 0:
            sum_profit += profit
            cnt_positive_profit += 1

average_dict.update({'average_profit': sum_profit / cnt_positive_profit})
data_list = [firm_dict, average_dict]

with open('task7.json', 'w', encoding='UTF-8') as json_file:
    json.dump(data_list, json_file)

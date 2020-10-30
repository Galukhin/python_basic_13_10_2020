"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
from my_module import (my_map,
                       my_sum)
result_dict = {}
with open('task6.txt', 'r', encoding='UTF-8') as my_file:
    while True:
        dict_itm = my_file.readline().split(':')
        if not dict_itm[0]:
            break
        hours = ''
        for itm in dict_itm[1]:
            if itm.isdigit() or itm == ' ':
                hours += itm
        hours_list = list(my_map(int, hours.split()))
        result_dict.update({dict_itm[0]: my_sum(hours_list)})
print(result_dict)

"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from my_module import (my_map,
                       my_sum)

while True:
    try:
        my_list = list(my_map(float, input('Введите набор чисел, разделенных пробелами\n>>>').split()))
        break
    except ValueError:
        print('Необходимо вводить числа!')

my_list = list(my_map(str, my_list))
with open('task5.txt', 'w', encoding='UTF-8') as my_file:
    my_file.write(' '.join(my_list))

with open('task5.txt', 'r', encoding='UTF-8') as my_file:
    my_list = list(my_map(float, my_file.read().split()))

print('Результат:', my_sum(my_list))

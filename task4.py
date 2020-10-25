"""
4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""
from my_module import my_map
while True:
    try:
        user_list = list(my_map(int, input('Введите список целых чисел через пробел\n>>>').split()))
        break
    except ValueError:
        print('Неверно введенные данные')
result = [itm for itm in user_list if user_list.count(itm) == 1]
print('Результат:', result)

"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def is_number(user_str):
    """
    Проверяет, является ли строка числом

    :param user_str: принимает строку
    :return: возвращает bool
    """
    try:
        float(user_str)
        return True
    except ValueError:
        return False


def my_max(*args):
    """
    Находит максимальное число в последовательности

    :param args: tuple float, int
    :return: float, int
    """
    max_item = args[0]
    for itm in args:
        if itm > max_item:
            max_item = itm
    return max_item


def my_func(el1, el2, el3):
    """
    Находит сумму двух наибольших аргументов

    :param el1, el2, el3:
    :return:
    """
    tmp_list = [el1, el2, el3]
    max1 = my_max(*tmp_list)
    tmp_list.remove(max1)
    max2 = my_max(*tmp_list)
    result = max1 + max2
    return result


while True:
    user_number_str = input('Введите через запятую три числа:\n>>>')
    try:
        el1, el2, el3 = user_number_str.split(',')
    except ValueError:
        print('Три числа, Карл!')
        continue
    if is_number(el1) and is_number(el2) and is_number(el3):
        el1 = float(el1)
        el2 = float(el2)
        el3 = float(el3)
        break
    print('Аргументы должны быть числом!')

print("Результат:", my_func(el1, el2, el3))

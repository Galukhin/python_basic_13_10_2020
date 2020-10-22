"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
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


def divide(arg1, arg2):
    """
    Возвращает частное от деления

    :param arg1: делимое, int или float
    :param arg2: делитель, int или float
    :return: частное, float или None
    """
    try:
        result = arg1 / arg2
        return result
    except ZeroDivisionError:
        return None


while True:
    user_number_str = input('Введите через запятую два числа:\n>>>')
    try:
        arg1, arg2 = user_number_str.split(',')
    except ValueError:
        print('Два числа, Карл!')
        continue
    if is_number(arg1) and is_number(arg2):
        break
    print('Аргументы должны быть числом!')
result = divide(float(arg1), float(arg2))
if result == None:
    print('Делить на ноль нельзя!')
else:
    print('Результат деления:', result)

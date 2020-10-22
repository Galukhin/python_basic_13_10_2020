"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже
подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
к полученной ранее сумме и после этого завершить программу.
"""


def my_sum(*args):
    """
    Возвращает сумму входящих элементов

    :param args: int, float
    :return: int, float
    """
    result = 0
    for itm in args:
        result = result + itm
    return result


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


result_list = []  # Общий список
next_enter = True
print("Вводите строки чисел через пробел. Для остановки программы введите q в конце строки")
while next_enter:
    incorrect_input = False
    tmp_str = input(">>>")
    tmp_list = tmp_str.split() # Текущий пользовательский список
    tmp_float_list = []
    try:
        idx_max = tmp_list.index('q')  # Определяем срез списка до знака выхода
        next_enter = False
    except ValueError:
        idx_max = len(tmp_list)  # Если знака выхода нет, обходим весь список
    idx = 0
    while idx < idx_max:
        if not is_number(tmp_list[idx]):  # Проверяем, что все элементы - числа
            incorrect_input = True
            break
        tmp_float_list.append(float(tmp_list[idx]))  # Если все числа, делаем список из float
        idx += 1
    if incorrect_input:  # Если же были введены не числа - цикл начинаем заново
        print("В строке должны быть числа или q")
        continue
    result_list.extend(tmp_float_list[:idx_max])  # Добавляем текущий пользовательский список в общий
    result = my_sum(*result_list)
    print("Сумма всех введеных чисел:", result)

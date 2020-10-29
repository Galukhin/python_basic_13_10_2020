"""
Файл с аналогами встроенных функций
"""


def my_map(funk, iter_obj):
    """
    Применяет функцию к итерируемому объекту
    :param funk: функция
    :param iter_obj: итерируемый объект
    :return:
    """
    for itm in iter_obj:
        yield funk(itm)


def my_range(stop_itm, start_itm=0, step=1):
    """Функция-генератор последовательности
    :param stop_itm: int, элементы последовательности меньше stop_itm
    :param start_itm: int,первый элемент последовательности
    :param step: int, шаг последовательности
    :return: generate object
    """
    itm = start_itm
    while itm < stop_itm:
        yield itm
        itm += step


def my_reduce(func, iter_obj):
    """Применяет указанную функцию к набору объектов и сводит его к единственному значению
    :param func: функция
    :param iter_obj: итерируемый объект
    :return: возвращаемый тип - как у func
    """
    idx = 1
    tmp = iter_obj[0]
    while idx < len(iter_obj):
        tmp = func(tmp, iter_obj[idx])
        idx += 1
    return tmp


def my_sum(iter_obj):
    tmp = 0
    for itm in iter_obj:
        tmp += itm
    return tmp

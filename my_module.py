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
    itm = start_itm
    while itm < stop_itm:
        itm += step
        yield itm + step

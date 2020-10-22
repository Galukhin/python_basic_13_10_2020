"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
"""


def my_capitalize(word):
    """
    Возвращает слово с прописной буквы

    :param word: str
    :return: str
    """
    result = ''.join([word[0].upper(), word[1:].lower()])
    return result


def my_map(funk, iter_obj):
    """
    Применяет функцию к итерируемому объекту
    :param funk: функция
    :param iter_obj: итерируемый объект
    :return:
    """
    for itm in iter_obj:
        yield funk(itm)


user_str = input('Введите строку из слов, разделенных пробелом\n>>>')
my_list = user_str.split()
result = ' '.join(list(my_map(my_capitalize, my_list)))
print(result)

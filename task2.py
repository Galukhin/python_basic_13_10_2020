"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def one_string(**kwargs):
    """
    Реализует вывод данных словаря одной строкой

    :param kwargs: элементы словаря, например пункты анкеты пользователя
    :return: str
    """
    result_list = []
    for key, value in kwargs.items():
        result_list.append(f'{key}: {value}')
    result_str = ', '.join(result_list)
    return result_str


user_template = {
    'Имя': ("Имя", str),
    'Фамилия': ('Фамилия', str),
    'Год рождения': ('Год рождения', int),
    'Город проживания': ('Город проживания', str),
    'email': ('email', str),
    'телефон': ('телефон', str),
}

user_dict = {}
for key, value in user_template.items():
    while True:
        user_value = input(f'{value[0]}\n')
        try:
            user_value = value[1](user_value)
        except ValueError:
            print("Не верное значение данных")
            continue
        user_dict[key] = user_value
        break

result = one_string(**user_dict)
print(result)

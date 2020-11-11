"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:
    user_date = ''
    dd = 0
    mm = 0
    yy = 0

    def __init__(self, user_date: str):
        Date.user_date = user_date

    @classmethod
    def get_full_date(cls):
        cls.dd, cls.mm, cls.yy = list(map(int, cls.user_date.split('-')))

    @staticmethod
    def valid_date(dd: int, mm: int, yy: int) -> bool:
        # Не проверяю год. Отрицательный год - до н.э.
        month_dict = {1: 31, 3: 31, 4: 30,
                      5: 31, 6: 30, 7: 31,
                      8: 31, 9: 30, 10: 31,
                      11: 30, 12: 31}
        is_leap = True if not yy % 4 else False
        if mm < 1 or mm > 12:
            return False
        if mm == 2:
            max_day = 29 if is_leap else 28
        else:
            max_day = month_dict[mm]
        valid_day = True if 0 < dd <= max_day else False
        return valid_day


if __name__ == '__main__':
    while True:
        my_date = Date(input('Введите дату в формате день-месяц-год:\n>>>'))
        try:
            my_date.get_full_date()
        except ValueError:
            print('Неверный формат ввода!')
            continue
        if not Date.valid_date(my_date.dd, my_date.mm, my_date.yy):
            print('Неверная дата!')
            continue
        else:
            print('Все отлично! Завершение программы')
            break

"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа
должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


if __name__ == '__main__':
    while True:
        dividend, divisor = input('Введите делимое и делитель\n>>>').split()
        try:
            dividend = int(dividend)
            divisor = int(divisor)
            if divisor == 0:
                raise MyZeroDivisionError('Делить на ноль нельзя!')
        except ValueError:
            print('Требуется ввести числа!')
            continue
        except MyZeroDivisionError as err:
            print(err)
            continue
        print('Результат:', dividend / divisor)
        break

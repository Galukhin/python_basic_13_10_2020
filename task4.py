"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def my_power(base, power):
    """
    Выполняет возведение действительного положительного числа в целую отрицательную степень

    :param base: float, base > 0
    :param power: int, power < 0
    :return: float
    """
    result = 1  # result = base**power
    cnt = 0
    max_cnt = abs(power)
    while cnt < max_cnt:
        result /= base
        cnt += 1
    return result


while True:
    try:
        base = float(input("Введите действительное положительное число\n>>>"))
    except ValueError:
        print("Это не число!")
        continue
    if float(base) > 0:
        base = float(base)
        break
    print("Число должно быть положительным!")

while True:
    try:
        power = int(input("Введите целое отрицательное число\n>>>"))
    except ValueError:
        print("Это не целое число!")
        continue
    if int(power) < 0:
        power = int(power)
        break
    print("Число должно быть отрицательным!")

print("Результат:", my_power(base, power))

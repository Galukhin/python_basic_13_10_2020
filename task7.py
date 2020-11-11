"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры
класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class Complex:

    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, other):
        if not isinstance(other, (type(self), int, float)):
            raise TypeError('Ошибка операции сложения')
        if isinstance(other, (int, float)):
            new_complex = type(self)(self.re + other, self.im)
            return new_complex
        if isinstance(other, type(self)):
            new_complex = type(self)(self.re + other.re, self.im + other.im)
            return new_complex

    def __mul__(self, other):
        if not isinstance(other, (type(self), int, float)):
            raise TypeError('Ошибка операции умнножения')
        if isinstance(other, (int, float)):
            new_complex = type(self)(self.re * other, self.im * other)
            return new_complex
        if isinstance(other, type(self)):
            new_complex = type(self)(self.re * other.re - self.im * other.im,
                                     self.re * other.im + self.im * other.re)
            return new_complex

    def __str__(self):
        result = str((self.re, self.im))
        return result


if __name__ == '__main__':
    comp1 = Complex(2, 5)
    print(comp1)
    comp2 = Complex(-3, 12)
    print(comp2)
    try:
        print(comp1 + 2)
        print(comp2 * 3)
        print(comp1 + comp2)
        print(comp1 * comp2)
        print(comp1 + 'comp')
    except TypeError as err:
        print(err)

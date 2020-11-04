"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""
from typing import List


class Matrix:

    def __new__(cls, matrix_list: List[List]):
        for itm in matrix_list:
            if len(itm) != len(matrix_list[0]):
                raise ValueError('Количество элементов в строках матрицы должно быть одинаковым!')
        return super().__new__(cls)

    def __init__(self, matrix_list: List[List]):
        self.__matrix_list = matrix_list
        self.row_num = len(matrix_list)
        self.col_num = len(matrix_list[0])

    def __str__(self):
        result = ''
        for row in self.__matrix_list:
            for col in row:
                result += f'{col: <10}'
            result += '\n'
        return result

    def __eq__(self, other):
        return self.col_num == other.col_num and self.row_num == other.row_num

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError('Складывать между собой можно только матрицы!')

        if self != other:
            raise TypeError('Матрицы разного размера!')

        result_matrix = []
        for idx_row in range(self.row_num):
            result_row = []
            for idx_col in range(self.col_num):
                result_row.append(self.__matrix_list[idx_row][idx_col] + other.__matrix_list[idx_row][idx_col])
            result_matrix.append(result_row)
        return Matrix(result_matrix)


matrix1 = Matrix([[1, 2, 3], [4, 5, 6]])
matrix2 = Matrix([[7, 8, 9], [10, 11, 12]])
print(matrix1)
print(matrix2)
print(matrix1 == matrix2)
print(matrix1 + matrix2)

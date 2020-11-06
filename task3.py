"""
3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны применяться только
к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток,
соответственно. В методе деления должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных
двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух
клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества
ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление
количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному
аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет
строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет
строку: *****\n*****\n*****.
"""
from random import randint


class Cell:
    collection = []
    cnt_instance = 0

    def __init__(self, partition: int):
        self.partition = partition
        self.collection.append(self)
        self.cnt_instance += 1

    def __le__(self, other):
        return self.partition <= other.partition

    def __lt__(self, other):
        return self.partition < other.partition

    def __add__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError('С клеткой можно складывать только клетку!')

        new_cell = type(self)(self.partition + other.partition)
        self.collection.remove(self)
        other.collection.remove(other)
        return new_cell

    def __sub__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError('Из клетки можно вычитать только клетку!')

        if self <= other:
            return 'Не нападай на мелких!'

        new_cell = type(self)(self.partition - other.partition)
        self.collection.remove(self)
        other.collection.remove(other)
        return new_cell

    def __mul__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError('На клетку можно умножать только клетку!')

        new_cell = type(self)(self.partition * other.partition)
        self.collection.remove(self)
        other.collection.remove(other)
        return new_cell

    def __truediv__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError('На клетку можно делить только клетку!')

        if self < other:
            return 'Не нападай на мелких!'

        new_cell = type(self)(self.partition // other.partition)
        self.collection.remove(self)
        other.collection.remove(other)
        return new_cell

    def make_order(self, row_partition: int):
        result = ('* ' * self.partition).split()
        cnt_row = -1
        while cnt_row + row_partition < len(result):
            result.insert(cnt_row + row_partition + 1, '\n')
            cnt_row += row_partition + 1
        return ''.join(result)


if __name__ == '__main__':  # Имитация естественного отбора
    """a1 = Cell(3)
    a2 = Cell(5)
    a3 = Cell(1)
    print(a3 - a1)
    print(a1.collection)
    print(a3 + a1)
    print(a2.collection)"""
    for i in range(0, 5):
        Cell(randint(1, 5))
    print(Cell.collection)
    print(Cell.collection[0] + Cell.collection[1])
    print(Cell.collection)
    i = 0
    while len(Cell.collection) > 1:
        idx1 = randint(0, len(Cell.collection) - 1)
        idx2 = randint(0, len(Cell.collection) - 1)
        while idx1 == idx2:
            idx2 = randint(0, len(Cell.collection) - 1)
        num_op = randint(0, 3)
        print(idx1, idx2, num_op)
        if num_op == 0:
            a = Cell.collection[idx1] + Cell.collection[idx2]
            print(Cell.collection)
        elif num_op == 1:
            Cell.collection[idx1] - Cell.collection[idx2]
            print(Cell.collection)
        elif num_op == 2:
            Cell.collection[idx1] * Cell.collection[idx2]
            print(Cell.collection)
        else:
            Cell.collection[idx1] + Cell.collection[idx2]
            print(Cell.collection)
        i += 1
    print(Cell.collection)

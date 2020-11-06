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


class Cell:
    collection = []

    def __init__(self, partition: int):
        self.partition = partition
        self.collection.append(self)

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


if __name__ == '__main__':
    cell1 = Cell(25)
    cell2 = Cell(12)
    cell3 = Cell(10)
    cell4 = Cell(17)
    cell5 = Cell(2)
    for itm in cell1.collection:
        print(f'{itm}:\n{itm.make_order(5)}')
    cell6 = cell1 + cell2
    print(f'cell1 + cell2:\n{cell6.make_order(10)}')
    print(f'cell3 - cell4:\n{cell3 - cell4}')
    cell7 = cell4 - cell3
    print(f'cell4 - cell3:\n{cell7.make_order(5)}')
    cell8 = cell6 / cell7
    print(f'cell6 / cell7:\n{cell8.make_order(5)}')
    cell9 = cell8 * cell5
    print(f'cell8 * cell5:\n{cell9.make_order(5)}')
    print(cell9.collection)  # Осталась одна клетка в коллекции

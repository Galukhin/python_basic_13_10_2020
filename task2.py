"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    __collection = []

    def __init__(self, brand: str):
        self.brand = brand
        self.__collection.append(self)

    @abstractmethod
    def textile(self):
        pass

    @property
    def sum_textile(self):
        result = 0
        for itm in self.__collection:
            result += itm.textile
        return result


class Coat(Clothes):

    def __init__(self, brand: str, size: float):
        self._size = size
        super().__init__(brand)

    @property
    def textile(self):
        return self._size / 6.5 + 0.5


class Suit(Clothes):

    def __init__(self, brand: str, height: float):
        self._height = height
        super().__init__(brand)

    @property
    def textile(self):
        return 2 * self._height + 0.3


if __name__ == '__main__':
    coat1 = Coat('Zara', 50)
    coat2 = Coat('UniClo', 48)
    suit1 = Suit('Prada', 1.86)
    suit2 = Suit('Сударь', 1.72)
    print(f'{type(coat1).__name__} {coat1.brand} need {coat1.textile:.2f} textile')
    print(f'{type(coat2).__name__} {coat2.brand} need {coat2.textile:.2f} textile')
    print(f'{type(suit1).__name__} {suit1.brand} need {suit1.textile:.2f} textile')
    print(f'{type(suit2).__name__} {suit2.brand} need {suit2.textile:.2f} textile')
    print(f'Summary textile: {coat1.sum_textile:.2f}')

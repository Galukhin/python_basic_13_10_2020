"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов:
TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод
show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
from random import randint


class Car:

    def __init__(self, color, name, is_police):
        self.speed = randint(0, 200)
        self.color = color
        self. name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print('Машина поехала', direction)

    def show_speed(self):
        print('Текущая скорость автомобиля:', self.speed)


class TownCar(Car):

    def __init__(self, color, name):
        super().__init__(color, name, is_police=False)

    def show_speed(self):
        Car.show_speed(self)
        if self.speed > 60:
            print('Нарушаете скоростной режим!')


my_car = TownCar('blue', 'Kia Rio')
print(my_car.speed, my_car.is_police)
my_car.show_speed()

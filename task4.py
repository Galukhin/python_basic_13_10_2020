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
    collection = []

    def __init__(self, color, name, is_police):
        self.color = color
        self.name = name
        self.is_police = is_police
        self.speed = randint(0, 200)
        self.collection.append(self)

    def go(self):
        print(f'{self.color} {self.name} поехал')

    def stop(self):
        print(f'{self.color} {self.name} остановился')

    def turn(self, direction):
        print(f'{self.color} {self.name} повернул {direction}')

    def show_speed(self):
        print('Текущая скорость автомобиля:', self.speed)


class TownCar(Car):

    def __init__(self, color, name):
        super().__init__(color, name, is_police=False)

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Нарушаете скоростной режим!')


class WorkCar(Car):

    def __init__(self, color, name):
        super().__init__(color, name, is_police=False)

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Нарушаете скоростной режим!')


class SportCar(Car):

    def __init__(self, color, name):
        super().__init__(color, name, is_police=False)


class PoliceCar(Car):

    def __init__(self, color, name):
        super().__init__(color, name, is_police=True)


def get_instance_attributes(instance):
    print(f'Имя: {instance.name}')
    print(f'Цвет: {instance.color}')
    print(f'Полицейская?: {instance.is_police}')
    print(f'Скорость: {instance.speed}')


def call_instance_methods(instance):
    instance.go()
    instance.turn('left')
    instance.turn('right')
    instance.show_speed()
    instance.stop()


if __name__ == '__main__':
    my_town_car = TownCar('black', 'Kia Rio')
    my_work_car = WorkCar('brown', 'Belarus')
    my_sport_car = SportCar('red', 'Lamborghini')
    my_police_car = PoliceCar('white-blue', 'Nissan')

    for itm in Car.collection:
        get_instance_attributes(itm)
        call_instance_methods(itm)

"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Скорость автомобиля {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'(!) Вы превысили разрешенную скорость в 60 км/ч.')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'(!) Вы превысили разрешенную скорость в 40 км/ч.')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


if __name__ == '__main__':
    town_car = TownCar(65, 'gray', 'Lada')
    print(f'Автомобиль: {town_car.name}, цвет: {town_car.color}')
    town_car.go()
    town_car.show_speed()
    town_car.turn('налево')
    town_car.stop()
    print()

    sport_car = SportCar(180, 'yellow', 'Ferrari')
    print(f'Автомобиль: {sport_car.name}, цвет: {sport_car.color}')
    sport_car.go()
    sport_car.show_speed()
    sport_car.turn('направо')
    sport_car.stop()
    print()

    work_car = WorkCar(50, 'yellow', 'Bus')
    print(f'Автомобиль: {work_car.name}, цвет: {work_car.color}')
    work_car.go()
    work_car.show_speed()
    work_car.turn('направо')
    work_car.stop()
    print()

    police_car = PoliceCar(90, 'black', 'Patriot')
    print(f'Автомобиль: {police_car.name}, цвет: {police_car.color}')
    police_car.go()
    police_car.show_speed()
    police_car.turn('направо')
    police_car.stop()
    print()

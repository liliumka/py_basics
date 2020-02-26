"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = None

    def running(self):
        while True:
            self.next_color()
            self.show_color()
            self.color_timing()

    def next_color(self):
        if self.__color == 'зеленый' or not self.__color:
            self.__color = 'красный'
        elif self.__color == 'красный':
            self.__color = 'желтый'
        elif self.__color == 'желтый':
            self.__color = 'зеленый'

    def show_color(self):
        print(f'цвет {self.__color.upper()}')

    def color_timing(self):
        if self.__color == 'красный':
            self._countdown(7)
        elif self.__color == 'желтый':
            self._countdown(3)
        elif self.__color == 'зеленый':
            self._countdown(5)

    def _countdown(self, sec):
        for s in range(-sec, 0):
            print(abs(s))
            sleep(1)


if __name__ == '__main__':
    lighter = TrafficLight()
    lighter.running()

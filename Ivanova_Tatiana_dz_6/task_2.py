"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.

Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_mass(self, weight=25, height=1):
        """ Результат возвращаем строкой в тоннах """
        return f'{(self._length * self._width * weight * height / 1000):.00f} т'


if __name__ == '__main__':
    this_road = Road(5000, 20)
    print(this_road.get_mass())
    print(this_road.get_mass(25, 5))

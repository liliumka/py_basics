"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    title = 'пишущий инструмент'

    def __str__(self):
        return f'Мы взяли {self.title}'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    title = 'ручку'

    def draw(self):
        print('Пишем заметки в тетради')


class Pencil(Stationery):
    title = 'карандаш'

    def draw(self):
        print('Рисуем рисунок')


class Handle(Stationery):
    title = 'маркер'

    def draw(self):
        print('Отмечаем важные места в заметках')


if __name__ == '__main__':
    pen = Pen()
    print(pen)
    pen.draw()
    print()

    pencil = Pencil()
    print(pencil)
    pencil.draw()
    print()

    handle = Handle()
    print(handle)
    handle.draw()
    print()

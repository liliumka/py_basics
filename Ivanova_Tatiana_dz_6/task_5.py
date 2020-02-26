"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f'Мы взяли {self.title}'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Пишем заметки в тетради')


class Pencil(Stationery):
    def draw(self):
        print('Рисуем рисунок')


class Handle(Stationery):
    def draw(self):
        print('Отмечаем важные места в заметках')


if __name__ == '__main__':
    pen = Pen('ручку')
    print(pen)
    pen.draw()
    print()

    pencil = Pencil('карандаш')
    print(pencil)
    pencil.draw()
    print()

    handle = Handle('маркер')
    print(handle)
    handle.draw()
    print()

"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.

К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    _item_type = 'одежда'

    def __init__(self, size_param, title=''):
        self.title = title
        self.size_param = size_param

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = str(value)

    @property
    def size_param(self):
        return self._size_param

    @size_param.setter
    def size_param(self, value):
        if isinstance(value, int):
            self._size_param = int(value)
        elif isinstance(value, float):
            self._size_param = float(value)
        else:
            raise ValueError('ERROR!!! Параметр размера необходимо указывать числом!')

    @abstractmethod
    def calc_material(self):
        pass

    @staticmethod
    def total_sum_material(*args):
        return sum(map(lambda obj: obj.calc_material(), args))

    def __str__(self):
        title = f' "{self.title}"' if self.title else ''
        return f'Это {self._item_type}{title}'


class Coat(Clothes):
    _item_type = 'пальто'

    def __str__(self):
        parent_str = super().__str__()
        return f'{parent_str}, размер: {self.size_param}'

    def calc_material(self):
        return round(self.size_param / 6.5 + 0.5, 2)


class Suit(Clothes):
    _item_type = 'костюм'

    def __str__(self):
        parent_str = super().__str__()
        return f'{parent_str}, ростовка: {self.size_param} м'

    def calc_material(self):
        return round(2 * self.size_param + 0.3, 2)


if __name__ == '__main__':
    coat_1 = Coat(36, 'Baldinini')  # будем считать что у нас немецкая размерная сетка и для пальто нужна подкладка, подстежка...
    print(coat_1)
    print(coat_1.calc_material())
    print('-' * 80)

    suit_1 = Suit(1.75, 'Calvin Klein')  # рост указываем в метрах
    print(suit_1)
    print(suit_1.calc_material())
    print('-' * 80)

    # общее кол-во материала для изготовления пальто и костюма
    print('Ателье "ВЕСЕЛЫЕ ПОРТНЫЕ"')
    total_sum_material = Clothes.total_sum_material(coat_1, suit_1)
    print(f'Для пошива пальто и костюма нам понадобится {total_sum_material} метров ткани')

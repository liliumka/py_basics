"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

    31 22
    37 43
    51 86

    3 5 32
    2 4 6
    -1 64 -8

    3 5 8 3
    8 3 7 1

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц)
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""
from copy import deepcopy


class Matrix(object):
    def __init__(self, data):
        self._data = data
        self.__max_el_len = 0
        self.check_format_data()

    def __str__(self):
        result = []
        for row in self._data:
            # ровные ячейки получаются за счет форматирования
            # {self.__max_el_len}d позволяет каждой ячейке быть одинаковой ширины
            str_row = ' | '.join(map(lambda el: f'{el:{self.__max_el_len}d}', row))
            result.append(f'| {str_row} |')
        return '\n'.join(result)

    def __add__(self, other):
        if not self.is_equal_matrix(other):
            raise TypeError('Ошибка! Нельзя складывать матрицы разных размеров!')
        else:
            result = [list(map(sum, zip(row_s, row_o))) for row_s, row_o in zip(self._data, other._data)]
            return Matrix(result)

    def is_equal_matrix(self, other):
        return len(self._data) == len(other._data) and len(self._data[0]) == len(other._data[0])

    def check_format_data(self):
        equal_len = None
        if self._data and isinstance(self._data, list):
            for row in self._data:
                if row and isinstance(row, list):
                    # сработает только один раз, получаем длину первой строки
                    # и проверяем по ней эквивалентность размера других строк
                    if equal_len is None:
                        equal_len = len(row)
                    if len(row) == equal_len:
                        for el in row:
                            el_len = len(str(el))
                            # здесь нахожу самое длинное по кол-ву знаков число для того,
                            # чтобы потом сделать красивый вывод в __str__
                            if el_len > self.__max_el_len:
                                self.__max_el_len = el_len
                    else:
                        raise ValueError('Ошибка! Кол-во элементов в каждой строке матрицы должно быть одинаково!')
                else:
                    raise TypeError('Ошибка! Вы не передали матрицу!')
        else:
            raise TypeError('Ошибка! Вы не передали матрицу!')


if __name__ == '__main__':
    matrix_1 = Matrix([
        [2, 2, 2],
        [2, 2, 2],
        [2, 2, 2],
    ])
    print(matrix_1)
    print('-' * 80)

    matrix_2 = Matrix([
        [3, 3, 3],
        [3, 3, 3],
        [3, 3, 3],
    ])
    print(matrix_2)
    print('-' * 80)

    matrix_3 = Matrix([
        [5, 5, 5],
        [5, 5, 5],
        [5, 5, 5],
    ])
    print(matrix_3)
    print('-' * 80)

    print('СУММА МАТРИЦ:')
    print('-' * 80)
    print(matrix_1 + matrix_2 + matrix_3)

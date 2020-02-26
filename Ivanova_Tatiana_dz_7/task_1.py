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
        self.data = data
        self.__max_el_len = 0
        self.check_format_data()

    def __str__(self):
        result = []
        for row in self.data:
            # ровные ячейки получаются за счет форматирования
            # {self.__max_el_len}d позволяет каждой ячейке быть одинаковой ширины
            str_row = ' | '.join(map(lambda el: f'{el:{self.__max_el_len}d}', row))
            result.append(f'| {str_row} |')
        return '\n'.join(result)

    # самый простой вывод матрицы БЕЗ форматирования и выравнивания элементов в зависимости от "длины" чисел
    # def __str__(self):
    #     result = []
    #     for row in self.data:
    #         result.append(' '.join(map(str, row)))
    #     return '\n'.join(result)

    def __add__(self, other):
        rows_self = len(self.data)
        rows_other = len(other.data)

        # в new_data мне нужна матрица с большим кол-вом строк
        # (DEEPCOPY подзволит оставить нетронутыми исходные матрицы)
        new_data, ex_data = deepcopy(self.data), deepcopy(other.data)
        if rows_self <= rows_other:
            new_data, ex_data = ex_data, new_data

        # далее из двух матриц получаю максимальное кол-во элементов в строке
        # для дополнения строк результирующей матрицы до нужной длины
        max_el_rows = len(new_data[0]) if len(new_data[0]) >= len(ex_data[0]) else len(ex_data[0])

        # пакую суммируемые матрицы, при этом каждый элемент будет являться парой строк из двух матриц
        group_data = zip(new_data, ex_data)

        # далее я прохожу по матрице, которую буду возвращать, и меняю в ней строки на суммы строк
        for idx, row in enumerate(new_data):
            try:
                row_1, row_2 = next(group_data)
                # определяю самую длинную строку из пары
                biggest_row = row_1 if len(row_1) >= len(row_2) else row_2
                # получаю длину короткой
                small_len = len(row_1) if len(row_1) < len(row_2) else len(row_2)
                # в первой части суммирую элементы строк, имеющие пару в другой строке, потом добавляю элементы,
                # оставшиеся без пары
                sum_rows = [x + y for x, y in zip(row_1, row_2)] + biggest_row[small_len:]
                # перезаписываю строку
                new_data[idx] = sum_rows
            except StopIteration as e:
                # если у меня матрицы имеют разное кол-во строк, то мы попадем сюда
                # и будем дополнять строки без пары до нужной длины при необходимости
                while len(row) < max_el_rows:
                    row.append(0)
                # перезаписываю строку
                new_data[idx] = row
        return Matrix(new_data)

    def check_format_data(self):
        equal_len = None
        if self.data and isinstance(self.data, list):
            for row in self.data:
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
    # todo: поочередно раскомментируйте easy_test, чтобы провести разные тесты с матрицами. \
    #  Если не указывать отработает простой пример с матрицами 3х3
    # easy_test = 'easy'
    easy_test = 'different size simple'
    # easy_test = 'different size'

    if easy_test == 'easy':
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

    elif easy_test == 'different size simple':
        matrix_1 = Matrix([
            [5, 5],
            [5, 5],
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
            [2, 2, 2, 2],
            [2, 2, 2, 2],
            [2, 2, 2, 2],
            [2, 2, 2, 2],
        ])
        print(matrix_3)
        print('-' * 80)

    elif easy_test == 'different size':
        matrix_1 = Matrix([
            [31, 22],
            [37, 43],
            [51, 86]
        ])
        print(matrix_1)
        print('-' * 80)

        matrix_2 = Matrix([
            [3, 5, 32],
            [2, 4, 6],
            [-1, 6450, -8]
        ])
        print(matrix_2)
        print('-' * 80)

        matrix_3 = Matrix([
            [3, 5, 8, 3],
            [8, 3, 7, 1],
        ])
        print(matrix_3)
        print('-' * 80)

    print('СУММА МАТРИЦ:')
    print('-' * 80)
    print(matrix_1 + matrix_2 + matrix_3)

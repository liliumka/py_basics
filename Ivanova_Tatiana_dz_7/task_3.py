"""
3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
целочисленное (с округлением до целого) деление клеток, соответственно.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
больше нуля, иначе выводить соответствующее сообщение.

Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется
как произведение количества ячеек этих двух клеток.

Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется
как целочисленное деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
"""


class Cage:
    def __init__(self, count_cell):
        self.count_cell = count_cell

    @property
    def count_cell(self):
        if not isinstance(self._count_cell, int):
            raise ValueError('ERROR!!! Внимание, нарушена целостность данных!')
        else:
            return self._count_cell

    @count_cell.setter
    def count_cell(self, value):
        try:
            int(value)
        except ValueError:
            print('ERROR!!! Кол-во ячеек должно быть числом!')
        else:
            self._count_cell = int(value)

    def __str__(self):
        return f'Ячеек в клетке: {self.count_cell}'

    def __add__(self, other):
        sum_cell = self.count_cell + other.count_cell
        return Cage(sum_cell)

    def __sub__(self, other):
        sub_cell = self.count_cell - other.count_cell
        if sub_cell > 0:
            return Cage(sub_cell)
        else:
            return 'Разность кол-ва ячеек клеток равна нулю, либо имеет отрицательное значение!'

    def __mul__(self, other):
        mul_cell = self.count_cell * other.count_cell
        return Cage(mul_cell)

    def __truediv__(self, other):
        try:
            div_cell = self.count_cell // other.count_cell
        except ZeroDivisionError:
            print('Ошбика! На ноль делить нельзя!')
        else:
            return Cage(div_cell)

    def make_order(self, count_cell_in_rows):
        try:
            int(count_cell_in_rows)
        except ValueError:
            print('ERROR!!! Кол-во ячеек в ряду должно быть числом!')
        else:
            count_cell_in_rows = int(count_cell_in_rows)

            count_rows = self.count_cell // count_cell_in_rows
            count_remainder = self.count_cell % count_cell_in_rows
            result = []
            for row in range(count_rows):
                result.append('*' * count_cell_in_rows)
            if count_remainder:
                result.append('*' * count_remainder)
            return '\n'.join(result)


if __name__ == '__main__':
    cage_1 = Cage(12)
    print(cage_1)
    print(cage_1.make_order(5))
    print('-' * 80)

    cage_2 = Cage('50')
    print(cage_2)
    print(type(cage_2.count_cell))  # мы передали строковое значение кол-ва ячеек, а сеттер делает его числом
    print(cage_2.make_order(25))
    print('-' * 80)

    cage_3 = Cage(25.5)
    print(cage_3)
    print(type(cage_3.count_cell))  # вещественные числа также преобразуются к целому числу
    print('-' * 80)

    print(f'Сложение: {cage_1 + cage_2 + cage_3}')
    print(f'Разность: {cage_1 - cage_2}')
    print(f'Умножение: {cage_1 * cage_2}')
    print(f'Деление: {cage_1 / cage_2}')
    print('-' * 80)

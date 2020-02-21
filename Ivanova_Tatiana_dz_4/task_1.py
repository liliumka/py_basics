"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
# todo: посмотреть модуль argparse
import sys

'''
- полный набор параметров - 4 шт.: название_файла число_выработка число_часы число_премия
- для безопасной распаковки аргументов в переменные, дополняю последовательность нулями, 
отбросив первый элемент (range(1, 4)), хранящий название файла
- преобразую элементы последовательности в числа и либо ловлю исключение, либо выдаю расчет
'''
try:
    work_time, cost_by_time, bonus = map(int, (sys.argv[a] if len(sys.argv) > a else 0 for a in range(1, 4)))
except ValueError as e:
    print('Параметры для расчета заработной платы должны быть числами')
else:
    print(work_time * cost_by_time + bonus)
print()


# Другое решение:
def salary(hours, rate, reward=0):
    return hours * rate + reward


try:
    print(f'Salary is: {salary(*map(int, sys.argv[1:4]))}')
except TypeError:
    print('Not enough argument')
except ValueError:
    print('Wrong argument')

"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
import sys

command = sys.argv

if len(command) >= 3:
    try:
        work_time, cost_by_time = map(int, command[1:3])
    except ValueError as e:
        print('Параметры для расчета заработной платы должны быть числами')
    else:
        try:
            bonus = 0
            if len(command) > 3:
                bonus = int(command[3])
        except ValueError as e:
            print('Укажите премию числом')
        else:
            print(work_time * cost_by_time + bonus)

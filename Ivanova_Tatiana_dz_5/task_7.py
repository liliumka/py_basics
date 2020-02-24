"""
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать
данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка:
    [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
    [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджер контекста.
"""
import json

try:
    with open('text_7.txt', 'r', encoding='utf-8') as f_firms, \
            open('firms.json', 'w', encoding='utf-8') as f_json:
        total_profit = []
        result = []
        for row in f_firms:
            firm_name, firm_type, revenue, costs = row.strip().split()
            profit = int(revenue) - int(costs)
            result.append({firm_name: profit})
            if profit > 0:
                total_profit.append(profit)
        result.append({'average_profit': round(sum(total_profit) / len(total_profit), 2)})
        print(result)
        # записываем полученный результат в файл с помощью модуля json
        # json.dump(result, f_json)
except FileNotFoundError as e:
    print(f'no file: {e}')
except Exception as e:
    print(f'strange error: {e}')

"""
6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь
с параметрами (характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
    [
        (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
        (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
        (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
    ]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
например название, а значение — список значений-характеристик, например список названий товаров.
Пример:
    {
        “название”: [“компьютер”, “принтер”, “сканер”],
        “цена”: [20000, 6000, 2000],
        “количество”: [5, 2, 7],
        “ед”: [“шт.”]
    }
"""

# Ввод данных пользователем
# data = []
# temp = {
#     "название": "Введите название товара: ",
#     "цена": "Укажите цену: ",
#     "количество": "Количество: ",
#     "eд": "Единица измерения: "
# }
# n = 1
# print("[!] Чтобы закончить ввод данных, нажмите Enter без ввода данных.")
# while True:
#     item = {}
#     correct = True
#     print(f'Товар #{n}')
#     for key, msg in temp.items():
#         user_input = input(msg)
#         if not user_input:
#             correct = False
#             break
#         else:
#             if key in ["цена", "количество"]:
#                 user_input = int(user_input)
#         item.setdefault(key, user_input)
#     if correct:
#         data.append((n, item))
#         n += 1
#     else:
#         break

data = [
    (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
    (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
    (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."}),
    (4, {"название": "монитор", "цена": 10000, "количество": 4, "eд": "шт."}),
]
# print(*data, sep='\n')

# Варинат 1 ++
data = dict(data)
stat_data = {}
for item in data.values():
    for key, val in item.items():
        stat_data.setdefault(key, []).append(val)
print(stat_data)


# Вариант 2
# new_data = list(zip(*data))
# new_data = new_data.pop(1)
# stat_data = {}
# for item in zip(*[el.items() for el in new_data]):
#     zipped_item = list(zip(*item))
#     key = set(zipped_item[0]).pop()
#     val = list(zipped_item[1])
#     stat_data.setdefault(key, val)
# print(stat_data)


# Вариант 3
# data = dict(data).values()
# pack = [el.items() for el in data]
# pack_by_type = zip(*pack)
# stat_data = {}
# for item in pack_by_type:
#     key, val = zip(*item)
#     stat_data.setdefault(set(key).pop(), list(val))
# print(stat_data)

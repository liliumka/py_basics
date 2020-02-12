"""
1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""

data = [1, 2.5, 'hi', b'go', True, None, [3, 5], (9, 0), {'a', 'b'}, {'one': 1, 'two': 2}]
for el in data:
    # if isinstance(el, str):
    #     pass
    # elif isinstance(el, tuple):
    #     pass
    # ...

    if type(el) == str:
        print(f'{el} is {str}')
    elif type(el) == int:
        print(f'{el} is {int}')
    elif type(el) == float:
        print(f'{el} is {float}')
    elif type(el) == bool:
        print(f'{el} is {bool}')
    # ...
    else:
        print(f'{el} is {type(el)}')

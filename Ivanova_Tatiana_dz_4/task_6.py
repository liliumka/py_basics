"""
6. Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
"""
from Ivanova_Tatiana_dz_4.my_tools import my_range, my_cycle

for n in my_range(5):
    print(n)

print()
for n in my_range(3, 9):
    print(n)

print()
for n in my_cycle('Hello!', 2):
    print(n)

print()
some_list = [50, 100]
amount = len(some_list)
for n in my_cycle(some_list, amount * 3):
    print(n)

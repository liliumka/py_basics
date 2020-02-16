"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


# Вариант 1
def my_summ_2_max(a, b, c):
    """
    Возвращает сумму наибольших двух аргументов.

    :param int|float a: число
    :param int|float b: число
    :param int|float c: число
    :return:
    """
    data = list(vars().values())  # data = [a, b, c]
    data.remove(min(data))
    return sum(data)


print(my_summ_2_max(5, 10, 5))
print(my_summ_2_max(1, 2, 3))
print('-' * 80)


# Вариант 2
def my_summ_2_max_f(a, b, c):
    """
    Возвращает сумму наибольших двух параметров, при условии что все параметры различны.

    Исключения:

    Вернет 0, если все параметры равны.

    Если два параметра будут соответствовать минимальному значению, то будет возвращено значение максимального.

    :param int|float a: число
    :param int|float b: число
    :param int|float c: число
    :return:
    """
    data = [a, b, c]
    return sum(filter(lambda x: x > min(data), data))


print(my_summ_2_max_f(5, 10, 15))
print(my_summ_2_max_f(5, 5, 5))
print(my_summ_2_max_f(5, 5, 20))


# Вариант 3
def my_summ_args(*args):
    if len(args) > 3:
        raise TypeError('my_summ_args() takes max 3 positional arguments but 4 were given')
    return sum(args) - min(args)


try:
    print(my_summ_args(5, 10, 15))
except TypeError as e:
    print(e)

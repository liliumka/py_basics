def my_range(start_n, end_n=0):
    """
    Генератор на основе итератора count.

    Отсчет начинается с переданного параметра start_n. Если указан второй параметр end_n (> start_n),
    то выполняется end_n итераций цикла, иначе только 10.

    :param int start_n:
    :param int end_n:
    :return:
    """
    from itertools import count

    if not end_n > start_n:
        end_n = start_n + 10
    for el in count(start_n):
        if el > end_n:
            break
        yield el


def my_cycle(data, amount=0):
    """
    Генератор на основе итератора cycle.

    На каждой итерации выдает элемент последовательности data бесконечно, повторяя сначала, когда закончился перебор.
    Для выхода из цикла используется параметр amount. Если он не задан, срабатывает ограничение в 10 итераций.

    :param str|list|tuple|set data:
    :param int amount:
    :return:
    """
    from itertools import cycle

    if not amount > 0:
        amount = 10
    c = 0
    for el in cycle(data):
        c += 1
        if c > amount:
            break
        yield el


if __name__ == '__main__':
    for n in my_range(3):
        print(n)

    print()
    for n in my_range(3, 9):
        print(n)

    print()
    for n in my_cycle('Hello!', 5):
        print(n)

    print()
    for n in my_cycle([50, 100], 2):
        print(n)

"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
# number = int(input('Введите целое положительное число: '))
number = 1235742
print(f'Вы ввели число: {number}')

max_n = 0
while number:
    # на каждой итерации получаем целочисленный остаток от деления на 10,
    # по сути это будет перебор всех цифр числа справа налево
    n = number % 10

    # промежуточная распечатка числа и его крайней правой цифры
    # print(number, n)

    # у самого числа постепенно убираем разряды
    number = int((number - n) / 10)

    # а здесь каждый раз проверяем максимальную цифру
    max_n = n if max_n < n else max_n

print(f'Самая большая цифра в вашем числе: {max_n}')

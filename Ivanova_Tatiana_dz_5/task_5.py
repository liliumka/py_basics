"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from random import randint

str_of_nums = ' '.join(map(str, (randint(1, 50) for _ in range(20))))

try:
    with open('text_5.txt', 'w+', encoding='utf-8') as f:
        print(f'Запишем в файл строку чисел: {str_of_nums}')
        f.write(str_of_nums)
        sum_nums = sum(map(int, str_of_nums.split()))
        print(f'Сумма всех чисел: {sum_nums}')
except Exception as e:
    print(f'strange error: {e}')

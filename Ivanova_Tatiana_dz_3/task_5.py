"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом
и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
к полученной ранее сумме и после этого завершить программу.
"""

# Вариант 1
total_sum = 0
in_process = True
print('Для завершения ввода введите символ "q"')
while in_process:
    nums = input('Введите числа, разделяя их пробелами: ').split()

    if 'q' in nums:
        in_process = False
        nums = nums[:nums.index('q')]

    nums = map(int, nums)
    total_sum += sum(nums)

    print(f'Общая сумма: {total_sum}')

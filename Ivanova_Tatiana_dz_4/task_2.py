"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
"""
from random import randint

nums = [randint(1, 50) for _ in range(20)]
result = [b for a, b in zip(nums, nums[1:]) if a < b]

print(nums)
print(result)
print()


# Другие примеры: интересный вариант с генератором
gen_nums = (el for el in nums)
result = [el for el in nums[1:] if el > next(gen_nums)]
print(nums)
print(result)
print()


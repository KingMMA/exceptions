"""
Помилки (номери рядків через пробіл, цей рядок - №2): 9-14!!!
"""


def non_negatives(nums):
    """Удалить из списка чисел 'nums' отрицательные элементы и вернуть
    измененный список."""
    new_nums = []
    for i in nums:
        if not (i < 0):
            new_nums.append(i)

    return new_nums

import random
n = 10
nums = [round(random.uniform(-10, 10), 2) for i in range(n)]
print(nums)
print(non_negatives(nums))
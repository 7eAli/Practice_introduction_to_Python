# Задача 3. Задайте квадратную матрицу, состоящую
# из случайных чисел. Найдите самый часто
# встречающийся элемент в этой матрице.

import numpy as np

size = (10, 10)
numbers = np.random.randint(1, 10, size)
print(numbers)

uniq_list, uniq_counts = np.unique(numbers, return_counts=True)
print(f'Уникальные элементы             {uniq_list}')
print(f'Количество уникальных элементов {uniq_counts}')
print(f'Самый часто встречающийся элемент {uniq_list[np.argmax(uniq_counts)]}')
# Задача 2. Дан массив случайных чисел. Создайте
# его с помощью NumPy. Определите его среднее
# арифметическое.
# На ввод подаётся число. Определите ближайший по
# значению к нему элемент массива.
# [1.2, 4.2, 5.6, 7.1] -> 4.525
# 6.1 -> 5.6

import numpy as np

size = 10
numbers = np.random.randint(10, 100, size)
print(numbers, type(numbers))

average = np.mean(numbers)
print(f'Среднее арифметическое {average}')

number = int(input("\nВведите число: "))
dist = [abs(el - number) for el in numbers]
print(f'дистанции {dist}')
print(f'минимальное расстояние {np.min(dist)}')
print(f'индекс минимального расстояния {dist.index(min(dist))}')
print(f'ближайший элемент к введенному {numbers[dist.index(min(dist))]}')
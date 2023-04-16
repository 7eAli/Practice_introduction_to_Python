# Задача 0. Создайте кортеж. Запишите в него 10
# случайных чисел.
import random

numbers = tuple(
                random.randint(1, 10) 
                                    for i in range(10))

print(numbers)
print(type(numbers))
print(numbers[0])

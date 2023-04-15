# Задача 0. Дан список, заполненный случайными
# числами от 0 до 10. Определите, является ли сумма
# всех элементов чётной.

import random

length = 10
numbers = list(random.randint(0, 10) for el in range(length))
sum = 0

for index in range(length):
    sum += numbers[index]

print(numbers)
print(set(numbers))
print(sum)
if sum % 2 == 0:
    print("Сумма элементов четная")
else:
    print("Сумма элементов нечетная")
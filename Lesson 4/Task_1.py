# Создайте кортеж, заполненный случайными числами.
# Напишите метод, который заменяет элемент в
# кортеже по заданному индексу другим случайным
# числом.

import random

def Change_elements(Array):
    index = int(input("Введите номер элемента для изменения: "))
    Array = list(Array)
    print(Array)
    Array[index] = random.randint(1, 10)
    Array = tuple(Array)
    return Array

def Change_elements_different(Array):
    index = int(input("Введите номер элемента для изменения: "))    
    Array = Array[:index] + (random.randint(1, 10),) + Array[index + 1:]
    return Array



numbers = tuple(
                random.randint(1, 10) 
                                    for _ in range(10))
print(numbers)
numbers = Change_elements_different(numbers)
print(numbers)
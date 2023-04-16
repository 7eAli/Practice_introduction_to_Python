# Сгенерируйте список случайных чисел от 1 до 20,
# состоящий из 10 элементов. Удалите из списка
# дубликаты уже имеющихся элементов. Определите,
# сколько элементов было удалено.

import random

numbers = [random.randint(1, 20) for _ in range(10)]
print(numbers)
new_numbers = set(numbers)
print(new_numbers)
print(f"Удалено {len(numbers) - len(new_numbers)} элементов")
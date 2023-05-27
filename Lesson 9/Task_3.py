# Задача 4. Дан двумерный массив, заполненный
# нулями и единицами. Определите, есть ли в нём
# нулевые столбцы.

import numpy as np

size = (3, 6)

numbers = np.random.randint(0, 2, size)
print(numbers)

result = ~numbers.any(axis=0)
if True in result:
    print("Есть")
else:
    print("Нет")
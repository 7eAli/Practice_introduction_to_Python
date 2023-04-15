# Задача 1. В списке хранятся сведения о количестве
# осадков, выпавших за каждый день июня.
# Определите в какой период выпало больше осадков:
# в первой или второй половине июня.
# Примечание: список заполняется
# случайными числами от 0 до 25.

import random

rain = list(random.randint(0, 25) for i in range(1, 31))
sum_first_half = 0
sum_second_half = 0

for day in range(1, 16):
    sum_first_half += rain[day]
    sum_second_half += rain[int(len(rain)) - day]
if sum_first_half > sum_second_half:
    print("В первой половине месяца выпало больше осадков")
else:
    print("Во второй половине месяца выпало больше осадков")
print(sum_first_half)
print(sum_second_half)
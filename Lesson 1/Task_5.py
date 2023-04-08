# Напишите программу, которая находит наибольшее и
# наименьшее число из списка значений

numbers = [1, 6, 9, 10, -3, -4, 5]
max = numbers[0]
min = numbers[1]
print(numbers)
for i in range(2, len(numbers)):
    if numbers[i] > max:
        max = numbers[i]
    elif numbers[i] < min:
        min = numbers[i]

print(f"max = {max}")
print(f"min = {min}")
# Задача 3. Напишите скрипт генератора паролей
# заданной длины, состоящих из латинских букв и
# чисел.

import random

symbols = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F',
           'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K','l', 'L', 'm', 'M',
           'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T',
           'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z', 0, 1, 2, 3,
           4, 5, 6, 7, 8, 9]

# symbols = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789'


pass_length = int(input("Введите длину пароля: "))
password = list(symbols[random.randint(0, len(symbols))] for i in range(pass_length))
for i in range(0, pass_length - 1):
    print(f"{password[i]}", end='')

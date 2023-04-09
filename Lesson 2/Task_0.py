# Дано число N. Найти все его делители. Для
# каждого делителя укажите чётный он или нечётный.

number = int(
            input("Введите число: "))

for i in range(1, number + 1):
    if number % i == 0:
        if i % 2 == 0:
            if i != number:
                print(f"{i}, четный", end="; ")
            else:
                print(f"{i}, четный")
        else:
            if i != number:
                print(f"{i}, нечетный", end="; ")
            else:
                print(f"{i}, нечетный.")
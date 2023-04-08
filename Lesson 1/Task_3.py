# Напишите программу, которая будет на вход
# принимать число N и выводить числа от -N до N

number = int(input('Введите число: '))
if number > 0:
    for i in range(-number, number + 1):
        if i == number:
            print(i)
        else:
            print(f"{i}", end=', ')
else:
    for i in range(-number, number - 1, -1):
        if i == number:
            print(i)
        else:
            print(f"{i}", end=', ')

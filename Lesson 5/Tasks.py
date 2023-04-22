from Module import *
import random

# Задача 0. С помощью анонимной функции найдите в списке на 15 элементов числа, кратные 5. 
# Заполните список случайным образом числами от 1 до 100.
def Task_0():
    print()
    numbers = [random.randint(1, 100) for i in range(15)]
    print(numbers)
    numbers = list(
                    filter(
                            lambda x: x % 5 == 0, numbers))
    print(numbers)

# Задача 1. На вход подаётся четырёхзначное число. 
# Получите список, состоящий из цифр данного числа, увеличенных на 10.
def Task_1():
    print()
    number = input("Введите четырехзначное число: ")
    if len(number) != 4:
        print("Вы ввели неправильное число")
    else:
        digits = list(
                      map(
                          lambda x: int(x) + 10, number))
        print(digits)

# Задача 2. В зоопарк отправили отчёт о новом поступлении
# зверей с ошибкой, в результате которой некоторые данные не
# расшифровались. Расшифруйте данные. Определите, в какой
# клетке находится лев. Номер клетки совпадает с номером
# строки.
def Task_2():
    print()
    cyphered_animals = ['010100001100001001010011001011000000',
                        '000001011100001011',
                        '001011001111010011',
                        '010010010011001111010001001111000111',
                        '001100000101000010',
                        '001011010001001111001100001001001011',
                        '001101010100001100',
                        '000001000000010001010010010100001011',
                        '000011000101010000000000010001000100',
                        '010010001111001101',
                        '010010001111000001000000001011000000',
                        '011000001001000111']
    letters = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
    letters = list(letters)
    d = {}
    for i in range(len(letters)):
        d[convert_binary(i)] = letters[i]
    print(d)
    result = list(map(lambda x: [d[x[i:i+6]] for i in range(0, len(x), 6)], cyphered_animals))
    result = list(map(lambda x: ''.join(x), result))
    print(result)
    for i in range(0, len(result)):
        if result[i] == 'лев':
            print(i + 1)
    

flag = True
while flag:
    print()
    choice = input("Введите номер задания или нажмите q для выхода: ")
    if choice == "0":
        Task_0()
    elif choice == "1":
        Task_1()
    elif choice == "2":
        Task_2()
    # elif choice == "3":
    #     Task_3()
    # elif choice == "4":
    #     Task_4()
    elif choice == "q":
        flag = False
    else:
        print("Нет такого задания")
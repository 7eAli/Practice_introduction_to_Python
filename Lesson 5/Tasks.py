from Module import *
import random

# Задача 0. С помощью анонимной функции найдите в списке на 15 элементов числа, кратные 5. 
# Заполните список случайным образом числами от 1 до 100.
def Task_0():
    numbers = [random.randint(1, 100) for i in range(15)]
    print(numbers)
    numbers = list(
                    filter(
                            lambda x: x % 5 == 0, numbers))
    print(numbers)

flag = True
while flag:
    print()
    choice = input("Введите номер задания или нажмите q для выхода: ")
    if choice == "0":
        Task_0()
    # elif choice == "1":
    #     Task_1()
    # elif choice == "2":
    #     Task_2()
    # elif choice == "3":
    #     Task_3()
    # elif choice == "4":
    #     Task_4()
    elif choice == "q":
        flag = False
    else:
        print("Нет такого задания")
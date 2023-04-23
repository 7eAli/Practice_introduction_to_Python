import random

# Задача 1. Дан список случайных элементов.
# Проверьте, что все его элементы уникальны.
def Task_1():
    numbers = [random.randint(1, 100) for i in range(10)]
    check = set(numbers)
    print(numbers)
    if len(numbers) == len(check):
        print("Да")
    else:
        print("Нет")




flag = True
while flag:
    print()
    choice = input("Введите номер задания или нажмите q для выхода: ")
    if choice == "1":
        Task_1()
    elif choice == "2":
        Task_2()
    elif choice == "3":
        Task_3()
    # elif choice == "4":
    #     Task_4()
    elif choice == "q":
        flag = False
    else:
        print("Нет такого задания")
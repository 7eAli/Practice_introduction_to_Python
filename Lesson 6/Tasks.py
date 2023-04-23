import random

def merge_sort(list):
    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1

def Convert_Number(num):
    num = str(num)
    num = list(num)
    print(num)
    result = []
    for i in range(len(num)):
        result.append(int(num[i]))
    return result

def Check_Numbers(num_1, num_2):
    count = 0
    for i in range(len(num_1)):
        if num_1[i] != num_2[i]:
            count += 1
    if count == 0: print("Да")
    else: print("Нет")

    

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

# Задача 2. Даны два случайных пятизначных числа.
# Определить, состоят ли они из одних и тех же цифр.
def Task_2():
    num_1 = random.randint(10000, 99999)
    num_2 = random.randint(10000, 99999)
    num_1_dig = Convert_Number(num_1)
    num_2_dig = Convert_Number(num_2)    
    merge_sort(num_1_dig)
    merge_sort(num_2_dig)
    print(num_1_dig)
    print(num_2_dig)
    Check_Numbers(num_1_dig, num_2_dig)
    


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
    elif choice == "4":
        Task_4()
    elif choice == "q":
        flag = False
    else:
        print("Нет такого задания")
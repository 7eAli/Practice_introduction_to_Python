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

# Задача 3. Напишите программу вычисления арифметического
# выражения заданного строкой. Используйте операции +,-,/,*.
# приоритет операций стандартный.
# а) Решите задачу для одного действия;
# б) Дополнительное задание. Решите задачу для нескольких
# действий;
# в) Решите задачу средствами python.    
def Task_3():
    expression = input("Введите арифметическое выражение: ")
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]    
    result = 0
    numbers = []    
    temp = ''
    for i in range(len(expression)):
        if expression[i] in digits:
            temp += expression[i]
            if i == len(expression) - 1:
                temp = int(temp)
                numbers.append(temp)
                temp = ''
            elif expression[i + 1] not in digits:
                temp = int(temp)
                numbers.append(temp)
                temp = ''
    if '+' in expression:
        result = numbers[0] + numbers[1]
    elif '-' in expression:
        result = numbers[0] - numbers[1]
    elif '*' in expression:
        result = numbers[0] * numbers[1]
    elif '/' in expression:
        result = numbers[0] / numbers[1]
    print(result)
    
            

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
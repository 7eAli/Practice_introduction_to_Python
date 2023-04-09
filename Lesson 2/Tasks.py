# Дано число N. Найти все его делители. Для
# каждого делителя укажите чётный он или нечётный.
def Task_0():
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

# Task_0()


# Выведите таблицу истинности для
# выражения ¬ X ∨ Y.

def Task_1():    
    for x in range(2):
        for y in range(2):
            print(f"{x} {y}", end=" ")
            if not x or y:
                print(1)
            else:
                print(0)

# Task_1()


# Напишите программу, в которой
# пользователь будет задавать две строки, а программа
# - определять количество вхождений одной строки в
# другую.

def Task_2():
    text_1 = input("Введите что-нибудь: ")
    text_2 = input("Введите еще что-нибудь: ")
    count = 0
    for i in text_1:
        if text_1[i: i + len(text_2)] == text_2:
            count += 1
    print(count)


# Task_2()


# Дано число N. Заполните список длиной N
# элементами 1, -3, 9, -27, 81, -243...

def Task_3():
    number = int(
                input("Введите число N: "))
    numbers = [1] * (number + 1)
    for i in range(0, len(numbers)):        
        numbers[i] = (-3) ** i
    print(numbers)

# Task_3()


# Найдите все числа до 10000, у который
# количество делителей равно 10.
def Task_4():
    count = 0
    for i in range(1, 10001):
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
        if count == 10:            
            print(f"{i}\t", end=' ')
        count = 0        

Task_4()
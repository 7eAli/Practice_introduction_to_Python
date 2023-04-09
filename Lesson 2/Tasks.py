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

Task_1()



# Task_2()
# Task_3()
# Task_4()
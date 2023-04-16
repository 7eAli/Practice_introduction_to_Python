# На вход подаются два числа. Напишите метод, который вернёт
# сумму, разность, произведение и частное этих чисел.

def Calculations(num_1, num_2):
    results = {'Сумма': num_1 + num_2, 'Разность': num_1 - num_2, 'Произведение': num_1 * num_2, 'Частное': num_1 / num_2}
    return results

def Calculations_in_tuple(num_1, num_2):
    results = (num_1 + num_2, num_1 - num_2, num_1 * num_2, num_1 / num_2)
    return results

num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))

print(Calculations(num_1, num_2))
print(Calculations_in_tuple(num_1, num_2))
sum, diff, prod, div = Calculations_in_tuple(num_1, num_2)
print(sum, diff, prod, div)
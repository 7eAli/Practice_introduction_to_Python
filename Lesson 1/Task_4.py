# Напишите программу, которая будет принимать на вход дробь
# и показывать первую цифру дробной части числа.

number = float(
                input('Введите дробное число: '))
number *= 10
round(number, 0)
number = int(number)
print(number % 10)


# Задача 3. Создайте декоратор для метода нахождения суммы.

def our_format(func):
    def decorator(*args):
        for arg in args:
            print(f'{arg} + ', end='')      
        print('\b\b= ', end='')      
        func(*args)
    return decorator

@our_format
def sum(a, b):
    print(a + b)

@our_format
def sum_4(a, b, c, d):
    print(a + b + c + d)

sum(3, 51)
sum_4(4, 6, 1, 0)
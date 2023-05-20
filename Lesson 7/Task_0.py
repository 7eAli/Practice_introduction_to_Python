def our_filter(func, numbers):
    return (el for el in numbers if func(el))

numbers = [1, 14, 6, 10, 3, 2, 5]

#print( list(filter(lambda x: x > 5, numbers)))
print( list(our_filter(lambda x: x > 5, numbers)))
# Задача 2. Напишите программу, которая позволит пользователю
# заполнить анкету, последовательно вводя в программу:
# - имя;
# - возраст;
# - хобби;
# - любимое животное.
# После окончания ввода, выводится заполненная анкета.

profile = {'Имя': input("Введите свое имя: "), 
           'Возраст': input("Сколько вам лет? "), 
           'Хобби': input("Чем вы увлекаетесь? "), 
           'Любимое животное': input("Какое у вас любимое животное? ")}

for key, value in profile.items():
    print(f"{key}: {value}")
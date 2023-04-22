

flag = True
while flag:
    print()
    choice = input("Введите номер задания или нажмите q для выхода: ")
    if choice == "0":
        Task_0()
    elif choice == "1":
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
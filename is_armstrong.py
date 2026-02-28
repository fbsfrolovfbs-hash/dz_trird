is_continue = True

while is_continue:
    print("1 - Start\n"
          "4 - exit\n")
    user_choice = input("Enter action number: ")
    if user_choice == '1':
        test1 = input("Enter a number: ")
        if test1.isdigit():
            goal = int(test1)
        else:
            print("Attention, look more closely!")
            exit()
        answer = goal
        lenght = len(str(goal))
        list_of_numbers = []
        sum_of_digits = 0
        for i in range(lenght, 0, -1):
            digit = goal // 10 ** (i - 1)
            list_of_numbers.append(digit)
            goal = goal % (10 ** (i - 1))
        for j in range(0, len(list_of_numbers)):
            sum_of_digits += list_of_numbers[j] ** lenght
        if sum_of_digits == answer:
            print(answer, "is a armstrong number!")
        else:
            print(answer, "is not a armstrong number!")

    elif user_choice == '4':
        is_continue = False
    else:
        print("No such action!")

    print("=" * 50)

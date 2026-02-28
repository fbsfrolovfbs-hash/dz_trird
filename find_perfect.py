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
        for num in range(2, goal + 1):
            sum_of_digits = 0
            for i in range(1, num):
                if num % i == 0:
                    sum_of_digits += i
            if sum_of_digits == num:
                print(num, "is a perfect number!")
    elif user_choice == '4':
        is_continue = False
    else:
        print("No such action!")

    print("=" * 50)

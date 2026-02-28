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
        step = 0
        answer = goal
        while goal != 1:
            if goal % 2 == 0:
                step += 1
                goal /= 2
            else:
                goal *= 3
                goal += 1
                step += 1
        print(f"Step {step}: {answer}")
    elif user_choice == '4':
        is_continue = False
    else:
        print("No such action!")

    print("=" * 50)

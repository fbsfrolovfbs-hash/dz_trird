is_continue = True

while is_continue:
    print("1 - Start\n"
          "4 - exit\n")
    user_choice = input("Enter action number: ")
    if user_choice == '1':
        test1 = input("Enter a goal: ")
        if test1.isdigit():
            goal = int(test1)
        else:
            print("Attention, look more closely!")
            exit()
        test2 = input("Enter how much she can save a day: ")
        if test2.isdigit():
            save_money = int(test2)
        else:
            print("Attention, look more closely!")
            exit()
        savings = 0
        step = 0
        while savings < goal:
            step += 1
            if step % 7 != 0:
                savings += save_money

        print(f"{step} day u need!")
    elif user_choice == '4':
        is_continue = False
    else:
        print("No such action!")

    print("=" * 50)
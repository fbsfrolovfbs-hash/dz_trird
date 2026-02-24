is_continue = True
is_inprogress = True
list_numbers = []
while is_continue:
    print("1 - Start\n"
          "4 - exit\n")
    user_choice = input("Enter action number: ")
    if user_choice == '1':
        while is_inprogress:
            print("1 - append\n"
                  "2 - show list\n"
                  "3 - show max\n"
                  "4 - show min\n"
                  "5 - exit\n")
            user_choice_second = input("Enter action number: ")
            if user_choice_second == '1':
                test1 = input("Which one do you want?")
                if test1.isdigit():
                    append = int(test1)
                else:
                    print("Attention, look more closely!")
                    exit()
                list_numbers.append(append)
            elif user_choice_second == '2':
                print(list_numbers)
            elif user_choice_second == '3':
                print(max(list_numbers))
            elif user_choice_second == '4':
                print(min(list_numbers))
            elif user_choice_second == '5':
                is_inprogress = False
            else:
                print("No such action!")
    elif user_choice == '4':
        is_continue = False
    else:
        print("No such action!")

    print("=" * 50)

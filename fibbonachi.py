is_continue = True

while is_continue:
    print("1 - Start\n"
          "4 - exit\n")
    user_choice = input("Enter action number: ")
    if user_choice == '1':
        test1 = input("Enter a last number: ")
        if test1.isdigit():
            goal = int(test1)
        else:
            print("Attention, look more closely!")
            exit()
        numbers = [1, 1, 2, 3]
        if goal < 3:
            print("Too small!")
            is_continue = False
        while numbers[len(numbers) - 1] < goal:
            numbers.append((numbers[len(numbers) - 1])+numbers[len(numbers) - 2])
        print(f"Result: {numbers}")
    elif user_choice == '4':
        is_continue = False
    else:
        print("No such action!")

    print("=" * 50)

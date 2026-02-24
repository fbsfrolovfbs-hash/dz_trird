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
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        i = 0
        first = 0
        second = len(numbers) - 1
        while i != goal:
            if numbers[0] == goal:
                print(f"Goal: 0")
                break
            elif numbers[second] == goal:
                print(f"Goal: {second}")
                break
            elif numbers[(first + second)//2] == goal:
                i = (first + second) // 2
                print(f"Goal: {i}")
                break
            elif goal < numbers[(first + second)//2]:
                second = (first + second)//2
            else:
                first = (first + second)//2

    elif user_choice == '4':
        is_continue = False
    else:
        print("No such action!")

    print("=" * 50)

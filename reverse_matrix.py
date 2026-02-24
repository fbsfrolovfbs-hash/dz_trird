from random import randint

is_continue = True

while is_continue:
    print("1 - Start\n"
          "4 - exit\n")
    user_choice = input("Enter action number: ")
    if user_choice == '1':
        rows_number = int(input("Enter rows number: "))
        columns_number = int(input("Enter columns number: "))
        matrix = []
        for r_num in range(0, rows_number):
            empty_row = []
            matrix.append(empty_row)
            for c_num in range(0, columns_number):
                elem = randint(0, 100)
                matrix[r_num].append(elem)
            print(matrix[r_num])
        i = columns_number - 1
        summa = 0
        for r_num in range(0, rows_number):
            for c_num in range(0, columns_number):
                if c_num - r_num == i:
                    summa += matrix[r_num][c_num]
                    i -= 2
        print(f"Sum of main diag is: {summa}")

    elif user_choice == '4':
        is_continue = False
    else:
        print("No such action!")

    print("=" * 50)

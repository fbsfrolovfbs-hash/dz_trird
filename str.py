
is_continue = True

while is_continue:
    print("1 - Старт\n"
          "4 - Выход\n")
    user_choice = input("Выберите действие: ")
    if user_choice == '1':
        text = input("Введите строку: ")
        vowels = "аеёиоуыэюяAEЁИОУЫЭЮЯaeiouyAEIOUY"
        vowel_count = 0
        consonant_count = 0
        for char in text:
            if char.isalpha():
                if char in vowels:
                    vowel_count += 1
                else:
                    consonant_count += 1
        print("Гласных букв:", vowel_count)
        print("Согласных букв:", consonant_count)
    elif user_choice == '4':
        is_continue = False
    else:
        print("No such action!")

    print("=" * 50)

def roman_to_int(roman):
    roman_numerals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    roman = roman.upper()
    roman_organize = []

    for letter in roman:
        if letter in roman_numerals:
            roman_organize.append(letter)
        else:
            print("\nIncorrect value, try again.")
            choose()
            return

    roman_organize.reverse()

    result = 0
    prev_value = 0

    for letter in roman_organize:
        current_value = roman_numerals[letter]

        if current_value < prev_value:
            result -= current_value
        else:
            result += current_value
        prev_value = current_value

    print(f"\nhere is your number: {result}")


def int_to_roman(integer):
    print()


def choose():
    print("\n ---------- Roman Numberals Conversion ----------")
    print(" > 1 - Convert an integer to a roman numerals,")
    print(" > 2 - Convert a roman numerals to an integer.")
    option = input("Choose an option (1 or 2): ")
    if option == "1":
        sequence = input("Insert a Roman number to convert: ")
        roman_to_int(sequence)
    elif option == "2":
        sequence == input("insert a number to convert: ")
        int_to_roman(sequence)
    else:
        print("\ncommand invalid. Try it again.\n")
        choose()


choose()

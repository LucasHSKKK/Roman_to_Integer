def roman_to_int(roman):
    roman_numerals = {
        "I": 1,
        "X": 10,
        "C": 100,
        "V": 5,
        "D": 500,
        "M": 1000,
    }
    roman = roman.upper()
    for letter in roman:
        if letter in roman_numerals:
            print("correct")
        else:
            print("Incorrect value, try again.")
            choose()
            break


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
        int_to_roman()
    else:
        print("\ncommand invalid. Try it again.\n")
        choose()


choose()

def roman_to_int():
    roman_numerals = {
        "I": 1,
        "X": 10,
        "C": 100,
        "V": 5,
        "D": 500,
        "M": 1000,
    }
    number_organized = []
    sequence = input("Insert a Roman number to convert: ")
    sequence = sequence.upper()
    for letter in sequence:
        if letter in roman_numerals:
            # need to figure out how i will make this compares values
            number_organized.append(letter)
        else:
            print("Incorrect value, try again.")
            roman_to_int()


def int_to_roman():
    print()


def choose():
    print(" ---------- Roman Numberals Conversion ----------")
    print(" > 1 - Convert an integer to a roman numerals,")
    print(" > 2 - Convert a roman numerals to an integer.")
    option = input("Choose an option (1 or 2): ")
    if option == "1":
        roman_to_int()
    elif option == "2":
        int_to_roman()
    else:
        print("\ncommand invalid. Try it again.\n")
        choose()


choose()

def roman_to_int():
    roman_numerals_less = {
        "I": 1,
        "X": 10,
        "C": 100,
    }
    roman_numerals_normal = {
        "V": 5,
        "D": 500,
        "M": 1000,
    }
    number_organized = {}
    sequence = input("Insert a Roman number to convert: ")
    sequence = sequence.upper()
    for letter in sequence:
        # fix this line
        if letter not in roman_numerals_less or not roman_numerals_normal:
            print("Incorrect value, try again.")
            roman_to_int()
        else:
            print("correct")


def int_to_roman():
    print()


def choose():
    print(" ---------- Roman Numberals Conversion ----------")
    print(" > 1 - Convert an integer to a roman numerals,")
    print(" > 2 - Convert a roman numerals to an integer.")
    option = input("Choose an option (1 or 2): ")
    if option == "1":
        roman_to_int()
    else:
        int_to_roman()


choose()

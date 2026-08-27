# sum_difference.py
#
# This program has two functions:
#   1. add_numbers      -> returns first + second
#   2. subtract_numbers -> returns first - second
#
# The main() function calls both and checks them against known answers.


def add_numbers(first, second):
    # Adds two numbers together and returns the result.
    result = first + second
    return result


def subtract_numbers(first, second):
    # Subtracts the second number from the first and returns the result.
    result = first - second
    return result


def main():
    # ---- Part 1: check the functions against the required test cases ----
    print("Checking add_numbers:")
    print("2 + 5 =", add_numbers(2, 5))
    print("37 + 57 =", add_numbers(37, 57))
    print("-19 + 41 =", add_numbers(-19, 41))

    print()
    print("Checking subtract_numbers:")
    print("20 - 7 =", subtract_numbers(20, 7))
    print("8 - 26 =", subtract_numbers(8, 26))
    print("270 - 157 =", subtract_numbers(270, 157))

    # ---- Part 2: CUSTOMIZE HERE ----
    # This is where YOU interact with the program and provide your own
    # numbers, instead of using the hardcoded examples above. Typing your
    # own input and seeing the result live is a simple way to show this
    # is your own work, not just copied test cases.
    print()
    print("Now try your own numbers!")
    first = int(input("Enter the first number: "))
    second = int(input("Enter the second number: "))

    print(f"{first} + {second} = {add_numbers(first, second)}")
    print(f"{first} - {second} = {subtract_numbers(first, second)}")


# This line makes sure main() only runs when you run this file directly.
if __name__ == "__main__":
    main()

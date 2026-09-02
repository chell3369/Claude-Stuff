# sum_difference.py
#
# This program has four functions:
#   1. add_numbers      -> returns first + second
#   2. subtract_numbers -> returns first - second
#   3. multiply_numbers -> returns first * second
#   4. divide_numbers   -> returns first / second


def add_numbers(first, second):
    # Adds two numbers together and returns the result.
    result = first + second
    return result


def subtract_numbers(first, second):
    # Subtracts the second number from the first and returns the result.
    result = first - second
    return result


def multiply_numbers(first, second):
    # Multiplies two numbers together and returns the result.
    result = first * second
    return result


def divide_numbers(first, second):
    # Divides the first number by the second and returns the result.
    # Rejects division by zero instead of letting it crash the program.
    if second == 0:
        raise ValueError("Cannot divide by zero.")
    result = first / second
    return result


def main():
    print("Checking add_numbers:")
    print("2 + 5 =", add_numbers(2, 5))
    print("37 + 57 =", add_numbers(37, 57))
    print("-19 + 41 =", add_numbers(-19, 41))

    print()
    print("Checking subtract_numbers:")
    print("20 - 7 =", subtract_numbers(20, 7))
    print("8 - 26 =", subtract_numbers(8, 26))
    print("270 - 157 =", subtract_numbers(270, 157))

    print()
    print("Checking multiply_numbers:")
    print("3 x 5 =", multiply_numbers(3, 5))
    print("121 x (-4) =", multiply_numbers(121, -4))
    print("389 x 0 =", multiply_numbers(389, 0))

    print()
    print("Checking divide_numbers:")
    print(f"24 / 3 = {divide_numbers(24, 3):g}")
    print(f"224 / (-16) = {divide_numbers(224, -16):g}")
    print(f"88 / 11 = {divide_numbers(88, 11):g}")

    print()
    print("Now try your own numbers!")
    first = int(input("Enter the first number: "))
    second = int(input("Enter the second number: "))

    print(f"{first} + {second} = {add_numbers(first, second)}")
    print(f"{first} - {second} = {subtract_numbers(first, second)}")
    print(f"{first} x {second} = {multiply_numbers(first, second)}")
    try:
        print(f"{first} / {second} = {divide_numbers(first, second):g}")
    except ValueError as error:
        print(f"{first} / {second} = Error: {error}")

if __name__ == "__main__":
    main()

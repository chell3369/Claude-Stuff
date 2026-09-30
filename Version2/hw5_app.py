# hw5_app.py
#
# Homework #5 - application that uses the CyberMath library (cybermath.py).

from cybermath import (
    getLibraryVersion,
    add_numbers,
    subtract_numbers,
    multiply_numbers,
    divide_numbers,
)


def main():
    print("HW 5 using " + getLibraryVersion())

    print()
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

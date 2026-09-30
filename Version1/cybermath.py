# cybermath.py
#
# CyberMath library - calculator functions used by the HW 5 application.


def getLibraryVersion():
    return "CyberMath version 1.0"


def add_numbers(first, second):
    return first + second


def subtract_numbers(first, second):
    return first - second


def multiply_numbers(first, second):
    return first * second


def divide_numbers(first, second):
    if second == 0:
        raise ValueError("Cannot divide by zero.")
    return first / second

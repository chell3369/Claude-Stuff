def add(first, second):
    return first + second


def subtract(first, second):
    return first - second


def main():
    sum_cases = [
        (2, 5, 7),
        (37, 57, 94),
        (-19, 41, 22),
    ]
    difference_cases = [
        (20, 7, 13),
        (8, 26, -18),
        (270, 157, 113),
    ]

    for first, second, expected in sum_cases:
        result = add(first, second)
        status = "PASS" if result == expected else "FAIL"
        print(f"{first} + {second} = {result} (expected {expected}) [{status}]")

    for first, second, expected in difference_cases:
        result = subtract(first, second)
        status = "PASS" if result == expected else "FAIL"
        print(f"{first} - {second} = {result} (expected {expected}) [{status}]")


if __name__ == "__main__":
    main()

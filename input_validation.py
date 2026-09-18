# input_validation.py
#
# Homework #3 - Input Validation
#
# This program has five functions:
#   1. check_zip   -> PASS/FAIL: is the string a valid ZIP code?
#   2. check_sql   -> PASS/FAIL: is the string safe to use in an SQL statement?
#   3. check_web   -> PASS/FAIL: is the string safe to show on a web page?
#   4. check_shell -> PASS/FAIL: is the string safe to run as a shell command?
#   5. main        -> reads a text file and prints the results for every line

import re


def check_zip(text):
    pattern = r"^\d{5}(-\d{4})?$"
    if re.match(pattern, text):
        return "PASS"
    else:
        return "FAIL"


def check_sql(text):
    bad_characters = ["'", '"', "‘", "’", ";", "(", ")", "="]
    for character in text:
        if character in bad_characters:
            return "FAIL"

    if "--" in text:
        return "FAIL"

    bad_words = ["select", "insert", "update", "delete", "drop", "union"]
    lower_text = text.lower()
    for word in bad_words:
        if word in lower_text:
            return "FAIL"

    return "PASS"


def check_web(text):
    bad_characters = ["<", ">", '"', "'", "&"]
    for bad_character in bad_characters:
        if bad_character in text:
            return "FAIL"

    if "javascript:" in text.lower():
        return "FAIL"

    return "PASS"


def check_shell(text):
    bad_characters = [";", "&", "|", "`", "$", "(", ")", "<", ">", "*", "?", '"', "'"]
    index = 0
    while index < len(text):
        if text[index] in bad_characters:
            return "FAIL"
        index = index + 1

    if text.startswith("./") or text.startswith("/"):
        return "FAIL"

    return "PASS"


def main():
    filename = "test_strings.txt"

    try:
        input_file = open(filename, "r")
    except OSError as error:
        print(f"Could not read {filename}: {error}")
        return

    lines = input_file.readlines()
    input_file.close()

    print("*" * 30)
    print("Homework 3 - Input Validation")
    print()
    print(f"{'Line#':<8}{'ZIP':<8}{'SQL':<8}{'Web':<8}{'Shell':<8}{'String'}")

    line_number = 1
    for line in lines:
        text = line.rstrip("\n")

        zip_result = check_zip(text)
        sql_result = check_sql(text)
        web_result = check_web(text)
        shell_result = check_shell(text)

        print(f"{line_number:<8}{zip_result:<8}{sql_result:<8}{web_result:<8}{shell_result:<8}{text}")
        line_number = line_number + 1

    print()
    print("Now try your own string!")
    my_string = input("Enter a string to test: ")
    print("ZIP:  ", check_zip(my_string))
    print("SQL:  ", check_sql(my_string))
    print("Web:  ", check_web(my_string))
    print("Shell:", check_shell(my_string))


if __name__ == "__main__":
    main()

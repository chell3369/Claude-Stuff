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
    # A US ZIP code is 5 digits, or 5 digits, a dash, then 4 more digits.
    pattern = r"^\d{5}(-\d{4})?$"
    if re.match(pattern, text):
        return "PASS"
    else:
        return "FAIL"


def check_sql(text):
    # These characters are used to break out of an SQL statement and add
    # extra commands, so any string containing one of them fails. This
    # includes curly quotes, since Word sometimes autocorrects a plain
    # quote into one.
    bad_characters = ["'", '"', "‘", "’", ";", "(", ")", "="]
    for character in text:
        if character in bad_characters:
            return "FAIL"

    # Two dashes in a row start an SQL comment, which can be used to cut
    # off the rest of a statement.
    if "--" in text:
        return "FAIL"

    # These words are used to build or change an SQL query.
    bad_words = ["select", "insert", "update", "delete", "drop", "union"]
    lower_text = text.lower()
    for word in bad_words:
        if word in lower_text:
            return "FAIL"

    return "PASS"


def check_web(text):
    # These characters let a string close an HTML tag or attribute and
    # start a new one, which is how a script gets injected into a page.
    # This includes curly quotes, since Word sometimes autocorrects a
    # plain quote into one.
    bad_characters = ["<", ">", '"', "'", "&", "‘", "’"]
    for character in text:
        if character in bad_characters:
            return "FAIL"

    # javascript: links run code instead of going to a normal web address.
    if "javascript:" in text.lower():
        return "FAIL"

    return "PASS"


def check_shell(text):
    # These characters let a string chain commands together, redirect
    # output, or run a second command inside the first one. This includes
    # curly quotes, since Word sometimes autocorrects a plain quote into
    # one.
    bad_characters = [";", "&", "|", "`", "$", "(", ")", "<", ">", "*", "?", '"', "'", "‘", "’"]
    for character in text:
        if character in bad_characters:
            return "FAIL"

    # A string that starts with ./ or / is trying to run a specific file.
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
        # readlines() keeps the newline character at the end of each line,
        # so strip it off before testing the string.
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

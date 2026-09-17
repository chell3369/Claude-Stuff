# input_validation.py
#
# Homework #3 - Input Validation
#
# Reads a text file of arbitrary length (one candidate string per line) and
# tests each line against four different validation contexts:
#   ZIP   - well-formed US ZIP or ZIP+4 code
#   SQL   - safe to place into an SQL statement or store in a database
#   Web   - safe to render on a web page without injecting a script
#   Shell - safe to pass to a shell command
#
# Every test uses a whitelist: a string PASSes only if it contains nothing
# but characters known to be safe for that context. Anything else FAILs,
# instead of trying to blacklist every possible attack pattern.

import re
import sys

ZIP_RE = re.compile(r"^\d{5}(-\d{4})?$")

# Only plain letters, digits, spaces, and a few harmless punctuation marks
# are allowed in a SQL value. Quotes, semicolons, parentheses, and comment
# markers are exactly the characters an injection needs to escape the
# intended value, so any of them fails the test.
SQL_SAFE_RE = re.compile(r"^[A-Za-z0-9 ,.@_-]+$")
SQL_KEYWORDS = ("select", "insert", "update", "delete", "drop", "union", "where", "from", "values", "into")

# Characters that let a value break out of HTML/attribute context or start
# a script, plus the javascript: URI scheme used for script injection.
WEB_DANGEROUS_CHARS = set("<>\"'&‘’“”")
WEB_DANGEROUS_SUBSTRINGS = ("javascript:",)

# Shell metacharacters that can chain, redirect, or substitute commands.
SHELL_DANGEROUS_CHARS = set(";&|`$()<>*?[]{}~#!\"'\\‘’“”")


def is_valid_zip(value):
    return bool(ZIP_RE.match(value))


def is_safe_sql(value):
    if not SQL_SAFE_RE.match(value):
        return False
    if "--" in value:
        return False
    lowered = value.lower()
    return not any(re.search(rf"\b{keyword}\b", lowered) for keyword in SQL_KEYWORDS)


def is_safe_web(value):
    if any(ch in WEB_DANGEROUS_CHARS for ch in value):
        return False
    lowered = value.lower()
    return not any(token in lowered for token in WEB_DANGEROUS_SUBSTRINGS)


def is_safe_shell(value):
    if any(ch in SHELL_DANGEROUS_CHARS for ch in value):
        return False
    if value.startswith("./") or value.startswith("../") or value.startswith("/"):
        return False
    return "&&" not in value and "||" not in value


def result(passed):
    return "PASS" if passed else "FAIL"


def run_tests(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = [line.rstrip("\n").rstrip("\r") for line in f]
    except OSError as error:
        print(f"Could not read {filename}: {error}")
        sys.exit(1)

    print("*" * 30)
    print("Homework 3 - Input Validation")
    print()
    print(f"{'Line#':<8}{'ZIP':<8}{'SQL':<8}{'Web':<8}{'Shell':<8}{'String'}")

    for line_number, line in enumerate(lines, start=1):
        zip_result = result(is_valid_zip(line))
        sql_result = result(is_safe_sql(line))
        web_result = result(is_safe_web(line))
        shell_result = result(is_safe_shell(line))
        print(f"{line_number:<8}{zip_result:<8}{sql_result:<8}{web_result:<8}{shell_result:<8}{line}")


def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else "test_strings.txt"
    run_tests(filename)


if __name__ == "__main__":
    main()

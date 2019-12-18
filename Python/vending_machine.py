# Model for a vending machine that has the following items
# Item #1       15
# Item #2       25
# Item #3       30

import re


def accept_tokens(tokens):
    regex = r"[ab]|[[aa|b][a|c]]|[ac]"
    regex_eval = re.findall(regex, tokens)
    return regex_eval


def check_validity(regex_eval):
    total = 0
    for item in regex_eval:
        total += (
            5 if item == "a" else (10 if item == "b" else (20 if item == "c" else 0))
        )
    print(total)
    print("Accepted" if (total == 15 or total == 25 or total == 30) else "Not accepted")


def main():
    tokens = input("[a = 5] [b = 10] [c = 20]\nEnter tokens: ")
    regex_eval = accept_tokens(tokens)
    check_validity(regex_eval)


main()

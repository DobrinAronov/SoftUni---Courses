import re


def find_numbers(some_string: str):
    pattern = r"\d+"
    return re.findall(pattern, some_string)


while True:
    input_string = input()

    if not input_string:
        break

    number = find_numbers(input_string)
    if number:
        print(' '.join(number), end=' ')
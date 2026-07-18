import re


def find_numbers(some_numbers: str):
    pattern = r"\b_[A-Za-z0-9]+\b"
    return re.finditer(pattern, some_numbers)


numbers = input()
matches = find_numbers(numbers)

for match in matches:
    print(match.group(), end=' ')

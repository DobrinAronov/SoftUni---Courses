import re


def find_phone_number(numbers: str) -> list:
    pattern = r"\+359 2 \d{3}\ \d{4}\b|\+359-2-\d{3}\-\d{4}\b"
    return re.findall(pattern, numbers)


phone_numbers = input()

matches = find_phone_number(phone_numbers)
print(', '.join(matches))

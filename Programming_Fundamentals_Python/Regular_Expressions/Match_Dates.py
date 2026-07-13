import re


def find_date(some_date: str):
    pattern = r"([0-3][0-9])([./-])([A-Z][a-z]{2})\2(\d{4})"
    return re.finditer(pattern, some_date)


dates = input()
matches = find_date(dates)

for match in matches:
    day = match.group(1)
    month = match.group(3)
    year = match.group(4)

    print(f"Day: {day}, Month: {month}, Year: {year}")

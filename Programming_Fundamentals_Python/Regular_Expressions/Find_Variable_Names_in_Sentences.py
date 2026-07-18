import re


def find_variable(some_string: str):
    pattern = r"(?<!_)_([A-Za-z0-9]+)\b(?!_)"
    return re.findall(pattern, some_string)


input_string = input()

matches = find_variable(input_string)
print(','.join(matches))

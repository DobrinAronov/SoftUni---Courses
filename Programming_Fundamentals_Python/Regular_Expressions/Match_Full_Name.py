import re


def find_full_name(text: str) -> list:
    patern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
    return re.findall(patern, text)


names = input()
matches = find_full_name(names)
print(' '.join(matches))

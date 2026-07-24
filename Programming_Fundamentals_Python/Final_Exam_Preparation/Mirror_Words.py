import re

text = input()

pattern = r"([@#]{1,2})(?P<word_first>[A-Za-z]{3,})\1\1(?P<word_second>[A-Za-z]{3,})\1"
matches = list(re.finditer(pattern, text))

mirror_words = []

for match in matches:
    word_first = match.group('word_first')
    word_second = match.group('word_second')
    if word_first == word_second[::-1]:
        mirror_words.append(f'{word_first} <=> {word_second}')

if not matches:
    print("No word pairs found!")
else:
    print(f"{len(matches)} word pairs found!")

if mirror_words:
    print("The mirror words are:")
    print(', '.join(mirror_words))
else:
    print("No mirror words!")

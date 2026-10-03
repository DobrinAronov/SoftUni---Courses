import re

with open("words.txt", "r") as file:
    words = file.read().split()

words_count = {}
with open("input_file.txt", "r") as file:
    text = file.read()

    for word in words:
        pattern = rf"\b{word}\b"
        matches = re.findall(pattern, text, re.IGNORECASE)

        words_count[word] = words_count.get(word, 0) + len(matches)

with open("output.txt", "w") as output:
    for word, count in sorted(words_count.items(), key=lambda x: -x[1]):
        output.write(f"{word} - {count}\n")
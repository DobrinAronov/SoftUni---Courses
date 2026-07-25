import re

text = input()

pattern = r"(::|\*\*)([A-Z][a-z]{2,})\1"
matches = re.findall(pattern, text)

total_sum = 1
for symbol in text:
    if symbol.isdigit():
        total_sum *= int(symbol)
print(f"Cool threshold: {total_sum}")
print(f"{len(matches)} emojis found in the text. The cool ones are:")

for match in matches:
    current_sum = 0
    for letter in match[1]:
        current_sum += ord(letter)
    if current_sum >= total_sum:
        text = match[0] + match[1] + match[0]
        print(text)

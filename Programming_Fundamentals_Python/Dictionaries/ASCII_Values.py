ascii_values = {}

letters_list = input().split(', ')

for letter in letters_list:
    if letter not in ascii_values:
        ascii_values[letter] = ord(letter)

print(ascii_values)
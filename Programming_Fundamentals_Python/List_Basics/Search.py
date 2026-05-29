number_of_strings = int(input())
word = input()

all_strings = []
strings_with_word = []

for number in range(number_of_strings):
    input_string = input()
    if word in input_string:
        strings_with_word.append(input_string)
    all_strings.append(input_string)

print(all_strings)
print(strings_with_word)

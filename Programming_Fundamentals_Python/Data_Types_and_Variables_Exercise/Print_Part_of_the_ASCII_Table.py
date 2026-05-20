start_character = int(input())
last_character = int(input())

total_string = ''

for number in range(start_character, last_character + 1):
    total_string += chr(number)

print(f"{' '.join(total_string)}")
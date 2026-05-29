numbers = input().split()
input_string = input()

message = ''

for number in numbers:
    index = sum([int(digit) for digit in number])

    if index >= len(input_string):
        index = index - len(input_string)

    message += input_string[index]
    input_string = input_string.replace(input_string[index], '', 1)

print(message)

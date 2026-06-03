def data_types(some_command: str, num_or_str: str):
    if some_command == 'int':
        return int(num_or_str) * 2
    elif some_command == 'real':
        return f"{(float(num_or_str) * 1.5):.2f}"
    else:
        return '$' + num_or_str + '$'


command = input()
number_or_string = input()

print(data_types(command, number_or_string))

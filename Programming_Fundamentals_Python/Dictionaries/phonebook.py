phonebook = {}

current_command = input()
while '-' in current_command:

    name, number = current_command.split('-')
    phonebook.setdefault(name, number)

    current_command = input()

number = int(current_command)

for i in range(number):
    searching_name = input()
    if searching_name in phonebook:
        print(f"{searching_name} -> {phonebook[searching_name]}")
    else:
        print(f"Contact {searching_name} does not exist.")
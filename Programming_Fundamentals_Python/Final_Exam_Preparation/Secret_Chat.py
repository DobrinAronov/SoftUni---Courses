def insert_space(some_string, part_to_split: str) -> tuple[str, str]:
    index = int(part_to_split)
    if index in range(len(some_string)):
        some_string = some_string[:index] + ' ' + some_string[index:]
    return some_string, ''


def reverse(some_string, part_to_split: str) -> tuple[str, str]:
    substring = part_to_split
    if substring in some_string:
        some_string = some_string.replace(substring, '', 1)
        reverse_substring = substring[::-1]
        some_string = some_string + reverse_substring
        return some_string, ''
    return some_string, 'error'


def change_all(some_string, part_to_split: str) -> tuple[str, str]:
    substring, replacement = part_to_split.split(':|:')
    if substring in some_string:
        some_string = some_string.replace(substring, replacement)
        return some_string, ''
    return some_string, ''


all_commands = {
    'InsertSpace': insert_space,
    'Reverse': reverse,
    'ChangeAll': change_all
}

concealed_message = input()

while (current_command := input()) != "Reveal":
    command, arguments = current_command.split(':|:', 1)
    concealed_message, message = all_commands[command](concealed_message, arguments)
    if message:
        print(message)
    else:
        print(concealed_message)

print(f"You have a new text message: {concealed_message}")

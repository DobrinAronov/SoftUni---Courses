import re


def check_string_valid(some_string: str) -> tuple[bool, str, str]:
    pattern = r"!(?P<command>[A-Z][a-z]{2,})!:\[(?P<string>[A-Za-z]{8,})\]"

    matches = re.finditer(pattern, some_string)

    some_command = ''
    string_after_command = ''

    for match in matches:
        some_command = match.group('command')
        string_after_command = match.group('string')

    if some_command and string_after_command:
        return True, some_command, string_after_command
    return False, some_command, string_after_command


count_of_strings = int(input())

for number in range(count_of_strings):
    current_string = input()
    is_valid, command, string = check_string_valid(current_string)
    if is_valid:
        translate_string = []
        for letter in string:
            translate_string.append(str(ord(letter)))
        print(f"{command}: {' '.join(translate_string)}")
    else:
        print("The message is invalid")

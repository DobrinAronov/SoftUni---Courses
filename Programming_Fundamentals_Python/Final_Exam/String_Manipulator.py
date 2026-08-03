def translate(some_string: str, part_to_split: str) -> str:
    char, replacement = part_to_split.split()

    if char in some_string:
        some_string = some_string.replace(char, replacement)
        return some_string
    return some_string


def includes(some_string: str, part_to_split: str) -> str:
    substring = part_to_split

    if substring in some_string:
        return 'True'
    return 'False'


def start(some_string: str, part_to_split: str) -> str:
    substring = part_to_split

    if some_string.startswith(substring):
        return 'True'
    return 'False'


def lowercase(some_string: str) -> str:
    return some_string.lower()


def find_index(some_string: str, part_to_split: str) -> int:
    char = part_to_split
    index_to_find = 0
    for idx in range(len(some_string) -1, -1, -1):
        if some_string[idx] == char:
            index_to_find = idx
            break
    return index_to_find


def remove(some_string: str, part_to_split: str) -> str:
    start_index, count = part_to_split.split()
    start_index, count = int(start_index), int(count)

    some_string = some_string[:start_index] + some_string[(start_index + count):]
    return some_string


input_string = input()

while (current_command := input()) != "End":

    if current_command == "Lowercase":
        input_string = lowercase(input_string)
        print(input_string)
    else:
        command, arguments = current_command.split(maxsplit=1)

        if command == "Translate":
            input_string = translate(input_string, arguments)
            print(input_string)

        elif command == "Includes":
            is_include = includes(input_string, arguments)
            print(is_include)

        elif command == "Start":
            is_start = start(input_string, arguments)
            print(is_start)

        elif command == "FindIndex":
            index = find_index(input_string, arguments)
            print(index)

        elif command == "Remove":
            input_string = remove(input_string, arguments)
            print(input_string)

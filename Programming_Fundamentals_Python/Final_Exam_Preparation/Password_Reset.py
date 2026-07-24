def take_odd(some_string: str) -> str:
    output_string = [some_string[idx] for idx in range(len(some_string)) if idx % 2 != 0]
    return ''.join(output_string)


def cut(some_string: str, idx: int, some_len: int) -> str:
    return some_string[:idx] + some_string[(idx + some_len):]


def substitute(some_string: str, sub_str: str, replacement: str) -> tuple[str, str]:
    if sub_str in some_string:
        some_string = some_string.replace(sub_str, replacement)
        return some_string, ''
    return some_string, "Nothing to replace!"


password = input()

while (current_command := input()) != "Done":
    if current_command == "TakeOdd":
        password = take_odd(password)
        print(password)
    else:
        command, part_to_split = current_command.split(maxsplit=1)

        if command == 'Cut':
            index, length = part_to_split.split()
            index, length = int(index), int(length)
            password = cut(password, index, length)
            print(password)

        elif command == "Substitute":
            substring, some_substitute = part_to_split.split()
            password, message = substitute(password, substring, some_substitute)
            if message:
                print(message)
            else:
                print(password)

print(f"Your password is: {password}")

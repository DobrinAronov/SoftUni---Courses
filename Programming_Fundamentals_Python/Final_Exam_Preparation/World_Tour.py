def add_stop(some_string: str, index: str, string: str) -> str:
    index = int(index)
    if 0 <= index < len(some_string):
        some_string = some_string[:index] + string + some_string[index:]
    return some_string


def remove_stop(some_string: str, start_index: str, end_index: str) -> str:
    start_index, end_index = int(start_index), int(end_index)
    if 0 <= start_index <= end_index < len(some_string):
        some_string = some_string[:start_index] + some_string[end_index + 1:]
    return some_string


def exchange(some_string: str, old_string: str, new_string: str) -> str:
    if old_string in some_string:
        some_string = some_string.replace(old_string, new_string)
    return some_string


all_commands = {
    'Add Stop': add_stop,
    'Remove Stop': remove_stop,
    'Switch': exchange
}

all_stops = input()

while (current_command := input()) != "Travel":
    command, first_argument, second_argument = current_command.split(':')
    all_stops = all_commands[command](all_stops, first_argument, second_argument)
    print(all_stops)

print(f"Ready for world tour! Planned stops: {all_stops}")

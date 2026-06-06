def add_to_do_list(lst: list) -> list:
    output_list = []
    sorted_list = sorted(lst, key=lambda x: int(x.split('-')[0]))

    for element in sorted_list:
        importance_note = element.split('-')
        output_list.append(importance_note[1])
    return output_list


to_do_list = []

while (current_command := input()) != 'End':
    to_do_list.append(current_command)

to_do_list = add_to_do_list(to_do_list)

print(to_do_list)

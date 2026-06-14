def urgent(lst: list, some_item: str) -> list:
    if some_item not in lst:
        lst.insert(0, item)
    return lst


def unnecessary(lst: list, some_item: str) -> list:
    if some_item in lst:
        lst.remove(item)
    return lst


def correct(lst: list, some_item: str, some_new_item: str) -> list:
    if some_item in lst:
        idx_old_item = lst.index(item)
        lst[idx_old_item] = some_new_item
    return lst


def rearrange(lst: list, some_item: str) -> list:
    if some_item in lst:
        idx_rearrange_item = lst.index(some_item)
        rearrange_item = lst.pop(idx_rearrange_item)
        lst.append(rearrange_item)
    return lst


initial_list = input().split('!')

while (current_command := input()) != 'Go Shopping!':
    spit_command = current_command.split()
    command, item = spit_command[0], spit_command[1]

    if command == 'Urgent':
        initial_list = urgent(initial_list, item)
    elif command == 'Unnecessary':
        initial_list = unnecessary(initial_list, item)
    elif command == 'Correct':
        new_item = spit_command[2]
        initial_list = correct(initial_list, item, new_item)
    elif command == 'Rearrange':
        initial_list = rearrange(initial_list, item)

print(', '.join(initial_list))

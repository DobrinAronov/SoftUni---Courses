def exchange(lst: list[int], idx: int):
    left_part = lst[:idx + 1]
    right_part = lst[idx + 1:]
    result = right_part + left_part
    return result


def max_even_odd(lst: list[int], sec_cmd: str):
    filtered_list = []

    if sec_cmd == 'even':
        filtered_list = [element for element in lst if element % 2 == 0]
    elif sec_cmd == 'odd':
        filtered_list = [element for element in lst if element % 2 != 0]

    if filtered_list:
        max_number = max(filtered_list)
        for idx in range(len(lst) - 1, - 1, - 1):
            if lst[idx] == max_number:
                return idx

    return "No matches"


def min_even_odd(lst: list[int], sec_cmd: str):
    filtered_list = []

    if sec_cmd == 'even':
        filtered_list = [element for element in lst if element % 2 == 0]
    elif sec_cmd == 'odd':
        filtered_list = [element for element in lst if element % 2 != 0]

    if filtered_list:
        min_number = min(filtered_list)
        for idx in range(len(lst) - 1, - 1, - 1):
            if lst[idx] == min_number:
                return idx

    return "No matches"


def first_even_odd(lst: list[int], some_count: int, sec_cmd: str):
    if some_count > len(lst):
        return "Invalid count"

    output_list = []

    for element in lst:
        if (sec_cmd == 'even' and element % 2 == 0) or \
                (sec_cmd == 'odd' and element % 2 != 0):
            output_list.append(element)
            if len(output_list) == some_count:
                break

    return output_list


def last_even_odd(lst: list[int], some_count: int, sec_cmd: str):
    if some_count > len(lst):
        return "Invalid count"

    output_list = []

    for element in lst[:: -1]:
        if (sec_cmd == 'even' and element % 2 == 0) or \
                (sec_cmd == 'odd' and element % 2 != 0):
            output_list.append(element)
            if len(output_list) == some_count:
                break

    return output_list[:: -1]


initial_list = [int(number) for number in input().split()]

while (current_command := input()) != "end":

    split_command = current_command.split()
    command = split_command[0]

    if command == 'exchange':
        index = int(split_command[1])
        if not (0 <= index < len(initial_list)):
            print("Invalid index")
        else:
            initial_list = exchange(initial_list, index)

    elif command == 'max':
        second_command = split_command[1]
        print(max_even_odd(initial_list, second_command))

    elif command == 'min':
        second_command = split_command[1]
        print(min_even_odd(initial_list, second_command))

    elif command == 'first':
        count, second_command = int(split_command[1]), split_command[2]
        print(first_even_odd(initial_list, count, second_command))

    elif command == 'last':
        count, second_command = int(split_command[1]), split_command[2]
        print(last_even_odd(initial_list, count, second_command))

print(initial_list)
def swap(lst: list, idx_1: int, idx_2: int) -> list:
    lst[idx_1], lst[idx_2] = lst[idx_2], lst[idx_1]
    return lst


def multiply(lst: list, idx_1: int, idx_2: int) -> list:
    lst[idx_1] *= lst[idx_2]
    return lst


def decrease(lst: list) -> list:
    lst = [element - 1 for element in lst]
    return lst


initial_numbers = [int(number) for number in input().split()]

while (current_command := input()) != "end":
    split_command = current_command.split()
    command = split_command[0]

    if command == "swap":
        index_1, index_2 = int(split_command[1]), int(split_command[2])
        initial_numbers = swap(initial_numbers, index_1, index_2)
    elif command == "multiply":
        index_1, index_2 = int(split_command[1]), int(split_command[2])
        initial_numbers = multiply(initial_numbers, index_1, index_2)
    elif command == "decrease":
        initial_numbers = decrease(initial_numbers)

print(f"{', '.join(str(element) for element in initial_numbers)}")

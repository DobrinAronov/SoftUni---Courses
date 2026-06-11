def merge(lst: list, start_idx: int, end_idx: int) -> list[str]:

    start_idx = max(start_idx, 0)
    end_idx = min(len(lst) - 1, end_idx)

    range_of_merge = range(start_idx, end_idx + 1)
    output_list = []
    merge_string = ''

    for index in range(len(lst)):
        if index in range_of_merge:
            merge_string += lst[index]
            # Checking the case when index is last in list and last in merge range
            if index == end_idx:
                output_list.append(merge_string)
        else:
            output_list.append(lst[index])
    return output_list


def divide(lst: list, idx: int, partition: int) -> list[str]:
    output_list = []

    if partition > 0:
        for index in range(len(lst)):
            if index != idx:
                output_list.append(lst[index])
            else:
                word = lst[index]
                divide_length = len(lst[index]) // partition
                # Divide word in equal partition
                for i in range(partition):
                    divide_part = word[:divide_length]
                    if i == partition - 1:  # Checking when the index is last
                        divide_part = word  # We add rest letters from word, if it's more than divide_length
                        output_list.append(divide_part)  # Last time, we don't have to add space!
                    else:
                        output_list.append(divide_part)
                        word = word[divide_length:]

        return output_list
    else:
        return lst


all_commands = {
    'merge': merge,
    'divide': divide
}

list_of_data = input().split()

while (current_command := input()) != "3:1":

    command, number_1, number_2 = current_command.split()
    number_1, number_2 = int(number_1), int(number_2)

    list_of_data = all_commands[command](list_of_data, number_1, number_2)

print(' '.join(list_of_data))

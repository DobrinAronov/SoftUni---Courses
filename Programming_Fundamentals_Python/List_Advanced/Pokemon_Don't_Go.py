def list_manipulation(lst: list, idx: int):
    if idx < 0:
        remove_number = lst.pop(0)
        last_element = lst[-1]
        lst.insert(0, last_element)

    elif idx >= len(lst):
        remove_number = lst.pop()
        first_number = lst[0]
        lst.append(first_number)

    else:
        remove_number = lst.pop(idx)

    lst = [element + remove_number if element <= remove_number else element - remove_number for element in lst]

    return lst, remove_number


numbers = [int(element) for element in input().split()]
all_removed_elements = 0

while True:

    if not numbers:
        break

    command = input()

    integer = int(command)
    numbers, add_remove_element = list_manipulation(numbers, integer)
    all_removed_elements += add_remove_element

print(all_removed_elements)

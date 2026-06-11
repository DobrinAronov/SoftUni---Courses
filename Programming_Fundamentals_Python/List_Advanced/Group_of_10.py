def group_tens(lst: list, group: int) -> tuple:
    output_list = [element for element in lst if element <= group]
    lst = [element for element in lst if element not in output_list]
    return output_list, lst


sequence_of_numbers = [int(number) for number in input().split(', ')]

current_group = 10

while sequence_of_numbers:
    list_of_numbers, sequence_of_numbers = group_tens(sequence_of_numbers, current_group)
    print(f"Group of {current_group}'s: {list_of_numbers}")
    current_group += 10
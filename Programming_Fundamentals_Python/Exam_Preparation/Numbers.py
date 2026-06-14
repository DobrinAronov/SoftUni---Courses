def sorted_list(lst: list) -> list:
    average_num = sum(lst) / len(lst)
    sorted_lst = [number for number in lst if number > average_num]
    sorted_lst = sorted(sorted_lst, reverse=True)

    if len(sorted_lst) > 5:
        return sorted_lst[:5]
    return sorted_lst


numbers = [int(element) for element in input().split()]

numbers = sorted_list(numbers)
if not numbers:
    print("No")
else:
    numbers_str = [str(element) for element in numbers]
    print(' '.join(numbers_str))

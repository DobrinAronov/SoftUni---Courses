def sorted_list(lst : list) -> list:
    return sorted(lst)


input_list = [int(element) for element in input().split()]

print(sorted_list(input_list))
def absolute_values(lst : list) -> list:
    return [abs(number) for number in lst]


input_list = [float(element) for element in input().split()]

print(absolute_values(input_list))